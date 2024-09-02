import asyncio
import ujson
import json
import httpx
import logging
import aiohttp
import os

from datetime import datetime
from typing import Type

from aiogram.types import Message
from aiohttp.http_exceptions import HttpBadRequest

from dotenv import load_dotenv

# from db.db_profile import Session, Profile
# from db.router import cursor, conn


load_dotenv()


class Crm:
    def __init__(self) -> None:
        self.login = os.getenv("LOGIN")
        self.password = os.getenv("PASSWORD")
        self.bearer = os.getenv("BEARER_TOKEN")
        self.company_id = os.getenv("CID")
        self.user = os.getenv("USER_TOKEN")


class Yclients:

    def __init__(self, bearer_token: str, company_id: int, user_token: str = "",  language: str = 'ru-RU') -> None:
        self.company_id = company_id
        self.headers = {
            "Accept": "application/vnd.yclients.v2+json",
            "Accept-Language": language,
            "Authorization": f"Bearer {bearer_token}, User {user_token}",
            "Cache-Control": "no-cache"
        }
        self.logging = False

    @staticmethod
    def loging():
        logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
        

    async def info_db(self) -> None:
        """Get info for Database"""
        url = f"https://api.yclients.com/api/v1/company/{self.company_id}/clients/search"
        for _ in range(9):
            payload = {
                "page": _,
                "page_size": 200,
                "fields": [
                    "id",
                    "name",
                    "phone",
                    "visits_count",
                    "last_visit_date",
                    "first_visit_date"
                ]
            }
            async with httpx.AsyncClient() as c:
                response = await c.post(url=url, json=payload, headers=self.headers)
            res = ujson.loads(response.text)

            if res['success']:
                # this in feature updatre data in DB
                print(res['data'])

    async def history(self, phone: str, client_id: int) -> None:
        "Get traning history client"
        url = f"https://api.yclients.com/api/v1/company/{self.company_id}/clients/visits/search"
        payload = {
            "client_id": client_id,
            "client_phone": phone[-11:],
            "from": "2023-01-01",
            "to": datetime.now().strftime('%Y-%m-%d')
        }
        async with httpx.AsyncClient() as c:
            response = await c.post(url=url, json=payload, headers=self.headers)
        res = ujson.loads(response.text)

        if res['success']:
            data = res['data']['records']

            dates_history = ""

            for _ in data:
                dates_history += "%s\n" % _['date']

            if dates_history != "":
                return dates_history
            else:
                return "История тренировок отсутствует"
        else:
            raise HttpBadRequest("Bad request")

    async def abonement(self, phone: str) -> None:
        url = f"https://api.yclients.com/api/v1/loyalty/abonements/"
        querystring = {
            "company_id": self.company_id,
            'phone': phone[-11:]
        }
        async with httpx.AsyncClient() as c:
            response = await c.get(url=url, headers=self.headers, params=querystring)
        res = ujson.loads(response.text)
        
        message = ''
        if res['success']:
            for _ in range(len(res['data'])):
                msg = (f"{res['data'][_]['type']['title']}\n"
                    f"Период: {res['data'][_]['type']['period']}\t"
                    f"Статус: {res['data'][_]['status']['title']}\n\n")

                message += msg

            return message
        else:
            return "Абонемент у данного пользователя отсутствует."
        
    async def referals(self, client_id: int) -> None:
        url = f"https://api.yclients.com/api/v1/loyalty/client_cards/{client_id}"
        async with httpx.AsyncClient() as c:
            response = await c.get(url=url, headers=self.headers)
        res = ujson.loads(response.text)
    
        if res['success']:
            if not res['data']:
                return "Баланс: 0 баллов"
            else:
                return (f"{res['data'][0]['type']['title']}\n"
                        f"Баланс: {res['data'][0]['balance']} баллов")
            
    async def gender(self, client_id: int) -> None:
        url = f"https://api.yclients.com/api/v1/client/{self.company_id}/{client_id}"
        async with httpx.AsyncClient() as c:
            response = await c.get(url=url, headers=self.headers)
        res =ujson.loads(response.text)
        if res['success']:
            return res['data']['sex']

    async def id(self, phone: str) -> None:
        """Get id client"""
        url = f"https://api.yclients.com/api/v1/company/{self.company_id}/clients/search"
        payload = {
            "page": 1,
            "page_size": 200,
            "fields": [
                "id"
            ],
            "filters":[
                {
                    "type": "quick_search",
                    "state": {
                        "value": f"{phone}"
                    }
                }
            ]
        }
        async with httpx.AsyncClient() as c:
            response = await c.post(url=url, json=payload, headers=self.headers)
        res = ujson.loads(response.text)
        
        if res['success']:
            if not res['data']:
                return None
            
            return res['data'][0]['id']
        

    async def name(self, phone) -> None:
        """Get name client"""
        url = f"https://api.yclients.com/api/v1/company/{self.company_id}/clients/search"
        payload = {
            "page": 1,
            "page_size": 200,
            "fields": [
                "name"
            ],
            "filters":[
                {
                    "type": "quick_search",
                    "state": {
                        "value": f"{phone}"
                    }
                }
            ]
        }
        async with httpx.AsyncClient() as c:
            response = await c.post(url=url, json=payload, headers=self.headers)
        res = ujson.loads(response.text)
        
        if res['success']:
            return res['data'][0]['name']

        
async def user_token(login: str, password: str, bearer_token: str, language: str = 'ru-RU') -> None:
        """Get user token for headers"""
        url = "https://api.yclients.com/api/v1/auth"
        headers = {
            "Accept": "application/vnd.yclients.v2+json",
            "Accept-Language": language,
            "Authorization": f"Bearer {bearer_token}, User {user_token}",
            "Cache-Control": "no-cache"
        }
        payload = {
            "login": login,
            "password": password
        }
        async with httpx.AsyncClient() as c:
            response = await c.post(url=url, json=payload, headers=headers)
        res = ujson.loads(response.text)
        
        # if success we get user_token of admin
        if res['success']:
            return res['data']['user_token']
        else:
            raise HttpBadRequest("Плохой запрос")


async def main():

    # Not prod: Буспалова Полина
    # +79213224013

    # Not prod: Кондратьев Виктор
    # +79151539393

    # Not prod: Карпенко Павел
    # +79111584140

    # Not prod: Виктория Заметаева
    # +79219471530

    # this is user_token
    # await user_token(login=Crm().login, password=Crm().password, bearer_token=Crm().bearer)

    api = Yclients(bearer_token=Crm().bearer, company_id=Crm().company_id, user_token=Crm().user)
    # await api.info_db()
    # await api.abonement("+79213224013")
    # await api.id("+79213224013")
    # await api.name("+79219471530")
    # await api.history("+79213224013", await api.id("+79213224013"))
    # await api.referals(await api.id("+79219471530"))
    # await api.gender(await api.id("+79213224013"))
    


if __name__ == '__main__':
    asyncio.run(main())

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
        payload = {
            "page": 1,
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
        print(res)
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
        print(res)

    async def abonement(self, phone: str) -> None:
        url = f"https://api.yclients.com/api/v1/loyalty/abonements/"
        querystring = {
            "company_id": self.company_id,
            'phone': phone[-11:]
        }
        async with httpx.AsyncClient() as c:
            response = await c.get(url=url, headers=self.headers, params=querystring)
        res = ujson.loads(response.text)
        print(res)

    async def id(self, phone: str) -> None:
        """Get id client"""
        url = f"https://api.yclients.com/api/v1/company/{self.company_id}/clients/search"
        payload = {
            "page": 1,
            "page_size": 200,
            "fields": [
                "id",
                "phone"
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
            return res['data'][0]['id']

    async def name(self, phone) -> None:
        """Get name client"""
        url = f"https://api.yclients.com/api/v1/company/{self.company_id}/clients/search"
        payload = {
            "page": 1,
            "page_size": 200,
            "fields": [
                "id",
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

    # +79213224013

    # this is user_token
    # await user_token(login=Crm().login, password=Crm().password, bearer_token=Crm().bearer)

    api = Yclients(bearer_token=Crm().bearer, company_id=Crm().company_id, user_token=Crm().user)
    # await api.info_db()
    # await api.abonement("+79213224013")
    # await api.id("+79213224013")
    # await api.name("+79213224013")
    await api.history("+79213224013", await api.id("+79213224013"))


if __name__ == '__main__':
    asyncio.run(main())

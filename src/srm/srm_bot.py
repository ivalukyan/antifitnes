import asyncio
import datetime
import aiohttp


from env import LOGIN, PASSWORD, BEARER_TOKEN, USER_TOKEN, CID
from src.db.router import conn, cursor
from aiohttp.http_exceptions import HttpBadRequest

bearer_token = BEARER_TOKEN
user_token = USER_TOKEN
CID = CID

login = LOGIN
password = PASSWORD

headers = {
    f"Accept": "application/vnd.yclients.v2+json",
    f'Accept-Language': 'ru-RU',
    f'Authorization': f"Bearer {bearer_token}, User {user_token}",
    f'Cache-Control': "no-cache"
}

""" PROFILE """


# get all staff
async def get_all_staff():
    url = f"https://yclients.com/api/v1/staff/{CID}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            response = await response.json()

    all_staff_info = response["data"]
    return all_staff_info


async def get_user_token(login: str, password: str):
    url = "https://api.yclients.com/api/v1/auth"
    querystring = {
        "login": login,
        "password": password
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=querystring) as response:
            response = await response.json()
    try:
        return response['data']['user_token']
    except HttpBadRequest:
        raise HttpBadRequest("Bad request - 400")


async def get_clients_ids(user_tok: str):
    url = f"https://api.yclients.com/api/v1/company/{CID}/clients/search"
    head = {
        f"Accept": "application/vnd.yclients.v2+json",
        f'Accept-Language': 'ru-RU',
        f'Authorization': f"Bearer {bearer_token}, User {user_tok}",
        f'Cache-Control': "no-cache"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=head) as response:
            dt = await response.json()

    dt = dt['data']
    ids = [_['id'] for _ in dt]
    try:
        return ids
    except HttpBadRequest:
        raise HttpBadRequest("Bad request - 400")


async def get_client_by_id(list_id: list, user_tok: str):
    head = {
        f"Accept": "application/vnd.yclients.v2+json",
        f'Accept-Language': 'ru-RU',
        f'Authorization': f"Bearer {bearer_token}, User {user_tok}",
        f'Cache-Control': "no-cache"
    }
    clients = []
    for _ in list_id:
        url = f"https://api.yclients.com/api/v1/client/{CID}/{_}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=head) as response:
                response = await response.json()
        if response['success']:
            clients.append(response['data'])

    return clients


async def get_phones_users(list_id: list, user_tok: str):
    head = {
        f"Accept": "application/vnd.yclients.v2+json",
        f'Accept-Language': 'ru-RU',
        f'Authorization': f"Bearer {bearer_token}, User {user_tok}",
        f'Cache-Control': "no-cache"
    }
    phones = []
    for _ in list_id:
        url = f"https://api.yclients.com/api/v1/client/{CID}/{_}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=head) as response:
                response = await response.json()
        if response['success']:
            phones.append(response['data']['phone'][-10:])

    return phones


async def get_history_client(user_tok: int, phone: str, client_id: str):
    url = f"https://api.yclients.com/api/v1/company/{CID}/clients/visits/search"
    head = {
        f"Accept": "application/vnd.yclients.v2+json",
        f'Accept-Language': 'ru-RU',
        f'Authorization': f"Bearer {bearer_token}, User {user_tok}",
        f'Cache-Control': "no-cache"
    }

    payload = {
        "client_id": client_id,
        "client_phone": phone[-11:],
        "from": "2024-01-01",
        "to": datetime.datetime.now().strftime('%Y-%m-%d')
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=head, data=payload) as response:
            response = await response.json()

    if response['success']:
        data = response['data']['records']

        dates_history = ""

        for _ in data:
            dates_history += f"{_['date']}\n"

        return data
    else:
        raise HttpBadRequest("Bad Request - 400")


async def get_abonements(user_tok: int, phone_number: str):
    url = f"https://api.yclients.com/api/v1/loyalty/abonements/"
    head = {
        f"Accept": "application/vnd.yclients.v2+json",
        f'Accept-Language': 'ru-RU',
        f'Authorization': f"Bearer {bearer_token}, User {user_tok}",
        f'Cache-Control': "no-cache"
    }
    querystring = {
        "company_id": CID,
        'phone': phone_number
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=head, params=querystring) as response:
            response = await response.json()

    message = ''
    if response['success']:
        for _ in range(len(response['data'])):

            msg = f"Название - {response['data'][_]['type']['title']}\n"\
                  f"Период - {response['data'][_]['type']['period']}\n"\
                  f"Статус - {response['data'][_]['status']['title']}\n\n"

            message += msg

        return message
    else:
        return "Абонемент у данного пользователя отсутствует."


async def update_profile(phone_number: str, user_id):
    phone = '+7' + phone_number[-10:]
    key = '+7' + phone_number[-10:]
    arr = await get_clients_ids(await get_user_token(LOGIN, PASSWORD))
    phone_numbers = await get_phones_users(arr, await get_user_token(LOGIN, PASSWORD))
    cursor.execute("""UPDATE app_bot_profile SET training_history = %s, info_subscription = %s WHERE id = %s """, (
        await get_history_client(await get_user_token(LOGIN, PASSWORD), phone,
                                 arr[await search(phone_numbers, key)]),
        await get_abonements(await get_user_token(LOGIN, PASSWORD), phone),
        user_id
    ))

    conn.commit()


async def check_crm(phone_number: str) -> bool:
    if phone_number[-10:] in await get_phones_users(await get_clients_ids(await get_user_token(LOGIN, PASSWORD)),
                                                    await get_user_token(LOGIN, PASSWORD)):
        return True
    return False


async def search(arr: list, key: str):
    for _ in range(len(arr)):
        if arr[_] == (key[-10:]):
            return _

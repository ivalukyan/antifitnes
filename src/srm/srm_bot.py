import asyncio
import datetime
import aiohttp
import logging


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

logging.basicConfig(level=logging.INFO, filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

crm = {
    'user_token': str,
    'ids': dict,
    'phones': dict,
    'names': dict,
    'sexes': dict
}


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


async def get_clients_ids(user_tok):
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

    ids = {}
    i = 1

    for _ in range(len(dt['data'])):
        ids[i] = dt['data'][_]['id']
        i += 1

    # dt = dt['data']
    # ids = [_['id'] for _ in dt]
    try:
        return ids
    except HttpBadRequest:
        raise HttpBadRequest("Bad request - 400")


async def get_client_by_id(list_id, user_tok):
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


async def get_phones_users(list_id, user_tok):
    head = {
        f"Accept": "application/vnd.yclients.v2+json",
        f'Accept-Language': 'ru-RU',
        f'Authorization': f"Bearer {bearer_token}, User {user_tok}",
        f'Cache-Control': "no-cache"
    }
    phones = {}
    i = 1
    for _ in list_id:
        url = f"https://api.yclients.com/api/v1/client/{CID}/{_}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=head) as response:
                response = await response.json()
        if response['success']:
            phones[i] = (response['data']['phone'][-10:])
            i += 1

    return phones


async def get_history_client(user_tok, phone, client_id):
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
        "from": "2023-01-01",
        "to": datetime.datetime.now().strftime('%Y-%m-%d')
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=head, data=payload) as response:
            response = await response.json()

    if response['success']:
        data = response['data']['records']

        dates_history = ""

        for _ in data:
            dates_history += "%s\n" % _['data']

        if dates_history != "":
            return data
        else: return "История тренировок отсутствует"
    else:
        raise HttpBadRequest("Bad Request - 400")


async def get_abonements(user_tok, phone_number):
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
    cursor.execute("""UPDATE bot_app_profile SET training_history = %s, info_subscription = %s WHERE id = %s """, (
        await get_history_client(crm['user_token'], phone, crm['ids'][await search(key)]),
        await get_abonements(crm['user_token'], phone),
        user_id
    ))

    conn.commit()


async def check_crm(phone_number: str) -> bool:
    if phone_number is not None:
        if phone_number[-10:] in crm['phones'].values():
            return True
        return False
    return False


async def search(key):
    for _ in range(len(crm['phones'].values())):
        if crm['phones'][_ + 1] == (key[-10:]):
            return _ + 1


async def crm_info():
    crm['user_token'] = await get_user_token(LOGIN, PASSWORD)

    crm['ids'] = await get_clients_ids(crm['user_token'])

    crm['phones'] = await get_phones_users(crm['ids'].values(), crm['user_token'])

    crm['names'] = await get_name(crm['ids'].values(), crm['user_token'])

    crm['sexes'] = await get_sex(crm['ids'].values(), crm['user_token'])


async def get_name(list_id, user_tok):
    head = {
        f"Accept": "application/vnd.yclients.v2+json",
        f'Accept-Language': 'ru-RU',
        f'Authorization': f"Bearer {bearer_token}, User {user_tok}",
        f'Cache-Control': "no-cache"
    }
    names = {}
    i = 1
    for _ in list_id:
        url = f"https://api.yclients.com/api/v1/client/{CID}/{_}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=head) as response:
                response = await response.json()

        names[i] = response['data']['name']
        i += 1

    return names


async def get_sex(list_id, user_tok):
    head = {
        f"Accept": "application/vnd.yclients.v2+json",
        f'Accept-Language': 'ru-RU',
        f'Authorization': f"Bearer {bearer_token}, User {user_tok}",
        f'Cache-Control': "no-cache"
    }
    sex = {}
    i = 1
    for _ in list_id:
        url = f"https://api.yclients.com/api/v1/client/{CID}/{_}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=head) as response:
                response = await response.json()

        sex[i] = response['data']['sex']
        i += 1

    return sex

import asyncio
import aiohttp
import logging
import datetime


from aiohttp.http_exceptions import HttpBadRequest
from aiogram.types import Message

from env import LOGIN, PASSWORD, BEARER_TOKEN, USER_TOKEN, CID
from src.db.router import cursor, conn

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
    'sexes': dict,
    'total_count': 0
}


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
    ids = {}
    cnt = 1

    for _ in range(71):
        await asyncio.sleep(0.12)
        url = f"https://api.yclients.com/api/v1/company/{CID}/clients/search"
        head = {
            f"Accept": "application/vnd.yclients.v2+json",
            f'Accept-Language': 'ru-RU',
            f'Authorization': f"Bearer {bearer_token}, User {user_tok}",
            f'Cache-Control': "no-cache"
        }
        querystring = {
            "page": _
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=head, params=querystring) as response:
                resp = await response.json()

        if resp['success']:
            for i in range(len(resp['data'])):
                ids[cnt] = resp['data'][i]['id']
                cnt += 1

    return ids


# GET All clients into CRM
async def get_client_by_id(list_id, user_tok):
    head = {
        f"Accept": "application/vnd.yclients.v2+json",
        f'Accept-Language': 'ru-RU',
        f'Authorization': f"Bearer {bearer_token}, User {user_tok}",
        f'Cache-Control': "no-cache"
    }

    for _ in list_id:
        url = f"https://api.yclients.com/api/v1/client/{CID}/{_}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=head) as response:
                response = await response.json()

        print(response)


async def get_info_about_users(list_id, user_tok, msg):
    sexes = {}
    names = {}
    phones = {}
    cnt = 1

    head = {
        f"Accept": "application/vnd.yclients.v2+json",
        f'Accept-Language': 'ru-RU',
        f'Authorization': f"Bearer {bearer_token}, User {user_tok}",
        f'Cache-Control': "no-cache"
    }

    for _ in list_id:
        url = f"https://api.yclients.com/api/v1/client/{CID}/{_}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=head) as response:
                resp = await response.json()

        # print("%s - %s - %s - %s" % (cnt, resp['data']['phone'], resp['data']['name'], resp['data']['sex']))

        if resp['success']:
            phones[cnt] = resp['data']['phone'][-10:]
            names[cnt] = resp['data']['name']
            sexes[cnt] = resp['data']['sex']

            cnt += 1

        await print_progress(cnt, len(list_id))
        await print_process(cnt, len(list_id), msg)

    return phones, names, sexes


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
            dates_history += "%s\n" % _['date']

        if dates_history != "":
            return dates_history
        else:
            return "История тренировок отсутствует"
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
    if response['success'] and response['meta']['count'] > 0:
        for _ in range(len(response['data'])):
            msg = f"Название - {response['data'][_]['type']['title']}\n" \
                  f"Период - {response['data'][_]['type']['period']}\n" \
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


# async def crm_info():
#     crm['user_token'] = await get_user_token(LOGIN, PASSWORD)
#
#     crm['ids'] = await get_clients_ids(crm['user_token'])
#
#     crm['phones'] = await get_phones_users(crm['ids'].values(), crm['user_token'])
#
#     crm['names'] = await get_name(crm['ids'].values(), crm['user_token'])
#
#     crm['sexes'] = await get_sex(crm['ids'].values(), crm['user_token'])


async def get_name_by_id(key):
    return crm['names'][key]


async def get_personal_id(key):
    return crm['ids'][key]


async def print_progress(cnt, total):
    pr1 = round(cnt / total * 100, 1)
    cnt_10 = 0
    cnt_30 = 0
    cnt_50 = 0
    cnt_70 = 0
    cnt_90 = 0
    if pr1 == 10 and cnt_10 == 0:
        print('[= 10%           ]')
        cnt_10 += 1
    elif pr1 == 20:
        print('[= 20% =         ]')
    elif pr1 == 30 and cnt_30 == 0:
        print('[== 30% =        ]')
        cnt_30 += 1
    elif pr1 == 40:
        print('[=== 40% =       ]')
    elif pr1 == 50 and cnt_50 == 0:
        print('[==== 50% =      ]')
        cnt_50 += 1
    elif pr1 == 60:
        print('[===== 60% =     ]')
    elif pr1 == 70 and cnt_70 == 0:
        print('[===== 70% ==    ]')
        cnt_70 += 1
    elif pr1 == 80:
        print('[===== 80% ===   ]')
    elif pr1 == 90 and cnt_90 == 0:
        print('[===== 90% ====  ]')
        cnt_90 += 1
    elif pr1 == 100:
        print('[===== 100% =====]')


async def print_process(cnt, total, message: Message):
    pr1 = round(cnt / total * 100, 3)
    cnt_10 = 0
    cnt_30 = 0
    cnt_50 = 0
    cnt_70 = 0
    cnt_90 = 0
    if pr1 == 10 and cnt_10 == 0:
        await message.answer('[= 10%           ]')
        cnt_10 += 1
    elif pr1 == 20:
        await message.answer('[= 20% =         ]')
    elif pr1 == 30 and cnt_30 == 0:
        await message.answer('[== 30% =        ]')
        cnt_30 += 1
    elif pr1 == 40:
        await message.answer('[=== 40% =       ]')
    elif pr1 == 50 and cnt_50 == 0:
        await message.answer('[==== 50% =      ]')
        cnt_50 += 1
    elif pr1 == 60:
        await message.answer('[===== 60% =     ]')
    elif pr1 == 70 and cnt_70 == 0:
        await message.answer('[===== 70% ==    ]')
        cnt_70 += 1
    elif pr1 == 80:
        await message.answer('[===== 80% ===   ]')
    elif pr1 == 90 and cnt_90 == 0:
        await message.answer('[===== 90% ====  ]')
        cnt_90 += 1
    elif pr1 == 100:
        await message.answer('[===== 100% =====]')


async def checking_info_in_db() -> bool:
    cursor.execute("""SELECT phone_number FROM bot_app_profile""")
    data = cursor.fetchall()
    if len(data) == 0:
        return False
    else:
        return True


async def checking_update_in_db(total_count: int) -> bool:
    if total_count != await get_total_count(crm['user_token']):
        return False
    else:
        print("Has not updated")
        return True


async def update_db(total_count: int, message) -> None:
    crm['ids'] = await get_clients_ids(crm['user_token'])
    result = await get_info_about_users(crm['ids'].values(), crm['user_token'], message)
    crm['phones'] = result[0]
    crm['names'] = result[1]
    crm['sexes'] = result[2]
    for _ in range(total_count, await get_total_count(crm['user_token'])):
        print("%s - %s - %s" % (result[0][_ + 1], result[1][_ + 1], result[2][_ + 1]))
        phone = result[0][_ + 1]
        name = result[1][_ + 1]
        sex = result[2][_ + 1]
        cursor.execute("""INSERT INTO bot_app_profile(telegram_id, first_name, username, gender, phone_number, 
                    training_history, number_of_referral_points, info_subscription, current_standard, telegram_status) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (None, name, None, sex,
                                                                 phone, None, None, None, None,
                                                                 None))
        conn.commit()


async def get_total_count(user_tok) -> int:
    url = f"https://api.yclients.com/api/v1/company/{CID}/clients/search"
    head = {
        f"Accept": "application/vnd.yclients.v2+json",
        f'Accept-Language': 'ru-RU',
        f'Authorization': f"Bearer {bearer_token}, User {user_tok}",
        f'Cache-Control': "no-cache"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=head) as response:
            resp = await response.json()

    if resp['success']:
        return resp['meta']['total_count']


async def CRMain(msg):

    crm['user_token'] = await get_user_token(LOGIN, PASSWORD)
    print("token: %s" % crm['user_token'])

    if await checking_info_in_db() and await checking_update_in_db(crm['total_count']):
        print("DB is already filled in")
    else:
        await update_db(crm['total_count'], msg)
        crm['total_count'] = await get_total_count(crm['user_token'])
        print("DB updated")
        print("total count: %s" % crm['total_count'])

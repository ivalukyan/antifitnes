import asyncio
import datetime
import logging
from datetime import datetime

import aiohttp
from aiogram.types import Message
from aiohttp.http_exceptions import HttpBadRequest


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
    'total_count': 0,
    'proces': 10,
    'proces_': 10
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
        "to": datetime.now().strftime('%Y-%m-%d')
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
    if crm['phones'].values() is not None:
        for _ in range(len(crm['phones'].values())):
            if crm['phones'][_ + 1] == (key[-10:]):
                return _ + 1
    return None


async def get_name_by_id(key):
    return crm['names'][key]


async def get_personal_id(key):
    if crm['ids'][key] is not None:
        return crm['ids'][key]
    return None


async def print_progress(cnt, total):
    progress = round(cnt / total * 100, 1)

    if progress == 100 and crm['proces'] == 100:
        crm['proces'] = 10
        print('[===== 100% =====]')
    elif progress == 90 and crm['proces'] == 90:
        crm['proces'] = 100
        print('[===== 90% ====  ]')
    elif progress == 80 and crm['proces'] == 80:
        crm['proces'] = 90
        print('[===== 80% ===   ]')
    elif progress == 70 and crm['proces'] == 70:
        crm['proces'] = 80
        print('[===== 70% ==    ]')
    elif progress == 60 and crm['proces'] == 60:
        crm['proces'] = 70
        print('[===== 60% =     ]')
    elif progress == 50 and crm['proces'] == 50:
        crm['proces'] = 60
        print('[==== 50% =      ]')
    elif progress == 40 and crm['proces'] == 40:
        crm['proces'] = 50
        print('[=== 40% =       ]')
    elif progress == 30 and crm['proces'] == 30:
        crm['proces'] = 40
        print('[== 30% =        ]')
    elif progress == 20 and crm['proces'] == 20:
        crm['proces'] = 30
        print('[= 20% =         ]')
    elif progress == 10 and crm['proces'] == 10:
        crm['proces'] = 20
        print('[= 10%           ]')


async def print_process(cnt, total, message: Message):
    progress = round(cnt / total * 100, 1)

    if progress == 100 and crm['proces_'] == 100:
        crm['proces_'] = 10
        await message.answer('[===== 100% =====]')
    elif progress == 90 and crm['proces_'] == 90:
        crm['proces_'] = 100
        await message.answer('[===== 90% ====  ]')
    elif progress == 80 and crm['proces_'] == 80:
        crm['proces_'] = 90
        await message.answer('[===== 80% ===   ]')
    elif progress == 70 and crm['proces_'] == 70:
        crm['proces_'] = 80
        await message.answer('[===== 70% ==    ]')
    elif progress == 60 and crm['proces_'] == 60:
        crm['proces_'] = 70
        await message.answer('[===== 60% =     ]')
    elif progress == 50 and crm['proces_'] == 50:
        crm['proces_'] = 60
        await message.answer('[==== 50% =      ]')
    elif progress == 40 and crm['proces_'] == 40:
        crm['proces_'] = 50
        await message.answer('[=== 40% =       ]')
    elif progress == 30 and crm['proces_'] == 30:
        crm['proces_'] = 40
        await message.answer('[== 30% =        ]')
    elif progress == 20 and crm['proces_'] == 20:
        crm['proces_'] = 30
        await message.answer('[= 20% =         ]')
    elif progress == 10 and crm['proces_'] == 10:
        crm['proces_'] = 20
        await message.answer('[= 10%           ]')


async def checking_info_in_db(total_count) -> bool:
    cursor.execute("""SELECT phone_number FROM bot_app_profile""")
    data = cursor.fetchall()

    if len(data) != total_count:
        return False
    else:
        return True


async def checking_update_in_db(total_count: int) -> bool:
    if total_count != await get_total_count(crm['user_token']):
        return False
    else:
        print("Has not updated")
        return True


async def update_db(total_count: int, msg) -> None:
    crm['ids'] = await get_clients_ids(crm['user_token'])
    result = await get_info_about_users(crm['ids'].values(), crm['user_token'], msg)
    crm['phones'] = result[0]
    crm['names'] = result[1]
    crm['sexes'] = result[2]
    for _ in range(total_count, await get_total_count(crm['user_token'])):
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
    hour = datetime.now().hour
    minute = datetime.now().minute

    time = '[ %s : %s ]' % (hour, minute)

    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day

    crm['user_token'] = await get_user_token(LOGIN, PASSWORD)
    print("%s - token: %s" % (time, crm['user_token']))

    if await checking_info_in_db(await get_total_count(crm['user_token'])):
        print("%s - DB is already filled in" % time)
    else:
        await msg.answer("%s - Идет обновление...\nПодождите!" % time)
        await update_db(crm['total_count'], msg)
        await msg.answer("%s - Обновление завершено - %s/%s/%s" % (time, day+1, month, year))

        crm['total_count'] = await get_total_count(crm['user_token'])

        print("%s - DB updated" % time)
        print("%s - total count: %s" % (time, crm['total_count']))


async def task(msg):
    while True:
        await CRMain(msg)
        await asyncio.sleep(3600)

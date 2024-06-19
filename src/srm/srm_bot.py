import requests
from env import LOGIN, PASSWORD, BEARER_TOKEN, USER_TOKEN, CID
from src.db.router import conn, cursor

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
    all_staff_info = requests.get(url, headers=headers).json()['data']

    return all_staff_info


# get info about services
async def get_info_about_services():
    url = f"https://yclients.com/api/v1/services/{CID}"
    all_service_info = requests.get(url, headers=headers).json()['data']
    titles = []
    ids = []
    for _ in range(len(all_service_info)):
        ids.append(all_service_info[_]['id'])
        titles.append(all_service_info[_]['title'])

    return titles, ids


# get info about available days
async def get_info_availible_days():
    url = f"https://yclients.com/api/v1/book_dates/{CID}"
    all_available_days = requests.get(url, headers=headers).json()['data']

    return all_available_days


async def get_user_token(login: str, password: str):
    url = "https://api.yclients.com/api/v1/auth"
    querystring = {
        "login": login,
        "password": password
    }
    response = requests.post(url, headers=headers, data=querystring)
    data = response.json()
    return data['data']['user_token']


async def get_clients_ids(user_tok: str):
    url = f"https://api.yclients.com/api/v1/company/{CID}/clients/search"
    head = {
        f"Accept": "application/vnd.yclients.v2+json",
        f'Accept-Language': 'ru-RU',
        f'Authorization': f"Bearer {bearer_token}, User {user_tok}",
        f'Cache-Control': "no-cache"
    }
    response = requests.post(url, headers=head)
    dt = response.json()['data']
    ids = []
    for _ in dt:
        ids.append(_['id'])

    return ids


async def get_client_by_id(list_id: list, user_tok: str):
    clients = []
    for _ in list_id:
        url = f"https://api.yclients.com/api/v1/client/{CID}/{_}"
        head = {
            f"Accept": "application/vnd.yclients.v2+json",
            f'Accept-Language': 'ru-RU',
            f'Authorization': f"Bearer {bearer_token}, User {user_tok}",
            f'Cache-Control': "no-cache"
        }
        response = requests.get(url, headers=head)
        if response.status_code == 200:
            clients.append(response.json()['data'])

    return clients


async def get_phones_users(list_id: list, user_tok: str):
    phones = []
    for _ in list_id:
        url = f"https://api.yclients.com/api/v1/client/{CID}/{_}"
        head = {
            f"Accept": "application/vnd.yclients.v2+json",
            f'Accept-Language': 'ru-RU',
            f'Authorization': f"Bearer {bearer_token}, User {user_tok}",
            f'Cache-Control': "no-cache"
        }
        response = requests.get(url, headers=head)
        phones.append(response.json()['data']['phone'][-10:])

    return phones


async def get_history_client(user_tok: int):
    url = f"https://api.yclients.com/api/v1/company/{CID}/clients/visits/search"
    head = {
        f"Accept": "application/vnd.yclients.v2+json",
        f'Accept-Language': 'ru-RU',
        f'Authorization': f"Bearer {bearer_token}, User {user_tok}",
        f'Cache-Control': "no-cache"
    }

    payload = {
        "client_id": 230494945,
        "client_phone": "79687518203",
        "from": "2024-06-01",
        "to": "2024-06-30",
        "attendance": None
    }

    response = requests.post(url, headers=head, data=payload)
    data = response.json()['data']['records']

    dates_history = ""

    for _ in data:
        dates_history += f"{_['date']}\n"

    return dates_history


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
    response = requests.get(url, headers=head, params=querystring)

    if response.status_code == 200 and response.json()['meta']['count'] > 0:
        msg = (f"Название - {response.json()['data']['balance_string']}\n"
               f"Период - {response.json()['data']['period']}\n"
               f"Статус - {response.json()['data']['status']['title']}")

        return msg
    else:
        return "Абонемент у данного пользователя отсутствует."


async def update_profile(phone_number: str, user_id):
    cursor.execute("""UPDATE app_bot_profile SET training_history = %s, info_subscription = %s WHERE id = %s """, (
        await get_history_client(await get_user_token(LOGIN, PASSWORD)),
        await get_abonements(await get_user_token(LOGIN, PASSWORD), phone_number),
        user_id
    ))

    conn.commit()


async def check_crm(phone_number: str) -> bool:
    if phone_number[-10:] in await get_phones_users(await get_clients_ids(await get_user_token(LOGIN, PASSWORD)),
                                                    await get_user_token(LOGIN, PASSWORD)):
        return True
    return False

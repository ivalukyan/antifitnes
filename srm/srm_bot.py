from yclients import YClientsAPI
import requests

# bearer_token = '36224dc01758b86bf0475d37b04c73f7'
# user_token = 'z86ztue9x5ypue8dsc5a'
# CID = 363723
# FID = 363723

bearer_token = 'y6d2r449m7g7ck4nbr5a'
user_token = ''
CID = 1069469

login = 'ivan230704@mail.ru'
password = 'ccr6sb'

headers = {
    f"Accept": "application/vnd.yclients.v2+json",
    f'Accept-Language': 'ru-RU',
    f'Authorization': f"Bearer {bearer_token}, User {user_token}",
    f'Cache-Control': "no-cache"
}

""" PROFILE """


# get all staff
def get_all_staff():
    url = f"https://yclients.com/api/v1/staff/{CID}"
    all_staff_info = requests.get(url, headers=headers).json()['data']

    return all_staff_info


# get info about services
def get_info_about_services():
    url = f"https://yclients.com/api/v1/services/{CID}"
    all_service_info = requests.get(url, headers=headers).json()['data']
    titles = []
    ids = []
    for _ in range(len(all_service_info)):
        ids.append(all_service_info[_]['id'])
        titles.append(all_service_info[_]['title'])

    return titles, ids


# get info about available days
def get_info_availible_days():
    url = f"https://yclients.com/api/v1/book_dates/{CID}"
    all_available_days = requests.get(url, headers=headers).json()['data']

    return all_available_days


def get_user_token(login: str, password: str):
    url = "https://api.yclients.com/api/v1/auth"
    querystring = {
        "login": login,
        "password": password
    }
    response = requests.post(url, headers=headers, data=querystring)
    data = response.json()
    return data['data']['user_token']


def get_clients(user_tok: str):
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


def get_client_by_id(list_id: list, user_tok: str):
    for _ in list_id:
        url = f"https://api.yclients.com/api/v1/client/{CID}/{_}"
        head = {
            f"Accept": "application/vnd.yclients.v2+json",
            f'Accept-Language': 'ru-RU',
            f'Authorization': f"Bearer {bearer_token}, User {user_tok}",
            f'Cache-Control': "no-cache"
        }
        response = requests.get(url, headers=head)
        print(response.json())


def get_history_client(user_tok: int):
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
    # paid_abonements = data['services'][0]['paid_abonements_count']

    dates_history = []

    for _ in data:
        dates_history.append(_['date'])

    return dates_history


if __name__ == '__main__':
    user_token = get_user_token(login, password)
    users_list = get_clients(user_token)
    get_client_by_id(users_list, user_token)
    get_history_client(user_token)

from yclients import YClientsAPI
import requests

bearer_token = '36224dc01758b86bf0475d37b04c73f7'
user_token = "z86ztue9x5ypue8dsc5a"
CID = 363723
FID = 363723

headers = {
    f"Accept": "application/vnd.yclients.v2+json",
    f'Accept-Language': 'ru-RU',
    f'Authorization': f"Bearer {user_token}, User {bearer_token}",
    f'Cache-Control': "no-cache"
}

""" BOOKING """

# get all staff
url = f"https://yclients.com/api/v1/staff/{CID}"
all_staff_info = requests.get(url, headers=headers).json()['data']
staff_id = all_staff_info[0]['id']

# get info about services
url = f"https://yclients.com/api/v1/services/{CID}"
all_service_info = requests.get(url, headers=headers).json()['data']
titles = []
ids = []
for _ in range(len(all_service_info)):
    ids.append(all_service_info[_]['id'])
    titles.append(all_service_info[_]['title'])

# print(titles)
# print(ids)


# get info about available days
url = f"https://yclients.com/api/v1/book_dates/{CID}"
all_available_days = requests.get(url, headers=headers).json()['data']
# print(all_available_days['working_dates'])


# get all_clients
url = f"https://api.yclients.com/api/v1/clients/{CID}"
all_clients = requests.get(url, headers=headers).json()
print(all_clients)

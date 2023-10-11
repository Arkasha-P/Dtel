'''
Добавление пользователей в квартиры после создания аккаунтов
'''
from db.mysql import get_houseuid_address
import csv
import requests
import json


file = f"/home/ubu/Рабочий стол/users.csv"

list_id = []

street = get_houseuid_address()



fias = ""

user_id = open(r'txt/user_id.txt', 'r')

apartment = open(file,'r', newline='')

apartment = csv.reader(apartment)

for apartment_list in apartment:
    for user_id_list in user_id:
        
        print(f"{apartment_list[0]}  {user_id_list}")

        url = f"https://crm.dtel.ru/front/flats/{fias}:{apartment_list[0]}/users"
        print(url)

        payload = json.dumps({
        "userId": int(user_id_list)
        })

        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic YWRtaW46dTNXMmtiM25iQQ==',
        'Cookie': 'PHPSESSID_TD_CRM=hjui5lr4i0kqori9j14fi9jhsi; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response)
        break


with open(r'txt/user_id.txt', 'w') as f:
    f = ""



'''
Добавление пользователей в квартиры после создания аккаунтов
'''


"""
API  обновление пользователей
https://core.is74.ru/api/v1/mb/user/sync/all

POST

Payload
{
    "date_create": "2023-09-17T15:33"
}


API на добавление пользователей

https://web-core.is74.ru/bundles/grouping/users/

POST


"""
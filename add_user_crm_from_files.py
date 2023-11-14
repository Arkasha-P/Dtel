"""
Добавление пользователей в CRM через файл .csv
"""
from db.mysql import *
import csv
import requests
import json
import os
import datetime
import time 

t = time.localtime() 
current_time = time.strftime("%H:%M", t) 
date = datetime.date.today()

data_api = f"{date}T{current_time}"

os.system('clear')

file = f"txt/users.csv"

list_id = []

apartment = ""

def add_user_crm(user, password):

    url = "https://crm.dtel.ru/front/user/create"

    payload = json.dumps({
    "login": user,
    "password": password,
    "buyerId": "140"
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic YWRtaW46dTNXMmtiM25iQQ==',
    'Cookie': 'PHPSESSID_TD_CRM=48rc3lqs73636e4bda29kt69rd; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    
    if "false" in response.text:
        print(response.text, end = "")
        print(f" login  --  {user}")

    if "true" in response.text:
        response = response.json()
        print(response['newUserId'])

        list_id.append(response['newUserId'])
        

    return list_id

def add_user_MPUSER(list_id):

    url = f"https://crm.dtel.ru/front/user/{list_id}/main-info"

    payload = json.dumps({
    "data": {
    "id": list_id_list,
    "password": "",
    "operatorId": None,
    "buyerId": 140,
    "externalUserId": 0,
    "roles": [
    "person"
    ],
    "dontUnlinkFromFlats": False,
    "comment": None
    }
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic YWRtaW46dTNXMmtiM25iQQ==',
    'Cookie': 'PHPSESSID_TD_CRM=skc9tq8k6cvciiqm8eup2rviag; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D'
    }

    requests.request("POST", url, headers=headers, data=payload)

    print(f"права 'пользователя МП' выданы  --  {list_id_list}")

def add_user_group(list_id):

    url = f"https://crm.dtel.ru/front/user/{list_id}/groups"

    payload = json.dumps({
  "groups": [
    "1"
  ]
})
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic YWRtaW46dTNXMmtiM25iQQ==',
    'Cookie': 'PHPSESSID_TD_CRM=skc9tq8k6cvciiqm8eup2rviag; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D'
    }

    requests.request("POST", url, headers=headers, data=payload)

    print("Добавление пользователя в группу Dtel")

def add_user_sip_acc(user, password, list_id_list):

    url = f"https://crm.dtel.ru/front/user/{list_id_list}/sip"

    payload = json.dumps({
    "data": {
    "login": user,
    "password": password,
    "domain": "sipdomofon.dtel.ru",
    "port": 7777,
    "type": "USER",
    "id": None
  }
})

    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic YWRtaW46dTNXMmtiM25iQQ==',
    'Cookie': 'PHPSESSID_TD_CRM=skc9tq8k6cvciiqm8eup2rviag; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D'
    }

    requests.request("POST", url, headers=headers, data=payload)

    print(f"Добавление Sip  --  {user}")

def add_user_id_csv(list_id):

    # Открываем исходный CSV файл для чтения
    with open(file, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Добавляем данные в определенную колонку
    new_data = list_id
    column_index = 4  # индекс колонки, в которую нужно добавить данные

    for i in range(len(rows)):
        rows[i].insert(column_index, new_data[i])

    # Открываем новый CSV файл для записи
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def get_fias(address):
    
    list = get_houseuid_address()

    input_text = address

    for list_list in list:
        list_list[1] = list_list[1].replace("Сочи, ул. ","")
        list_list[1] = list_list[1].replace(" Офис Dtel","")
        list_list[1] = list_list[1].replace("Сочи, пос.Дагомыс, ул.","")
        input_text   = input_text.replace("Сочи, ул. ","")
        if input_text == list_list[1]:
            return list_list[0]

def send_api_add_user_in_apartament(fias,apartment,user_id):

    url = f"https://crm.dtel.ru/front/flats/{fias}:{apartment}/users"

    payload = json.dumps({
    "userId": int(user_id)
    })

    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic YWRtaW46dTNXMmtiM25iQQ==',
    'Cookie': 'PHPSESSID_TD_CRM=hjui5lr4i0kqori9j14fi9jhsi; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D'
    }

    requests.request("POST", url, headers=headers, data=payload)
    print(f"{user_id}  -- Добавлен в квартиру")

def add_user_apartament():

    users = open(file,'r', newline='')
    users = csv.reader(users)

    for user_list in users:
        fias = get_fias(user_list[0])
        apartment = user_list[1]
        user_id = user_list[4]

        send_api_add_user_in_apartament(fias,apartment,user_id)

def opt_sync():

    url = "https://core.is74.ru/api/v1/mb/user/sync/all"

    payload = ""
    headers = {
    'Access-Control-Request-Method': 'POST',
    'Authorization': 'Basic ZGFnb21pc2FkbWluOmRhZ29taXNwYXNzd29yZA=='
    }

    response = requests.request("OPTIONS", url, headers=headers, data=payload)

    print(response.text)
    print(response)

def sync_web_core():

    t = time.localtime() 
    current_time = time.strftime("%H:%M", t) 
    date = datetime.date.today()

    data_api = f"{date}T{current_time}"
    print(data_api)

    url = "https://core.is74.ru/api/v1/mb/user/sync/all"

    payload = json.dumps({
  "date_create": data_api
    })
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru,en;q=0.9',
    'Content-Length': '0',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiIsImtpZCI6ImI4NGNhMmNmYjIzNjA0NDdjNTZlMTFkYjc5MjI4YzE2IiwidHlwIjoiSldUIn0.eyJhdWQiOiJkYWdvbWlzYWRtaW4iLCJleHAiOjE2OTU2NDYzMzgsInN1YiI6IjcxMDIzMjYxLWExZDAtNGZkYy05M2Y0LWVlNTI5M2UzYTNmMiJ9.2d2NqmFRUSvNEVngcU1bGphHo9wiWk3mX-PFSdN9_a0XAUosP71zbUXrRCO19cm8_XIp8MA7bi0qDHnJNmlkgg',
    'Cookie': 'coreheaders=%7B%7D; coretoken=eyJhbGciOiJIUzUxMiIsImtpZCI6ImI4NGNhMmNmYjIzNjA0NDdjNTZlMTFkYjc5MjI4YzE2IiwidHlwIjoiSldUIn0.eyJhdWQiOiJkYWdvbWlzYWRtaW4iLCJleHAiOjE2OTU2NDYzMzgsInN1YiI6IjcxMDIzMjYxLWExZDAtNGZkYy05M2Y0LWVlNTI5M2UzYTNmMiJ9.2d2NqmFRUSvNEVngcU1bGphHo9wiWk3mX-PFSdN9_a0XAUosP71zbUXrRCO19cm8_XIp8MA7bi0qDHnJNmlkgg'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response)
    print("Синхронизация завершина")

with open(file, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        add_user_crm(row[2],row[3]) # Добавлеине пользователя в CRM

add_user_id_csv(list_id) # Добавлеине пользователя uid в csv файл

for list_id_list in list_id:
    add_user_MPUSER(list_id_list) # Добавлеине пользователя права МП пользователи
    add_user_group(list_id_list) # Добавлеине пользователя в группу Dtel

with open(file, newline='') as f:
    reader = csv.reader(f)
    
    for list_id_list in list_id:
        for row in reader:
            add_user_sip_acc(row[2], row[3], list_id_list) # Добавлеине пользователя sip acc
            break

add_user_apartament()

# opt_sync()

# sync_web_core()

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
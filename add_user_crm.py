import csv
import requests
import json

file = f"/home/ubu/Рабочий стол/На выдачу Тепличная 79.csv"

list_id = []

fias = "7e0602ba-eea5-4ed7-93d3-5b11bae19463"

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

    response = response.json()

    list_id.append(response['newUserId'])

    print(user, password)

    return list_id

def add_user_MPUSER():

    url = f"https://crm.dtel.ru/front/user/{list_id_list}/main-info"

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

def add_user_group():

    url = f"https://crm.dtel.ru/front/user/{list_id_list}/groups"

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

    print(user, password, list_id_list)

def add_user_id_txt():

    file = r"txt/user_id.txt"

    with open(file, 'w') as modified:
        for list_id_list in list_id:
            modified.write(f"{list_id_list}\n")


with open(file, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        add_user_crm(row[0],row[1]) # Добавлеине пользователя в CRM

for list_id_list in list_id:
    add_user_MPUSER()
    add_user_group()
            

with open(file, newline='') as f:
    reader = csv.reader(f)
    
    for list_id_list in list_id:
        for row in reader:
            add_user_sip_acc(row[0], row[1], list_id_list)
            break

add_user_id_txt()

def add_apartment_user():
    
    url = f"https://crm.dtel.ru/front/flats/{fias}:{apartment}/users"

    payload = json.dumps({
    "userId": 561
})

    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic YWRtaW46dTNXMmtiM25iQQ==',
    'Cookie': 'PHPSESSID_TD_CRM=skc9tq8k6cvciiqm8eup2rviag; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D'
    }

    requests.request("POST", url, headers=headers, data=payload)

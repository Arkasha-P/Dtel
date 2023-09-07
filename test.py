import csv
import requests
import json

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

    response = response.json()
    
    print(response)
    
    print(user, password)

    return list_id


user = "69895"
password = "72-G5dU0"

add_user_crm(user, password)
"""
Добавление ключей в crm из файла keys.csv (пока Тепличный 79) и 79/1
"""
import csv
import requests
import json
import argparse

# Создаем экземпляр парсера аргументов
parser = argparse.ArgumentParser()

# Добавляем ключи, которые ожидаем получить, с помощью метода add_argument()
parser.add_argument('-path', type=str, help='Описание аргумента -path')

# Разбираем аргументы командной строки
args = parser.parse_args()

Cookie = "PHPSESSID_TD_CRM=65r54f5l3r6ne8hpvsmfh27js3; _csrf=11319b03dd44ab191f63862cf53eb348ea36d7e773bb47d99df5f539ce7169e8a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22pN_pI8mSdIOpNKkEcMUyRxD2VbNMfWPH%22%3B%7D; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D"

# file = r"txt/keys.csv"
file = args.path


def send_api(mac, apartment, key):
    
    url = f"https://crm.dtel.ru/front/device-keys/{mac}/create-key"

    payload = json.dumps({
    "value": key,
    "numberSystem": "16",
    "flatNum": apartment,
    "inner": "1"
    })
    headers = {
    'Cookie': Cookie,
    'Content-Type': 'application/json',
    }

    requests.request("POST", url, headers=headers, data=payload)

print(file)
with open(file, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == f"79":
            if 1 <= int(row[1]) <= 96: # 1 - 96 квартир 1 подъезд
                print(f"{row[0]} - {row[1]} - {row[2]}")
                mac = "08:13:CD:00:0F:B4"
                send_api(mac, row[1], row[2])
            
            elif 97 <= int(row[1]) <= 1000: # 97 - 272 квартиры 2 подъезд
                print(f"{row[0]} - {row[1]} - {row[2]}")
                mac = "08:13:CD:00:0F:E9"
                send_api(mac, row[1], row[2])

        elif row[0] == "79/1":
            if 1 <= int(row[1]) <= 96: # 1 - 96 квартир 1 подъезд
                print(f"{row[0]} - {row[1]} - {row[2]}")
                mac = "08:13:CD:00:0F:BB"
                send_api(mac, row[1], row[2])
            
            elif 97 <= int(row[1]) <= 272: # 97 - 272 квартиры 2 подъезд
                print(f"{row[0]} - {row[1]} - {row[2]}")
                mac = "08:13:CD:00:0F:BF"
                send_api(mac, row[1], row[2])


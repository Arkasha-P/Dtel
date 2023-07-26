import requests
import json

#---Переменные-------------------------------------------------
protocol = "http://"
ipaddres_tep_klaitka_2 = "10.85.171.6"
ipaddres_tep_klaitka_3 = "10.85.171.7"
metod = "/key/store"
key = ""
apartment = 0
bool_encryption = "false"
num_entrance = 0 # Номер подезда
Authorization = 'Basic cm9vdDo1MTY4OWY3YTNl'

#----ввод-данных-----------------------------------------------

print("Введите номер подезад: ", end = "") # выводи сообщение без новой строки 
num_entrance = input()

print("Введите номер квартиры: ", end = "") # выводи сообщение без новой строки 
apartment = int(input())

print("Введите ключ: ", end = "") # выводи сообщение без новой строки 
key = input()

def kalitka_1():       # Калитка 1 \ http://10.85.171.8 \ root \ 51689f7a3e \ 08:13:CD:00:07:D0

    ipaddres_tep_klaitka_1 = "10.85.171.8"
    apartment = 0 # все ключи добавляются в квартиру 0        
    url = protocol + ipaddres_tep_klaitka_1 + metod

    payload = json.dumps({
    "uuid": key,
    "panelCode": apartment,
    "encryption": bool_encryption,
    
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': Authorization
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response: print("OK - ключ добавлен - калитка 1")
    else: print(response.status_code);print(response.text)

def kalitka_2():        # Калитка 2 \ http://10.85.171.6 \ root \ 51689f7a3e \ 08:13:CD:00:07:7F

    ipaddres_tep_klaitka_1 = "10.85.171.6"
    apartment = 0 # все ключи добавляются в квартиру 0        
    url = protocol + ipaddres_tep_klaitka_1 + metod

    payload = json.dumps({
    "uuid": key,
    "panelCode": apartment,
    "encryption": bool_encryption,
    
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': Authorization
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response: print("OK - ключ добавлен - калитка 2")
    else: print(response.status_code);print(response.text)

def kalitka_3():        # Калитка 3 \ http://10.85.171.7 \ root \ 51689f7a3e \ 08:13:CD:00:02:30

    ipaddres_tep_klaitka_1 = "10.85.171.7"
    apartment = 0 # все ключи добавляются в квартиру 0        
    url = protocol + ipaddres_tep_klaitka_1 + metod

    payload = json.dumps({
    "uuid": key,
    "panelCode": apartment,
    "encryption": bool_encryption,
    
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': Authorization
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response: print("OK - ключ добавлен - калитка 3")
    else: print(response.status_code);print(response.text)

kalitka_1()

kalitka_2()

kalitka_3()







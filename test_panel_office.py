import requests
import json

#---Переменные-------------------------------------------------
protocol = "http://"
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
apartment = int(10) #int(input())

print("Введите ключ: ", end = "") # выводи сообщение без новой строки 
key = "12345678" #input()


def panel_office():
    
    ipaddres_office = "10.85.200.144"
    url = protocol + ipaddres_office + metod

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

    if response: print("OK - ключ добавлен")
    else: print(response.status_code);print(response.text)

panel_office()
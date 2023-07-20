import requests
import datetime

#---Переменные-------------------------------------------------

mac_tep75_gates_1 = "08:13:CD:00:07:D0" 
mac_tep75_gates_2 = "08:13:CD:00:07:7F"
mac_tep75_gates_3 = "08:13:CD:00:02:30"

mac_tep75_entrance_1 = "08:13:CD:00:07:96"
mac_tep75_entrance_2 = "08:13:CD:00:07:85"

mac_tep75_1_entrance_1 = "08:13:CD:00:04:12"
mac_tep75_1_entrance_2 = "08:13:CD:00:07:77"

mac_gai5_5_entrance_1 = "08:13:CD:00:00:0C"

mac_vin22_1_entrance_1 = "08:13:CD:00:01:3D"
mac_vin22_1_entrance_2 = "08:13:CD:00:03:1C"

mac_panel_office = "08:13:CD:00:06:C4"

now = datetime.datetime.now()

mac = str()
key = str()
apartment = str()

num_home = int()

with open("keys.txt", "r") as f:
    file = f.readlines()

#----ввод-данных-----------------------------------------------

print("Введите номер квартиры: ", end = "") # выводи сообщение без новой строки 
apartment

#----Headers---------------------------------------------------

headers = {
    'Authorization': 'Basic YWRtaW46dTNXMmtiM25iQQ==',
    'Cookie': 'PHPSESSID_TD_CRM=6v1jol7bvdb3119v9u51m3n9mm; _csrf=7c4a213cb9fc8b7861c7cfeafd443f7a4c3b09aeabb53d1fc07caccf4c78ed8fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%220Vqr-psPWsj-ZwOuy3hAAXyHRldGux8t%22%3B%7D; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D'
    }

payload = {}


#--------------------------------------------------------------


mac = [
    mac_tep75_gates_1,
    mac_tep75_gates_2,
    # mac_tep75_gates_3,
    mac_tep75_entrance_1,
    mac_tep75_entrance_2,
    mac_tep75_1_entrance_1,
    mac_tep75_1_entrance_2,
    mac_gai5_5_entrance_1,
    mac_vin22_1_entrance_1,
    mac_vin22_1_entrance_2
    # mac_panel_office
]
for mac_list in mac:
    for key_list in file:

        now = datetime.datetime.now()

        key_list = key_list.strip()

        url = f"https://crm.dtel.ru/front/device/{mac_list}/key/000000{key_list}/delete"
        

        response = requests.request("DELETE", url, headers=headers, data=payload)
     
        if "true" in response.text: print(f"OK - ключ удалён - {key_list} - {mac_list} - {now.strftime('%d-%m-%Y %H:%M:%S')} \n{url}\n")
        else: print(response.status_code, " - ", end="");print(response.text);print(f"{key_list} - {mac_list} - {now.strftime('%d-%m-%Y %H:%M:%S')} \n{url}\n")
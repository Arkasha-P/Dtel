# ДОБАВЛЕНИЕ КЛЮЧА ЧЕРЕЗ CRM 

import requests
import json

url = "https://crm.dtel.ru/front/device-keys/08:13:CD:00:02:30/create-key"

payload = json.dumps({
  "value": "12345678",
  "numberSystem": "16",
  "flatNum": "10",
  "inner": "1"
})
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.4.674 Yowser/2.5 Safari/537.36',
  'Cookie': '_identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D; _csrf=f31ac87f70db1148db6fa26b8fa898fb6f242bbc8665ccb838907798e58b09c0a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22qzOK4QMFEr7JNTQMytUUgdsHRGzAszSY%22%3B%7D; PHPSESSID_TD_CRM=48nsnl3vtfv64ufcfiridtogi3; PHPSESSID_TD_CRM=jegtldbjb8dcsfav5q97pcl3m2; _csrf=6b415ca5afa745d94a1deddf374d99a1bed9cc20496aa0dc6c71e7a0ee602794a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22YtYRalz3vIa0HWIdQVJHBFavl-daPsFD%22%3B%7D; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D',
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46dTNXMmtiM25iQQ=='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# # ПРОВЕРКА НА НАЛИЧИЕ КЛЮЧА В СИСТЕМЕ

# import requests
# import json

# url = "https://crm.dtel.ru/front/keys/duplicate"

# payload = json.dumps({
#   "values": [
#     "12345678"
#   ],
#   "numberSystem": "16"
# })
# headers = {
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.4.674 Yowser/2.5 Safari/537.36',
#   'Cookie': '_identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D; _csrf=f31ac87f70db1148db6fa26b8fa898fb6f242bbc8665ccb838907798e58b09c0a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22qzOK4QMFEr7JNTQMytUUgdsHRGzAszSY%22%3B%7D; PHPSESSID_TD_CRM=48nsnl3vtfv64ufcfiridtogi3; PHPSESSID_TD_CRM=lp3jbjcktmb734qlbh0c1otnm9; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D',
#   'Content-Type': 'application/json',
#   'Authorization': 'Basic YWRtaW46dTNXMmtiM25iQQ=='
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# response = response.json()

# print(response["result"]) # Прверка на наличие ключа

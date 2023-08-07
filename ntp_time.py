import requests
import json
from db import *

#---Переменные-------------------------------------------------
ip = get_all_ip()

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic cm9vdDo1MTY4OWY3YTNl'
}

api = "/system/settings" # Обращение к настройке

payload = json.dumps({ # передача настроек
  "log_level": {
    "api": 3,
    "uart": 3,
    "camofon": 3,
    "streamer": 3,
    "proguard": 3,
    "store": 3,
    "baresip": 3,
    "libre": 3
  },
  "tz": "Europe/Moscow",
  "dns": {
    "auto": True,
    "nameservers": [
      "10.89.255.2",
      "10.89.255.3"
    ]
  },
  "ntp": [
    "192.168.96.21",
    "1.ru.pool.ntp.org",
    "89.110.32.178"
  ],
  "assist": {
    "enable": True,
    "online": True
  }
})

for ip_list in ip:

    url = f"http://{ip_list}{api}"
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.status_code," - ",ip_list)

   

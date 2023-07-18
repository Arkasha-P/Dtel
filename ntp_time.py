import requests
import json

#---Переменные-------------------------------------------------

ip_tep75_gates_1 =          "10.85.171.8" 
ip_tep75_gates_2 =          "10.85.171.6"
ip_tep75_gates_3 =          "10.85.171.7"

ip_tep75_entrance_1 =       "10.85.171.3"
ip_tep75_entrance_2 =       "10.85.171.2"

ip_tep75_1_entrance_1 =     "10.85.171.4"
ip_tep75_1_entrance_2 =     "10.85.171.5"

ip_gai5_5_entrance_1 =      "10.87.180.2"

ip_vin22_1_entrance_1 =     "10.85.249.250"
ip_vin22_1_entrance_2 =     "10.85.249.251"

ip_panel_office =           "10.85.200.144"

ip = [
      ip_tep75_gates_1,
      ip_tep75_gates_2,
      #ip_tep75_gates_3,
      ip_tep75_entrance_1,
      ip_tep75_entrance_2,
      ip_tep75_1_entrance_1,
      ip_tep75_1_entrance_2,
      ip_gai5_5_entrance_1,
      ip_vin22_1_entrance_1,
      ip_vin22_1_entrance_2,
      ip_panel_office
      ]

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

   

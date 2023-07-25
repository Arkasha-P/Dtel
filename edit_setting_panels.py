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
      # ip_tep75_gates_1,
      # ip_tep75_gates_2,
      # ip_tep75_gates_3,
      # ip_tep75_entrance_1,
      # ip_tep75_entrance_2,
      # ip_tep75_1_entrance_1,
      # ip_tep75_1_entrance_2,
      ip_gai5_5_entrance_1,
      # ip_vin22_1_entrance_1,
      # ip_vin22_1_entrance_2,
      # ip_panel_office
      ]

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic cm9vdDo1MTY4OWY3YTNl'
}

api = "/v2/camera/osd" # Обращение к настройке

# передача настроек
payload = json.dumps([
  {
    "size": 2,
    "text": "",
    "color": "0x000000",
    "date": {
      "enable": True,
      "format": "%d-%m-%Y"
    },
    "time": {
      "enable": True,
      "format": "%H:%M:%S"
    },
    "position": {
      "x": 10,
      "y": 6
    },
    "background": {
      "enable": True,
      "color": "0xFFFFFF"
    }
  },
  {
    "size": 2,
    "text": "",
    "color": "0x000000",
    "date": {
      "enable": False,
      "format": ""
    },
    "time": {
      "enable": False,
      "format": ""
    },
    "position": {
      "x": 90,
      "y": 90
    },
    "background": {
      "enable": True,
      "color": "0xffffff"
    }
  },
  {
    "size": 2,
    "text": "Сочи, пос.Дагомыс, ул.Гайдара 5/5",
    "color": "0x000000",
    "date": {
      "enable": False,
      "format": ""
    },
    "time": {
      "enable": False,
      "format": ""
    },
    "position": {
      "x": 10,
      "y": 680
    },
    "background": {
      "enable": True,
      "color": "0xFFFFFF"
    }
  }
])

for ip_list in ip:

    url = f"http://{ip_list}{api}"
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.status_code," - ",ip_list)

   

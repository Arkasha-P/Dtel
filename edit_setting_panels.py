import requests
import json
import os
#---Переменные-------------------------------------------------

os.system('clear')


ip = ["10.83.171.2", "10.83.171.4", "10.85.179.2", "10.85.179.3", "10.85.249.250", "10.85.249.251", "10.87.180.2", "10.90.171.10", "10.90.171.11", "10.90.171.12", "10.90.171.13", "10.90.171.2", "10.90.171.3", "10.90.171.4", "10.90.171.5", "10.90.171.6", "10.90.171.7", "10.90.171.8"]


api = "/v1/ddns" # Обращение к настройке

# передача настроек
payload = json.dumps({
  "enabled": False,
  "interval": 300,
  "server": {
    "port": 8081,
    "address": "10.199.63.7",
    "username": "default",
    "password": "default"
  },
  "data": {
    "hostname": "ddns.ISCom"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic cm9vdDo1MTY4OWY3YTNl'
}

for ip_list in ip:
  hostname = ip_list
  response = os.system(f'ping -c 1 {hostname} > nul')

  if response == 0:
    url = f"http://{ip_list}{api}"
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(ip_list)
  else:
    print(f"{hostname} is down!")




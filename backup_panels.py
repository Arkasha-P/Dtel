import requests
import time
import datetime
import os

os.system('clear')

ip = open(r'txt/ip_all_panels.txt', 'r')

ip = ["10.90.171.4", "10.90.171.5", "10.90.171.2", "10.90.171.3", "10.90.171.8", "10.90.171.6", "10.85.200.144", "10.85.249.250", "10.85.249.251", "192.168.88.251", "192.168.199.252", "10.90.171.7", "10.87.180.2", "10.83.171.4", "10.83.171.2", "10.95.171.2", "10.95.171.3", "10.90.171.11", "10.90.171.10", "10.90.171.12", "10.90.171.13", "10.83.171.5", "10.86.171.2", "10.86.171.3", "10.76.171.2", "10.83.243.2", "10.83.243.3", "192.168.10.45", "192.168.10.228", "192.168.10.44", "192.168.10.42"]

def get_mac(ip):
    url = f"http://{ip}/system/info"

    payload = {}
    headers = {
      'Authorization': 'Basic cm9vdDo1MTY4OWY3YTNl'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    response = response.json()
    return response['mac']

def get_date_time():
  t = time.localtime() 
  current_time = time.strftime("%H:%M:%S", t) 
  date = datetime.date.today()

  data_api = f"{date} -- {current_time}"
  return data_api

def get_backup(ip):
   

  url = f"http://{ip}/system/backup"

  payload = {}
  headers = {
    'Authorization': 'Basic cm9vdDo1MTY4OWY3YTNl'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  name = f"{ip} -- {get_mac(ip)} -- {get_date_time()}"
  save_path = f"/home/ubu/Загрузки/{name}.bin"


  with open(save_path, 'wb') as file:
      file.write(response.content)

  print(name)

def copy_nextcloud():
    os.system('cp *.bin /home/ubu/Nextcloud/') 
    os.system('rm *.bin')

for ip_list in ip:
  hostname = ip_list
  response = os.system(f'ping -c 3 {hostname} > nul')

  if response == 0:
    print(f"{hostname} is up!", end="  --  ")
    print(get_mac(ip_list))
    get_backup(ip_list)
  else:
    print(f"{hostname} is down!")

copy_nextcloud()
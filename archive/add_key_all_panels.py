import requests
import json
import os

ip = open('txt/ip_all_panels.txt', 'r')


def send_api(ip):
    url = f"http://{ip}/key/store"

    print(url)
    payload = json.dumps({
    "uuid": "695FDBAB",
    "panelCode": 0,
    "encryption": False
})
    headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic cm9vdDo1MTY4OWY3YTNl'
}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)




for ip_list in ip:
    ip_list = ip_list.replace('\n','')
    hostname = ip_list
    response = os.system(f'ping -c 3 {hostname} > nul')

    if response == 0:
        send_api(ip_list)
    else:
        print(f"{hostname} is down!")
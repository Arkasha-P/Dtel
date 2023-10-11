import requests
import json
from config import keys, MAC_ADRESS, Cookie

def api_add_keys(mac,key,apartment,name):
    url = f"https://crm.dtel.ru/front/device-keys/{mac}/create-key"

    payload = json.dumps({
    "value": key,
    "numberSystem": "16",
    "flatNum": apartment,
    "inner": "1"
    })
    headers = {
    'Cookie': Cookie,
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if "true" in response.text: print(f"OK - ключ добавлен - {name} - {key}")
    else: print(response.status_code);print(response.text, f" - {name}")

for key in keys:

    key = key.replace('\n', '')
    for list in MAC_ADRESS.items():
        try:
            api_add_keys(list[1],key,0,list[0])
        except: pass
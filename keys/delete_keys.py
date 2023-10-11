import requests
from config import keys, MAC_ADRESS, Cookie

def api_delete_keys(mac,key):
    
    name = mac
    url = f"https://crm.dtel.ru/front/device/{mac}/key/000000{key}/delete"

    headers = {
    'Cookie': Cookie,
    'Content-Type': 'application/json',
    }

    response = requests.request("DELETE", url, headers=headers)

    if "true" in response.text: print("\033[33m {}\033[0m" .format(f"OK - ключ удалён - {name} - {key}"))
    else: print(response.status_code, " " ,response.text, f"- {name}  ")

for key in keys:
    key = key.replace('\n', '')
    for list in MAC_ADRESS.items():
        try:
            api_delete_keys(list[1],key)
        except: pass
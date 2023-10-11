import requests
import json
from cfg.cfg import headers_crm
import time


while (1):

    
    url = f"http://192.168.10.211/log/last"

    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic cm9vdDo1MTY4OWY3YTNl'
    }

    payload = json.dumps({})

    response = requests.request("get", url, headers=headers, data=payload)

    print(response.text)
    time.sleep(5)

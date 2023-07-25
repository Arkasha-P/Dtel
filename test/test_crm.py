import requests
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler()
    ]
)

url = "https://crm.dtel.ru/front/device-card/device/08:13:CD:00:06:C4"

payload = {}
headers = {
  'Authorization': 'Basic YWRtaW46dTNXMmtiM25iQQ==',
  'Cookie': 'PHPSESSID_TD_CRM=t9tdj2qscop4sia5ma8jspcf4c; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D'
}

response = requests.request("GET", url, headers=headers, data=payload)

response =  json.loads(response.text)

# print(response['device']['mac'])

logging.info(f'So should this: {response["device"]["mac"]}')

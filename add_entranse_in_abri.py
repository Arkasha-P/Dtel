"""
Скрипт который добавляет 1 подъезд во все квартиры по Абрикосовой 21
"""

import requests
import json

entranse = list(range(1,109))

print(entranse)

for entranse_list in entranse:

    url = f"https://crm.dtel.ru/front/flats/2e592a9a-15ff-482e-85bc-49f6e54a5862:{entranse_list}/link-entrance"

    payload = json.dumps({
    "entranceUid": "64d9dffe-3af9-4c3b-8a1b-c8a60f35b54b"
    })
    headers = {
    'Cookie': '_identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D; __ddg1_=ZW6L4EwFK3xzvo5eEg21; _ym_uid=1691760724803007292; _ym_d=1691760724; PHPSESSID_TD_CRM=amv8jl37gc6ja90gv9ia4cqqpe; _csrf=097f71efcb33b01bd92b6d94929d6496b1637e4222acf938e79279c5c9f0f552a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22buuFSxEUalgqbe8F9fS-7lR_zSFWPOSV%22%3B%7D; PHPSESSID_TD_CRM=c7gdtfpdstcblaq7mb7jmujc8f; _csrf=fad1b0479dc3689a0fa08a0afbeec4edd95cb5d8bc3bcfdda55fd50292766428a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22_F_AKBmLFiNY_zRfLjNj3voVEdm93Bh-%22%3B%7D; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D',
    'Content-Type': 'application/json',
    'Authorization': 'Basic QXJrYWR5OlFhZWQxMjM0NSE='
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(entranse_list)
    print(response.text)


from db.mysql import *
import csv
import requests
import json
import os
import datetime
import time 

def opt_sync():

    url = "https://core.is74.ru/api/v1/mb/user/sync/all"

    payload = ""
    headers = {
    'Access-Control-Request-Method': 'POST',
    'Authorization': 'Basic ZGFnb21pc2FkbWluOmRhZ29taXNwYXNzd29yZA=='
    }

    response = requests.request("OPTIONS", url, headers=headers, data=payload)

    print(response.text)
    print(response)

def sync_web_core():

    t = time.localtime() 
    current_time = time.strftime("%H:%M", t) 
    date = datetime.date.today()

    data_api = f"{date}T{current_time}"
    print(data_api)

    url = "https://core.is74.ru/api/v1/mb/user/sync/all"

    payload = json.dumps({
    "date_create": data_api
    # "date_create_to": data_api
})
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru,en;q=0.9',
    'Content-Length': '0',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiIsImtpZCI6ImI4NGNhMmNmYjIzNjA0NDdjNTZlMTFkYjc5MjI4YzE2IiwidHlwIjoiSldUIn0.eyJhdWQiOiJkYWdvbWlzYWRtaW4iLCJleHAiOjE2OTU2NDYzMzgsInN1YiI6IjcxMDIzMjYxLWExZDAtNGZkYy05M2Y0LWVlNTI5M2UzYTNmMiJ9.2d2NqmFRUSvNEVngcU1bGphHo9wiWk3mX-PFSdN9_a0XAUosP71zbUXrRCO19cm8_XIp8MA7bi0qDHnJNmlkgg',
    'Cookie': 'coreheaders=%7B%7D; coretoken=eyJhbGciOiJIUzUxMiIsImtpZCI6ImI4NGNhMmNmYjIzNjA0NDdjNTZlMTFkYjc5MjI4YzE2IiwidHlwIjoiSldUIn0.eyJhdWQiOiJkYWdvbWlzYWRtaW4iLCJleHAiOjE2OTU2NDYzMzgsInN1YiI6IjcxMDIzMjYxLWExZDAtNGZkYy05M2Y0LWVlNTI5M2UzYTNmMiJ9.2d2NqmFRUSvNEVngcU1bGphHo9wiWk3mX-PFSdN9_a0XAUosP71zbUXrRCO19cm8_XIp8MA7bi0qDHnJNmlkgg'
    }

    response = requests.request("POST", url, headers=headers, data=payload)


    print(payload)
    print(response.text)
    print("Синхронизация завершина")

# opt_sync()

# sync_web_core()

ip = ["10.90.171.5", "10.90.171.4", "10.90.171.2", "10.90.171.3", "10.90.171.8", "10.90.171.6", "10.90.249.250", "10.90.249.251", "10.90.171.7", "10.87.180.2", "10.83.171.4", "10.83.171.2", "10.90.179.2", "10.90.179.3", "10.90.171.11", "10.90.171.10", "10.90.171.12", "10.90.171.13", "10.85.200.144"]

ip = "10.90.171.5"

def get_mac(ip):
    url = f"http://{ip}/system/info"

    payload = {}
    headers = {
      'Authorization': 'Basic cm9vdDo1MTY4OWY3YTNl'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    response = response.json()
    return response['mac']

print(get_mac(ip))
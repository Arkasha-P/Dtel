
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

def get_mac(ip):  
    url = f"http://{ip}/system/info"

    payload = {}
    headers = {
      'Authorization': 'Basic cm9vdDo1MTY4OWY3YTNl'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    response = response.json()
    return response['mac']

# opt_sync()

# sync_web_core()

ip = ["10.90.171.4", "10.90.171.5", "10.90.171.2", "10.85.243.18", "10.90.171.3", "10.90.171.8", "10.90.171.6", "10.85.243.3", "10.85.200.144", "10.85.243.4", "10.85.249.250", "10.85.243.7", "10.85.249.251", "10.90.171.7", "10.90.171.9", "10.87.180.2", "10.83.171.4", "10.85.243.9", "10.85.243.8", "10.83.171.2", "10.95.171.2", "10.95.171.3", "10.90.171.11", "10.90.171.10", "10.90.171.12", "10.90.171.13", "10.83.171.5", "10.86.171.2", "10.86.171.3"]

# ip = ["192.168.10.211"]
# print(get_mac(ip))

payload_conf = """
### TEMPLATES ###
template(name="LongTagForwardFormat" type="list") {
    constant(value="<")
    property(name="pri")
    constant(value=">")
    property(name="timestamp" dateFormat="rfc3339")
    constant(value=" ")
    property(name="hostname")
    constant(value=" ")
    property(name="syslogtag" position.from="1" position.to="32")
    property(name="msg" spifno1stsp="on" )
    property(name="msg")
    constant(value="\n")
}

template (name="ProxyForwardFormat" type="string"
    string="<%PRI%>1 %TIMESTAMP:::date-rfc3339% %FROMHOST-IP% %APP-NAME% %HOSTNAME% - -%msg%")


###RULES ####
*.*;cron.none     /tmp/syslog.log;LongTagForwardFormat
*.*;cron.none     @91.210.24.5:1514;ProxyForwardFormat
*.*;cron.none     @crm.dtel.ru:1514;LongTagForwardFormat
*.*;cron.none     @loganalyzer.dtel.ru:1514
*.*;cron.none     @logdomofon.dtel.ru:1514;LongTagForwardFormat
"""


for ip_list in ip:
    hostname = ip_list
    response = os.system(f'ping -c 3 {hostname} > nul')

    if response == 0:
        print(f"{hostname} is up!", end="  --  ")
        url = f"http://{ip_list}/system/files/rsyslogd.conf"

        payload = payload_conf
        headers = {
        'Content-Type': 'text/plain',
        'Authorization': 'Basic cm9vdDo1MTY4OWY3YTNl'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        print(response)

    else:
        print(f"{hostname} is down!")
import requests
import json
import time
import sys

address = "Сочи, ул."
ip_panels = "192.168.10.211"
ip_server_tftp = "192.168.10.247"
url_update = "http://iscom.hues.top/X2/2.2.5.8.10"

authorization = 'Basic cm9vdDoxMjM0NTY='

keys_ois = [
"A3D8E16A",
"A3C76A8A",
"A3C8882A",
"FB13DEF7",
"FB33F587",
"6991FEAB",
"A3CB30AA",
"6984badb"
]


rsyslog = """
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

def update_stage1():

    print("Обновление 1 этапа начато")
    url = f"http://{ip_panels}:8080/system/cam/upgrade"

    payload = json.dumps({
    "server": ip_server_tftp,
    "folder": "/2.5.7.23",
    "opt": True,
    "stm": True,
    "rootfs": True,
    "media": True
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': authorization,
    'Cookie': 'PHPSESSID_TD_CRM=2ahncopu8d7878uv27p4bbmf99; _csrf=1a9b481a5e475988b41f5991c53739baf868885bb45cabe18e7b0f73f2d7810ca%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22gAY7alUi94lMxQxuacbWQeabjrBqpZjO%22%3B%7D; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response)


    

    for remaining in range(180, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rComplete!            \n")
    print("Обновление 1 этапа завершино")

def update_stage2():

    url = f"http://{ip_panels}/v2/system/upgrade"

    payload = json.dumps({
    "url": url_update,
    "opt": True,
    "media": True,
    "rootfs": True,
    "mcu": True
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': authorization
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)

    for remaining in range(180, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rComplete!            \n")

    print("Обновление 2 этапа завершино")

def update_config_rsyslogd():

    url = f"http://{ip_panels}/system/files/rsyslogd.conf"

    payload = rsyslog
    headers = {
    'Content-Type': 'text/plain',
    'Authorization': authorization
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)

def update_time_zone():

    url = f"http://{ip_panels}/system/settings"

    payload = json.dumps({"tz": "Europe/Moscow"})
    headers = {
    'Content-Type': 'application/json',
    'Authorization': authorization
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)

def off_W_B_mode():
        
    url = f"http://{ip_panels}/camera/whiteBlack"

    payload = json.dumps({
    "threshold": {
        "exposureLight": 22000,
        "exposureNight": 2500000
    }
})
    headers = {
    'Content-Type': 'application/json',
    'Authorization': authorization
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)

def add_label_address():

    url = f"http://{ip_panels}/v2/camera/osd"

    payload = json.dumps([
    {
        "size": 2,
        "text": "",
        "color": "0x000000",
        "date": {
        "enable": True,
        "format": "%d-%m-%Y"
        },
        "time": {
        "enable": True,
        "format": "%H:%M:%S"
        },
        "position": {
        "x": 10,
        "y": 6
        },
        "background": {
        "enable": True,
        "color": "0xFFFFFF"
        }
    },
    {
        "size": 1,
        "text": address,
        "color": "0xFFFFFF",
        "date": {
        "enable": False,
        "format": "%d %m %y"
        },
        "time": {
        "enable": False,
        "format": "%R"
        },
        "position": {
        "x": 10,
        "y": 700
        },
        "background": {
        "enable": False,
        "color": "0xFFFFFF"
        }
    },
    {
        "size": 2,
        "text": "",
        "color": "0xFFFFFF",
        "date": {
        "enable": False,
        "format": "%d %m %y"
        },
        "time": {
        "enable": False,
        "format": "%R"
        },
        "position": {
        "x": 140,
        "y": 0
        },
        "background": {
        "enable": True,
        "color": "0xFFFFFF"
        }
    }
    ])
    headers = {
    'Content-Type': 'application/json',
    'Authorization': authorization
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)

def update_5sec_open():

    url = f"http://{ip_panels}/relay/1/settings"

    payload = json.dumps({
    "switchTime": 5,
    "alwaysOpen": False
    })

    headers = {
    'Content-Type': 'application/json',
    'Authorization': authorization
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)

def turn_on_aac():

    url = f"http://{ip_panels}/camera/audio"

    payload = json.dumps({
	"aac_enable": True
    })

    headers = {
    'Content-Type': 'application/json',
    'Authorization': authorization
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)

def turn_off_echoD():
        
    url = f"http://{ip_panels}/sip/options"

    payload = json.dumps({
	"dtmf": {
		"1": "1",
		"2": "2"
	},
	"callDelay": 0,
	"talkDuration": 180,
	"ringDuration": 60,
	"echoD": False
    })

    headers = {
    'Content-Type': 'application/json',
    'Authorization': authorization
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)

def add_apartament_998():

    url = f"http://{ip_panels}:8080/panelCode"

    payload = json.dumps({
    "panelCode": 998,
    "callsEnabled": {
        "handset": True,
        "sip": True
    }
})

    headers = {
    'Content-Type': 'application/json',
    'Authorization': authorization
    }

    response = requests.request("post", url, headers=headers, data=payload)

    print(response.text)

def add_code_23123_apartament_0():

    url = f"http://{ip_panels}/openCode"

    payload = json.dumps({
    "code": 23123,
    "panelCode": 0
})

    headers = {
    'Content-Type': 'application/json',
    'Authorization': authorization
    }

    response = requests.request("post", url, headers=headers, data=payload)

    print(response.text)

def add_code_96369_apartament_0():

    url = f"http://{ip_panels}/openCode"

    payload = json.dumps({
    "code": 96369,
    "panelCode": 0
})

    headers = {
    'Content-Type': 'application/json',
    'Authorization': authorization
    }

    response = requests.request("post", url, headers=headers, data=payload)

    print(response.text)

def add_key_ois_apartament_998():

    with open(r"txt/keys_ois.txt", "r") as f:
        file = f.read().splitlines()

    

    for list_file in keys_ois:

        print(list_file)

        url = f"http://{ip_panels}/key/store"

        payload = json.dumps({
        "uuid": list_file,
        "panelCode": 998,
        "encryption":False
        })

        headers = {
        'Content-Type': 'application/json',
        'Authorization': authorization
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

def off_ddns():
    url = f"http://{ip_panels}/v1/ddns"

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
    'Authorization': authorization
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)

def change_pass():
    url = f"http://{ip_panels}/user/change_password"

    payload = json.dumps({
    "newPassword": "51689f7a3e"
})
    headers = {
    'Content-Type': 'application/json',
    'Authorization': authorization
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)

update_stage1()
update_stage2()
update_config_rsyslogd()
off_ddns()
update_time_zone()
off_W_B_mode()
add_label_address()
update_5sec_open()
turn_on_aac()
turn_off_echoD()
add_apartament_998()
add_code_23123_apartament_0()
add_code_96369_apartament_0()
add_key_ois_apartament_998()
change_pass()

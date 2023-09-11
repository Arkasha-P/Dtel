import requests
import json
import time

address = "Сочи, ул. Тепличная дом 79 подъезд 4"
ip_panels = "192.168.10.107"
ip_server_tftp = "192.168.10.247"


def update_stage1():

    url = f"http://{ip_panels}:8080/system/cam/upgrade"

    payload = json.dumps({
    "server": ip_server_tftp,
    "folder": "/2.5.7.18",
    "opt": True,
    "stm": True,
    "rootfs": True,
    "media": True
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic cm9vdDoxMjM0NTY='
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)

    time.sleep(180)
    print("Обновление 1 этапа завершино")

def update_stage2():

    url = f"http://{ip_panels}/v2/system/upgrade"

    payload = json.dumps({
    "url": "http://iscom.hues.top/X2/2.2.5.8.10",
    "opt": True,
    "media": True,
    "rootfs": True,
    "mcu": True
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic cm9vdDoxMjM0NTY='
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)

    time.sleep(180)
    print("Обновление 2 этапа завершино")

def update_config_rsyslogd():


    url = f"http://{ip_panels}/system/files/rsyslogd.conf"

    payload = "### TEMPLATES ###\ntemplate(name=\"LongTagForwardFormat\" type=\"list\") {\n    constant(value=\"<\")\n    property(name=\"pri\")\n    constant(value=\">\")\n    property(name=\"timestamp\" dateFormat=\"rfc3339\")\n    constant(value=\" \")\n    property(name=\"hostname\")\n    constant(value=\" \")\n    property(name=\"syslogtag\" position.from=\"1\" position.to=\"32\")\n    property(name=\"msg\" spifno1stsp=\"on\" )\n    property(name=\"msg\")\n    constant(value=\"\\n\")\n}\n\ntemplate (name=\"ProxyForwardFormat\" type=\"string\"\n    string=\"<%PRI%>1 %TIMESTAMP:::date-rfc3339% %FROMHOST-IP% %APP-NAME% %HOSTNAME% - -%msg%\")\n\n\n###RULES ####\n\n*.*;cron.none     /tmp/syslog.log;LongTagForwardFormat\n*.*;cron.none     @91.210.24.5:1514;ProxyForwardFormat\n*.*;cron.none     @crm.dtel.ru:1514;LongTagForwardFormat"
    headers = {
    'Content-Type': 'text/plain',
    'Authorization': 'Basic cm9vdDoxMjM0NTY='
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)

def update_time_zone():

    url = f"http://{ip_panels}/system/settings"

    payload = json.dumps({"tz": "Europe/Moscow"})
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic cm9vdDoxMjM0NTY='
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
    'Authorization': 'Basic cm9vdDoxMjM0NTY='
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
    'Authorization': 'Basic cm9vdDoxMjM0NTY='
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
    'Authorization': 'Basic cm9vdDoxMjM0NTY='
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
    'Authorization': 'Basic cm9vdDoxMjM0NTY='
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
    'Authorization': 'Basic cm9vdDoxMjM0NTY='
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)

def add_apartament_999():

    url = f"http://{ip_panels}:8080/panelCode"

    payload = json.dumps({
    "panelCode": 999,
    "callsEnabled": {
        "handset": True,
        "sip": True
    }
})

    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic cm9vdDoxMjM0NTY='
    }

    response = requests.request("post", url, headers=headers, data=payload)

    print(response.text)

def add_code_23123_apartament_999():

    url = f"http://{ip_panels}/openCode"

    payload = json.dumps({
    "code": 23123,
    "panelCode": 0
})

    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic cm9vdDoxMjM0NTY='
    }

    response = requests.request("post", url, headers=headers, data=payload)

    print(response.text)

def add_code_96369_apartament_999():

    url = f"http://{ip_panels}/openCode"

    payload = json.dumps({
    "code": 96369,
    "panelCode": 0
})

    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic cm9vdDoxMjM0NTY='
    }

    response = requests.request("post", url, headers=headers, data=payload)

    print(response.text)

def add_key_ois_apartament_999():

    with open(r"txt/keys_ois.txt", "r") as f:
        file = f.read().splitlines()

    for list_file in file:

        print(list_file)

        url = f"http://{ip_panels}/key/store"

        payload = json.dumps({
        "uuid": list_file,
        "panelCode": 999,
        "encryption":False
        })

        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic cm9vdDoxMjM0NTY='
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)



update_stage1()
update_stage2()
update_config_rsyslogd()
update_time_zone()
off_W_B_mode()
add_label_address()
update_5sec_open()
turn_on_aac()
turn_off_echoD()
add_apartament_999()
add_code_23123_apartament_999()
add_code_96369_apartament_999()
add_key_ois_apartament_999()

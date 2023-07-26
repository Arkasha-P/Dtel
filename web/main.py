from flask import Flask, render_template, request
import requests

app = Flask(__name__)

url = "https://crm.dtel.ru/front/device-card/device/08:13:CD:00:0E:94"

payload = {}
headers = {
  'Authorization': 'Basic Og==',
  'Cookie': 'PHPSESSID_TD_CRM=ev7toj9e3e1sirt5714lqdvp1r; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D'
}

response = requests.request("GET", url, headers=headers, data=payload)

response = response.json()

print(response['device']['mac'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action', methods=['POST'])
def action():
    
    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()
    print(response['device']['mac'])
    
    result = response['device']['mac']
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run()



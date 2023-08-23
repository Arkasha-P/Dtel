DB_FILE = r"C:\Users\sever\Documents\api_sokol\db\base_panels.db"

headers_crm = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic QVBJX0Fya2FkeTpRYWVkNDIyISEh',
  'Cookie': 'PHPSESSID_TD_CRM=2ahncopu8d7878uv27p4bbmf99; _csrf=1a9b481a5e475988b41f5991c53739baf868885bb45cabe18e7b0f73f2d7810ca%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22gAY7alUi94lMxQxuacbWQeabjrBqpZjO%22%3B%7D; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D'
}

def print_output(response, key):
    if "true" in response.text: 
        print_output = f"OK - ключ добавлен - {key}"
    else: 
        print_output = f"{response.status_code} {response.text}"
    return print(print_output)

file = open(r'txt/keys.txt', 'r')
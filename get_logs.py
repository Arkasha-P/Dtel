import logging
import requests
import os
os.system('cls')

logging.basicConfig(level=logging.INFO)

filename = "log.txt"

pattern = "UART_EV_PASS_OPEN"
# pattern = "is not present in database"


new_string = pattern

url = "http://10.85.200.144/v2/logs/all"

logging.basicConfig(level=logging.INFO)

payload = ""
headers = {
  'Authorization': 'Basic cm9vdDo1MTY4OWY3YTNl',
  'Accept-Language': 'ru,en;q=0.9',
  'Accept-Encoding': 'gzip, deflate, br'
}

response = requests.request("GET", url, headers=headers, data=payload)

log = response.text

app = []

def check_string_in_log(log, pattern): # сравнивает по шаблону текст лога и выводит найденные строки
  lines = log.split("\n")  # Разделить лог на строки
  for line in lines:
      if pattern in line:
          # print("Найдены совподения: " + line)
          app.append(line)
  return(f"\n".join(app))
        
app = check_string_in_log(log, pattern)
app = app.split("\n")

with open("log.txt", "r+") as f:
    file = f.readlines()

file = f"\n".join(file)



my_list = app
my_string = file

for app in app:
  if app in file:
      print("Строка найдена в списке")
  else:
      print("Строка не найдена в списке")
      with open('log.txt', 'a') as f:
        f.write(f"{app}\n")
      print(f"Строка '{app.strip()}' добавлена в файл.")
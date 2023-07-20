import requests
import logging
import re



url = "http://10.85.200.144/v2/logs/all"
# url = "http://10.85.200.144/log/last"

target_string = f"is not present in database"
file_path = r'C:\Users\sever\Documents\api_sokol\log.txt'
logging.basicConfig(level=logging.INFO)

payload = ""
headers = {
  'Authorization': 'Basic cm9vdDo1MTY4OWY3YTNl',
  'Accept-Language': 'ru,en;q=0.9',
  'Accept-Encoding': 'gzip, deflate, br'
}

response = requests.request("GET", url, headers=headers, data=payload)

    # RFID 000000696BBAFB is not present in database

log = response.text

target_string = f"is not present in database"

def check_string_in_log(log, target_string):
    lines = log.split("\n")  # Разделить лог на строки
    for line in lines:
        if re.search(re.escape(target_string), line):
             # Возвращаем полностью найденную строку без пробельных символов в начале и конце
            return(line.strip())

line = check_string_in_log(response.text, target_string)
filename = "log.txt"
pattern = line
new_string = line

# Функция для поиска строки в файле
def search_and_add_string(filename, pattern, new_string):
    # Открываем файл для чтения и записи
    with open(filename, 'r+') as file:
        # Читаем содержимое файла
        content = file.read()
        
        # Проверяем, найдено ли совпадение с шаблоном
        if re.search(re.escape(pattern), content):
            print("Такая строка уже существует в файле.")
        else:
            new_string = "\n" + new_string
            # Добавляем новую строку в файл
            file.write(new_string)
            print(f"Строка '{new_string.strip()}' добавлена в файл.")

search_and_add_string(filename, pattern, new_string)
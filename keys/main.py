import os
moution = '''выберите действие:
1) Добавить ключи в квартиру
2) Добавить ключи во все панели
3) Удалить ключи со всех панелей
4) Добавить ключи из файла .csv
'''
print(moution)
num = str(input())
if num == "1": os.system("clear");exec(open(r'keys/add_keys_in_apartment.py',encoding="utf-8").read())
if num == "2": os.system("clear");exec(open(r'keys/add_keys_all_panels.py',encoding="utf-8").read())
if num == "3": os.system("clear");exec(open(r'keys/delete_keys.py',encoding="utf-8").read())
if num == "4": os.system("clear");exec(open(r'keys/add_keys_for_file.py',encoding="utf-8").read())
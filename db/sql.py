import sqlite3

DB_FILE = r"C:\Users\sever\Documents\api_sokol\db\base_panels.db"



db = sqlite3.connect(DB_FILE)
cursor = db.cursor()

def get_all_ip():
    list = cursor.execute('SELECT ip FROM panels WHERE ip <> 1')
    list = [i[0] for i in list]
    return list

def get_all_mac():
    list = cursor.execute('SELECT mac FROM panels WHERE mac <> 1')
    list = [i[0] for i in list]
    return list

def get_panel_sn(sn):
    result = cursor.execute('SELECT * FROM panels WHERE serial_number == (?)', (sn,)).fetchall()
    return result

def get_panel_mac(mac):
    result = cursor.execute('SELECT * FROM panels WHERE mac == (?)', (mac,)).fetchall()
    return result

def get_panel_ip(ip):
    result = cursor.execute('SELECT * FROM panels WHERE ip == (?)', (ip,)).fetchall()
    return result


ip = get_all_ip()

print(ip)

    # # curs.execute('INSERT INTO panels VALUES ()') # INSERT INTO -  Добавить запись, затем в какую таблицу и VALUES () - значения согласно колчество коллонок
    # #
    #     curs.execute('SELECT mac FROM panels WHERE mac <> 1')# Выводит информацию SELECT - выберает колонку или все * FROM - Выберает таблицу
    # # WHERE местное условие аналог IF
    # item = curs.fetchall()
    # for el in item:
    #     print(el)

    # db.commit()

    # db.close()


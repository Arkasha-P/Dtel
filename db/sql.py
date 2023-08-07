import sqlite3


DB_FILE = r"C:\Users\sever\Documents\api_sokol\db\base_panels.db"



db = sqlite3.connect(DB_FILE, check_same_thread=False)
cursor = db.cursor()

def get_all_ip(): # выводит список всех IP
    list = cursor.execute('SELECT ip FROM panels WHERE ip <> 1')
    list = [i[0] for i in list]
    db.close
    return list

def get_all_mac(): # выводит список всех MAC
    list = cursor.execute('SELECT mac FROM panels WHERE mac <> 1')
    list = [i[0] for i in list]
    db.close
    return list

def get_panel_sn(sn): # Получаем инфу по сирийному номеру
    result = cursor.execute('SELECT * FROM panels WHERE serial_number == (?)', (sn,)).fetchall()
    db.close
    return result

def get_panel_mac(mac): # Получаем инфу по МАК
    result = cursor.execute('SELECT * FROM panels WHERE mac == (?)', (mac,)).fetchall()
    db.close
    return result

def get_panel_ip(ip): # Получаем инфу по IP
    result = cursor.execute('SELECT * FROM panels WHERE ip == (?)', (ip,)).fetchall()
    db.close
    return result

def add_panel(mac, ip): 
    result = cursor.execute("INSERT INTO `panels` (`mac`,`ip`) VALUES (?,?)", (mac,ip,)) # Создаёт новую строку в БД 
    db.commit()
    db.close
    return result

def set_panel_ip(mac, ip):
    result = cursor.execute("UPDATE `panels` SET `ip` = ? WHERE `mac` = ?", (ip, mac,)) # Изменяет ip по мак адресу
    db.commit()
    db.close
    return result

def set_panel_adress(mac, adress):
    result = cursor.execute("UPDATE `panels` SET `adress` = ? WHERE `mac` = ?", (adress, mac,)) # Изменяет адрес по мак адресу
    db.commit()
    db.close
    return result

def set_panel_entrance(mac, entrance):
    result = cursor.execute("UPDATE `panels` SET `entrance` = ? WHERE `mac` = ?", (entrance, mac,)) # Изменяет подъезд по мак адресу
    db.commit()
    db.close
    return result

def set_panel_serial_number(mac, serial_number):
    result = cursor.execute("UPDATE `panels` SET `serial_number` = ? WHERE `mac` = ?", (serial_number, mac,)) # Изменяет ip по мак адресу
    db.commit()
    db.close
    return result

def set_panel_ext_entrance(mac, ext_entrance):
    result = cursor.execute("UPDATE `panels` SET `ext_entrance` = ? WHERE `mac` = ?", (ext_entrance, mac,)) # Изменяет ip по мак адресу
    db.commit()
    db.close
    return result

def set_panel_reley(mac, reley):
    result = cursor.execute("UPDATE `panels` SET `reley` = ? WHERE `mac` = ?", (reley, mac,)) # Изменяет ip по мак адресу
    db.commit()
    db.close
    return result



    # # curs.execute('INSERT INTO panels VALUES ()') # INSERT INTO -  Добавить запись, затем в какую таблицу и VALUES () - значения согласно колчество коллонок
    # #
    #     curs.execute('SELECT mac FROM panels WHERE mac <> 1')# Выводит информацию SELECT - выберает колонку или все * FROM - Выберает таблицу
    # # WHERE местное условие аналог IF
    # item = curs.fetchall()
    # for el in item:
    #     print(el)

    # db.commit()

    # db.close()


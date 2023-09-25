import pymysql

def get_mac():
    s = 'crm.dtel.ru' #Your server(host) name 
    d = 'crm' #Your database name
    u = 'root' #Your login user
    p = 'myX6FMXz' #Your login password
    conn = pymysql.connect(host=s, user=u, password=p, database=d)
    cursor = conn.cursor()
    cursor.execute("SELECT mac FROM device_house")

    mac = list()

    for row in cursor.fetchall():
        row = list(row)
        mac.append(row)

    conn.close()

    return mac

def get_ip():

    s = 'crm.dtel.ru' #Your server(host) name 
    d = 'crm' #Your database name
    u = 'root' #Your login user
    p = 'myX6FMXz' #Your login password
    conn = pymysql.connect(host=s, user=u, password=p, database=d)
    cursor = conn.cursor()
    cursor.execute("SELECT mac FROM device_house")

    mac = list()

    for row in cursor.fetchall():
        row = list(row)
        mac.append(row)

    conn.close()

    return mac

def get_street():

    s = 'crm.dtel.ru' #Your server(host) name 
    d = 'crm' #Your database name
    u = 'root' #Your login user
    p = 'myX6FMXz' #Your login password
    conn = pymysql.connect(host=s, user=u, password=p, database=d)
    cursor = conn.cursor()
    cursor.execute("SELECT houseUid, address FROM houses")

    street = list()

    for row in cursor.fetchall():
        row = list(row)
        street.append(row)

    conn.close()

    return street

def get_houseuid_address():

    s = 'crm.dtel.ru' #Your server(host) name 
    d = 'crm' #Your database name
    u = 'root' #Your login user
    p = 'myX6FMXz' #Your login password
    conn = pymysql.connect(host=s, user=u, password=p, database=d)
    cursor = conn.cursor()
    cursor.execute("SELECT houseUid, address FROM houses")

    houseuid_address = list()

    for row in cursor.fetchall():
        row = list(row)
        houseuid_address.append(row)

    conn.close()

    return houseuid_address


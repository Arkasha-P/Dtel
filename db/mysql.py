import pymysql
s = 'crm.dtel.ru' #Your server(host) name 
d = 'crm' #Your database name
u = 'root' #Your login user
p = 'myX6FMXz' #Your login password
conn = pymysql.connect(host=s, user=u, password=p, database=d)
cursor = conn.cursor()
cursor.execute("SELECT * FROM device_house")
for row in cursor.fetchall():
    print(row)

conn.close()
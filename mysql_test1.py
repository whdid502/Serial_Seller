import pymysql

conn = pymysql.connect(host='220.71.235.155', user='root', password='Whdid7738@', db='serial_seller', charset='utf8')
curs = conn.cursor()
sql = "select * from table_A"
curs.execute(sql)
data = curs.fetchall()
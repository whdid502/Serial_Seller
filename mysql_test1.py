import pymysql

conn = pymysql.connect(host='13.209.3.126', user='root', password='Whdid7738@', db='test1', charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)

try:
    sql2 = "DELETE from korea"
    curs.execute(sql2)
    conn.commit()
    for num in range(30, 40):
        sql = "INSERT INTO korea (id, name, model_num, model_type) VALUES(" + str(num) + ", 'i5', '7700', 'Kaby Lake')"
        curs.execute(sql)
        conn.commit()
    # sql = "DELETE from korea"
    # curs.execute(sql)
    # conn.commit()
finally:
    conn.close()
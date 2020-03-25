import pymysql

conn = pymysql.connect(host='13.209.3.126', user='root', password='Whdid7738@', db='test1', charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)


try:
    cursor = conn.cursor()
    name = 'doom'
    for num in range(10, 20):
        sql = "INSERT INTO korea (id, name, model_num, model_type) VALUES(" + str(num) + ", " + name + ", '7700', 'Kaby Lake')"
        print(sql)
        cursor.execute(sql)

    conn.commit()
    print(cursor.lastrowid)
finally:
    conn.close()

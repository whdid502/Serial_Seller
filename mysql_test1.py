import pymysql

conn = pymysql.connect(host='13.209.3.126', user='root', password='Whdid7738@', db='test1', charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)

try:
    # cursor = db.cursor()
    for num in range(10, 20):
        sql = "INSERT INTO korea (id, name, model_num, model_type) VALUES(" + str(num) + ", 'i5', '7700', 'Kaby Lake')"
        print(sql)
        curs.execute(sql)

    conn.commit()
    print(curs.lastrowid)
finally:
    conn.close()

    try:
        for num in range(10, 20):
            sql = "INSERT INTO cpu_info (id, name, model_num, model_type) VALUES(" + str(
                num) + ", 'i5', '7700', 'Kaby Lake')"
            print(sql)
            curs.execute(sql)

        conn.commit()
        print(curs.lastrowid)
    finally:
        conn.close()
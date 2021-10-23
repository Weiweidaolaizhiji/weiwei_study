import pymysql

#连接数据库
conn = pymysql.connect(
                      host="localhost",
                       port=3306,
                       user="root",
                       passwd="root",
                       database="books"
                        )
course = conn.cursor()
sql = "select id, title, `read`, `comment` from t_book;"
course.execute(sql)
#查询游标总行数
print(course.rowcount)
#查询第一条数据
print(course.fetchone())
#注意游标使用，fetchall从游标当前位置开始查询所有数据
print(course.fetchall())
#可以重置游标位置，查询所有数据
course.rownumber=0
print(course.fetchall())
course.close()
conn.close()

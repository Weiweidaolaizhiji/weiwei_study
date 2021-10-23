import pymysql

# 连接数据库
conn = pymysql.connect(
                      host="localhost",
                       port=3306,
                       user="root",
                       passwd="root",
                       database="books"
                        )

#创建游标
course = conn.cursor()
#查询数据
course.execute("select version()")
result = course.fetchall()
print(result)
#关闭游标
course.close()
conn.close()


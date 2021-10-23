import pymysql
conn = pymysql.connect(
                      host="localhost",
                       port=3306,
                       user="root",
                       passwd="root",
                       database="books",
                        autocommit=True
                        )
course = conn.cursor()
#注意read字段与关键字read进行区分，采用`read`，注意sql语句结尾分号
sql = "insert into t_book(id,title,`read`) values(4,'西游记',34);"
course.execute(sql)
print(course.rowcount)
course.close()
conn.close()
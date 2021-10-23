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
sql = "update t_book set title= '东游记' where title='西游记';"
course.execute(sql)
print("影响的数据行数：",course.rowcount)
course.close()
conn.close()
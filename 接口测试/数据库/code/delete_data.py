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
sql = "delete from t_book where title = '东游记';"
course.execute(sql)
print("影响的数据行数：", course.rowcount)
course.close()
conn.close()
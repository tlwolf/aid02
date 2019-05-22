"""
    数据库读操作演示
    select
"""
import pymysql

db=pymysql.connect(host='localhost',
            user='root',
            passwd='123456',
            database='stu',
            charset='utf8')

#创建游标
cur=db.cursor()

sql="select * from myclass where age=13;"

#执行语句  cur拥有查询结果
cur.execute(sql)

one_row=cur.fetchall()
print(one_row)

one_row=cur.fetchone()
print(one_row)

one_row=cur.fetchmany(2)
print(one_row)

cur.close()
db.close()
"""
    增删改练习

"""

import pymysql

#创建链接

db=pymysql.connect(host='localhost',
                   user='root',
                   passwd='123456',
                   database='stu',
                   charset='utf8')

#创建游标
cur=db.cursor()

while True:
    name=input('Name:')
    age=input('Age:')
    gender=input('m or w:')
    score=input('Score:')

    # sql="insert into myclass (name,age,gender,score) values ('%s',%d,'%s',%f);"%(name,age,gender,score)

    sql = "insert into myclass (name,age,gender,score) values (%s,%s,%s,%s);"

    try:
        # cur.execute(sql)
        cur.execute(sql,[name,age,gender,score])
        db.commit()
    except Exception as e:
        db.rollback()   #失败回滚到操作之前的状态
        print("Faild:",e)

cur.close()
db.close()
"""
pymysql基本流程演示
"""

import pymysql

#链接数据库
db=pymysql.connect(host='localhost',port=3306,
                   user='root',password='123456',
                   database='test',charset='utf8')
#获取游标
cur=db.cursor()

#数据操作

#执行ｓｑｌ语句
cur.execute("insert into myclass values (7,'Emma',11,'w',86.5);")

#将修改内容提交到数据库
db.commit()

#关闭游标和数据库链接
cur.close()
db.close()
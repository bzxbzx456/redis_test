from datetime import datetime

import redis
from dbhelper1 import DBHelper


red = redis.StrictRedis()

sno = input("请输入学号:")

# 1 访问redis
# 'student:no'
key = 'student:'+ sno

# print(red.exists(key))

if red.exists(key): # 在redis
    stu = red.hmget(key, 'sno','sname', 'ssex', 'sclass','sbirthday')
    print("数据在redis中：")
    print(stu)
else:
    from setting import dbparams
    # 如果不在redis中，应该查询mysql
    db = DBHelper(dbparams)
    data = db.where(sno=sno).table('student').select()
    print(data)
    datetime.strftime("%y:%b:%w-%H:%m:%s")
    red.hmset(key,data[0])
    # import pymysql
    # conn = pymysql.Connect(**dbparams)
    # cursor = conn.cursor(pymysql.cursors.DictCursor)
    # res = cursor.execute("select * from student where sno=%s",[sno])
    # print(res)
    # if res > 0:
    #     data = cursor.fetchall()
    #     print(data[0])
    #     # 将数据存入redis
    #     red.hmset(key,data[0])
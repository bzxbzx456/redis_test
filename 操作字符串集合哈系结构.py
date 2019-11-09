import redis
if __name__ == '__main__':
    r = redis.StrictRedis()
    # redis数据库的命令名称与Redis实例对象的方法名称对应
    r.set('fruit','apple')
    # 给集合添加元素
    r.sadd('tom:hobby','reading','food','music')
    r.sadd('alice:hobby','food','sleep')
    #  获取集合的交集
    common_hobby = r.sinter(['tom:hobby','alice:hobby'])
    print(common_hobby)
    for hobby in common_hobby:
        print(hobby.decode())
    print("*"*20)
    # 设置学生对象，使用hash数据类型
    r.hmset("student:101",{"name":"风清扬","age":25,"score":93.5})
    # 根据key获取所有的field-value对，并封装为字典
    # （该字典的k,v都是字节码）
    data = r.hgetall("student:101")
    student_data = {}
    for k,v in data.items():
        # 将解码后的k,v添加到字典中
        student_data[k.decode()] = v.decode()
    print("学生信息为：",student_data)


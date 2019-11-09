import redis

# 链接redis
red = redis.StrictRedis()
print(red)
# string 类型操作
# 设置值
# red.set('name','白子旭',ex=10)
# 返回值是二进制字符串需要转换
# name = red.get('name')
# print(name.decode('utf-8'))

# incr用法
date = red.incr('a',10)
print(date)
red.close()
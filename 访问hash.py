import redis

red = redis.StrictRedis()

# hash哈希对象存取
red.hset('tom','name','tom')
red.hset('tom','age','20')
red.hmset('tom',{'sex':'男','class':'1909'})

# 获取
data = red.hmget('tom','name','age','sex','class')
print(data)

red.close()
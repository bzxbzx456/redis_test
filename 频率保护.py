import redis

red = redis.StrictRedis()
key = "counter:127.0.0.1"

#ex 过期时间 秒为单位
# nx 如果为True，则当key存在时，不执行操作
res = red.set(key,0,ex=60,nx=True)
print(res)
if res or red.incr(key)<=5:
    print('欢迎')
else:
    print("访问过于频繁,请稍候再访问")

red.close()
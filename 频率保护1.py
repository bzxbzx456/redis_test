import redis
if __name__ == '__main__':
    key = "limit:ip"
    # 创建StrictRedis对象，与redis服务器建⽴连接
    r = redis.StrictRedis()
    r_ip = r.set(key,1,ex=60,nx=True)
    if r_ip or r.incr(key)<=5:
        print("这是第",r.get(key).decode(),"次访问")
    else:
        print("访问过于频繁，请稍候再试！")

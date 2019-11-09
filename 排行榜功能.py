import redis
r = redis.StrictRedis()
if __name__ == '__main__':
    key = "competion_rank"
    origin_data = {"tom":0,"jerry":0,"alice":0}
    #  在redis中设置三名选手的初始成绩，以有序集合类型存储于redis中
    r.zadd(key,origin_data)

    r.zincrby(key,5,"tom")
    r.zincrby(key,8,"jerry")
    r.zincrby(key,2,"alice")
    result_rank = r.zrevrange(key,0,-1,withscores=True)
    data = []
    for item_tuple in result_rank:
        member = item_tuple[0].decode()
        score = item_tuple[1]
        data.append(tuple([member,score]))
    print(data)


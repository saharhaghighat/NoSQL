import time

import redis
client = redis.Redis(host="localhost", port=6379, decode_responses=True)

# Set and Get and Delete
# client.set("personame", "Sahar")
# client.set("personviews",2)
# name = client.get("personame")
# views = client.get("personviews")
# print(f"name: {name}, views: {views}")
# client.delete("personame")
# name = client.get("personame")
# exists = client.exists("personame")
# print(f"exists: {exists}")

#Increasing
# client.incr('counter')
# counter = client.get('counter')
# print(counter)

# Increasing with argument
# client.incr('counter',5)
# counter = client.get('counter')
# print(counter)

# Decreasing with argument
# client.decr('counter',3)
# counter = client.get('counter')
# print(counter)


# Must get Error
# client.incr('personame')
# name = client.get("personame")
# print(name)


# Setx command
# client.setex("temporary_key", 30, "temporary_value" )

# Lists push
# client.rpush("tests","test2", "test3", "test4", "test5")
# client.lpush("tests", "test1")
#
# print(client.lrange("tests", 0, -1))


# Lists pop
# left = client.lpop("tests")
# right = client.rpop("tests")
# print(left)
# print(right)

# List length
# tests_len = client.llen("tests")
# print(tests_len)

# Lists INDEX
# first_test = client.lindex("tests",0)
# print(first_test)
# last_test = client.lindex("tests",-1)
# print(last_test)
# last_test2 = client.lindex("tests",2)
# print(last_test2)

# Lists Range
# tests1 = client.lrange("tests", 0, -1)
# print(tests1)
#
# tests2 = client.lrange("tests", 0, 1)
# print(tests2)
#
# tests3 = client.lrange("tests", 1, 2)
# print(tests3)
#
# tetsts0 = client.lrange('tests', -2 , -1)
# print(tetsts0)


# Lists Linsert ,LSET, LREM
# client.lset("tests", 0, "test0")
# client.linsert("tests", "before", "test3", "test2")
# client.linsert("tests", "after", "test0", "test1")
# client.linsert("tests", "after", "test1", "test1")
# client.linsert("tests", "after", "test1", "test1.5")

# client.lrem("tests", 1,"test1")
# client.linsert("tests", "after", "test0", "test1")
# client.linsert("tests", "after", "test1", "test1")

# client.lrem("tests", 2, "test1")
# client.linsert("tests", "after", "test0", "test1")
# client.linsert("tests", "after", "test1", "test1")

# client.lrem("tests", -1, "test1")
# client.lrem("tests", 0, "test1")
# ---------------------------------------------------------------

# HASHES
# client.hset("user1", "name", "Sahar")
# client.hset("user1", "age", "25")
# client.hset("user1", "gender", "female")
#
#
# client.hset("user2", mapping={
#     "name": "jon",
#     "age": "30",
#     "gender": "male",
# })

# name1 = client.hget("user1", "name")
# name2 = client.hget("user2", "name")
# print(name1, name2)
#
# user1 = client.hmget("user1", "name", "age")
# print("user1", user1)
#
# user2_data = client.hgetall("user2")
# print("user2 data", user2_data)
#
# client.hdel("user2", "name")
#
# user2_data = client.hgetall("user2")
# print("user2 data2", user2_data)

# exists1 = client.hexists("user2","name")
# print(exists1)
#
# exists2 = client.hexists("user2","age")
# print(exists2)

# keys = client.hkeys("user1")
# print(keys)
# all_keys = client.keys("*")
# print(all_keys)

# vals = client.hvals("user1")
# print(vals)

# hash_len = client.hlen("user1")
# print(hash_len)


# ---------------------------------------------------------------

# Sets

# client.sadd("bands", "redvi","queen","metallica", "sod", "asf")
# client.sadd("newbands", "nirvana", "pinkfloyd", "radiohead")
# members = client.smembers("bands")
# print(members)
# client.srem("bands","sod","asf")
# members = client.smembers("bands")
# print(members)
# count = client.scard("bands")
# print(count)
# is_member = client.sismember("bands", "sod")
# print(is_member)
# print(client.sismember("bands", "metallica"))
#
# interation = client.sinter("bands", "newbands")
# print(interation)

# bands = client.smembers("bands")
# newbands = client.smembers("newbands")
# print(f"bands: {bands}")
# print(f"newbands: {newbands}")

# union = client.sunion("bands", "newbands")
# print(f"union: {union}")

# set_diff = client.sdiff("bands", "newbands")
# print(f"set_diff: {set_diff}")
#
# set_diff = client.sdiff("newbands", "bands")
# print(f"set_diff: {set_diff}")

# client.sunionstore('allbands', 'newbands', 'bands')
# client.smove('newbands', 'bands', "radiohead")

# ------------------------------------------------------------


# Sorted Sets

# result = client.zadd("grades", {"mohammad": 50})
# print(result)
# increased_result = client.zincrby("grades", 100, "mohammad")
# print(increased_result)

# client.zadd("grades", {"SAHAR": 1000,"mobina": 1, "Reza":1000})
# ranges = client.zrange("grades", 0, -1)
# print(ranges)
# test = client.zrevrange("grades", 0, -1)
# print(test)
#
# grades = client.zrevrange("grades", 0, -1, withscores=True)
# print(grades)
#
# score = client.zscore("grades", "SAHAR")
# print(score)
#
# reza_rank = client.zrank("grades", "Reza")
# print(reza_rank)
#
# reza_rank_revers = client.zrevrank("grades", "Reza")
# print(reza_rank_revers)
#
# between_range = client.zrangebyscore("grades", "-inf", 600)
# print(between_range)
#
# client.zrem("grades", "SAHAR")
# client.zadd("grades", {
#     "setayesh":600,
#     "ghorbaghe": 900,
#     "elena": 1800
# })
# client.zrem("grades", "elena", "setayesh")

# client.zremrangebyscore("grades","-inf", 500)
# print(client.zcard("grades"))

# print(client.zcount("grades", 800, 1000))
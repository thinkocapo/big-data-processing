# redisClient.saad(timestamp_hour, url)
        # SMEMBERS for timestamp_hour gives you all the URL's


'''
$ docker exec -it 0a1c3f190cdd bash
root@0a1c3f190cdd:/data# redis-cli
127.0.0.1:6379> HSET 2019-09-20:12 www.google.com/url1 true
(integer) 1
127.0.0.1:6379> HGET 2019-09-20:12 www.google.com/url1
"true"
127.0.0.1:6379> HINCRBY 2019-09-20:12 count
(error) ERR wrong number of arguments for 'hincrby' command
127.0.0.1:6379> HINCRBY 2019-09-20:12 count 1
(integer) 1
127.0.0.1:6379> HGET 2019-09-20:12 count
"1"
127.0.0.1:6379> HINCRBY 2019-09-20:12 count 1
(integer) 2
127.0.0.1:6379> HINCRBY 2019-09-20:12 count 1
(integer) 3
127.0.0.1:6379> HGET 2019-09-20:12 count
"3"
127.0.0.1:6379> 
'''
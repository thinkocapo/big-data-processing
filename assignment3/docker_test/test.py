import argparse
import csv
import datetime
import redis

print('HELLO RESIDENT EARTH')


# Create a redis client
# docker network inspect bridge | grep IPv4
redisClient = redis.StrictRedis(host='172.17.0.2',port=6379)
redisClient.set("myfoo", "yourbar")


print('FINISHED LANDING OPERATIONS')


# host='localhost' port=6379
# host='172.17.0.2' port=6379 worked for running docker on host wcap
# host='172.17.0.2',port=8081
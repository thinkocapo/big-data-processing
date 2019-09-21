import redis
print('START')
# why don't have to put the Docker Host IPv4? Is DH getting resolved to localhost? Is localhost getting resolved to DH?
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('foo', 'zoo')
print(r.get('foo'))

print('FINISH')



# ASSIGNMENT3 PROBLEM1 QUERY1 - EXPERIMENT
# timestamp_key = '2019-09-20:12'
# url = 'www.google.com/url6'
# if r.hget(timestamp_key, url) == None:
#     print('IT WAS None')
#     r.hset(timestamp_key, url, 'true')
#     r.hincrby(timestamp_key, 'count', 1)
#     print('Now see if it was set ;)')
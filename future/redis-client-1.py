import redis
print('START')
# why don't have to put the Docker Host IPv4? Is DH getting resolved to localhost? Is localhost getting resolved to DH?
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('foo', 'zoo')
print(r.get('foo'))

print('FINISH')
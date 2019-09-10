import redis
print('START')
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('foo', 'zoo')
print(r.get('foo'))

print('FINISH')
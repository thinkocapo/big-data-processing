```
FLASK_APP=flask-redis.py
FLASK_ENV=development
flask run -p 3001
```

$ FLASK_APP=flask-redis.py flask run -p 3001

https://pypi.org/project/redis/ is redis-py


docker run --name redis-server -d -p 6379:6379 redis

from kafka import KafkaProducer
import random
import time
import uuid

producer = KafkaProducer(bootstrap_servers='172.31.4.229:9092')

var = 1
while var == 1 :
    num = random.randint(0,10)

    uid = uuid.uuid1()
    timestamp = time.time()
    url = 'url{}'.format(random.randint(0,20))
    user = 'user{}'.format(random.randint(0,100))
    value = '%s, %s, %s, %s' % (uid, timestamp, url, user)


    producer.send('hw9events' ,value=value, key=str(num) )
    time.sleep(1/20)

# from assignment8
# producer.send('hw9events', value=bytes(str(num), 'utf-8'), key=bytes(str(num), 'utf-8'))
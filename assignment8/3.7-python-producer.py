
from kafka import KafkaProducer
import time
import random

#producer = KafkaProducer(bootstrap_servers='kafka:32768')

producer = KafkaProducer(bootstrap_servers='localhost:32768')
var = 1
while var == 1 :
    num = random.randint(0,10)
    print(str(num))
    # producer.send('test_topic' ,value=key_bytes(str(num), 'utf-8'), key=str(num) )
    producer.send('test_topic' ,value=bytes(str(num), 'utf-8'), key=bytes(str(num), 'utf-8' ))
    #producer.send('test_topic' ,value=bytes('foo', 'utf-8'), key=str(num) )

    #producer.send('test_topic' ,value=str(num), key=str(num) )
    #producer.send('test_topic', value=b'foo', key=b'bar')
    time.sleep(1)

from kafka import KafkaProducer
import time
import random

#producer = KafkaProducer(bootstrap_servers='kafka:32768')

producer = KafkaProducer(bootstrap_servers='localhost:32768')
var = 1
while var == 1 :
    num = random.randint(0,10)
    print(str(num))
    # producer.send('test_topic' ,value=key_bytes(str(num), 'utf-8'), key=str(num) )
    producer.send('test_topic' ,value=bytes(str(num), 'utf-8'), key=bytes(str(num), 'utf-8' ))
    #producer.send('test_topic' ,value=bytes('foo', 'utf-8'), key=str(num) )

    #producer.send('test_topic' ,value=str(num), key=str(num) )
    #producer.send('test_topic', value=b'foo', key=b'bar')
    time.sleep(1)

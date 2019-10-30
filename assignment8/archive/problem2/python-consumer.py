from kafka import KafkaConsumer
import snappy

var = 1
# "You don't need this infinite loop" but what if finish all the 'message in consumer' below?
while var == 1 :
    consumer = KafkaConsumer(bootstrap_servers='centos_kafka_1:9092',group_id='consumer-1',auto_offset_reset='latest')

    # "No Brokers Available"
    #consumer = KafkaConsumer(bootstrap_servers='localhost:32777',group_id='consumer-1',auto_offset_reset='latest')
    consumer.subscribe(['problem2'])

    for message in consumer:
        print(message)
from kafka import KafkaConsumer

var = 1
# "You don't need this infinite loop" but what if finish all the 'message in consumer' below?
while var == 1 :
    consumer = KafkaConsumer(bootstrap_servers='kafka:9092',group_id='consumer-1',auto_offset_reset='latest')
    #consumer = KafkaConsumer(bootstrap_servers='localhost:32787',client_id="2",group_id='consumer-1',auto_offset_reset='latest')
    consumer.subscribe(['test_topic'])

    for message in consumer:
        print (message)
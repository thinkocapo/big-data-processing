import sys

from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

import os

#
# python - pass the 0.8
# class functions + attributes could be different?
# 0.10 has SSL / TLS support




# --packages org.apache.spark:spark-streaming-kafka...

'''
by default takes from latest offset, in KafkaUtils.createDirectStream w kafkaParams
'''


if __name__ == "__main__":
    print('000000000000000000')
    # Create Spark Context
    sc = SparkContext(appName="PythonStreamingDirectKafkaCount")
    ssc = StreamingContext(sc, 2)

    brokers, topic = sys.argv[1:]

    print(brokers)
    print(topic)

    print('1111111111111111111')


    sc.setLogLevel("WARN")

    #Create a DStream that will connect to Kafka
#    kafkaParams = {"metadata.broker.list": brokers, "auto.offset.reset": "smallest"}
    kafkaParams = {"metadata.broker.list": brokers}
    kafkaStream = KafkaUtils.createDirectStream(ssc, [topic], kafkaParams)


    def parse_log_line(line):
        # (uuid, timestamp, url, user, region, browser, platform, cd, ttf) = line.strip().split(",")
        (uuid, timestamp, url, user) = line.strip().split(",")
        hour = timestamp[0:13]
        return (hour, 1)

    # STEPS - problem1
    '''
        configure your Spark Streaming job to read data from the "hw9events" Kafka topic, with the batch window of 1 sec
        implement a job that :
        counts the number of clicks per URL per batch and prints the results after each batch
        counts the running total of clicks per URL and prints the results after each batch as well
    
        DOCUMENTATION
        https://spark.apache.org/docs/latest/streaming-programming-guide.html updateStateByKey *example*
        https://spark.apache.org/docs/2.1.0/api/python/pyspark.streaming.html
        rolling count
    '''

    lines = kafkaStream.map(lambda x: x[1])
    clicks = lines.map(parse_log_line)\
        .reduceByKey(lambda a, b: a + b)


    # clicks.pprint() won't execute till after ssc.start(), that's why you don't see anything logged between 222222 and 333333
    print('22222222222222222222\n')
    clicks.pprint()
    print('\n333333333333333333')


    # Start the computation
    ssc.start()
    # Wait for the computation to terminate
    ssc.awaitTermination()

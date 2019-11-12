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

if __name__ == "__main__":
    # Create Spark Context
    sc = SparkContext(appName="PythonStreamingDirectKafkaCount")
    ssc = StreamingContext(sc, 1) # batch window 1-second
    ssc.checkpoint("checkpoint")
    brokers, topic = sys.argv[1:]
    print(brokers)
    print(topic)
    sc.setLogLevel("WARN")
    #Create a DStream that will connect to Kafka
#    kafkaParams = {"metadata.broker.list": brokers, "auto.offset.reset": "smallest"}

    kafkaParams = {"metadata.broker.list": brokers}
    kafkaStream = KafkaUtils.createDirectStream(ssc, [topic], kafkaParams)

    def parse_log_line(line):
        # (uuid, timestamp, url, user, region, browser, platform, cd, ttf) = line.strip().split(",")
        (uuid, timestamp, url, user) = line.strip().split(",")
        return (user, 1)

    # RDD with initial state (key, value) pairs
    initialStateRDD = sc.parallelize([(u' user1', 0), (u' user2', 0)])


    dStream = kafkaStream.map(lambda x: x[1])
    # problem3
    urls = dStream.map(parse_log_line)

        # .groupByKey()\
        # .countByValue()
        # .countApproxDistinct()
        # .reduceByKeyAndWindow(lambda x, y: x + y, lambda x, y: x - y, 30, 30)\

    # executes after ssc.start()
    urls.foreachRDD(lambda rdd: rdd.countApproxDistinct())
    # urls.pprint()

    # .reduceByKeyAndWindow(lambda x, y: x + y, lambda x, y: x - y, 5, 5) # problem2
    # .window(5,5) #problem2
    # .updateStateByKey(updateFunc, initialRDD=initialStateRDD) #problem2 prob wrong
    # .reduceByKey(lambda a, b: a + b) #problem1
    # def updateFunc(new_values, last_sum):
    #     return sum(new_values) + (last_sum or 0)

    # Start the computation
    ssc.start()
    # Wait for the computation to terminate
    ssc.awaitTermination()

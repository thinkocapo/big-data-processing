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
        return (url, 1)

    # RDD with initial state (key, value) pairs
    initialStateRDD = sc.parallelize([(u' url1', 0), (u' url2', 0)])

    def updateFunc(new_values, last_sum):
        return sum(new_values) + (last_sum or 0)

    lines = kafkaStream.map(lambda x: x[1])
    # executes/prints once-per-batch
    clicks = lines.map(parse_log_line)\
        .window(lambda a, b: a + b, 5,5) # failed
        # .reduceByKeyAndWindow(lambda a, b: a + b, 5,5) # failed
        # .updateStateByKey(updateFunc, initialRDD=initialStateRDD) #problem2
        # .reduceByKey(lambda a, b: a + b) #problem1

    # executes after ssc.start()
    clicks.pprint()


    # Start the computation
    ssc.start()
    # Wait for the computation to terminate
    ssc.awaitTermination()

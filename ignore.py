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

    # Create Spark Context
    sc = SparkContext(appName="PythonStreamingDirectKafkaCount")

    ssc = StreamingContext(sc, 1) # 1 is batch window/interval/duration
    brokers, topic = sys.argv[1:]
    print(brokers)
    print(topic)
    sc.setLogLevel("WARN")
    #Create a DStream that will connect to Kafka
#    kafkaParams = {"metadata.broker.list": brokers, "auto.offset.reset": "smallest"}

    kafkaParams = {"metadata.broker.list": brokers}
    kafkaStream = KafkaUtils.createDirectStream(ssc, [topic], kafkaParams)

    def parse_log_line(line):
        (uuid, timestamp, url, user) = line.strip().split(",")
        return (url, 1)
    lines = kafkaStream.map(lambda x: x[1])
    clicks = lines.map(parse_log_line)\
        .reduceByKey(lambda a, b: a + b)

    # clicks.pprint() won't execute till after ssc.start()
    clicks.pprint()

    # Start the computation
    ssc.start()
    # Wait for the computation to terminate
    ssc.awaitTermination()

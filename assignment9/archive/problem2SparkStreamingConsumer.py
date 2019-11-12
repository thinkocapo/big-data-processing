import sys
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import os

if __name__ == "__main__":
    
    sc = SparkContext(appName="PythonStreamingDirectKafkaCount")
    ssc = StreamingContext(sc, 1)
    ssc.checkpoint("checkpoint")
    brokers, topic = sys.argv[1:]
    print(brokers)
    print(topic)
    sc.setLogLevel("WARN")

    kafkaParams = {"metadata.broker.list": brokers}
    kafkaStream = KafkaUtils.createDirectStream(ssc, [topic], kafkaParams)

    def parse_log_line(line):
        (uuid, timestamp, url, user) = line.strip().split(",")
        return (user, 1)

    DStream = kafkaStream.map(lambda x: x[1])

    clicks = DStream.map(parse_log_line)
        .reduceByKeyAndWindow(lambda x, y: x + y, lambda x, y: x - y, 5, 5)

    clicks.pprint()

    # Start the computation
    ssc.start()
    # Wait for the computation to terminate
    ssc.awaitTermination()

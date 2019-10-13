import sys
import datetime
from pyspark import SparkContext
from pyspark.sql import SparkSession


if __name__ == "__main__":

    # Create a SparkContext and a Spark Session
    sc=SparkContext(master="local[4]")
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

    # Create a dataframe from the csv
    df = spark.read.load("s3a://inputfilesassignment4/wordcount/", format="csv")

    # Write the datagrame as a parquet in HDFS
    df.write.parquet('hdfs:///user/hadoop/parquet1')

    sc.stop()

    # works
    # count = df.count()
    # print('\n~~~~~~~~~ count {}'.format(count))
    # first = df.head()
    # print('\n~~~~~~~~~ first {}'.format(first))
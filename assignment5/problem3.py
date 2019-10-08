'''
P2 and P3 - data frames. 
Since we did not mention it explicitly - you can use SQL as well, but try to use data frames to get a more versatile experience
'''
# parquetDF = ... read
# parquetDF.groupBy('day:hour', 'country')\
#     .agg(countDistinct('url'))\
#     .orderBy('hour', 'country')\
#     .collect()

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

    # # Create a dataframe from the csv
    # df = spark.read.load("s3a://inputfilesassignment4/wordcount/", format="csv")
    # # Write the datagrame as a parquet in HDFS
    # df.write.parquet('hdfs:///user/hadoop/parquet1')

    df_parquet = spark.read.load('hdfs:///user/hadoop/parquet1')
    # works
    count = df_parquet.count()
    print('\n~~~~~~~~~ count {}'.format(count))
    first = df_parquet.head()
    print('\n~~~~~~~~~ first {}'.format(first))

    sc.stop()
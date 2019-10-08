'''
P2 and P3 - data frames. 
Since we did not mention it explicitly - you can use SQL as well, but try to use data frames to get a more versatile experience
'''

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

    df_parquet_no_schema = spark.read.parquet('hdfs:///user/hadoop/parquet1')
    print('11111111111')
    parts = df_parquet_no_schema.rdd.map(lambda l: l.split(","))
    # turn timestamp into day/hour
    dateHour_country = parts.map(lambda p: Row(timestamp=p[1],url=p[2],user=p[3],country=p[4]))
    df_parquet = spark.createDataFrame(dateHour_country)
    print('22222222222')
    df_parquet.groupBy('timestamp', 'country')\
        .agg(countDistinct('url'))\
        .orderBy('timestamp', 'country')\
        .collect()

    # ORIGINAL 
    # df_parquet = spark.read.load('hdfs:///user/hadoop/parquet1')
    # works
    count = df_parquet.count()
    print('\n~~~~~~~~~ count {}'.format(count))
    first = df_parquet.head()
    print('\n~~~~~~~~~ first {}'.format(first))

    sc.stop()


    # ORIGINAL
    # df_parquet.groupBy('day:hour', 'country')\
    #     .agg(countDistinct('url'))\
    #     .orderBy('hour', 'country')\
    #     .collect()
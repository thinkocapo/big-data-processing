import sys
import datetime
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

'''
unique_urls_by_country_by_hour_for_time_range
'''
if __name__ == "__main__":

    # Create a SparkContext and a Spark Session
    sc=SparkContext(master="local[4]")
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
    df_parquet = spark.read.parquet('hdfs:///user/hadoop/parquet2')

    # WRONG - need date:hour instead of timestamp, at least according to classmate's example.
    df_parquet.groupBy('timestamp', 'country')\
        .agg(countDistinct('url'))\
        .orderBy('timestamp', 'country')\
        .collect()

    # ORIGINAL 
    # df_parquet = spark.read.load('hdfs:///user/hadoop/parquet1')
    
    # UPDATED
    count = df_parquet.count()
    print('\n++++++ Count {}'.format(count))
    first = df_parquet.head()
    print('\n++++++ First {}'.format(first))

    for item in df_parquet.rdd.collect():
        print(item)

    sc.stop()
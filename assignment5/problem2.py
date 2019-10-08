import sys
import datetime
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *

if __name__ == "__main__":

    # Create a SparkContext and a Spark Session
    sc=SparkContext(master="local[4]")
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

    # Create a dataframe from the csv
    schema = StructType([
        StructField('uuid', StringType(), True),
        StructField('timestamp', TimestampType(), True),
        StructField('url', StringType(), True),
        StructField('user', StringType(), True),
        StructField('country', StringType(), True),
    ])
    
    # ORIGINAL - no schema
    # df = spark.read.load("s3a://inputfilesassignment4/wordcount/", format="csv")
    
    # UPDATED - has schema
    df = spark.read.format('csv').schema(schema).load("s3a://inputfilesassignment4/wordcount/")

    # Write the datagrame as a parquet in HDFS
    df.write.parquet('hdfs:///user/hadoop/parquet2')

    sc.stop()

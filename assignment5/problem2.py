import sys
import datetime
from pyspark import SparkContext
from pyspark.sql import SparkSession
'''
P2 and P3 - data frames. 
Since we did not mention it explicitly - 
you can use SQL as well, 
but try to use data frames to get a more versatile experience
'''

if __name__ == "__main__":
    sc=SparkContext(master="local[4]")
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
    print('\n1111111111')


    # sqlContext = SQLContext(sc)
    
    # schema = StructType([
    #         StructField("col1", IntegerType(), True),
    #         StructField("col2", IntegerType(), True),
    #         StructField("col3", StringType(), True),
    #         StructField("col4", StringType(), True),
    #         StructField("col5", StringType(), True),
    #         StructField("col6", DoubleType(), True)])
    
    # rdd = sc.textFile("s3a://inputfilesassignment4/wordcount/").map(lambda line: line.split(","))
    # print('4444444444')
    
    # df = sqlContext.createDataFrame(rdd, schema)
    # print('5555555')

    df = spark.read.load("s3a://inputfilesassignment4/wordcount/", format="csv")
    print('\n2222222222')

    # df.write.parquet('/home/hadoop/parquets/parquet1')
    # TODO try writing to hdfs instead?
    # print('\n333333333')


    # WORKS 8:01
    count = df.count()
    print('\n~~~~~~~~~ count {}'.format(count))

    first = df.head()
    print('\n~~~~~~~~~ first {}'.format(first))






'''
https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html
df = spark.read.load("examples/src/main/resources/people.csv",
                    format="csv", sep=":", inferSchema="true", header="true")
'''
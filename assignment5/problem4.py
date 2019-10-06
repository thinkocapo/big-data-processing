from __future__ import print_function
import sys
from random import random
from operator import add
# from pyspark.sql import SparkSession # Spark SQL
from pyspark import SparkContext

if __name__ == "__main__":
    """
        Usage: pi [partitions]
    """
    spark = SparkSession\
        .builder\
        .appName("problem1")\
        .getOrCreate()
    spark.sparkContext.setLogLevel("WARN")
    partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    

    # def f(_):
    #     x = random() * 2 - 1
    #     y = random() * 2 - 1
    #     return 1 if x ** 2 + y ** 2 < 1 else 0
    # spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
    

    spark.stop()


# sudo spark-submit --master yarn pi.py 5

from __future__ import print_function
import sys
from random import random
from operator import add
from pyspark import SparkContext

if __name__ == "__main__":

    sc=SparkContext(master="local[4]")
    print(sc)


    linesRDD = sc.textFile("s3a://inputfilesassignment4/wordcount/")
    rdd = sc.textFile("s3a://inputfilesassignment4/wordcount/")
    print(len(rdd))
    

    def mapper(line):
        print('line')

    def reducer(string):
        print('reducer')

    rdd.map(mapper)
    rdd.reduce(reducer)

    rdd.collect()

    spark.stop()


# sudo spark-submit --master yarn pi.py 5

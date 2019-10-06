from __future__ import print_function
import sys
from random import random
from operator import add
from pyspark import SparkContext

if __name__ == "__main__":

    sc=SparkContext(master="local[4]")
    print(sc)


    # csvRDD = parallelize(csvfile....)
    # csvRDD.map/reduce()


    spark.stop()


# sudo spark-submit --master yarn pi.py 5

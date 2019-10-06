from __future__ import print_function
import sys
import datetime
from random import random
from operator import add
from pyspark import SparkContext


'''
sudo spark-submit --master yarn problem1.py
'''
if __name__ == "__main__":
    sc=SparkContext(master="local[4]")

    rdd1 = sc.textFile("s3a://inputfilesassignment4/wordcount/")

    def mapper1(_line):
        line = _line.split(",")
        timestamp = line[1]
        url = line[2]
        # Prepare a Date object from parsed csv timestamp
        date = datetime.time()
        try:
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError: 
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
        # Ensure that day and month are always 2-digits instead of 1-digit
        day = date.day
        if len(str(day)) == 1:
            day = '0{}'.format(day)
        month = date.month
        if len(str(month)) == 1:
            month = '0{}'.format(month)
        hour = date.hour
        if len(str(hour)) == 1:
            hour = '0{}'.format(hour)
        # Prepare a key in form <timestamp>:<hour>_<url>parquetDF.groupBy('day:hour', 'country')\
        timestamp_hour = '%s-%s-%s-%s' % (date.year, month, day, hour)
        timestamp_hour_url = '%s_%s' % (timestamp_hour, url)
        return (timestamp_hour, url)

    # MAP
    rdd2 = rdd1.map(mapper1)
    
    # REDUCE
    rdd3 = rdd2.distinct().groupByKey().sortByKey()    

    # print('\n ~~~~~~~~~~~ RDD4 {} \n'.format(rdd4.take(10)))
    for obj1, obj2 in rdd3.collect():
        print(obj1, len(obj2))

    sc.stop()

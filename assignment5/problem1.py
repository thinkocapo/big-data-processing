from __future__ import print_function
import sys
import datetime
from random import random
from operator import add
from pyspark import SparkContext
'''
parquetDF.groupBy('day:hour', 'country')\
    .agg(countDistinct('url'))\
    .orderBy('hour', 'country')\
    .collect()
'''

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
    print('\n ~~~~~~~~~~~ first {} \n'.format(rdd2.first()))

    # REDUCE
    # def reducer1(v1, v2):
    #     print('reducer1')

    # groupByKey() ?
    # reduceByKey() ?
    # rdd3 = rdd2.reduce(reducer1) 
    # print('\n ~~~~~~~~~~~ second {} '.format(rdd3.first()))


    rdd2.collect()
    sc.stop()


# sudo spark-submit --master yarn pi.py 5

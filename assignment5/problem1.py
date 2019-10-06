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

    # linesRDD = sc.textFile("s3a://inputfilesassignment4/wordcount/")
    rdd_csv = sc.textFile("s3a://inputfilesassignment4/wordcount/")


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
        # Prepare a key in form <timestamp>:<hour>
        timestamp_hour = '%s-%s-%s-%s' % (date.year, month, day, hour)
        timestamp_hour_url = '%s_%s' % (timestamp_hour, url)
        return timestamp_hour_url

    # MAP
    rdd_csv_mapped = rdd_csv.map(mapper1)
    print('\n ~~~~~~~~~~~ first {} \n'.format(rdd_csv_mapped.first()))

    # REDUCE
    # def reducer1(string):
    #     print('reducer')

    # rdd_csv_reduced = rdd_csv_mapped.reduce(reducer1)
    # print('\n ~~~~~~~~~~~ second {} '.format(rdd_csv_reduced.first()))


    print('\n ~~~~~~~~~~~~ count is {} \n'.format(rdd_csv_mapped.count()))
    
    
    rdd.collect()

    sc.stop()


# sudo spark-submit --master yarn pi.py 5

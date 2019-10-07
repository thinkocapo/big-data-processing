import sys
import datetime
from pyspark import SparkContext

'''
Get count of unique visitors per URL per hour
sudo spark-submit --master yarn problem1query1.py
sudo spark-submit --master yarn problem1query2.py
'''
if __name__ == "__main__":
    sc=SparkContext(master="local[4]")

    rdd1 = sc.textFile("s3a://inputfilesassignment4/wordcount/")

    def mapper2(_line):
        line = _line.split(",")
        timestamp = line[1]
        url = line[2]
        user = line[3]
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
        # Prepare a key in form <timestamp>:<hour>_<url>
        dateHour = '%s-%s-%s:%s' % (date.year, month, day, hour)
        dateHour_url = '%s_%s' % (dateHour, url)
        return (dateHour_url, user)

    # MAP
    rdd2 = rdd1.map(mapper2)
    
    # REDUCE
    rdd3 = rdd2.distinct().groupByKey().sortByKey()    

    # Print output
    for dateHour_url, users_distinct in rdd3.collect():
        print(dateHour_url, len(users_distinct))

    sc.stop()

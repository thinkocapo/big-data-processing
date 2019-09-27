#!/usr/bin/python3
import csv
import datetime
import sys

# hadoop jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount s3a://inputfilesassignment4/file-input1.csv s3a://inputfilesassignment4/wordcount

# Unique URLs per Hour
for line_in in sys.stdin:

    try:
        line = line_in.split(",")

        # TRY THIS
        # for col in line

        # timestamp = line[1]
        # url = line[2]

        timestamp = line[1]
        url = line[2]

        date = datetime.time()
        
        # Prepare a key in the form of <timestamp>:<hour>
        try:
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError: 
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')

        day = date.day
        if len(str(day)) == 1:
            day = '0{}'.format(day)
        month = date.month
        if len(str(month)) == 1:
            month = '0{}'.format(month)
        hour = date.hour
        if len(str(hour)) == 1:
            hour = '0{}'.format(hour)

        timestamp_hour = '%s-%s-%s:%s' % (date.year, month, day, hour)

        # Prepare a key
        timestamp_hour_url = '%s-%s' % (timestamp_hour, url)

        # Output, stdout
        # print('%s\t%d' % (timestamp_hour_url, 1))
        print('%s\t%d' % (timestamp_hour, 1))


    except ValueError as e:
        continue


# print("\nMapper-1 Process Completed")


#!/usr/bin/python3
# import argparse
import csv
import datetime
import sys

# hadoop jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount s3a://inputfilesassignment4/file-input1.csv s3a://inputfilesassignment4/wordcount
'''
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -file ./mapper-1.py -mapper ./mapper-1.py -file ./reducer-1.py -reducer
./reducer-1.py -input inputfilesassignment4/ -output wordcount1

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
    -file ./mapper-1.py \
    -mapper ./mapper-1.py \ 
    -file ./reducer-1.py \
    -reducer ./reducer-1.py \
    -input s3a://inputfilesassignment4/ \
    -output s3a://inputfilesassignment4/wc1
'''

field_names = ['uuid', 'timestamp', 'url', 'userId', 'country', 'ua_browser', 'ua_os', 'response_status', 'TTFB']


# Unique URLs per Hour
for line in sys.stdin:
    # TRY THIS
    # fields = line.split(",")

    # TRY THIS
    # for col in line

    timestamp = line[1]
    url = line[2]
    date = datetime.time()
    
    # Prepare a key in the form of <timestamp>:<hour>
    try:
        date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
    except ValueError: 
        date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
    timestamp_hour = '%s-%s-%s:%s' % (date.year, date.month, date.day, date.hour)

    # Prepare a key
    timestamp_hour_url = '%s-%s' % (timestamp_hour, url)

    # Output, stdout
    print('%s\t%s' % (timestamp_hour_url, 1))


# print("\nMapper-1 Process Completed")


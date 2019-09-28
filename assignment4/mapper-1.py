#!/usr/bin/python3

import datetime
import sys

# cat file-input1.csv | mapper-1.py | sort | reducer-1.py

# Unique URLs per Hour
for line_in in sys.stdin:
    # IF parsing csv...
    # import fileinput
    # for line in fileinput.input():
    # line = line.split(",")
    try:
        # Prepare the timestamp and url in python
        line = line_in.split(",")
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
  
        # was needed?
        # print(timestamp_hour)

        # K,V Output as stdout in form <YYYY-MM-DD-HH_URL, 1>
        print('%s\t%d' % (timestamp_hour_url, 1))

    except ValueError as e:
        continue

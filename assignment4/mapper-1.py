#!/usr/bin/python3

import datetime
import sys


# Unique URLs per Hour
for line_in in sys.stdin:

    try:
        line = line_in.split(",")

        timestamp = line[1]
        url = line[2]

        date = datetime.time()
        
        # Prepare a Date object from parsed csv timestamp
        try:
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError: 
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')

        # fix the zero's
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
        timestamp_hour = '%s-%s-%s:%s' % (date.year, month, day, hour)
        timestamp_hour_url = '%s-%s' % (timestamp_hour, url)

        # K,V Output as stdout
        print('%s\t%d' % (timestamp_hour_url, 1))


    except ValueError as e:
        continue


# print("\nMapper-1 Process Completed")


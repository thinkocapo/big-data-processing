#!/usr/bin/python3
# /Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import datetime
import sys

# Query2: get count of unique visitors per URL per hour
import fileinput
# for line_in in sys.stdin:
for line in fileinput.input():

    try:
        # Prepare the timestamp and url in python
        line = line.split(",")
        timestamp = line[1]
        url = line[2]
        user = line[3]
        country = line[4]

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
        timestamp_hour_country = '%s_%s' % (timestamp_hour, country)

        # make sure it's within time range
        timestamp_hour_comparison = '%s%s%s%s' % (date.year, month, day, hour)
        if int(timestamp_hour_comparison) < 2019091305 or int(timestamp_hour_comparison) > 2019091409:
            continue
  
        # K,V Output as stdout in form <YYYY-MM-DD-HH-COUNTRY, URL>
        print('%s\t%s' % (timestamp_hour_country, url))

    except ValueError as e:
        continue

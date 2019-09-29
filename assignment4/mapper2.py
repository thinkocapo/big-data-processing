#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import datetime
import sys

# testing
# cat file-input1.csv | mapper-1.py | sort | reducer-1.py

# Query2: get count of unique visitors per URL per hour
import fileinput
# for line_in in sys.stdin:
for line in fileinput.input():
    # IF parsing csv...
    try:
        # Prepare the timestamp and url in python
        line = line.split(",")
        # line = line_in.split(",")
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

        # Prepare a key in form <timestamp>:<hour>
        timestamp_hour = '%s-%s-%s-%s' % (date.year, month, day, hour)
        timestamp_hour_url = '%s_%s' % (timestamp_hour, url)
  
        # K,V Output as stdout in form <YYYY-MM-DD-HH, user>
        print('%s\t%s' % (timestamp_hour_url, user))

    except ValueError as e:
        continue

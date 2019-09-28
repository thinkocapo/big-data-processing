#!/usr/bin/python3

import sys

current_timestampHour_url = None
current_count = 1

for line in sys.stdin:
    try:
        timestampHour_url, count = line.strip().split('\t')

        if current_timestampHour_url:
            if timestampHour_url == current_timestampHour_url:
                current_count += int(count)
            else:
                print ("%s\t%d" % (current_timestampHour_url, current_count))
                current_count = 1
        current_timestampHour_url = timestampHour_url
    except ValueError as e:
        continue

if current_count > 1:
    print ("%s\t%d" % (current_timestampHour_url, current_count))
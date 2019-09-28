#!/usr/bin/python3

import sys
import fileinput

current_timestampHour_url = None
current_count = 1

timestampHour_url_dict = {}
timestampHour_dict = {}

for line in sys.stdin:
    try:
        timestampHour, url = line.strip().split('\t')
        if timestampHour in timestampHour_dict:
            if url in timestampHour_dict[timestampHour]:
                timestampHour_dict[timestampHour][url] = timestampHour_dict[timestampHour][url] + 1
            else:
                timestampHour_dict[timestampHour][url] = 1
        else:
            timestampHour_dict[timestampHour] = {}
            timestampHour_dict[timestampHour][url] = 1

    except ValueError as e:
        continue

    for timestampHour in timestampHour_dict:
        url_count = len(timestampHour_dict[timestampHour].keys())
        print("%s\t%d" % (timestampHour, url_count))

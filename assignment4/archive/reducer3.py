#!/usr/bin/python3

import sys
import fileinput

current_date_hour_url = None
date_hour_url = None
_dict = {}

# YYYY-MM-DD:H1:URL1 +1
# YYYY-MM-DD:H1:URL1 +2
# YYYY-MM-DD:H1:URL1 +3
# YYYY-MM-DD:H1:URL2 +1

# Query3 - Unique Events per URL Hour per Date
for line in sys.stdin:
    try:
        date_hour_url, count = line.strip().split('\t')
        if current_date_hour_url:
            # "if the one in iteration is same as previous..."
            if date_hour_url == current_date_hour_url:
                # depending on if it's in dict, we +1 or start at 1
                if date_hour_url in _dict:
                    _dict[date_hour_url] += 1
                else:
                    _dict[date_hour_url] = 1
            else:
                # if on to a new date_hour_url then print count for the previous
                if current_date_hour_url in _dict:
                    print ("%s\t%d" % (current_date_hour_url, _dict[current_date_hour_url]))
                _dict = {}
                _dict[date_hour_url] = 1
                
        current_date_hour_url = date_hour_url

    except ValueError as e:
        continue
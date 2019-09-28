#!/usr/bin/python3

import sys

current_timestampHour = None
_dict = {}

for line in sys.stdin:
    try:
        # This info comes in as <YYYY-MM-DD-HH_URL, 1>
        timestampHour_url, count = line.strip().split('\t')

        # Underscore '_' was used to split because using colon ':' interferred with URL's like https://
        split = timestampHour_url.split('_')
        timestampHour = '%s:%s' % (split[0][:-3], split[0][-2:])
        url = split[1]

        # This will sort in all the URL's for the timestampHour, until it changes, and the timestampHours are coming into reducer-1.py sorted
        if current_timestampHour:
            # If it finds the same timestamp in next sys.stdin line...then...
            if timestampHour == current_timestampHour:
                if timestampHour in _dict:
                    # Record each URL key and find the number of keys later
                    if url in _dict[timestampHour]:
                        _dict[timestampHour][url] += 1
                    else:
                        _dict[timestampHour][url] = 1
                else:
                    _dict[timestampHour] = {}
                    _dict[timestampHour][url] = 1
            else:
                # Done with line inputs for the current timestamp, so write out how many URL keys were for the current timestamp
                print ("%s\t%d" % (current_timestampHour, len(_dict[current_timestampHour].keys())) )
                
                # Reset the dict for the next timestamp (increment by hour) that's now in the reducer'
                _dict = {}
                _dict[timestampHour] = {}
                _dict[timestampHour][url] = 1
        
        # Start working on the next timestamp and hour's range of lines in the csv
        current_timestampHour = timestampHour

    except ValueError as e:
        continue

print ("%s\t%d" % (current_timestampHour, len(_dict[current_timestampHour].keys()) ))
#!/usr/bin/python3

import sys
import fileinput

current_timestampHour_url = None
current_count = 1

timestampHour_url_dict = {}
timestampHour_dict = {}

for line in sys.stdin:
    try:
        timestampHour, count = line.strip().split('\t')
        if timestampHour in timestampHour_dict:
            timestampHour_dict[timestampHour] = timestampHour_dict[timestampHour] + 1
        else:
            timestampHour_dict[timestampHour] = 1


        # timestampHour_url, count = line.strip().split('\t')

        # if timestampHour_url in timestampHour_url_dict:
        #     timestampHour_url_dict[timestampHour_url] = timestampHour_url_dict[timestampHour_url] + 1
        # else:
        #     timestampHour_url_dict[timestampHour_url] = 1

    except ValueError as e:
        continue

    for timestampHour in timestampHour_dict:
        count = timestampHour_dict[timestampHour]
        print("%s\t%s" % (timestampHour, count))

# ?????????
# if current_count > 1:
#     # Output
#     print ("%s\t%d" % (current_timestampHour_url, current_count))

# if it's sorted then it will match
# if current_timestampHour_url:
#     if timestampHour_url == current_timestampHour_url:
#         current_count += int(count)
#     else:
#         # Output
#         print ("%s\t%d" % (current_timestampHour_url, current_count))
#         current_count = 1
# current_timestampHour_url = timestampHour_url

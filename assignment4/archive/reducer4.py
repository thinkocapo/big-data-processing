#!/usr/bin/python3
# /Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import sys
current_date_hour_country = None
date_hour_country = None
_dict = {}

# YYYY-MM-DD:H1:COUNTRY URL1
# YYYY-MM-DD:H1:COUNTRY URL2

# Query4: unique_urls_by_country_by_hour_for_time_range
for line in sys.stdin:
    try:
        date_hour_country, url = line.strip().split('\t')
        
        if current_date_hour_country:
            if date_hour_country == current_date_hour_country:
                if date_hour_country in _dict:
                    # If url already seen for this date_hour_country then increment
                    if url in _dict[date_hour_country]:
                        _dict[date_hour_country][url] += 1
                    # it's a new url for this date_hour_country
                    else:
                        _dict[date_hour_country][url] = 1
                else:
                    # first time reducer sees this date_hour_country
                    _dict[date_hour_country] = {}
                    _dict[date_hour_country][url] = 1
            else:
                # no more of the current_date_hour_country in the sorted input coming in, so print   
                if current_date_hour_country in _dict:
                    print ("%s\t%d" % (current_date_hour_country, len(_dict[current_date_hour_country].keys())))
                _dict = {}
                _dict[date_hour_country] = {}
                _dict[date_hour_country][url] = 1
        current_date_hour_country = date_hour_country

    except ValueError as e:
        continue


print ("%s\t%d" % (current_date_hour_country, len(_dict[current_date_hour_country].keys()) ))
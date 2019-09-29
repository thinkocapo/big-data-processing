#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import sys

current_date_hour_url = None
date_hour_url = None
_dict = {}

# YYYY-MM-DD:H1:URL1 user1
# YYYY-MM-DD:H1:URL1 user2
# YYYY-MM-DD:H1:URL2 user3
# YYYY-MM-DD:H2:URL3

# Query2: get count of unique visitors per URL per hour
for line in sys.stdin:
    try:
        date_hour_url, user = line.strip().split('\t')
        
        if current_date_hour_url:
            if date_hour_url == current_date_hour_url:
                if date_hour_url in _dict: 
                    if user in _dict[date_hour_url]:
                        _dict[date_hour_url][user] += 1
                    else:
                        _dict[date_hour_url][user] = 1
                else:
                    _dict[date_hour_url] = {}
                    _dict[date_hour_url][user] = 1
            else:        
                if current_date_hour_url in _dict:
                    print ("%s\t%d" % (current_date_hour_url, len(_dict[current_date_hour_url].keys())))
                _dict = {}
                _dict[date_hour_url] = {}
                _dict[date_hour_url][user] = 1
        current_date_hour_url = date_hour_url

    except ValueError as e:
        continue


print ("%s\t%d" % (current_date_hour_url, len(_dict[current_date_hour_url].keys()) ))
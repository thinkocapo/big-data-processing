import argparse
import csv
import datetime
import redis


field_names = ['uuid', 'timestamp', 'url', 'userId', 'country', 'ua_browser', 'ua_os', 'response_status', 'TTFB']

def query1_unique_urls_per_hour(file_name):
    print('\n~~~~~~~~~ query1_unique_urls_per_hour ~~~~~~~~~')
    input_file = csv.DictReader(open(file_name), fieldnames=field_names)
    url_map = {}
    for row in input_file:
        timestamp = row['timestamp']
        url = row['url']
        date = datetime.time()
        try:
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError: 
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
        timestamp_hour = '%s-%s-%s:%s' % (date.year, date.month, date.day, date.hour)

        if redisClient.hget(timestamp_hour, url) == None:
            redisClient.hset(timestamp_hour, url, 'true')
            redisClient.hincrby(timestamp_hour, 'count', 1)
        # NOT SURE WHY NONE OF THIS WOULD EXECUTE...
        # with redisClient.pipeline() as pipe:
        # pipe.watch(timestamp_hour)
        # pipe = redisClient.pipeline()
        # pipe.multi()
        # if pipe.hget(timestamp_hour, url) == None:
        #     print('\n {} \n'.format(timestamp_hour))
        #     pipe.hset(timestamp_hour, url, 'true')
        #     pipe.hincrby(timestamp_hour, 'count', 1)
        # pipe.execute()
    return

query1_unique_urls_per_hour(file_name)
print("\nMapper Process Completed")


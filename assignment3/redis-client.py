import argparse
import csv
import datetime
import redis

# Argument Parser
prog = "assignment3"
desc = "Process data provided by log files and return query results"
parser = argparse.ArgumentParser(prog=prog, description=desc)
parser.add_argument("query", type=str, help="query1 | query2 | query3 | query4")
parser.add_argument('--logs-directory', '-ld', required=False, help="Directory where the log files are stored.")
parser.add_argument('--file', '-file', required=False, help="Name of the  log file are stored")

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


def query2_unique_visitors_per_url_per_hour(file_name):
    print('query2')
    input_file = csv.DictReader(open(file_name), fieldnames=field_names)
    for row in input_file:
        timestamp = row['timestamp']
        url = row['url']
        date = datetime.time()
        userId = row['userId']
        try:
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError: 
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
        # Prepare a timestamp string that we want to write into Redis shared state
        timestamp_hour = '%s-%s-%s:%s' % (date.year, date.month, date.day, date.hour)
        full_key = '%s:%s' % (timestamp_hour, url)

        # Write to Redis
        if redisClient.hget(full_key, userId) == None:
            redisClient.hset(full_key, userId, 'true')
            redisClient.hincrby(full_key, 'count', 1)
    return


def query3_unique_events_per_url_per_hour(file_name):
    print('query3')
    input_file = csv.DictReader(open(file_name), fieldnames=field_names)
    for row in input_file:
        timestamp = row['timestamp']
        url = row['url']
        date = datetime.time()
        userId = row['userId']
        try:
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError: 
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
        # Prepare a timestamp string that we want to write into Redis shared state
        timestamp_hour = '%s-%s-%s:%s' % (date.year, date.month, date.day, date.hour)

        redisClient.hincrby(timestamp_hour, url, 'true')
        redisClient.hincrby(timestamp_hour, count, 1)
    return

def query4_unique_urls_by_country_by_hour_for_time_range(file_name):
    print('query4')
    input_file = csv.DictReader(open(file_name), fieldnames=field_names)
    for row in input_file: 
        timestamp = row['timestamp']
        url = row['url']
        date = datetime.time()
        country = row['country']

        # Format dates, make sure single-digits are pre-pended with a '0'
        # Prepare a timestamp string that we want to write into Redis shared state
        try:
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError: 
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
        if len(date.day) == 1:
            date.day = '0{}'.format(date.day)
        if len(date.month) == 1:
            date.month = '0{}'.format(date.month)
        if len(date.hour) == 1:
            date.hour = '0{}'.format(date.hour)
        timestamp_hour = '%s-%s-%s:%s' % (date.year, date.month, date.day, date.hour)
        timestamp_hour_country = '%s:%s' % (timestamp_hour, country)

        # make sure is within timerange
        timestamp_hour_comparison = '%s%s%s%s' % (date.year, date.month, date.day, date.hour)
        if timestamp_hour_comparison < 2019091305 or timestamp_hour_comparison > 2019091409:
            continue
        if redisClient.hget(timestamp_hour_country, url) == None:
            redisClient.hset(timestamp_hour_country, url, 'true')
            redisClient.hincrby(timestamp_hour_country, 'count', 1)
    return

parsed_args = parser.parse_args()
# Find the file in ec2 filesystem, based on parameter
logs_dir = parsed_args.logs_directory
if logs_dir is None:
    # logs_dir = "input_files/"
    logs_dir = "./"
elif not logs_dir.endswith("/"):
    logs_dir = logs_dir + "/"
file_name = parsed_args.file

# Which program are we calling
queries={
    'query1': query1_unique_urls_per_hour, 
    'query2': query2_unique_visitors_per_url_per_hour, 
    'query3': query3_unique_events_per_url_per_hour}
query = queries[parsed_args.query]

print('\n~~~~~~~~~ Connecting to Redis Server ~~~~~~~~~~ \n')
redisClient = redis.StrictRedis(host='0.0.0.0',port=8081)

query(file_name)
print("\nProcess Completed")


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

# Calculate the unique url's per hour - per hour of every yy/mm/dd/hh?
def query1_unique_urls_per_hour(file_name):
    input_file = csv.DictReader(open(file_name), fieldnames=field_names)
    url_map = {}
    for row in input_file:
        print('\n++++++ query1 ++++++ \n')
        timestamp = row['timestamp']
        url = row['url']
        date = datetime.time()
        try:
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError: 
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
        timestamp_hour = '%s-%s-%s:%s' % (date.year, date.month, date.day, date.hour)

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

        if redisClient.hget(timestamp_hour, url) == None:
            print('\n timestamp_hour {}'.format(timestamp_hour))
            redisClient.hset(timestamp_hour, url, 'true')
            redisClient.hincrby(timestamp_hour, 'count', 1)
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

        # Write to Redis
        full_key = '%s:%s' % (timestamp_hour, url)
        if redisClient.hget(full_key, userId) == None:
            redisClient.hset(full_key, userId, 'true')
            redisClient.hincrby(full_key, 'count', 1)
        # redis-cli monitor
        # HGET 2019-09-14:14:http://example.com/?url=042
    return
    '''
    <date:hour:url>,  unique_user_count
    2019-09-14:14:http://example.com/?url=042, ??
    2019-09-12:19:http://example.com/?url=013, ??
    2019-09-14:03:http://example.com/?url=162, ??
    2019-09-13:01:http://example.com/?url=035, ??
    2019-09-14:10:http://example.com/?url=043, ??
    '''


def query3_unique_events_per_url_per_hour(file_name):
    input_file = csv.DictR# redisClient.saad(timestamp_hour, url)es=field_names)
    for row in input_file:        # SMEMBERS for timestamp_hour gives you all the URL's
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

        redisClient.hincrby(timestamp_hour, url, 1)
        # redis-cli monitor
        # HGET HGET 2019-09-14:14:http://example.com/?url=042
        '''
        <date:hour:url>,  event_count
        2019-09-14:14:http://example.com/?url=042, ??
        2019-09-12:19:http://example.com/?url=013, ??
        2019-09-14:03:http://example.com/?url=162, ??
        2019-09-13:01:http://example.com/?url=035, ??
        2019-09-14:10:http://example.com/?url=043, ??
        '''
    return

print('\n1111111111111 \n')
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

# Create a redis client
redisClient = redis.StrictRedis(host='0.0.0.0',port=8081)

query(file_name)
print("\nProcess Completed")


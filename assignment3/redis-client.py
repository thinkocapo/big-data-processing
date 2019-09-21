import argparse
import csv
import datetime
import redis

# Argument Parser
prog = "assignment3"
desc = "Process data provided by log files and return query results"
parser = argparse.ArgumentParser(prog=prog, description=desc)
parser.add_argument('--logs-directory', '-ld', required=False, help="Directory where the log files are stored.")
parser.add_argument('--file_name', '-file', required=False, help="Name of the  log file are stored")
parser.add_argument("query", type=str, , required=True, help="query1 query2 query3")

field_names = ['uuid', 'timestamp', 'url', 'userId', 'country', 'ua_browser', 'ua_os', 'response_status', 'TTFB']

# Calculate the unique url's per hour - per hour of every yy/mm/dd/hh?
# https://redis.io/commands/smembers
def query1_unique_urls_per_hour(file_name):
    input_file = csv.DictReader(open(fileName), fieldnames=field_names)
    url_map = {}
    for row in input_file:
        timestamp = row['timestamp']
        url = row['url']
        date = datetime.time()
        try:
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError: 
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
        # Prepare a timestamp string that we want to write into Redis shared state
        timestamp_hour = '%s-%s-%s:%s' % (date.year, date.month, date.day, date.hour)

        # Write to Redis
        # 2 python perations (if..not..in and url_map), 1 redis operation
        if url not in url_map:
            url_map[url] = True
            redisClient.hincrby(timestamp_hour, 'count' 1)
        
        # 0 python operations, but is 3 redis operations (get, set and increment), and a strange data structure?
        # if redisClient.hget(timestamp_hour, url) == None:
        #     redisClient.hset(timestamp_hour, url, 'true')
        #     redisClient.hincrby(timestamp_hour, 'count' 1)
        
        # redis-cli
        # HGET 2019-09-20:12 count

    return

def query2_unique_visitors_per_url_per_hour(file_name):
    print('query2')
    input_file = csv.DictReader(open(fileName), fieldnames=field_names)
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
            redisClient.hincrby(full_key, 'count' 1)
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
    print('query3')


parsed_args = parser.parse_args()
# Find the file in ec2 filesystem, based on parameter
logs_dir = parsed_args.logs_directory
if logs_dir is None:
    logs_dir = "input_files/"
elif not logs_dir.endswith("/"):
    logs_dir = logs_dir + "/"
file_name = parsed_args.file_name
if file_name is None:
    file_name = "file-564899aad2264f9bbc97dabaa879a017.csv"
file_name = logs_dir + file_name

# Which program are we calling
queries={
    'query1': query1_unique_urls_per_hour, 
    'query2': query2_unique_visitors_per_url_per_hour, 
    'query3': query3_unique_events_per_url_per_hour}
query = queries[args.query]

# Create a redis client
redisClient = redis.StrictRedis(host='localhost',port=6379)


query1_unique_urls_per_hour(file_name, url_info)
print "Process Completed"


# input_file = csv.DictReader(open(fileName), fieldnames=field_names)
# for row in input_file:
#     timestamp = row['timestamp']
#     url = row['url']
#     obj = datetime.time()
#     try:
#         obj = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
#     except ValueError: 
#         obj = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
#     timestamp_hour = '%s-%s-%s:%s' % (obj.year, obj.month, obj.day, obj.hour)



# if redisClient.hsetnx(timestamp_hour,'urls',1) == 0:
#         redisClient.hincrby(timestamp_hour,'urls')


# redisClient.saad(timestamp_hour, url)
        # SMEMBERS for timestamp_hour gives you all the URL's


'''
$ docker exec -it 0a1c3f190cdd bash
root@0a1c3f190cdd:/data# redis-cli
127.0.0.1:6379> HSET 2019-09-20:12 www.google.com/url1 true
(integer) 1
127.0.0.1:6379> HGET 2019-09-20:12 www.google.com/url1
"true"
127.0.0.1:6379> HINCRBY 2019-09-20:12 count
(error) ERR wrong number of arguments for 'hincrby' command
127.0.0.1:6379> HINCRBY 2019-09-20:12 count 1
(integer) 1
127.0.0.1:6379> HGET 2019-09-20:12 count
"1"
127.0.0.1:6379> HINCRBY 2019-09-20:12 count 1
(integer) 2
127.0.0.1:6379> HINCRBY 2019-09-20:12 count 1
(integer) 3
127.0.0.1:6379> HGET 2019-09-20:12 count
"3"
127.0.0.1:6379> 
'''
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

# Calculate the unique url's per hour - per hour of every yy/mm/dd/hh?
# https://redis.io/commands/smembers
def query1_unique_urls_per_hour(file_name):
    input_file = csv.DictReader(open(fileName), fieldnames=field_names)
    for row in input_file:
        timestamp = row['timestamp']
        url = row['url']
        date = datetime.time()
        try:
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError: 
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
        # Prepare a timestamp string that we want to write into Redis shared state
        timestamp_key = '%s-%s-%s:%s' % (date.year, date.month, date.day, date.hour)

        # Write to Redis
        # "key_name, score1, value"
        # "key_name, score2, value"
        # Insert a new key with initial value 1. If that key already exists, then the function returns 0
        # Else, Atomically increment the value for key by 1 if the key already exists
        # TODO if url not in dict ?
        redisClient.saad(timestamp_key, url)
        # TODO SERVER-SIDE: CLI COMMAND scard for getting cardinality (number of elements in the set), it's called smembers
        
    return

def query2_unique_visitors_per_url_per_hour(file_name):
    print('query2')
    input_file = csv.DictReader(open(fileName), fieldnames=field_names)
    for row in input_file:
        timestamp = row['timestamp']
        url = row['url']
        date = datetime.time()
        try:
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError: 
            date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
        # Prepare a timestamp string that we want to write into Redis shared state
        timestamp_key = '%s-%s-%s:%s' % (date.year, date.month, date.day, date.hour)

        # Write to Redis
        # "key_name, score1, value"
        # "key_name, score2, value"
        # Insert a new key with initial value 1. If that key already exists, then the function returns 0
        #if redisClient.hsetnx(timestamp_key,url,1) == 0:
            # Atomically increment the value for key by 1 if the key already exists
            #redisClient.hincrby(timestamp_key,url)


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
#     timestamp_key = '%s-%s-%s:%s' % (obj.year, obj.month, obj.day, obj.hour)



# if redisClient.hsetnx(timestamp_key,'urls',1) == 0:
#         redisClient.hincrby(timestamp_key,'urls')
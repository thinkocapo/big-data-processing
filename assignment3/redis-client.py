import argparse
import csv
import datetime
import redis

# Argument Parser
prog = "assignment3"
desc = "Process data provided by log files and return query results"
parser = argparse.ArgumentParser(prog=prog, description=desc)
parser.add_argument('--logs-directory', '-ld', required=False,
                    help="Directory where the log files are stored.")
parser.add_argument('--file_name', '-file', required=False,
                    help="Name of the  log file are stored")

# Calculate the unique url's per hour - per hour of every yy/mm/dd/hh?
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
        hour = date.hour
        # Prepare a timestamp string that we want to write into Redis shared state
        timestamp_key = '%s-%s-%s:%s' % (date.year, date.month, date.day, date.hour)

        # Write to Redis
        # "key_name, score1, value"
        # "key_name, score2, value"
        # Insert a new key with initial value 1. If that key already exists, then the function returns 0
        if redisClient.hsetnx("timestamp",url,1) == 0:
            # Atomically increment the value for key by 1 if the key already exists
            redisClient.hincrby("timestamp",url)
    return


parsed_args = parser.parse_args()
logs_dir = parsed_args.logs_directory
#print (logs_dir)
if logs_dir is None:
    logs_dir = "input_files/"
elif not logs_dir.endswith("/"):
    logs_dir = logs_dir + "/"
file_name = parsed_args.file_name
#print (file_name)
if file_name is None:
    file_name = "file-564899aad2264f9bbc97dabaa879a017.csv"
file_name = logs_dir + file_name
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
import argparse
import csv
import datetime
import json
import multiprocessing
from multiprocessing import Process, Value, Lock
import os
import pprint
import time
import threading
from random import randint


# Capture any exceptions and send to Sentry.io :)
if 'DSN_DATA_PIPELINE' in os.environ:
    import sentry_sdk
    sentry_sdk.init(os.environ['DSN_DATA_PIPELINE'])

field_names = ['uuid', 'timestamp', 'url', 'userId', 'country', 'ua_browser', 'ua_os', 'response_status', 'TTFB']

# Makes a data structure like { date1: { url:count } }
def query1(lock, fileName, server_process_dict):
    input_file = csv.DictReader(open(fileName), fieldnames=field_names)
    for row in input_file:
        timestamp = row['timestamp']
        url = row['url']
        obj = datetime.time()
        try:
            obj = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError: 
            obj = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
        timestamp_key = '%s-%s-%s:%s' % (obj.year, obj.month, obj.day, obj.hour)
        with lock:
            if timestamp_key in server_process_dict:
                url_dict = server_process_dict[timestamp_key]
                if url in server_process_dict[timestamp_key]:
                    url_dict[url] = url_dict[url] + 1
                    server_process_dict[timestamp_key] = url_dict
                else:
                    url_dict[url] = 1
                    server_process_dict[timestamp_key] = url_dict
            else:
                server_process_dict[timestamp_key] = { url: 1 }

# Makes a data structure like { timestamp: { url: [users] }}
def query2(lock, fileName, server_process_dict):
    input_file = csv.DictReader(open(fileName), fieldnames=field_names)
    for row in input_file:
        timestamp = row['timestamp']
        url = row['url']
        userId = row['userId']
        obj = datetime.time()
        try:
            obj = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError: 
            obj = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
        timestamp_key = '%s-%s-%s:%s' % (obj.year, obj.month, obj.day, obj.hour)

        with lock:
            if timestamp_key in server_process_dict:
                url_dict = server_process_dict[timestamp_key]
                if url in url_dict:
                    url_dict[url].append(userId)
                    server_process_dict[timestamp_key] = url_dict
                else:
                    url_dict[url] = [userId]
                    server_process_dict[timestamp_key] = url_dict
            else:
                server_process_dict[timestamp_key] = { url: [userId] }

# Makes a data structure that looks like { timestamp: { url: [uuids] }}
def query3(lock, fileName, server_process_dict):
    input_file = csv.DictReader(open(fileName), fieldnames=field_names)
    for row in input_file:
        timestamp = row['timestamp']
        url = row['url']
        userId = row['userId']
        uuid = row['uuid']
        obj = datetime.time()
        try:
            obj = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError: 
            obj = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
        timestamp_key = '%s-%s-%s:%s' % (obj.year, obj.month, obj.day, obj.hour)

        with lock:
            if timestamp_key in server_process_dict:
                url_dict = server_process_dict[timestamp_key]
                if url in url_dict:
                    url_dict[url].append(uuid)
                    server_process_dict[timestamp_key] = url_dict
                else:
                    url_dict[url] = [uuid]
                    server_process_dict[timestamp_key] = url_dict
            else:
                server_process_dict[timestamp_key] = { url: [uuid] }

# Makes a data structure that looks like { timestamp: { country: [urls] }}
def problem4(lock, fileName, server_process_dict):
    input_file = csv.DictReader(open(fileName), fieldnames=field_names)
    for row in input_file:
        timestamp = row['timestamp']
        url = row['url']
        country = row['country']
        obj = datetime.time()
        try:
            obj = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError:
            obj = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
        timestamp_key = '%s-%s-%s:%s' % (obj.year, obj.month, obj.day, obj.hour)

        with lock:
            if timestamp_key in server_process_dict:
                country_dict = server_process_dict[timestamp_key]
                if country in country_dict:
                    country_dict[country].append(url)
                    server_process_dict[timestamp_key] = country_dict
                else:
                    country_dict[country] = [url]
                    server_process_dict[timestamp_key] = country_dict
            else:
                server_process_dict[timestamp_key] = { country: [url] }

def printer(query):
    # Print the number of unique URL's per query
    if query == query1:
        for k,v in server_process_dict.items():
            unique_urls = server_process_dict[k].items()
            print k, len(unique_urls)
    # Print the number of unique visitors per URL per day
    if query == query2:
        for timestamp_key, url_dict in server_process_dict.items():
            for url, users in url_dict.items():
                unique_users = set(user for user in users)
                print timestamp_key, url, len(unique_users)
    # Print the number of uuids (unique event clicks) per URL per hour per day
    if query == query3:
        for timestamp_key, url_dict in server_process_dict.items():
            for url, uuids in url_dict.items():
                unique_uuids = set(uuid for uuid in uuids)
                print timestamp_key, url, len(unique_uuids)
    # Problem 4
    if query == problem4:
        for timestamp_key, country_dict in server_process_dict.items():
            for country, urls in  country_dict.items():
                unique_urls = set(url for url in urls)
                print timestamp_key, country, len(unique_urls)



# EXAMPLE USAGE:
# python3 countery.py query1
# python3 countery.py query2
# python3 countery.py query4
# python3 countery.py problem4
if __name__ == '__main__':

    # Specify the number of threads and query from command-line
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str, help="query1 query2 query3")
    args = parser.parse_args()
    
    # Which program are we calling
    queries={'query1': query1, 'query2': query2, 'query3': query3, 'problem4': problem4}
    query = queries[args.query]
    
    fileNames = ('./input_files/file-input1.csv', 'input_files/file-input2.csv', 'input_files/file-input3.csv', 'input_files/file-input4.csv')

    with multiprocessing.Manager() as manager:
        server_process_dict = manager.dict()
        lock = Lock()
        processes = []
        for i in range(4):
            process = multiprocessing.Process(target=query, args=(lock, fileNames[i], server_process_dict,))
            processes.append(process)
            process.start()
        for curr_process in processes:
            curr_process.join()

        printer(query)

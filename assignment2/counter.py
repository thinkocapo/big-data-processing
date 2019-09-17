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

def query1(lock, fileName, server_process_dict):
    input_file = csv.DictReader(open(fileName), fieldnames=field_names)
    for row in input_file:
        timestamp_str = row['timestamp']
        url = row['url']
        obj = datetime.time()
        try:
            obj = datetime.datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError: 
            obj = datetime.datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%SZ')
        timestamp_key = '%s-%s-%s:%s' % (obj.year, obj.month, obj.day, obj.hour)
        # dict_copy = server_process_dict[timestamp_key]
        # dict_copy[url] = dict_copy[url] + 1
        # server_process_dict[timestamp_key] = dict_copy
        with lock:
            if timestamp_key in server_process_dict:
                dict_copy = server_process_dict[timestamp_key]
                if url in server_process_dict[timestamp_key]:
                    dict_copy[url] = dict_copy[url] + 1
                    server_process_dict[timestamp_key] = dict_copy
                    # server_process_dict[timestamp_key][url] += 1
                else:
                    dict_copy[url] = 1
                    server_process_dict[timestamp_key] = dict_copy
                    # server_process_dict[timestamp_key][url] = 1
            else:
                server_process_dict[timestamp_key] = { url: 1 }

def query2(file):
    print('query2')

# Example usage:
# python3 countery.py query1
if __name__ == '__main__':
    print('main')

    # Specify the number of threads and query from command-line
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str, help="query1 query2 query3")
    args = parser.parse_args()
    
    # Which program are we calling
    queries={'query1': query1, 'query2': query2}
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

        # print(server_process_dict.items())
        for k,v in server_process_dict.items():
            unique_urls = server_process_dict[k].items()
            count_unique_urls = len(unique_urls)
            print k, count_unique_urls


# if full_key in server_process_dict:
#     server_process_dict[full_key] += 1    
# else:
#     server_process_dict[full_key] = 1   

# if timestamp_key in server_process_dict:
#     server_process_dict[timestamp_key].append(url)
# else:
#     server_process_dict[timestamp_key] = [url]

# full_key = '%s %s' % (timestamp_key, url)
import argparse
import csv
import datetime
import json
import multiprocessing
import os
import pprint
import time
import threading
from random import randint

# Capture any exceptions and send to Sentry.io :)
if 'DSN_DATA_PIPELINE' in os.environ:
    import sentry_sdk
    sentry_sdk.init(os.environ['DSN_DATA_PIPELINE'])

processes = []
field_names = ['uuid', 'timestamp', 'url', 'userId', 'country', 'ua_browser', 'ua_os', 'response_status', 'TTFB']

def query1(lock, fileName, server_process_dict):
    print('\n ~~~~~~~~ query1 ~~~~~~~~~~ \n')
    input_file = csv.DictReader(open(fileName), fieldnames=field_names)
    for row in input_file:
        timestamp_str = row['timestamp']
        obj = datetime.time()
        
        try:
            obj = datetime.datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError: 
            obj = datetime.datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%SZ')
        timestamp_output = '%s-%s-%s:%s' % (obj.year, obj.month, obj.day, obj.hour)

        # with lock:
        if timestamp_output not in server_process_dict:
            server_process_dict[timestamp_output] = 1
        else:
            server_process_dict[timestamp_output] += 1

def query2(file):
    print('query2')

def main():
    print('main')

    # Specify the number of threads and query from command-line
    parser = argparse.ArgumentParser()
    parser.add_argument("numThreads", type=int, help="numThreads")
    parser.add_argument("query", type=str, help="query1 query2 query3")
    args = parser.parse_args()
    print('ARGS {}'.format(args))
    # Which program are we calling
    queries={'query1': query1, 'query2': query2}
    query = queries[args.query]

    # And with how many threads
    numThreads = args.numThreads
    
    fileNames = ('./input_files/file-input1.csv', 'input_files/file-input2.csv', 'input_files/file-input3.csv', 'input_files/file-input4.csv')

    with multiprocessing.Manager() as manager:
        server_process_dict = manager.dict()
        for i in range(4):
            lock = multiprocessing.Lock()
            process = multiprocessing.Process(target=query, args=(lock, fileNames[i], server_process_dict,))
            processes.append(process)
            process.start()
        for curr_process in processes:
            curr_process.join()

        print('server_process_dict:')
        for k,v in server_process_dict.items():
            print k,v


def wait_for_threads():
    print('wait_for_threads')
    for thread in processes:
        thread.join()

# Example usages:
# python3 countery.py 4 query1
if __name__ == '__main__':
    main()
    # wait_for_threads()
else:
    print('this is a main level package')

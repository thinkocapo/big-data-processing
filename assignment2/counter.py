import argparse
import csv
import multiprocessing
import os
import time
import threading
from datetime import datetime
from random import randint

# Capture any exceptions and send to Sentry.io :)
if 'DSN_DATA_PIPELINE' in os.environ:
    import sentry_sdk
    sentry_sdk.init(os.environ['DSN_DATA_PIPELINE'])

processes = []
field_names = ['uuid', 'timestamp', 'url', 'userId', 'country', 'ua_browser', 'ua_os', 'response_status', 'TTFB']

def query1(fileName, shared_memory):
    input_file = csv.DictReader(open(fileName), fieldnames=field_names)
    for row in input_file:
        timestamp_str = row['timestamp']
        obj = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        timestamp_output = '%s-%s-%s:%s' % (obj.year, obj.month, obj.day, obj.hour)
        if timestamp_output not in shared_memory:
            shared_memory[timestamp_output] = 1
        else:
            shared_memory[timestamp_output] =+ 1



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
        shared_memory = manager.dict()
        for i in range(4):
            process = multiprocessing.Process(target=query, args=(fileNames[0], shared_memory,))
            processes.append(process)
            process.start()
            # process.join()
        for curr_process in processes:
            curr_process.join()
    print('shared_memory\n{}'.format(shared_memory))



def wait_for_threads():
    print('wait_for_threads')
    for thread in processes:
        thread.join()

# Example usages:
# python3 countery.py 4 query1
if __name__ == '__main__':
    main()
    wait_for_threads()
else:
    print('this is a main level package')






# Does not work consistently with threading, so not invoking this for now
# by simply running wait_for_threads() after main(), this seems to have fixed the problem
# def cleanup_files():
#         # wait_for_threads()
#         dir_name = os.getcwd()
#         files = os.listdir(dir_name)
#         for file in files:
#             if file.endswith(".txt"):
#                 os.remove(file)
# atexit.register(cleanup_files)



# not needed
# reader = csv.reader(open(fileName), delimiter=' ', quotechar='|')
# for row in reader:
#     print(', '.join(row))




    
# obj_3 = datetime.strptime(log_date, '%Y-%m-%dT%H:%M:%S.%f')    
#                 '2019-09-12T19:53:11.040Z'
# date_time_str = '2018-06-29 08:15:27.243860'
# date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')


# https://stackabuse.com/converting-strings-to-datetime-in-python/
# log_date = '2019-09-12T19:53:11.040Z'
# formatted = datetime.strptime(log_date, '%Y-%m-%dT%H:%M:%S.%fZ') 


# formatted.date()
# formatted.time()
# formatte.year
# formatted.hour
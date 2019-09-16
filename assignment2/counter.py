import argparse
import csv
import multiprocessing
import os
import time
import threading
from random import randint

# Capture any exceptions and send to Sentry.io :)
if 'DSN_DATA_PIPELINE' in os.environ:
    import sentry_sdk
    sentry_sdk.init(os.environ['DSN_DATA_PIPELINE'])

processes = []
# <uuid> <timestamp> <url> <userId> <country> <ua_browser><ua_os> <response_status> <TTFB> 
fieldNames = ['uuid', 'timestamp', 'url', 'userId', 'country', 'ua_browser', 'ua_os', 'response_status', 'TTFB']



def query1(fileName, output):
    input_file = csv.DictReader(open(fileName), fieldnames=fieldNames)
    for row in input_file:
        if row['data
        ']
        print row

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
        output = manager.dict()
        for i in range(4):
            process = multiprocessing.Process(target=query, args=(fileNames[0], output,))
            processes.append(process)
            process.start()
            # process.join()
        for curr_process in processes:
            curr_process.join()
    print('output\n{}'.format(output))



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
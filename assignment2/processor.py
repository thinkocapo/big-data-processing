import argparse
import atexit
import os
import sentry_sdk
import time
import threading
from random import randint

# Capture any exceptions and send to Sentry.io :)
sentry_sdk.init(os.environ['DSN_DATA_PIPELINE'])

# Does not work consistently, so not invoking this for now
def cleanup_files():
        # wait_for_threads()
        dir_name = os.getcwd()
        files = os.listdir(dir_name)
        for file in files:
            if file.endswith(".txt"):
                os.remove(file)
atexit.register(cleanup_files)

threads = []

# Create uniquely named files by using the thread name
def create_file():
    threadName = threading.currentThread().getName()
    print('THREAD NAME: {}'.format(threadName))
    fileName = '{}.txt'.format(threadName)
    
    while True:
        print("making file")
        file = open(fileName,'w+')
        for line in range(10000):
            file.write("I AM A LINE")
        file.close()
        os.remove(fileName)
        
# Run a big fibonacci sequence
def fibonacci():
    print('THREAD NAME: {}'.format(threading.currentThread().getName()))
    while True:
        time.sleep(1)
        a, b = 0, 1
        for i in range(0, 1000000000):
            a, b = b, a + b

def io_intensive(numThreads):
    print('io_intensive %s threads' % (numThreads))
    for t in range(numThreads):
        thread = threading.Thread(target=create_file)
        thread.start()
        threads.append(thread)

def cpu_intensive(numThreads):
    print('cpu_intensive %s threads' % (numThreads))
    for t in range(numThreads):
        thread = threading.Thread(target=fibonacci, name="MrFibonacciCPU")
        thread.start()
        threads.append(thread)

def main():

    # Specify the number of threads and program from command-line
    parser = argparse.ArgumentParser()
    parser.add_argument("numThreads", type=int, help="numThreads")
    parser.add_argument("program", type=str, help="io_intensive or cpu_intensive")
    args = parser.parse_args()
    print(args)

    # Which program are we calling
    programs={'io_intensive': io_intensive, 'cpu_intensive': cpu_intensive}
    program = programs[args.program]

    # And with how many threads
    numThreads = args.numThreads
    
    program(numThreads)


# No need to invoke this as while loops are occuring
def wait_for_threads():
    print('wait_for_threads')
    for thread in threads:
        thread.join()

# Example usage
# `python3 processor.py 2 io_intensive`
if __name__ == '__main__':
    main()
    wait_for_threads()
else:
    print('this is a main level package')

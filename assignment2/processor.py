import argparse
import multiprocessing
import os
import time
import threading
from random import randint

processes = []

# Create uniquely named files by using <PID> and <ThreadName>
# With Multiprocessing, the thread used is always MainThread of the new process
# an example file name is PID-14848-MainThread.txt
def create_file():
    fileName = 'PID-%s-%s.txt' % (os.getpid(), threading.currentThread().getName())
    while True:
        print("making file - {}".format(fileName))
        file = open(fileName,'w+')
        for line in range(10000):
            file.write("I AM A LINE")
        file.close()
        os.remove(fileName)
        
# Run a big fibonacci sequence. running it to 100,000 iterations because a billion woudln't complete, or it would freeze
# If I did 1million instead of 100,000 then CPU is at 99% for each
# But for 100,000 the cpu stays at 6% for each
def fibonacci():
    HUNDRED_THOUSAND = 100000
    while True:
        print( 'PID %s %s' % (os.getpid(), threading.currentThread().getName()))
        time.sleep(1)
        a, b = 0, 1
        for i in range(0, HUNDRED_THOUSAND):
            a, b = b, a + b

def io_intensive(numThreads):
    print('io_intensive %s threads' % (numThreads))
    for t in range(numThreads):
        process = multiprocessing.Process(target=create_file)
        processes.append(process)
        process.start()

def cpu_intensive(numThreads):
    print('cpu_intensive %s threads' % (numThreads))
    for t in range(numThreads):
        process = multiprocessing.Process(target=fibonacci)
        processes.append(process)
        process.start()

def main():

    # Specify the number of threads and program from command-line
    parser = argparse.ArgumentParser()
    parser.add_argument("numThreads", type=int, help="numThreads")
    parser.add_argument("program", type=str, help="io_intensive or cpu_intensive")
    args = parser.parse_args()

    # Which program are we calling
    programs={'io_intensive': io_intensive, 'cpu_intensive': cpu_intensive}
    program = programs[args.program]

    # And with how many threads
    numThreads = args.numThreads
    
    program(numThreads)


# We're using While Loops so this isn't as effective
# Need to understand better what happens with suddent KeyboardInterrupts and these outstanding threads
def wait_for_threads():
    print('wait_for_threads')
    for thread in processes:
        thread.join()

# Example usages:
# python3 processor.py <num_threads> <name_program>
# python3 processor.py 2 io_intensive
# python3 processor.py 4 cpu_intensive
if __name__ == '__main__':
    main()
    wait_for_threads()
else:
    print('this is a main level package')




# Capture any exceptions and send to Sentry.io :)
# if 'DSN_DATA_PIPELINE' in os.environ:
    # import sentry_sdk
    # sentry_sdk.init(os.environ['DSN_DATA_PIPELINE'])

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
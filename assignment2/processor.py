import argparse
import time
import threading
import logging #TODO
logging.basicConfig(format="%(threadName)s:%(thread)s")

threads = []

def create_file():
    print('THREAD NAME: {}'.format(threading.currentThread().getName()))

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
        thread = threading.Thread(target=create_file, name='Mrs. Creat_File IO')
        thread.start()
        threads.append(thread)

def cpu_intensive(numThreads):
    print('cpu_intensive %s threads' % (numThreads))
    for t in range(numThreads):
        thread = threading.Thread(target=fibonacci, name="Mr. Fibonacci CPU")
        thread.start()
        threads.append(thread)

def main():

    # specify the number of threads and program from command-line
    parser = argparse.ArgumentParser()
    parser.add_argument("numThreads", type=int, help="numThreads")
    parser.add_argument("program", type=str, help="io_intensive or cpu_intensive")
    args = parser.parse_args()
    print(args)

    # which program are we calling
    programs={'io_intensive': io_intensive, 'cpu_intensive': cpu_intensive}
    program = programs[args.program]

    # and with how many threads
    numThreads = args.numThreads
    
    program(numThreads)


# invoke this after main method or else process.py will terminate before threads finish
def wait_for_threads():
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
    wait_for_threads()
else:
    print('this is a main level package')




# def thread_decorator(func):
#     def wrapper(numLines, num):
#         thread = threading.Thread(target=func)
#         threads.append(thread)
#     return wrapper
# fibonacci = thread_decorator(fibonacci)
# create_file = thread_decorator(create_file)
import inspect
from random import randint
import sys
import threading

threads = []

# this executes in its own thread, see thread_decorator
def create_file(numLines, num):
    print('create_file',num)
    file = open("william_capozzoli_{}.txt".format(num),"w+")
    for numLine in range(numLines):
        file.write(text())

# creates each file in a thread, see thread_decorator
def generate_files(numFiles, numLines):
    print('generate_files')
    for num in range(numFiles):
        create_file(numLines, num)

# makes sure the threads finish creating files, or else problem_1.py will finish too soon
def run_the_threads():
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

def text():
    return '%s %s %s\n' % (randint(0,10), randint(0,10), randint(0,10))

# decorator for abstracting away all the 'threading' talk
# so app/business logic is separate from this threading/distributed/computer-sci stuff
def thread_decorator(func):
    def wrapper(numLines, num):
        thread = threading.Thread(target=func,args=(numLines, num))
        threads.append(thread)
    return wrapper
create_file = thread_decorator(create_file)


if __name__ == '__main__':
    numFiles = int(sys.argv[1])
    numLines = int(sys.argv[2])
    generate_files(numFiles, numLines)
    run_the_threads()


# Experiment
# ThreadPoolExecutor - https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor
# instead of a Decorator, could make a Class that inherits from Threading. example: https://www.geeksforgeeks.org/writing-files-background-python/

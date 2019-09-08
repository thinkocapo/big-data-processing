import inspect
from random import randint
import _thread
import threading

threads = []

def text():
    output = '%s %s %s\n' % (randint(0,10), randint(0,10), randint(0,10))
    return output

def create_file(numLines, num):
    print('create_file %s' % (num))
    file = open("william_capozzoli_{}.txt".format(num),"w+")
    for numLine in range(numLines):
        file.write(text())

def generate_files(numFiles, numLines):
    """numFiles to generate. numLines per file"""
    print('generate_file')
    for num in range(numFiles):
        print('num %s' % (num))
        create_file(numLines, num)

def run_the_threads():
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

# Abstract away all the 'threading' talk, using a decorator
def thread_decorator(func):
    def wrapper(numLines, num):
        thread = threading.Thread(target=func,args=(numLines, num))
        threads.append(thread)
    return wrapper
create_file = thread_decorator(create_file)


if __name__ == '__main__':
    numFiles = 2
    numLines = 3
    generate_files(numFiles, numLines)
    run_the_threads()




# experiment
# instead of Decorator, could do a Class that inherits from threading.Thread, like https://www.geeksforgeeks.org/writing-files-background-python/
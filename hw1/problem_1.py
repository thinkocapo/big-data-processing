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
        thread = threading.Thread(target=create_file,args=(numLines, num))
        threads.append(thread)

def run_the_threads():
    for thread in threads:
        thread.start()

    # Wait for all to complete
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    generate_files(2, 3)
    run_the_threads()


# experiment 1
# def thread_decorator(func):
#     def wrapper():
#         print("OPEN A THREAD")
#         func() # create_file inside of it
#         print("THREAD CLOSED?")
#     return wrapper
# generate_file = thread_decorator(generate_file)

# experiment 2
# instead of Decorator, could do a Class that inherits from threading.Thread, like https://www.geeksforgeeks.org/writing-files-background-python/
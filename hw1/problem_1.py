import inspect
from random import randint
import threading


def text():
    output = '%s %s %s\n' % (randint(0,10), randint(0,10), randint(0,10))
    return output

# wrap this (decorate?) in its own thread execution
def create_file(numLines, num):
    # wrap this part in its own thread execution
    file = open("william_capozzoli_{}.txt".format(num),"w+")
    for numLine in range(numLines):
        file.write(text())

def generate_file(numFiles, numLines):
    """numFiles to generate. numLines per file"""
    print('generate_file')
    for num in range(numFiles):
        create_file(numLines, num)
    print('\nDONE')



if __name__ == '__main__':
    generate_file(2, 3)
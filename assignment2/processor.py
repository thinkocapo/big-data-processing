import argparse

def io_intensive(numThreads):
    print('io_intensive')

def cpu_intensive(numThreads):
    print('cpu_intensive')

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

if __name__ == '__main__':
    main()
else:
    print('this is a main level package')
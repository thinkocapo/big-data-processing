import argparse


def io_processor():
    print('io_processor')

def cpu_processor():
    print('cpu_processor')

def program(func):
    func()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--threads", "-t", type="int", help="numThreads")
    args = parser.parse_args()
    print(args.echo)
    # func = io or cpi
    program()
else:
    print('this is a main level package')
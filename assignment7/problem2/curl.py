import argparse

# Argument Parser
prog = "assignment3"
desc = "Process data provided by log files and return query results"
parser = argparse.ArgumentParser(prog=prog, description=desc)
parser.add_argument("rate", type=str, help="rate, interval")
args = parser.parse_args()

def main():
    print('do things {}'.format(args.rate))




if __name__ == '__main__':
    main()
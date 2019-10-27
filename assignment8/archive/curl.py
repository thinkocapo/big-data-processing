import argparse
import os
import subprocess
import time

# Argument Parser
prog = "assignment3"
parser = argparse.ArgumentParser(prog=prog)
parser.add_argument("rate", type=str, help="rate/interval, of x times per second")
args = parser.parse_args()

# Writes to DEVNULL because we don't actually need the response. Flume will get it from log file via 'tail
def main():
    rate = int(args.rate)
    wait_time = 1.0 / rate
    print('wait_time {} \n'.format(wait_time))

    count = 0
    with open(os.devnull, 'w') as DEVNULL:
        while True:
            subprocess.call(['curl', '-s', 'http://ec2-18-191-210-25.us-east-2.compute.amazonaws.com:80'], stdout=DEVNULL)
            # subprocess.call(['curl', '-s', 'http://ec2-18-220-93-94.us-east-2.compute.amazonaws.com:80'], stdout=DEVNULL)
            count += 1
            if count % rate == 0:
                print('count {} \n'.format(count))
            time.sleep(wait_time)

if __name__ == '__main__':
    main()

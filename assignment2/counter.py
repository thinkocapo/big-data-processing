import argparse
import multiprocessing
import os
import time
import threading
from random import randint

# Capture any exceptions and send to Sentry.io :)
if 'DSN_DATA_PIPELINE' in os.environ:
    import sentry_sdk
    sentry_sdk.init(os.environ['DSN_DATA_PIPELINE'])



def main():
    print('main')





def wait_for_threads():
    print('wait_for_threads')
    for thread in processes:
        thread.join()

# Example usages:
# python3 countery.py <?> <?>
if __name__ == '__main__':
    main()
    wait_for_threads()
else:
    print('this is a main level package')






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
# reference : lab2 code : lab2_shared_count.py
# Problem 4: time range queries

import multiprocessing
from multiprocessing import Process, Value, Lock
import glob


"""
args   : manager : multiprocessing manager
         data_dict : multiprocessing dict to hold data
         datetime_hour : date plus hour key
         url_text : url string
purpose: Function adds country for every hour
"""


def add_country(manager,data_dict,datetime_hour,country_name):
    if country_name in data_dict[datetime_hour]:
        return                                                     # return country already exists
    else:                                                          # add new country key
        temp_dict = data_dict[datetime_hour]
        temp_dict[country_name] = manager.dict()
        data_dict[datetime_hour] = temp_dict



"""
args   : manager : multiprocessing manager
         data_dict : multiprocessing dict to hold data
         datetime_hour : date plus hour key
         url_text : url string
purpose: Function adds url for every hour, url combination
"""


"""
args   : manager : multiprocessing manager
         data_dict : multiprocessing dict to hold data
         datetime_hour : date plus hour key
         url_text : url string
         userid : user identifier
purpose: Function adds userid for every hour, url combination and also counts events
"""


def add_url(manager,data_dict,datetime_hour,country_name,url_text):
    if url_text in data_dict[datetime_hour][country_name]:         # if user id exits, increment counter for event
        temp_dict1 = data_dict[datetime_hour]
        temp_dict2 = temp_dict1[country_name]
        temp_dict2[url_text] += 1
        temp_dict1[country_name] = temp_dict2
        data_dict[datetime_hour] = temp_dict1
    else:
        temp_dict1 = data_dict[datetime_hour]                       # add new user id and instantiate counter to 1
        temp_dict2 = temp_dict1[country_name]
        temp_dict2[url_text] = 1
        temp_dict1[country_name] = temp_dict2
        data_dict[datetime_hour] = temp_dict1


"""
args   : manager : multiprocessing manager
         file : path of file to process
         lock : lock to support atomic updates to dict
         data_dict : multiprocessing dict to hold data
purpose: Function creates a process for every file and processes it to extract required attributes.
"""


def process_file(manager, file, lock, data_dict):
    f = open(file, 'r')                                                       # open file

    for file_line in f:                                                       # for every line in file
        line_list = file_line.split(',')                                      # create list of strings
        datetime, url, uid, country = line_list[1:5]                          # capture attributes
        fmtd_datetime_hour = datetime[:10] + ' ' + datetime.split(':')[0][-2:]  # format date , hour

        date = fmtd_datetime_hour.split(' ')[0].replace('-',"")
        hour = fmtd_datetime_hour[-2:]

        date_hour = int(date+hour)

        if date_hour < 2018091317 or date_hour > 2018091409:
            continue

        with lock:                                                             # lock to ensure atomic updates
            if fmtd_datetime_hour in data_dict:
                add_country(manager,data_dict,fmtd_datetime_hour,country)      # add country to dict
                add_url(manager,data_dict,fmtd_datetime_hour,country,url)      # add url and event to country, hour
            else:
                data_dict[fmtd_datetime_hour] = manager.dict()                 # add date hour key
                add_country(manager,data_dict,fmtd_datetime_hour,country)      # add country to dict
                add_url(manager,data_dict,fmtd_datetime_hour,country,url)      # add url and event to country, hour

    f.close()                                                                  # close file


if __name__ == '__main__':
    final_dict = dict()                                       # final regular dict
    with multiprocessing.Manager() as manager:                # initiate multiprocessing manager
        data_dict = manager.dict()                            # shared state dict
        lock = Lock()                                         # instantiate lock
        jobs = []                                             # place holder list for jobs

        path = '/home/centos/input_files/*'                   # path of file(s) location
        files = glob.glob(path)                               # find all path names matching pattern

        for file in files:                                    # process every file
            print('processing file = ' + str(file))           # start a process for every file
            t = multiprocessing.Process(
                target=process_file,
                args=(manager, file, lock, data_dict))
            jobs.append(t)                                    # add process to jobs list
            t.start()                                         # start the child process

        for curr_job in jobs:                                 # wait for all process to finish
            curr_job.join()

        print("Process Completed")
        final_dict = data_dict.copy()                         # copy shared dict


    print('\n\n')
    # getting unique url per country per hour
    print("Query4: get count of unique URLs by country by hour for a  specified time range [t1-t2]\n")
    print("t1 = 09/13/2018 5PM UTC\n")
    print("t2 = 09/14/2018 9AM UTC\n")
    for hour in sorted(final_dict.keys()):
        for country in sorted(final_dict[hour].keys()):
            print(hour,country,len(final_dict[hour][country].keys()))
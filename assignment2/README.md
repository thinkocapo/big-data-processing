

virtualenv -p /usr/bin/python3 name_of_virtualenv  

```
FLASK_APP=flask-redis.py
FLASK_ENV=development
flask run -p 3001
```

$ FLASK_APP=flask-redis.py flask run -p 3001

https://pypi.org/project/redis/ is redis-py



-----------------------------------------------------------
READING THROUGH ASSIGNMENTS FOR FIRST TIME...
09/10

For Problems 3-5, your programs have to keep the shared state in memory <-- write the URL counts of the csvs to Redis?
i'm thinking, 1 python app w/ 4 threads using 1 redis client <--something GET's from Redis, to act as the 'Analytics' component?
<--- or as each thread reads, is it supposed to be updating Redis? as in per-iteration?
 

how adding more threads affect I/O (and CPU)  utilization of your server <-- which metric in htop shows I/O?

Horizontal scaling means that you scale by adding more machines into your pool of resources whereas Vertical scaling means that you scale by adding more power (CPU, RAM) to an existing machine.


PREDICTION:
the '%CPU' will increase as you run on more threads
the '%CPU' will decrease as you run on more CPU's
"cpu usage" is % of total CPU in use by all processes? or the process's portion of the total CPU available?


-------------------------------------------------------------------------------

09/11 Lab

WHAT ARE LIMITATIONS FROM PHYSICAL RESOURCE PERSPECTIVE - PHYSICAL SERVER

System Bus - for Multi Process - to connect multiple-processes together
hyper-threading - find unused cores


Process contains code-to-execute, threads


there's Process Block Table , with PC?,


user threads map to kernel threads and physical cores


add more threads, but processing speed declines, because now not enough Cores.
context-switching between threads is great. but useful core by OS is constant



'logical cores' hyper-threading.



WHAT ARE LIMITATIONS FOR ROW LOCK CONTENTION IN PHYSICAL DATABASE
and options to address that
"SHARED STATE MANAGEMENT"

Shared State - result of computation
Shared Data - shared data...?


*Shared counters, as opposed to Raw Data....*
"pre-populate as much as you can about the data"


Shared State - calculation while data is being processed. otherwise you wait, for stored. pre-aggregation of answers as_you_go


Shared Memory - in-process cache - cached objects scoped to individual memory of each individual app

'local/remote distributed cache service' 'data is totally in memory''can configure disk persistence'



Option 1 - cached objects scoped to individual memory 
...


re-watch part from 4:22p PST 7:22 ESTp about DUPLICATE KEY...

with cache, schema stays the same


RDBMS
- hits disk every time
- fully-indexed. the write into the RDBMS updates the index structure and structure in the table
- supports ACID


IN-MEMORY CACHE
- 

*requests/data coming in across diff apps/labs/threads, so how make a counter shared across all*?



Why Cache is performant?
"Consistent Caching" algorithm. gaurantees return from function...
?


5p PST tomorrow lab, 8pEST


Redis - single threaded so no context switching or contention.
Redix - fixed amount of nodes...?


**REVIEW** - ACID, 'atomic'




--------- LAB --------
QUESTIONS
Q. For Problems 3-5, your programs have to keep the shared state in memory
    - https://docs.python.org/3.9/library/multiprocessing.shared_memory.html ?
    - Answer:
```
    # https://docs.python.org/3/library/multiprocessing.html#sharing-state-between-processes
    # https://stackoverflow.com/questions/6832554/multiprocessing-how-do-i-share-a-dict-among-multiple-processes
    d = manager.dict()
    d[1] = '1'
    d['2'] = 2

    p1 = Process(target=f, args=(d,))
    p2 = Process(target=f, args=(d,))
```
and "Manager, shared disk" someone said

ThreadPool executor? I'm thinkin NO https://docs.python.org/3/library/concurrent.futures.html need Multiprocessing
https://stackoverflow.com/questions/38311431/concurrent-futures-processpoolexecutor-vs-multiprocessing-pool-pool?noredirect=1&lq=1


Q. Did you say to use Multiprocess because Python allows one thread at a time? Or a certain Exercise in the Assignment when we introduce it?
- because python has the lock.
- "Yes, and We are giving you code for Exercise1, it has 
- ' how to create a jar in eclipse' <-- wasn't this expected as pre-req


- can create an /output folder in my zip
- t2.xlarge <-- she said 4Cores in htop demo


multiprocessing.Process,
"the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine."
https://docs.python.org/3/library/multiprocessing.html

- iotop is total usage of the Disk. but can't see process or pid
"iotop watches I/O usage information output by the Linux kernel (requires 2.6.20 or later) and displays a table of current I/O usage by processes or threads on the system."

- htop 
https://hisham.hm/htop/
press F2 to configure... F7, F8 to move up/down order of the columns. F9 is to remove. arrow keys
F3 for searching a process, filter it
F5 sorted view
can click on 1 , highlight it, "see that the CPU the process is running on keeps changing"



'pstree'-p <pid>'



JAVA time...
- java does does multi-threading better, don't have to select 'multiprocessing'








------------------------------------------------------------------------------
WASTE...
singl-thread, how to use scp,
'color schemes'
how to install htop






-------
t2.xlarge

sometimes need sudo:
 wcap  ~/<some>/<where> ▶  
 $ sudo ssh -i "the.pem" centos@ec2<params>.compute.amazonaws.com
Last login: Tue Sep 10 20:15:13 2019 from 146.115.176.44


need sudo:
[centos@ip-<IPv4> ~]$ sudo iotop


---------------
HOMEWORK 09/12

UPDATED FONT'Droid Sans Mono', 'monospace', monospace, 'Droid Sans Fallback'


TODO Need the multiprocessor thing, maybe htop will show it across multiple Processes? compare to 'multithreading' first attempted
TODO Figure out what those bars in htop are for
0 FOR_SUBMIT Sentry environmental var name
1 FOR_SUBMIT Cleanup Files not working
2 FOR_SUBMIT Export the threading and cleanup_files functions? decorators for both? Class instantiation?
3 FOR_SUBMIT create_file w/ more columns, randomness, borrow from lab
4 FOR_submit Colorized logging, sentry
5 FOR_SUBMIT threadName printed but no threadId
6 FOR_SUBMIT wait_for_threads or not at end?
7 FOR_SUBMIT README.md cleaned up!!!!!!
8 FOR_SUBMIT module generator, main(), if __name__, sentry, 

TODO iotop for io_intensive 4CPU, 8CPU

htop
System76 Oryx Pro has:
4.1 GHz i7-8750H (2.2 up to 4.1 GHz – 9MB Cache – 6 Cores – 12 Threads)

## Scp this to 4 CPU and 8 CPU EC2 Instances
#### don't forget to ctrl+c. I used to be able to ctrl+c to kill it, but now it hangs, ctrl+c fails, and swp space goes jup to 2.87G/4.00G 
```
python3 processor.py 2 cpu_intensive
python3 processor.py 4 cpu_intensive
python3 processor.py 16 cpu_intensive
```
## Scp this to 4 CPU and 8 CPU EC2 Instances
#### I ran it at 500 threads and bars went up to 30%, all 12 of them
```
python3 processor.py 2 io_intensive
python3 processor.py 4 io_intensive
python3 processor.py 16 io_intensive
```


#### filenames for htop screensehots
4 CPU
cpu_intensive_cpu4thread2 9-19%
cpu_intensive_cpu4thread4 9-19% on all four
cpu_intensive_cpu4thread16 30-60% on all four

cpu_intensive_cpu8thread2
cpu_intensive_cpu8thread4
cpu_intensive_cpu8thread16


8 CPU
io_intensive_cpu4thread2
io_intensive_cpu4thread4
io_intensive_cpu4thread16

io_intensive_cpu4thread2
io_intensive_cpu4thread4
io_intensive_cpu4thread16


often cycled like 18, 26, 34...
or 9, 16 back and forth


TODO 8:51
Problem3
reads and outputs:
```
cadf21578f704c0f92a73a9e47888281,2019-09-14T23:56:58.560Z,http://example.com/?url=081,user-061,EH,Edge,Linux,501,0.9176
65879e7f2243448a97fd9538ba21387f,2019-09-14T23:57:24.480Z,http://example.com/?url=179,user-050,ZW,Edge,Android,499,0.1753
30ba9096104a47ef9af9f65d2b7e3822,2019-09-14T23:57:50.400Z,http://example.com/?url=023,user-029,SG,Opera,Mac,415,0.3504
d8ea26e4706b48f79a7eecd0f4483f9f,2019-09-14T23:58:16.320Z,http://example.com/?url=105,user-074,EC,Opera,windows,507,0.4426
24b893f93f4949509b8b4ba077a9743a,2019-09-14T23:58:42.240Z,http://example.com/?url=104,user-054,AU,IE,windows,226,0.9244
ea5a9675f35d46b79fa07d41986776df,2019-09-14T23:59:08.160Z,http://example.com/?url=090,user-067,CU,IE,Android,511,0.2036
4dc76bdc00ee4322b326ab6b19e44972,2019-09-14T23:59:34.080Z,http://example.com/?url=020,user-024,ER,Opera,Android,507,0.7050
7aac76c8320347e5a33cf8b7ef86e241,2019-09-15T00:00:00Z,http://example.com/?url=008,user-001,MH,IE,windows,301,0.8516
[centos@ip-172-31-14-99 ~]$ 
```
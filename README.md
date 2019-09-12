# Big Data Processing
.pem for ssh to ec2

`import inspect` https://docs.python.org/3/library/inspect.html



# Python Package Hosting
so its ofishal

[pypiserver](https://www.linode.com/docs/applications/project-management/how-to-create-a-private-python-package-repository/)

[pypa/warehouse](https://github.com/pypa/warehouse)


# TODO
- debugger
- print current thread
- hosting python package over the internet
- instead of Decorator, could do a Class that inherits from threading.Thread, like https://www.geeksforgeeks.org/writing-files-background-python/
- 'background thread' concept, is that what it'll always be?

# Interesting
[import inspect](https://docs.python.org/3/library/inspect.html)
```
>>> test_for_class = inspect.stack()
>>> type(test_for_class)
<class 'list'>
>>> test_for_class.isclass()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'isclass'
>>> inspect.isclass(test_for_class)
False
```

sounds brutal:
https://stackoverflow.com/questions/11983938/python-appending-to-same-file-from-multiple-threads really need to do this?




```
# doesnt work
# print(threading.currentThread()) # or current_thread()
# or [2][3] for parent function

# is of type class:
# inspect.stack()


# print(inspect.getframeinfo())
# for thing in my_list:
#     print(thing)


# print(inspect.stack()) 
```


didnt work out  
_thread.start_new_thread(create_file, (numLines, num))
----------------------



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



the cpu IS a processor



// REMINDER 
// Put Sentry to this!!!! WILL'S PYTHON PROJECT....python-eat?#



----------------
LECTURE FROM 0th minute
09/12
DataProcessingApp (layer) we scaled veritically so far

CPU, IO, RAM  
*increase the throughput of buses that send instructions from Cores to to other units *


XY and Z Scaling

different types of power on your physical servers (ec2)


'Function PRogramming makes ZScaling for data decomposition'

Main concepts:
processor 
cpu
physical core
logical coroes => hyper-threading
logicalCPU vs virtualCPU vs cloud virtualization *
"Multiprocessor (with single core processor)" vs Multi-core architecture *



CPU-has-RAM? its own? or public RAM?
"one CPU can have multiple Cores (multi-core)"
"Multiple cores have tehir own memory adn share memory, within the same Processor (CPU!?)"
'the ALU is what executes the instructions (which are managed in Registers by CPU, among other details, scheduler, message bus...)' *
'the control unit. its like a coordinator between the components on the physical CPU'


"The logical/virtual cpu, has its own registers, but uses the same ALU unit"*
















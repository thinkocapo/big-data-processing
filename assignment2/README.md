## Problems 1,2
`process.py`
#### Run these on 4cpu EC2 and 8cpu EC2
```
python processor.py 2 cpu_intensive
python processor.py 4 cpu_intensive
python processor.py 16 cpu_intensive

python processor.py 2 io_intensive
python processor.py 4 io_intensive
python processor.py 16 io_intensive
```

#### filenames for htop screensehots
4 CPU
```
cpu_intensive_cpu4thread2.png
cpu_intensive_cpu4thread4 
cpu_intensive_cpu4thread16

cpu_intensive_cpu8thread2
cpu_intensive_cpu8thread4
cpu_intensive_cpu8thread16
```
8 CPU
```
io_intensive_cpu4thread2.png
io_intensive_cpu4thread4
io_intensive_cpu4thread16

io_intensive_cpu8thread2
io_intensive_cpu8thread4
io_intensive_cpu8thread16
```
## Problems 3,4
`counter.py`
#### Run these commands on a 4CPU EC2
```
python countery.py query1
python countery.py query2
python countery.py query4
python countery.py problem4
```
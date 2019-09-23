## Problem 1, 2 Instructions
1. `scp` the docker-compose.yaml, requirements, redis-clientpy, Dockerfile into ec2  
2.  
Terminal1 - `docker-compose build` and `docker-compose up` *  
Terminal2 - `docker exec -it <redis-server>` and redis-cli for the specified keys  
```
# query1
HGET 2019-9-14:23 count

# query2
HGET 2019-09-14:14:http://example.com/?url=042 count

<date:hour:url>,  unique_user_count
2019-09-14:14:http://example.com/?url=042, ??
2019-09-12:19:http://example.com/?url=013, ??
2019-09-14:03:http://example.com/?url=162, ??
2019-09-13:01:http://example.com/?url=035, ??
2019-09-14:10:http://example.com/?url=043, ??
    
# query3
HGET 2019-09-14:14 http://example.com/?url=042

<date:hour:url>,  event_count
2019-09-14:14:http://example.com/?url=042, ??
2019-09-12:19:http://example.com/?url=013, ??
2019-09-14:03:http://example.com/?url=162, ??
2019-09-13:01:http://example.com/?url=035, ??
2019-09-14:10:http://example.com/?url=043, ??

# query4
HGET 2019-09-14:02:BW count
        
 
```  
3. `docker-compose down`  
3. Update the docker-compose.yaml so it sends query2, query3, then `scp` again, follow steps 1-3 again**  


*ideally should end in a redis-cli monitor in the foreground, but I only saw `-d` detach option for sending all to background.  
**need parameterize the selected query so it's like `docker-compose up <query1>`  
## Problem 3 Bonus
## Problem 4 Instructions
"security group is on the subnet and your ssh from your laptop is not allowed"
1. ec2
2. select Master node ec2
3. view inbound rules > see your I.P. not in there. you'll see IP's of the subnet
4. click SecurityGroup: ElasticMapReduce-master
5. Inbound Rules...Edit...add my IP
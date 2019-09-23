# redisClient.saad(timestamp_hour, url)
        # SMEMBERS for timestamp_hour gives you all the URL's

'''
$ docker exec -it 0a1c3f190cdd bash
root@0a1c3f190cdd:/data# redis-cli
127.0.0.1:6379> HSET 2019-09-20:12 www.google.com/url1 true
(integer) 1
127.0.0.1:6379> HGET 2019-09-20:12 www.google.com/url1
"true"
127.0.0.1:6379> HINCRBY 2019-09-20:12 count
(error) ERR wrong number of arguments for 'hincrby' command
127.0.0.1:6379> HINCRBY 2019-09-20:12 count 1
(integer) 1
127.0.0.1:6379> HGET 2019-09-20:12 count
"1"
127.0.0.1:6379> HINCRBY 2019-09-20:12 count 1
(integer) 2
127.0.0.1:6379> HINCRBY 2019-09-20:12 count 1
(integer) 3
127.0.0.1:6379> HGET 2019-09-20:12 count
"3"
127.0.0.1:6379> 
'''

# Write to Redis
# 2 python perations (if..not..in and url_map), 1 redis operation
# if url not in url_map:
#     url_map[url] = True
#     redisClient.hincrby(timestamp_hour, 'count', 1)

'''
10:06p
PROOF THAT IT WORKED
 wcap  ~/thinkocapo/big-data-processing/assignment3 ▶  
 $ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
e0bad9f49ecd        redis               "docker-entrypoint.s…"   31 seconds ago      Up 30 seconds       0.0.0.0:8081->6379/tcp   assignment3_redis-server_1
 wcap  ~/thinkocapo/big-data-processing/assignment3 ▶  
 $ docker exec -it e0bad9f49ecd bash
root@e0bad9f49ecd:/data# redis-cli
127.0.0.1:6379> HGET 2019-9-14:23 count        94 (csv1) 101 (csv2)
"96"
127.0.0.1:6379> 
'''

# redis-cli monitor

# ElasticMapReduce
 $ ssh -i ~/keypairs/assignment2.pem hadoop@ec2-18-216-238-231.us-east-2.compute.amazonaws.com


# for testing on local hostname=wcap
python redis-client.py query1 --file file-input1.csv
python redis-client.py query1 --file file-input2.csv
python redis-client.py query1 --file file-input3.csv
python redis-client.py query1 --file file-input4.csv

4:48p
ssh...
sudo ssh -i ~/your.pem centos@ec2-<IP_AD_DRESS_HERE>.us-east-2.compute.amazonaws.com
scp...
sudo scp -i ~/your.pem ./docker-compose.yaml centos@ec2-<IP_AD_DRESS_HERE>.us-east-2.compute.amazonaws.com:./
sudo scp -i ~/your.pem ./Dockerfile centos@ec2-<IP_AD_DRESS_HERE>.us-east-2.compute.amazonaws.com:./
sudo scp -i ~/your.pem ./redis-client.py centos@ec2-<IP_AD_DRESS_HERE>.us-east-2.compute.amazonaws.com:./
sudo scp -i ~/your.pem ./requirements.txt centos@ec2-<IP_AD_DRESS_HERE>.us-east-2.compute.amazonaws.com:./


GET THE CSV'S TO LOCAL
sudo scp -i ~/your.pem centos@ec2-<IP_AD_DRESS_HERE>.us-east-2.compute.amazonaws.com:./input_files/file-input1.csv ./
sudo scp -i ~/your.pem centos@ec2-<IP_AD_DRESS_HERE>.us-east-2.compute.amazonaws.com:./input_files/file-input2.csv ./
sudo scp -i ~/your.pem centos@ec2-<IP_AD_DRESS_HERE>.us-east-2.compute.amazonaws.com:./input_files/file-input3.csv ./
sudo scp -i ~/your.pem centos@ec2-<IP_AD_DRESS_HERE>.us-east-2.compute.amazonaws.com:./input_files/file-input4.csv ./


docker-compose up
- then docker-compose down
- then docker images, docker image rm <image_id>

TRY TO RUN IT ONCE MORE
`docker-compose run python-redis-1`
but you'd have to re-build image if you had any code changes

HOW TO REBUILD IMAGES
docker-compose build
docker-compose up
^^ should only rebuild the python-redis clients,
check by `docker images` and see when images last updated

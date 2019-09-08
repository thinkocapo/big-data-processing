'''
$ docker run --name redis-server -d -p 6379:6379 redis
01ee114c2750aecaca5960bdfd238d71e614b689773d5fccccbb38d562f92a9f
 wcap  ~/thinkocapo/big-data-processing ▶  

 $ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
01ee114c2750        redis               "docker-entrypoint.s…"   7 seconds ago       Up 6 seconds        0.0.0.0:6379->6379/tcp   redis-server

 wcap  ~/thinkocapo/big-data-processing ▶  
 $ nc -vz localhost 6379
Connection to localhost 6379 port [tcp/*] succeeded!
'''

1:29a - turns out dont need this - using redis-cli






09/08/19

# it said '5432 already in use' so using 5433 instead
$ docker run --name postgres-bdp -d -p 5433:5433 postgres


# 2
$ docker exec -it cbd9c42ba80e bash

# 3 if you only write 'psql' then get error 'psql: FATAL:  role "root" does not exist'
$ psql -h localhost -U postgres
root@cbd9c42ba80e:
psql (11.5 (Debian 11.5-1.pgdg90+1))
Type "help" for help.
postgres=# 


OR
https://hub.docker.com/_/postgres
 or via psql
$ docker run -it --rm --network some-network postgres psql -h some-postgres -U postgres
/OR


postgres-# \c postgres
You are now connected to database "postgres" as user "postgres".
postgres=#

In a 'public' schema, create a table named "<your_last_name>_data" that contains the following:
an ID of type integer that cannot be null, and must increment automatically
a name that is a character string and cannot be null
a creation date that is of type date
a primary key (what should your primary key be?)
- was overhtinking it, as a pkey id auto incrementing is the expected behavior!
CREATE TABLE "capozzoli_data"(
    id SERIAL PRIMARY KEY,
    created DATE
);

INSERT INTO capozzoli_data(id, created) VALUES(DEFAULT, CURRENT_TIMESTAMP);
# Week 4 — Postgres and RDS

- [Summary](#summary)
- [Homework](#homework)
- [Homework Challenges](#homework-challenges)

## Summary
## Homework
## Homework Challenges
## Try Harder

## Steps

- Create RDS Database : PostGreSQL
    - Character set
    - Timezone
- Template free-tier
- Master username (turn off)
- Back up (turn off)

- Create AWS CLI
- Stop temp
- Bring back compose
- Connect to dynamodb localhost

- Create database cruder
- \l : list down database

Setting up the variables for connection_url

And prod_connection_url for RDS, and copy the endpoint of RDS from AWS.

- Create folder bin for bash script to create/drop
- Chmod for executable script
    - Chmod u+x
- Edit the connection url to ensure no name of database
- Register to path to easy call
- Configure the db schema load .sql for the schema
    - Realpath. 
    - #! /usr/bin/bash
- Configure arguments to easily switch between the local and cloud one
- Make up some color for other scripts
- Create tables: users and activities
    - Traps everywhere
    - Insert new user_uuid UUID NOT NULL into table activities
- Drop for some existed tables
- 4th script - dbconnect
- 5th db seed
- Some custom lambda function to put some cognito

- Commit [1d26acf](https://github.com/lhviet204/aws-bootcamp-cruddur-2023/commit/1d26acf5fef57905e8c1aa231279abbe89ad3284)

![](./assets/week2/)
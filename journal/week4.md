# Week 4 — Postgres and RDS

- [Summary](#summary)
- [Homework](#homework)
- [Homework Challenges](#homework-challenges)

## Summary
This week I learn three areas on AWS(RDS, Lambda, Network Security); on programming and project structure (how to establish DB script in bash for setup, connect, drop, create; how to manage SQL scripts seperately), on Python (splating, Interpolation, how to edit mutable python tuple object). There are many weeks I need to catch up with class. Continue from the previous setences, this week I start with the remaining of this week. AWS RDS data is created via AWS CLI and allowed the connection from GITPOD. I can load the seed data from AWS RDS from FE. I successlly impletemed the create activity functions on Cruddur, data will be insereted into AWS database RDS.

## Homework
- Since we modified the schema of DB to not allow NULL data, so we need to modify the db-seed data to be able for db-setup script.
![](./assets/week4/Homework_db_seed_modification.png)

- After we can setup the DB seed, we can load the seed data from FE.
![](./assets/week4/Homework_UI_loading_seed_from_RDS.png)

- We successfully implemented create_activity on our cruddur application, the data will be imported into AWS RDS

![](./assets/week4/Homework_create_activity_successfully.png)

SQL statement is recored on our AWS Cloud Watch logs
![](./assets/week4/Homework_create_activity_successfully_cloudtrail.png)
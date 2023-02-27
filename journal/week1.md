# Week 01 — App Containerization
- [Summary](#Summary)

- [Homework](#Homework)
  + [Containerize Backend and Frontend](#containerize-backend-and-frontend)
  + [Document the OpenAPI definitions](#updating-the-openapi-definitions)
  + [Updating the backend and frontend code to add notifications functionality](#updating-the-backend-and-frontend-code-to-add-notifications-functionality)
  + [DB part - DynamoDB and Postgres](#DB-part---DynamoDB-and-Postgres)

- [Homework Challenges](#homework-challenges)
  + [def](#def)



## Summary

This week, I was able to follow and complete the week's homework, however I haven't solved the issue with hardcode credentinal on docker compose for postgres database. For homework challenges, I finished 6/8 challenges expect the challenges for running outside Gitpod and on EC2. For the challenges on multi-stage build and best pratice for docker file, there are a lot of space to improve, since my handons exprience is not enough. 

## Homework

#### Containerize Backend and Frontend Application
- [backend docker file](https://github.com/lhviet204/aws-bootcamp-cruddur-2023/blob/main/backend-flask/Dockerfile)
- [frontend docker file](https://github.com/lhviet204/aws-bootcamp-cruddur-2023/blob/main/frontend-react-js/Dockerfile)

#### Document the OpenAPI definition
- Commits [ae07e6f](https://github.com/lhviet204/aws-bootcamp-cruddur-2023/commit/ae07e6fec09323d875d6188fb2cc744afa9f42a7) ; [922b5b6](https://github.com/lhviet204/aws-bootcamp-cruddur-2023/commit/922b5b63c32b4a9fb784aea705a6fcdfa50b4757) 

#### Write the backend and frontend code to add notification functionality
- Commits [ae07e6f](https://github.com/lhviet204/aws-bootcamp-cruddur-2023/commit/ae07e6fec09323d875d6188fb2cc744afa9f42a7) ; [922b5b6](https://github.com/lhviet204/aws-bootcamp-cruddur-2023/commit/922b5b63c32b4a9fb784aea705a6fcdfa50b4757)

![No authenticated session](assets/week1/crud_not_authenticated_profile.png) Applicaion without authenticated account


![authenticated session](assets/week1/crud_authenticated_profile.png)
Applicaion with authenticated account

#### DB part - DynamoDB and Postgres
Postgres DB was connected via two methods by extension and and via CLI

![postgre2](assets/week1/successful_connected_postgresql_2.png) Connect via extension

![postgrecli](assets/week1/successful_connected_postgresql_cli.png) Connect via CLI
![]()

## Homework Challenges

Container Image : https://hub.docker.com/layers/lhviet204/crud-backend-flask/1.0/images/sha256-092e191c0c80c9d815ae8920b759cde6ff1001762d03ed76884b01d1b36f05ff?tab=layers

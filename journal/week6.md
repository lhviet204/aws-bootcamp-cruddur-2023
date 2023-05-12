# Week 6 — Deploying Containers

- [Summary](#summary)
- [Homework](#homework)

## Summary
"Those weeks" I has learnt and gained many expereinces from various areas, especially end-to-end progress to publish the mordern applications consisting of front and back end into AWS environment with in-use AWS services like Route53, ALB, Target Group, ECS, ECR, RDS, DynamoDB, Cloudwatch logs, IAM roles ... The app is running normanlly on my own domain.

High level steps consist of
- create ECR for python, backend, frontend repository
- Build and Push new images
- Create ECS and Register task-definitions, services, security groups for ECS with correct IAM roles for service execution/task roles.
- Create Route53 public hosted-zones
- Create Public certificates for domains from ACM
- Create Target Groups, Security Groups for ALB, Create ALB, Listener and Manage rule to forward/redirect
- Create A records for FE and BE pointing to ALB
- Revise service and task definition with ALB supporting

## Homework

- Commit [1d26acf](https://github.com/lhviet204/aws-bootcamp-cruddur-2023/commit/1d26acf5fef57905e8c1aa231279abbe89ad3284)
![](./assets/week2/)

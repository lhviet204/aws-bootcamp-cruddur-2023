# Week 8 — Serverless Image Processing


- [Summary](#summary)
- [Homework](#homework)

## Summary
This week, I've learned about CDK to create AWS Services like Lambda, S3 bucket, IAM roles for Cruddur uploading avatars for User Profiles. The concept for now is user uploading images to AWS S3 folder named original, the images will be progressed by lambda with js sharp library to resize the pictures and send back confirmation to our application webhook (?)

In addition, I also learn about fundamental of AWS CDK. There are many construct type of data are being used i.e. Level 1, Level 2, Level 3. Level 1 is the native of cloud formation, level 2 is common pattern of using AWS services, level 3 is purely opinionated stack. Also how to leverage aws cdk synth to check the stack before deployment.

Design ideas on how to arch the stack, the resources ... to avoid the misconfiguration, mistakes.
How to use UI of AWS Cloud Formation
How to reference another AWS resources into the stack without deleteing them.

## Homework

High level of implementation is described as below:
- Setting CDK folder named "thumbing-serverless-cdk"
- Installing the required library "aws-cdk"
- Initing the CDK app by "type-script"
- Boosting trapping the folder for each region implemeting
- Implemeting the stack code with S3, Lambda, env library
- Implemeting the utilit scripts to upload data, clear data of samples

Implement AWS Cloud Front
Week08 : Serving Avatars via Cloud Front https://www.youtube.com/watch?v=Hl5XVb7dL6I

- Implement Cloud Front manually on console to review all the configuration and parameters
    - Origin domain == our assets.cruddur.com.s3.ca-central-1.amazonaws.com
    - Name of the origin == default
    - Origin Access
        - Origin access control settings
        - Create control settings
            - Signing behaviors
        - Viewer
            - Redirect HTTP to HTTPS
        - Restrict viewer access
            - Signed url and signed cookies
        - Cache policy
        - Origin Policy
    - Response headers policy
        - Simple CORS
    - Price Class
    - Alternate domain name (CNAME)
        - assets.cruddur.com
    - The certificate must be us-east-1; because Cloud Front is Global services
    - Description
- Get distributions domain name
    - Try the path name of s3 bucket

- Separate into two buckets, edit the local env for name of the bucket, edit the stack also.

- Setting up data retention on upload bucket

Current github commit https://github.com/omenking/aws-bootcamp-cruddur-2023/commits/week-8-again
 

Next steps:
- To implement AWS Cloud Front

- To integrate with the current applications
https://www.youtube.com/watch?v=WdVPx-LLjQ8






- Commit [1d26acf](https://github.com/lhviet204/aws-bootcamp-cruddur-2023/commit/1d26acf5fef57905e8c1aa231279abbe89ad3284)
![](./assets/week2/)

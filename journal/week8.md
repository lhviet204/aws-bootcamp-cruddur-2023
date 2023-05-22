# Week 8 — Serverless Image Processing


- [Summary](#summary)
- [Homework](#homework)

## TODO
- On gitpods

#1 Implement lambda progress images
cd aws/lambdas/process-images
npm init -y
npm install sharp @aws-sdk/client-s3

#2 bootstrapping for CKD to implement that Lambda
cd thumbing-serverless-cdk
touch .env.example
npm install aws-cdk -g
cdk init app --language typescript
npm install dotenv

Create stack ThumbingServerlessCdkStack:

run cdk synth to review cdk.out
run cdk bootstrap "aws://${AWS_ACCOUNT_ID}/${AWS_DEFAULT_REGION}" 
run cdk deploy

- AWS parts
    + implement cloud front
    + create dns records from route53 and its alias to point to new cloudfront distribution
    + create invalidation rules to let Cloud Front always server the latest avatars
    + implement lambda, iam roles, and buckets with CORS and Bucket Access Policy
    + AWS CLI for upload pictures and clear the pictures on the buckets 

- Implement CDK pipeline
    2nd commit https://github.com/omenking/aws-bootcamp-cruddur-2023/commit/5626b910c3d01ac49893ea182b186b4b9b1d7ebe#diff-8b72e4ebe6afc9b82fcdb1f144c2859c958ab22b41da71a16b22e3477411589b

    what does it implement in the nut shell ? lambda?
    
- Implement boostrapping and utilities scripts
    https://github.com/omenking/aws-bootcamp-cruddur-2023/commit/c0743853bb5f7761c253a4ddb21b7908d1d36724
    for local envirornment espeicall on database

- Implement lambda https://github.com/omenking/aws-bootcamp-cruddur-2023/commit/a1559e12f9791edf17024a7e4ccc545447487979#diff-a2ae174ea6ad8824e8dd9bbbe6235d2a8f51ab4ca4b17c1686750c00b589fa98
    - cruddur-upload-avatar
        + to ensure CORS as HTTP Header configuration https://github.com/omenking/aws-bootcamp-cruddur-2023/commit/f0b1469a1b075acb60762ab108a021d945c24d69#diff-8bb1ceece57f661ba58a537e598e8341708a57e707267ea40b4b3470b1f8a0fb

        revise to parse the UUID https://github.com/omenking/aws-bootcamp-cruddur-2023/commit/577be5a2ded14bb9572ed99892ecc58361956aec#diff-8bb1ceece57f661ba58a537e598e8341708a57e707267ea40b4b3470b1f8a0fb

        + to build the layer https://github.com/omenking/aws-bootcamp-cruddur-2023/commit/577be5a2ded14bb9572ed99892ecc58361956aec#diff-15a93ce383061e0d60c29596313d0c887c7bfdc7e8b24cde175e3dce0bc7b917
        + get the AWS CLI to push the layer and attach to the lambda

    - lambda authorizer
        + to ensure npm init the source code for packages

    - process-images
        + to ensure npm init the source code for packages json    

    - Search //TODO to fix the env of AWS CLI for dev and prod env
    - Search //TODO to fix the env from FE and BE source code
    - Think about only allow to upload specific extension of images

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

TODO: Missing steps for gitpod

npm install aws-cdk -g
cdk init app --language typescript
then edit on the folders with new code (skip)

https://github.com/omenking/aws-bootcamp-cruddur-2023/commit/cd7f2ebf4fa3034e4b2e0fe36fa4e04ee566e847
https://github.com/omenking/aws-bootcamp-cruddur-2023/blob/week-8-serverless-cdk/journal/week8.md


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
 

Next videos is week 8 - to implement migrations backend endpoint and profile form

- Edit python docker file on dev env to debug more easily.
- Edit gitpod yaml for fully functional working tabs
- Do sth to fix the prepare script for spin up the dev env
- Come 22:00 to do some config for frontend js.
- Implement edit profile form 25:18 (profile-form.js / profile-form.css)
- Import new form UserFeedPage.js
- Implement new popup.css, and import it into app.js as global
- Implement new endpoint for backend
    - Declare new route /api/profile/update
    - Import updateprofile
    - Implement update profile from services
- Implement new sql stored_procedure from user folder
    - SQL migration tool?
- Make new folder bin generate
    - File migration python
    - Folder migrate/rollback for bin folder.
    - We need new table so edit schema load for new table .
    - Update new arguments called verbose for python db.py
- Migration == sql academy, sql transaction from postgres
- Edit name of the query from db.py to correct name function query elect object  to query object json (actual a dict)
- Bio == bio from social medial 
- Edit project heading.js and css
- Edit show.sql to return bio from sql statement
Commit name : implement  implement migrations, implement the profile page, imeplement the endp…


Next thing:
- S3 bucket upload client side
- Upload s3 folder, then spit back out
- Lambda to check cache, and server it?

Steps to implement Avatar Uploading, the design will require to implement two Lambda (Authorization, Get pre-signed URL and upload the images with UUID name), API gateway with custom domain name.

- Create API gateway and get revoke URL, configure route
- Create two buckets and implement CORS for each of them
- Create Lambda function CruddurAvatarUpload
- Create a new role with basic Lambda permission and PresignedAvatarPresignedURL IAM permission, and make sure Cloud Watch logs permission to debug
- Revise local env for FE with new implementation including presigned URL, API GW endpoint, 
- Configure DB scripts with migrate, consolidate to one script to prepare for local env
- Configure FE new implmenetation 
- Configure Lambda Layers for RUBY lambday can validate and parse JWT token and name the avatar correctonly on the bucket.
- Implement new FE code to render avatar

Tips:
- Be aware of CORS, env every single time,  and custom domain name needs to be pointed correctly to revoke URL of API GW.
- To prepare AWS CLI for create lamda layers, apply layers for exisiting lambda
- To prepare lambda python instead of ruby
- To edit gitpod.yaml for productivity


- Commit [1d26acf](https://github.com/lhviet204/aws-bootcamp-cruddur-2023/commit/1d26acf5fef57905e8c1aa231279abbe89ad3284)
![](./assets/week2/)


### Raw note:
implement avatar uploading

- remind boostrap for s3 to upload sample datas to s3.

- will put profileform.js page

cd front-react-js
npm i @aws-sdk/client-s3 --save

how to configure the javascript client side

recommd using webpack to bunder the required SDK for java script files.

/ building sdk for browsers

pre-signed url to upload an object s3.

>> to decide API Gateway and lambda for doing
(support free tier)
find jwt authorizer for API

Create Lambda function
CruddurAvatarUpload
Create a new role with basic Lambda permission

Make new folder on source code for saving
20:00 https://www.youtube.com/watch?v=Bk2tq4pliy8
to configure rb
to configure the client by using local environment 
+ set up the bucketname for uploading avatar
+ ? configure the required content type for request.

install "ox" for library using from ruby.

implement the ruby exmaple
then run the command
"bundle exec ruby function.rb"

configure ways on uploading s3 via presigned url on vscode generated from previous step.

https://aws.amazon.com/blogs/compute/uploading-to-amazon-s3-directly-from-a-web-or-mobile-application/

running by method PUT for s3

create the life cycle configuration on s3 management

copy rb code to lambda ruby
crate iam policy for that
ensure to point directly to ARN

PresignedAvatarPresignedURL

Copy to source code also (folder policies)

edit sth on handler (what is handler)

still to required lambda authorizer

create new lambda authorizer 
file index.js from github of aws; (checking token_use)

zip and upload under zip for contain the package json for lambda authorizer

- create API Gateway
1. for upload
2. route


get the status of aws resources by CLI : 1:08:00

then attach authorizer for the upload lambda

create deployment

then have the invoke url, try the invoke url.

working with local env

compose up
db step
ddb schemaload, and ddb seed

then intergrate with new lambda

s3upload const
on profile form and profile css
- const backend url from revoke url from api gateway.
- post the request to get the presigned url
- then put the image by using presigned url

check api gateway on stage (deployment)

''' question?
CORS: options for api gateway
then put?
'''

issues with checking the implementation of profile page for local environment because the schema is missing bio, so we need to run migrate. /bin/db/migrate

get presigned url 

pass along binary data

still CORS issues with API gateway for uploading and authorize

+ commit name is "almost got uploading state completely"
CORS
access control allow header
access control expose header

###
new video for https://www.youtube.com/watch?v=eO7bw6_nOIc

1. fix the gitpod yaml with bash run required scripts like ecr login
2. ruby (not using generate env) >> might be we implement our own solution

add proxy for letting lambda handle the allow headers and expose headers

revise setup script to include the migrate script also.

and aslo pass orgin with the request from FE also on "ProfileForm.js"

remember about the syntax of CORS and Orgin, no need the forward trailling and slash.

commit name is "run migration when we do setup, generating out presigned url should work

Question
point our LB to our API GW, then create prefix >> to API GW, Fargate

create custom domain names to api.cruddur.com
>> how does it work?

next steps
- to watch videos for final cors
- to see the render avatar
- week 09

Ask GPT on working

env file for K8S
and CISA DEVSECOPS


@@@ 
Come to findal CORS
https://www.youtube.com/watch?v=uWhdz5unipA

- Implement CORS for Buckets on the left.
- Edit bucket policy for s3 https://youtu.be/uWhdz5unipA?t=267
- put new file into folder s3 at our source code.

then run db setup to include the migrate (put python infront of the script)

ALB can't be put 
infront of API GW, due to no target group.
so need to have custom domains.

be careful to create or update the API GW, the domain will be changed.

Be careful to check URL for FE, for API GW and BE. then to run the script upload.

on UI of API GW
- APIS >> when we change or update new URL will be generated
- Custom domain name needs to be mapped directly with APIs on the tops.

afer edit CORS on the bucket
edit the domain name and URL for API GW, the variables from the source code; we can upload image successfully

check logsource group of lambda named "cruddurAvatarUpload"

check the week 06 for default handler with Ms chinese

so right now we want to replace the real uploaded data instead of mock.jpg; we're doing some stuff to parse the jwt token, get the metadata from the images ....

lambda layers can solve the required dependices and library . ask bing on that

lambda ruby runtime (to check what is the default installation for runtime env)

>> zip the cruddur upload avatar again after install all required dependcies for ruby.

>> come to make lambda layers for ruby, kind of like docker layer

>> the using aws cli to edit or upload layers to our current lambda

upload layer
then configure the lamba to use that layer.

remember to configure orgin to prod env when we're working on the AWS

What we're trying to do is decode the jwt token to get uuid and put the name on the file, and upload into the bucket.

commit name is:
make sure we can upload the avatar

@ video about render avatar from cloud front
https://www.youtube.com/watch?v=xrFo3QLoBp8

Create ProfileAvatar.js and css
Edit CheckAuth
Import ProfileAvart to ProfileInfo.js
Edit ProfileHeading.js
Edit show.sql
https://github.com/omenking/aws-bootcamp-cruddur-2023/commit/ecd2f12ee5043b3ac731fb45ec5d268d8ffe192f


















code examples
Strangler pattern
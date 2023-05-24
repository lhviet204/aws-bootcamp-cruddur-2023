import boto3
import json
import jwt
import os

def handler(event, context):
    print(event)
    # return cors headers for preflight check
    if event['routeKey'] == "OPTIONS /{proxy+}":
        print(json.dumps({'step': 'preflight', 'message': 'preflight CORS check'}))
        return {
            'headers': {
                "Access-Control-Allow-Headers": "*, Authorization",
                "Access-Control-Allow-Origin": "https://3000-lhviet204-awsbootcampcr-bgsgpelsdm8.ws-us97.gitpod.io",
                "Access-Control-Allow-Methods": "OPTIONS,GET,POST"
            },
            'statusCode': 200
        }
    else:
        token = event['headers']['authorization'].split(' ')[1]
        print(json.dumps({'step': 'presignedurl', 'access_token': token}))

        body_hash = json.loads(event["body"])
        extension = body_hash["extension"]

        decoded_token = jwt.decode(token, None, False)
        cognito_user_uuid = decoded_token[0]['sub']

        s3 = boto3.resource('s3')
        bucket_name = os.environ["UPLOADS_BUCKET_NAME"]
        object_key = f"{cognito_user_uuid}.{extension}"

        print(json.dumps({'object_key': object_key}))

        obj = s3.Bucket(bucket_name).Object(object_key)
        url = obj.generate_presigned_url('put', ExpiresIn=60 * 5)
        body = json.dumps({'url': url})
        return {
            'headers': {
                "Access-Control-Allow-Headers": "*, Authorization",
                "Access-Control-Allow-Origin": "https://3000-lhviet204-awsbootcampcr-bgsgpelsdm8.ws-us97.gitpod.io",
                "Access-Control-Allow-Methods": "OPTIONS,GET,POST"
            },
            'statusCode': 200,
            'body': body
        }
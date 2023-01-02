import boto3
import os
from botocore.exceptions import ClientError
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

dynamo_client  =  boto3.resource(service_name = 'dynamodb',region_name = 'us-east-1',
              aws_access_key_id = os.getenv("AWS_ACCESS_KEYID"),
              aws_secret_access_key = os.getenv("SECRET_ACCESS_KEY"))


async def addUser(user_id,time_zone):
    user_table=dynamo_client.Table("MyTime_Discord_Bot")
    try:
        user_table.put_item(Item=
        {
            'userid':str(user_id),            
            'time_zone':str(time_zone),
        },
        ConditionExpression = 'attribute_not_exists(userid)')
    except ClientError as e:
        if e.response['Error']['Code']=='ConditionalCheckFailedException':
            return "User already exists"
    return "User added"
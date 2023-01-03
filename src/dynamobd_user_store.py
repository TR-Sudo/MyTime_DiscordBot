import boto3
import os
from botocore.exceptions import ClientError
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

dynamo_client  =  boto3.resource(service_name = 'dynamodb',region_name = os.getenv("REGION"),
              aws_access_key_id = os.getenv("AWS_ACCESS_KEYID"),
              aws_secret_access_key = os.getenv("SECRET_ACCESS_KEY"))

async def add_user(ctx,user_id,time_zone):

    #add to user table
    user_table=dynamo_client.Table("MyTime_Discord_Bot")
    try:
        res=user_table.put_item(Item={'userid':str(user_id),'time_zone':str(time_zone)})
    except ClientError as e: 
        print(e.response['Error']['Code'])

    #Returns message on status 200, else guide user to help 
    if res['ResponseMetadata']['HTTPStatusCode'] == 200:
        await ctx.send(f'{user_id} added with time zone {time_zone}')
    else:
        await ctx.send("failed to add user please enter [>help Mylocation]")

#returns users time zone from database
async def get_user(ctx,user_id):
    user_table=dynamo_client.Table("MyTime_Discord_Bot")
    res=user_table.get_item(Key={'userid':str(user_id)})
    if('Item' not in res):
        return "User needs to be added, Enter [>help MyLocation] for assistance"
    else:
        return (res['Item']['time_zone'])
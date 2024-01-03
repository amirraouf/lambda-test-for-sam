import pymysql
import boto3
import json
import os

def lambda_handler(event, context):
    print(event)
    return {
        'statusCode': 200,
        'body': 'Successfully processed DocumentDB change stream event.'
    }

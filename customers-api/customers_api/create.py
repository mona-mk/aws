import json
import boto3
import os

dynamodb = boto3.resource("dynamodb")
tablename = os.environ.get("CUSTOMERS_TABLE")


def lambda_handler(event, context):
    customer = json.loads(event["body"])
    table = dynamodb.Table(tablename)
    response = table.put_item(TableName=tablename, Item=customer)
    # async
    return {
        "statusCode": 201,
        "headers": {},
        "body": json.dumps({"message": "customer created in DynamoDB"}),
    }

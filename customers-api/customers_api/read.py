import simplejson as json
import boto3
from boto3.dynamodb.conditions import Key
import os

dynamodb = boto3.resource("dynamodb")
tablename = os.environ.get("CUSTOMERS_TABLE")


def lambda_handler(event, context):
    customer_id = int(event["pathParameters"]["id"])
    table = dynamodb.Table(tablename)
    response = table.query(KeyConditionExpression=Key("id").eq(customer_id))
    # async
    return {
        "statusCode": 200,
        "headers": {},
        "body": json.dumps(response["Items"]),
    }

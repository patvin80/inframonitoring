import json

def lambda_handler(event, context):
    return event["key1"][::-1]
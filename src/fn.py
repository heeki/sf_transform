import boto3
import json
import time
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

# initialization
session = boto3.session.Session()
client = session.client('sqs')
patch_all()

def handler(event, context):
    output = event
    print(json.dumps(output))
    time.sleep(30)
    return output

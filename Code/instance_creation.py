import json
import datetime
import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    
    # create a new EC2 instance
    instances = ec2.create_instances(
                ImageId='ami-09d95fab7fff3776c',
                MinCount=1,
                MaxCount=1,
                InstanceType='t2.micro',
                KeyName='aarpbitbucketpem'
    )
    return "Success"
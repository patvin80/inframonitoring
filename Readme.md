# Infra Monitoring Code Snippets

## Introduction
Code Snippets provided in the folder can be copied and pasted in the Lambda Console

## Contents

| # | File Name | Purpose | Description |
| -- | -- | -- | -- |
| 1. | getting_started.py | | A Simple Lambda Code program which simply reverses the string. |
| 2. | instance_creation.py | Boto3 | A program that creates a Lambda function which lets create an instance. |
| 3. | compliance_ebs_encryption.py | Compliance | Event Driven. Checks the EBS volumes encryption status and terminate the instance if the volume is not encrypted. |
| 4. | efficiency_volume_deletion.py | Efficiency | Periodic. Checks the EBS volumes in available status and clear it up. |
| 5. | validate_tags.py | Governance | Periodic. Checks the tags associated with the instances and if appropriate tags are not available then apply them. |

## CloudWatch Rules:
The Event Driven and Periodic execution is configured using the CloudWatch Rules. The Cloud Watch Rules can be configured to run on 
1. A Schedule like a cron job.
2. Event like EC2 Instance creation. 
import boto3
ec2 = boto3.resource('ec2')
def lambda_handler(event, context): 
    instance_to_tag = []
    for instance in ec2.instances.all():
        if instance['State']['Name'] == 'running':

            # If there is no `DoNotTerminate` tag
            if not [tag for tag in instance['Tags'] if tag['Key'] == 'DoNotTerminate' and tag['Value'] == 'True']:
                instance_to_tag.append(instance['InstanceId'])

    # Apply a tag to all instances found
    ec2.create_tags(Resources=instance_to_tag, Tags=[{'Key':'scheduler:ec2-startstop','Value':'True'}])
import json
import boto3

def lambda_handler(event, context):
    """
    Imagine an instance is provisioned with an EBS Volume without encryption. The function checks the volume and terminates it.
    """
    ec2 = boto3.client('ec2')
    try:
        print (event)
        print("==================== Instance Provisioning ================================")
        print(event["detail"]["instance-id"])
        ec2_inst = boto3.resource('ec2', region_name='us-east-1')
        # Filtering the Instance details of only the instance that has been provisioned
        instance = ec2_inst.Instance(event["detail"]["instance-id"])
        volumes = instance.volumes.all()
        for vol in volumes:
            volume = ec2_inst.Volume(vol.id)
            print(" Checking the Instance Volume Encryption")            
            if (not (volume.encrypted)):
                print("Identified Instance has unencrypted disk")
                response = ec2.stop_instances(
                            InstanceIds=[event["detail"]["instance-id"]],
                            DryRun=False)
                print ("Unencrypted disks are not allowed instance terminated")
    except:
        # Send some context about this error to Lambda Logs
        print("Error")

    return json.dumps("Done")
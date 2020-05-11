import boto3
session = boto3.session.Session(profile_name = "root")
ec2_console = session.resource('ec2')
instance = ec2_console.create_instances(
    ImageId='ami-0f7919c33c90f5b58',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
)

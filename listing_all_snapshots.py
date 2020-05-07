import boto3
aws_console = boto3.session.Session(profile_name="root")
ec2_console_re = aws_console.resource('ec2', region_name="us-east-2")

sts_con_cli = aws_console.client('sts')
a = sts_con_cli.get_caller_identity()
my_id = a.get('Account')
print(my_id)

filter_size = {"Name":"volume_size", "values":['8']}
for i in ec2_console_re.snapshots.filter(OwnerIds=['487928121165']):
    print(i)
    print(i.start_time)



import boto3
aws_console = boto3.session.Session(profile_name="root")
ec2_console_re = aws_console.resource('ec2', region_name="us-east-2")
cnt = 1
for i in ec2_console_re.instances.all():
    print(cnt,i,i.instance_id,i.instance_type,i.architecture,i.launch_time.strftime("%Y-%m-%d"),i.private_ip_address)
    cnt+=1

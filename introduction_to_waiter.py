import boto3
import time
aws_con = boto3.session.Session(profile_name="root")
ec2_con_re = aws_con.resource('ec2', region_name="us-east-2")
ec2_con_cli = aws_con.client('ec2', region_name="us-east-2")

my_instance_ob = ec2_con_re.Instance("i-0f759efe2c877e888")

print("your instance is starting.....")
#print(dir(my_instance_ob))
my_instance_ob.start()
#this is inbuilt waititing login in AWS
my_instance_ob.wait_until_running()
print("your instance is up and running now")

#This code for waiting logic for instance to turn into running  state
"""while True:
    my_instance_ob = ec2_con_re.Instance("i-0f759efe2c877e888")
    print("The current state is: ", my_instance_ob.state['Name'])
    if my_instance_ob.state['Name'] == 'running':
        break
    print("waiting to get running status")
    time.sleep(5)
print("Now your instance is up and running...")

"""

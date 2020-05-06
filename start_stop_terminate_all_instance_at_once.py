import boto3
from pprint import pprint
aws_man_con = boto3.session.Session(profile_name="root")
ec2_con_re = aws_man_con.resource('ec2')
ec2_con_cli = aws_man_con.client('ec2')
"""
#print(ec2_con_re.instances)  #This is instance collection object 
#print(dir(ec2_con_re.instances))
required_id = []
for i in ec2_con_re.instances.all():
#    print(i.id)
    required_id.append(i.id)
print("Starting all instances......")
ec2_con_re.instances.start()
#getting a client waiter 
waiter = ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=required_id)
print("your instances are up and running...")"""

#starting instances with specific names
test_ids = []
f1 = {"Name": "tag:Name", "Values":['testing1']}
for i in ec2_con_re.instances.filter(Filters=[f1]):
        test_ids.append(i.id)
print(test_ids)


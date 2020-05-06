import boto3
from pprint import pprint
aws_man_con = boto3.session.Session(profile_name="root")
ec2_con_re = aws_man_con.resource('ec2')
print(ec2_con_re.instances)  #This is instance collection object 
print(dir(ec2_con_re.instances))
#this will give all instances Ids(running,stopped etc)
for i in ec2_con_re.instances.all():
    print(i)
print("------------------------------")
#this will give id's of running instances 
f1 = {"Name": "instance-state-name", "Values":['running']}
f2 = {"Name": "instance-type", "Values":['t2.micro']}
for j in ec2_con_re.instances.filter(Filters=[f1,f2]):
    print(j)


print("-----------------------------")
#this will give only 1 instance id
for k in ec2_con_re.instances.limit(1):
    print(k)


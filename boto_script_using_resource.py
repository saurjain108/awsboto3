import boto3
aws_man_con=boto3.session.Session(profile_name="root")
#iam
iam_con_re=aws_man_con.resource(service_name="iam")
#ec2
ec2_con_re=aws_man_con.resource(service_name="ec2")
#s3
s3_con_re=aws_man_con.resource(service_name="s3")

#list all iam users
print(dir(iam_con_re.users))
a = (iam_con_re.users.all())
for i in a:
    print(dir(i))
    print(i.name)
    print(i.user_name)
    print(i.user_id)
print("----------------------------------")

#listing all buckets
print(dir(s3_con_re.buckets))
print(s3_con_re.buckets.all())
for x in s3_con_re.buckets.all():
    print(dir(x))
    print(x.name)
print("----------------------------------") 

#listing all ec2 instances
print(dir(ec2_con_re.instances))
print(ec2_con_re.instances.all())
for a in ec2_con_re.instances.all():
    print(dir(a))
    print(a.instance_id)

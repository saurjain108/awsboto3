import boto3
from pprint import pprint
aws_man_con = boto3.session.Session(profile_name="root")
ec2_con_re = aws_man_con.resource('ec2')
print(dir(ec2_con_re))
print("========================================")
print(dir(ec2_con_re.meta))
print("========================================")
print(dir(ec2_con_re.meta.client))
for each in (ec2_con_re.meta.client.describe_regions()['Regions']):
    print(each['RegionName'])


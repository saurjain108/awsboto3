import boto3 
boto3
aws_man_con = boto3.session.Session(profile_name="root")
ec2_con_re = aws_man_con.resource('ec2', region_name="us-east-2")
print(ec2_con_re.volumes.all())

print("--------------------------------------")

for i in ec2_con_re.volumes.all():
    print(i.id, i.state)

print("--------------------------------------")

f_ebs_unused = {"Name":"status","Values":["available"]}
for volume in ec2_con_re.volumes.filter(Filters=[f_ebs_unused]):
    if not volume.tags:
        print(volume.id, volume.state,volume.tags)
        print("Deleting unused and untagged volumes.....")
        volume.delete()





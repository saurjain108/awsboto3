import boto3
from pprint import pprint #this is used for formatting the output text
aws_man_con = boto3.session.Session(profile_name="root")
ec2_con_cli = aws_man_con.client('ec2')
resource = ec2_con_cli.describe_instances()['Reservations']
#pprint(resource)
for i in resource:
    for j in (i['Instances']):
#        pprint(j)
        print("The instance id is: {}\nThe image id is: {}\nThe launch time is: {}".format(j['InstanceId'],j['ImageId'],j['LaunchTime']))
        print("---------------------------------------")

#listing volumes

volume_response = ec2_con_cli.describe_volumes()['Volumes']
#pprint(volume_response)
#print('================')
for x in (volume_response):
    print("The volume id is: {}\n The availability zone is {}\n The volume type is {}".format(x['VolumeId'],x['AvailabilityZone'],x['VolumeType']))
print("============================")

#this is also one way of looping for just volume ids
for y in (volume_response):
    print(y['VolumeId'])


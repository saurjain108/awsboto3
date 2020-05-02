import boto3
aws_man_con=boto3.session.Session(profile_name="root")

#iam
iam_con_cli=aws_man_con.client(service_name="iam")

#ec2
ec2_con_cli=aws_man_con.client(service_name="ec2")

#s3
s3_con_cli=aws_man_con.client(service_name="s3")

#listing all user using client object
response=iam_con_cli.list_users()
print(response)
print("------------------------------------------")
for item in response['Users']:
   # print(item)
    print(item['UserName'])

#listing all ec2 instant id
ec2_response=(ec2_con_cli.describe_instances())
for i in ec2_response['Reservations']:
    for j in i['Instances']:
        print(j)
        print(j['VpcId'])
        print(j['InstanceId'])
        print(j['InstanceType'])
    print('----------------------------')

#gettinf names of buckets in s3
s3_response=(s3_con_cli.list_buckets())
for x in s3_response['Buckets']:
    print(x['Name'])


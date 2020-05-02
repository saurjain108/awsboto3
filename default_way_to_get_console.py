#To work this code we have to have default credential in .aws folder 
# use aws configure and provide required information

import boto3

iam_console=boto3.resource('iam',region_name='us-east-2')
for each_user in iam_console.users.all():
    print(each_user.name)

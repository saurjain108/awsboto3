import boto3
s3_ob=boto3.resource('s3')
#ec2_ob=boto3.resource('ec2')
#iam_ob=boto3.resource('iam')

for bucket in s3_ob.buckets.all():
    print(bucket.name)

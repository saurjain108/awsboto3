import boto3
aws_management_console=boto3.session.Session(profile_name="root")
s3_console=aws_management_console.resource('s3')
for bucket in s3_console.buckets.all():
    print(bucket.name)
    print(bucket)


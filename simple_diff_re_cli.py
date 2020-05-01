import boto3
aws_console = boto3.session.Session(profile_name="root")
iam_console_re = aws_console.resource('iam', region_name="us-east-2")
iam_console_cli = aws_console.client('iam', region_name="us-east-2")

#listing iam with resource object

for each_user in iam_console_re.users.all():
    print(each_user.name)	

print("-----------------------------------------")

#listing iam users witrh client object

for each in iam_console_cli.list_users()['Users']:
    print(each['UserName'])


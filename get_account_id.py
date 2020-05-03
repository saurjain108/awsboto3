import boto3
aws_mag_con_root = boto3.session.Session(profile_name="root")
sts_con_cli = aws_mag_con_root.client('sts')
a = sts_con_cli.get_caller_identity()
print(sts_con_cli.get_caller_identity().get('Account'))
print('--------')
print(a.get('Account'))
print('------------')
print(dir(sts_con_cli))



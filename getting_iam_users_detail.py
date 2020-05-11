import boto3
session = boto3.session.Session(profile_name="root")
iam_con_re = session.resource('iam')
#get detail of any user
"""print(dir(iam_con_re))
print("----------------------------")
iam_user_object = iam_con_re.User("Admin")
print(iam_user_object.user_name, iam_user_object.user_id, iam_user_object.arn, iam_user_object.create_date)
"""
for iam_user_object in iam_con_re.users.all():
    print(iam_user_object.user_name, iam_user_object.user_id, iam_user_object.arn, iam_user_object.create_date)
print("------")

for j in iam_con_re.groups.all():
    print(j.group_name)

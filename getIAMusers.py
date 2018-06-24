'''
To provide a list of all IAM users in AWS.
'''

import boto3
import botocore

try:
    accesskey = input("Please enter access key: ")
    secretkey = input("Please enter secret key: ")
    region = input("Please enter region: ")
except:
    print("Please ensure your access key and secret key are correct")

if accesskey is None:
    print("Please do not leave any keys null")

else:
    print("Continue with function")

def getusers():

        keys = boto3.client('iam',
                             aws_access_key_id=accesskey,
                             aws_secret_access_key=secretkey,
                             region_name=region
                             )

        users = keys.list_users()
        print(users)
def main():
    getusers()


main()

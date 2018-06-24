'''
To provide a list of all IAM users in AWS.
'''

import boto3
import botocore


class iamusers:
    try:
        def __init__(self, accesskey, secretkey, region):
            self.accesskey = accesskey
            self.secretkey = secretkey
            self.region = region

            if self.accesskey is None:
                print("No parameters are meant to be null. Please try again")

    except TypeError:
        print("Wrong type. Please try putting in the specific access key, secret key, and region")

    def iamusers(self):

        creds = boto3.client('iam',
                             aws_access_key_id=self.accesskey,
                             aws_secret_key=self.secretkey,
                             region_name=self.region
                             )

        iamuseroutput = creds.list_users()
        print(iamuseroutput)


iamusers("AKIAIOFBQPAAKM2HVPOQ", "OT6GgqATmT04i7T1sKCDAidFVe8UyNFykwpXDTFl", "us-east-1")
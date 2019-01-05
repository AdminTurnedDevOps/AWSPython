#!/usr/bin/env python

import boto3
import sys

global s3buckeyfile
global s3bucketfile_key_location

# Choose a file in your S3 bucket and a place you want to store the fie (localhost or remote)
s3buckeyfile = input('Please choose a file in your S3 bucket')
s3bucketfile_key_location = input('Please choose a location for your file to be saved to')

# Connect to your AWS account (proper programmatic access and an IAM user is required)
def copy_config_file(access_key, secret_key, bucket_name, region):
    try:
        _S3 = boto3.resource('s3',
                                 region_name=region,
                                 aws_access_key_id=access_key,
                                 aws_secret_access_key=secret_key)
         
         # Collects information from your bucket
        _bucket = _S3.Bucket(bucket_name)

        for file in _bucket.objects.all():
            config = file.key
            
            # If the file you specified exists, it will now be copied to wherever you asked
            if s3buckeyfile in config:
                _bucket.download_file(s3buckeyfile, s3bucketfile_key_location)

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The file in your specified S3 bucket does not exist. Please try again.")


access_key = sys.argv[1]
secrey_key = sys.argv[2]
bucket_name = sys.argv[3]
region = sys.argv[4]

if __name__ == '__main__':
    copy_config_file(access_key, secrey_key, bucket_name, region)

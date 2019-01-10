import boto3
import os
import json
import sys

def make_redis_file(fileLocationOutput):

    try:
        os.popen("touch {}/redis_output.txt".format(fileLocationOutput))
        return fileLocationOutput
    except:
        print("file not created. Please try again")
        exit()

make_redis_file(fileLocationOutput=input("Please enter a location for your file to be stored"))

def describe_redis_url(accessKey, secretKey, redisClusterID):

    try:
        redis = boto3.client('elasticache',
                            region_name='us-east-1',
                            aws_access_key_id=accessKey,
                            aws_secret_access_key=secretKey)

        redis_url = redis.describe_replication_groups(ReplicationGroupId=redisClusterID)

        for cluster in redis_url['ReplicationGroups']:
            for i in cluster.items():
                dict_string_redis = json.dumps(i)
                string_redis = ''.join(dict_string_redis)


                with open(make_redis_file(), 'r+') as f:
                    read_redis = f.read()
                    write_redis = f.write(string_redis)
                    append_redis = f.write(dict_string_redis)

    except ValueError:
        print('Please check your access key, secret key, and redis cluster ID to confirm all is correct')


accessKey = sys.argv[1]
secretKey = sys.argv[2]
redisClusterID = sys.argv[3]

if __name__ == '__main__':
    describe_redis_url(accessKey, secretKey, redisClusterID)

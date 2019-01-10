import boto3
import sys

def describe_redis_url(region, accessKey, secretKey, redisClusterID):
    try:
        redis = boto3.client('elasticache',
                             region_name=region,
                             aws_access_key_id=accessKey,
                             aws_secret_access_key=secretKey)

        redis_url = redis.describe_replication_groups(ReplicationGroupId=redisClusterID)

        for cluster in redis_url['ReplicationGroups']:
            for i in cluster.items():
                print(i)
                
    except ValueError:
        print('Please check your access key, secret key, and redis cluster ID to confirm all is correct')


region = sys.argv[1]
accessKey = sys.argv[2]
secretKey = sys.argv[3]
redisClusterID = sys.argv[4]

if __name__ == '__main__':
    describe_redis_url(region, accessKey, secretKey, redisClusterID)

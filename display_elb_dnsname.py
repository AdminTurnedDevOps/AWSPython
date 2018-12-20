import sys
import boto3

def display_ELB_DNS(accessKey, secretKey, LBName):
    response = boto3.client(service_name='elb',
                            region_name='default',
                            aws_access_key_id=accessKey,
                            aws_secret_access_key=secretKey)

    showelb = response.describe_load_balancers(
        LoadBalancerNames = [
                                LBName,
                            ],
         )

    for elb in showelb['LoadBalancerDescriptions']:
        print(str(elb['DNSName']))


accessKey = sys.argv[1]
secretKey = sys.argv[2]
LBName = sys.argv[3]

display_ELB_DNS(accessKey, secretKey, LBName)

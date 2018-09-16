import boto3

accessKey = input("Please enter your access key: ")
secretKey = input("Please enter your secret key: ")

useast1reg = str("us-east-1")
useast2reg = str("us-east-2")
uswest1reg = str("us-west-1")

def useast1():
    ec2useast1 = boto3.resource(service_name='ec2',
                                region_name=useast1reg,
                                aws_access_key_id=accessKey,
                                aws_secret_access_key=secretKey)

    print("Public IP's for us-east-1:")
    for ip in ec2useast1.instances.all():
        print(ip.public_ip_address)

def useast2():
    ec2useast2 = boto3.resource(service_name='ec2',
                                region_name=useast2reg,
                                aws_access_key_id=accessKey,
                                aws_secret_access_key=secretKey)

    print("Public IP's for us-east-2:")
    for ip in ec2useast2.instances.all():
        print(ip.public_ip_address)

def uswest1():
    ec2useast2 = boto3.resource(service_name='ec2',
                                region_name=uswest1reg,
                                aws_access_key_id=accessKey,
                                aws_secret_access_key=secretKey)

    print("Public IP's for us-west-1:")
    for ip in ec2useast2.instances.all():
        print(ip.public_ip_address)

def main():
    useast1()
    useast2()
    uswest1()
main()

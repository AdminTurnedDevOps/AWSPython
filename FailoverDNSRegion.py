import boto3 as aws
new_route = aws.client('route53')

HostedZoneId = input("Please type in your hosted zone ID")
RecordSetName = input("Please type in your Resource Record Set name")
setID = input("Please type in your Set Identifier")
dnsName = input("Please type in your DNSName for your ELB")

def newdnsrouteipv4():
        new_route53_record = new_route.change_resource_record_sets(
            HostedZoneId=HostedZoneId,
            ChangeBatch={
                'Comment': 'us-east-1 and us-east-2 failed. Switching to your specified region',
                'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': RecordSetName,
                    'Type': 'A',
                    'SetIdentifier': setID,
                    'TTL': 300,
                    'AliasTarget': {
                        'DNSName': dnsName,
                        'EvaluateTargetHealth': True
                        }
                    }
                }
            ]
        }
    )
def newdnsrouteipv6():
        new_route53_record = new_route.change_resource_record_sets(
            HostedZoneId=HostedZoneId,
            ChangeBatch={
                'Comment': 'us-east-1 and us-east-2 failed. Switching to your specified region',
                'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': RecordSetName,
                    'Type': 'AAAA',
                    'SetIdentifier': setID,
                    'TTL': 300,
                    'AliasTarget': {
                        'DNSName':dnsName,
                        'EvaluateTargetHealth': True
                        }
                    }
                }
            ]
        }
    )
def main():
    newdnsrouteipv4()
    newdnsrouteipv6()
main()

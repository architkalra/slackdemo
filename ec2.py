from pathlib import Path
import boto3

my_file = Path("/home/ec2-user/.aws/credentials")

if my_file.is_file():
    print ("Credential file exits! ")
    for i in range(0,3):
        print("Launching EC2 instance #",i,"...")

        ec2 = boto3.resource('ec2')
        instance = ec2.create_instances(
        ImageId='ami-0e9089763828757e1',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='archit',
        SecurityGroupIds= ['sg-2b4f3303', 'sg-0570c047e91ffdb2c'],
        TagSpecifications = [{'ResourceType': 'instance','Tags':[{'Key':'Name','Value':'Archit-{i}' }]}]
        )

        print ("Created EC2 instance ",instance[0].id)
else:
    print ("file does not exit.")

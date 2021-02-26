# Filename:: ec2.py
# Author:: Archit Kalra
# Email:: archit.kalra@gmail.com

#importing rquired modules
from pathlib import Path
import boto3

#For Loop for creating 3 instances, technically for loop is not needed EC2 resrouce can handle multiple nodes. Only added for illustrations purposes
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
    TagSpecifications = [{'ResourceType': 'instance','Tags':[{'Key':'Name','Value':'Archit' }]}]
    )
    #Printing Instance ID for the newly created instance in AWS
    print ("Created EC2 instance ",instance[0].id)


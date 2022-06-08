import boto3

session = boto3.session.Session(profile_name='harvest')
client = session.client('athena')


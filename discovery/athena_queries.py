import boto3

session = boto3.session.Session(profile_name='data')
client = session.client('athena')


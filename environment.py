
from aws_cdk import core

def get_environment()-> core.Environment:
    return core.Environment(region='eu-west-1', account='885617958043')

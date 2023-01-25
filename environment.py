
import aws_cdk as cdk

def get_environment()-> cdk.Environment:
    return cdk.Environment(region='eu-west-1', account='<<>>')

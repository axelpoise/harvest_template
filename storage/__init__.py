import aws_cdk as cdk

from environment import get_environment
from constructs import Construct

class StorageSetupStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, name: str) -> None:
        super().__init__(scope, construct_id, env=get_environment())
        self.add_s3_buckets(name)


    def add_s3_buckets(self, name: str):
        self.bronze_bucket: cdk.aws_s3.Bucket = cdk.aws_s3.Bucket(self, f"BronzeBucket{name}",
                          block_public_access=cdk.aws_s3.BlockPublicAccess.BLOCK_ALL,
                          removal_policy=cdk.RemovalPolicy.DESTROY,
                          access_control=cdk.aws_s3.BucketAccessControl.PRIVATE,
                          )


from aws_cdk import core, aws_s3

from environment import get_environment


class BaseSetupStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, name: str) -> None:
        super().__init__(scope, construct_id, env=get_environment())

        self.add_s3_buckets(name)


    def add_s3_buckets(self, name: str):

        self.raw_bucket: aws_s3.Bucket = aws_s3.Bucket(self, f"BronzeBucket{name}",
                      block_public_access=aws_s3.BlockPublicAccess.BLOCK_ALL,
                      removal_policy=core.RemovalPolicy.DESTROY,
                      access_control=aws_s3.BucketAccessControl.PRIVATE,
                      )

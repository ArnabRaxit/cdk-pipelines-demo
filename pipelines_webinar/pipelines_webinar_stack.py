from os import path

from aws_cdk import core
import aws_cdk.aws_lambda as lmb
import aws_cdk.aws_apigateway as apigw
import aws_cdk.aws_codedeploy as codedeploy
import aws_cdk.aws_cloudwatch as cloudwatch

class PipelinesWebinarStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        this_dir = path.dirname(__file__)

        handler = lmb.Function(self, 'Handler',
            runtime=lmb.Runtime.PYTHON_3_7,
            handler='handler.handler',
            # code=lmb.Code.from_asset(path.join(this_dir, 'lambda')))
            code = lmb.Code.from_inline("def handler(event, context): return {'body': 'Oops','statusCode': '500'}"))
        self.url_output = core.CfnOutput(self, 'Url',
            value='test dummy url')
from os import path

from aws_cdk import core
import aws_cdk.aws_lambda as lambda_
import aws_cdk.aws_apigateway as apigw
import aws_cdk.aws_codedeploy as codedeploy
import aws_cdk.aws_cloudwatch as cloudwatch
import aws_cdk.aws_events as events
import aws_cdk.aws_events_targets as targets


class PipelinesWebinarStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)




        with open("lambda-handler.py", encoding="utf8") as fp:
            handler_code = fp.read()

        lambdaFn = lambda_.Function(
            self, "Singleton",
            code=lambda_.InlineCode(handler_code),
            handler="index.main",
            timeout=core.Duration.seconds(300),
            runtime=lambda_.Runtime.PYTHON_3_7,
        )

        # Run every day at 6PM UTC
        # See https://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html
        rule = events.Rule(
            self, "Rule",
            schedule=events.Schedule.cron(
                minute='0',
                hour='18',
                month='*',
                week_day='MON-FRI',
                year='*'),
        )
        rule.add_target(targets.LambdaFunction(lambdaFn))

        self.url_output = core.CfnOutput(self, 'Url',
            value='test url none')


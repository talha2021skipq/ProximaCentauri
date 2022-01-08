
from aws_cdk import (
    core as cdk,
    aws_lambda as _lambda,
    aws_events as events_,
    aws_events_targets as targets_,# aws_sqs as sqs,
    aws_iam,
    aws_cloudwatch as cloudwatch_,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions_,
    aws_cloudwatch_actions as actions_,
    aws_s3 as s3_, 
    aws_dynamodb as db_,
  #  aws_lambda_event_sources as lambda_events_,
    
)


from sprint4.sprint4_stack import Sprint4Stack

class TalhaStage(cdk.Stage):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        infra_stack=Sprint4Stack(self, 'talhaStack')
        
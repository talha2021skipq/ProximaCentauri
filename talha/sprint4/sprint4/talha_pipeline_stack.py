from aws_cdk import( core as cdk,
pipelines,
aws_codepipeline_actions as captions,
aws_iam)

from sprint4.talha_stage import TalhaStage

class TalhaPipelineStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        #Creating role for my pipeline
        pipeline_role=self.create_role()
        iam_=aws_iam.PolicyStatement(resources=['*'],actions=['iam:*'])
        sts_=aws_iam.PolicyStatement(resources=['*'],actions=['sts:*'])
#creating source
        source=pipelines.CodePipelineSource.git_hub(repo_string="talha2021skipq/ProximaCentauri", branch='main',
        authentication=cdk.SecretValue.secrets_manager('talha_pipeline_sprint2'),
        trigger=captions.GitHubTrigger.POLL)
        
        synth = pipelines.CodeBuildStep("synth", 
            input=source,
            commands=["cd talha/sprint4",
                    "pip install -r requirements.txt", 
                    "npm install -g aws-cdk", "cdk synth",
                    "npm ci", "npm run build", "npx cdk synth"
                   ],
            primary_output_directory="talha/sprint4/cdk.out",
            role=pipeline_role,
            role_policy_statements=[iam_,sts_])
    #Creating a pipeline for Codes, mainly to deploy CDK apps
        pipeline=pipelines.CodePipeline(self, "Pipeline", synth=synth)
        ############################## Defining beta stage to my code pipeline #######################
        beta= TalhaStage(self, "Beta", 
        env={
            'account':'315997497220',
            'region': 'us-east-2'
            })
    
      #  unit_test=pipelines.CodeBuildStep('unit_and_intg_test',
       #     commands=[ "cd talha/sprint4",
        #            "pip install -r requirements.txt", 
        #            "pytest unittests",  "pytest integtests"],
        #            role=pipeline_role,
         #           role_policy_statements=[iam_,sts_])
        ############ Adding beta stage to pipeline with pre test #####################
        pipeline.add_stage(beta)#,post=[unit_test])
        
    ############# Defining and adding production stage in my pipeline with pre  manual approval############## 
        prod= TalhaStage(self, "Prod", 
            env={'account':'315997497220',
                'region': 'us-east-2'} )
        pipeline.add_stage(prod, 
            pre=[  pipelines.ManualApprovalStep("PromoteToProd") ])
        
    def create_role(self):
        role=aws_iam.Role(self,"pipeline-role",
        assumed_by=aws_iam.CompositePrincipal(
            aws_iam.ServicePrincipal("lambda.amazonaws.com"),
            aws_iam.ServicePrincipal("sns.amazonaws.com"),
            aws_iam.ServicePrincipal("codebuild.amazonaws.com")
            ),
        managed_policies=[
            aws_iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSLambdaBasicExecutionRole'),
            aws_iam.ManagedPolicy.from_aws_managed_policy_name('CloudWatchFullAccess'),
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess"),
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("AwsCloudFormationFullAccess"),
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMFullAccess"),
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("AWSCodePipeline_FullAccess"),
            #aws_iam.ManagedPolicy.from_aws_managed_policy_name("AWSLambdaInvocation-DynamoDB"),
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess")
            ])
        return role 
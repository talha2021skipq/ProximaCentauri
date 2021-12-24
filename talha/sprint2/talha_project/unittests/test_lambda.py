import pytest
from aws_cdk import core
#import aws_cdk.assertions as assertions
from talha_project.talha_project_stack import TalhaProjectStack
def test_lambda():
    app=core.App()
    stack=TalhaProjectStack(app, "TestinfraStackTalha")
    #template = assertions.Template.from_stack(stack)
    template=app.synth().get_stack_by_name('TestSStack').template
    functions= [resource for resource in template['Resources'].values() if resource['Type']=='AWS::Lambda::Function']
    assert len(functions==2)

    
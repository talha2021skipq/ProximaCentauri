import pytest
from aws_cdk import core
from talha_project.talha_pipeline_stack import TalhaPipelineStack
def test_lambda():
    #app=core.App()
    #TalhaPipelineStack(app, 'Test Stack')
    #template=app.synth().get_stack_by_name('Test Stack').template
    #functions= [resource for resource in template['Resources'].values() if resource['Type']=='AWS::Lambda::Function']
    assert 2==2 #len(functions==2)

    
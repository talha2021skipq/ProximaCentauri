from aws_cdk import (
    core as cdk,
    aws_cloudwatch as cloudwatch_,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions_,
    aws_cloudwatch_actions as actions_,
)
import boto3
from resources import constants as constants
from boto3.dynamodb.conditions import Key

import os
class dynamoTablePutURLData:
    def __init__(self):
        self.resource = boto3.resource('dynamodb') 
    def wdynamo_data(self, tableName, message):
        #db=boto3.client('dynamodb')
        table = self.resource.Table(tableName)
        values = {}
        values['URL'] = message
        #values['Reason'] = reason
        table.put_item(Item = values)
    #    db.put_item(tableName,Item = values)
    def rdynamo_data(self,tableName):
        dynamodb = boto3.resource('dynamodb')
        table = self.resource.Table(tableName)
#        table = dynamodb.Table(tableName)
        response = table.scan()
        data = response['Items']
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])
        return data
    #Function for dynamodb table to delete an element
    def ddynamo_data(self,tableName,message):
        dynamodb = boto3.resource('dynamodb')
        table = self.resource.Table(tableName)
        #table = self.client.Table(tableName)
        response = table.delete_item(Key={'URL': message})
        return response
    
    def Newcreate_alarm(self, URLLS,topicarn):
        sns = boto3.resource('sns')
        topic = sns.Topic(topicarn)
        for el in URLLS:
            web=el["URL"]
            dimension= {'URL':  web}
    #create cloudwatch metric for availability 
            availability_metric=(cloudwatch_.Metric( namespace=constants.URL_MONITOR_NAMESPACE,metric_name=web+constants.URL_MONITOR_NAME1A,
                    dimensions_map=dimension, period=cdk.Duration.minutes(1), label=web+'Avaiability_metric'))
    #setting an alarm for availability
            availability_alarm=( cloudwatch_.Alarm(self,
                     id=web+'Availability_alarm', metric=availability_metric,
                    comparison_operator= cloudwatch_.ComparisonOperator.LESS_THAN_THRESHOLD, 
                    datapoints_to_alarm=1,
                    evaluation_periods=1, 
                    threshold= constants.THRESHOLD_AVAIL
                    ))
    #create a metric class for latency
            latency_metric=(cloudwatch_.Metric(namespace= constants.URL_MONITOR_NAMESPACE, metric_name=web+constants.URL_MONITOR_NAME1L, 
                    dimensions_map=dimension, period=cdk.Duration.minutes(1),label=web+'Latency_metric'))
    #create an alarm for latency
            latency_alarm=(cloudwatch_.Alarm(self,
                id=web+'Latency_alarm', metric=latency_metric,
                comparison_operator= cloudwatch_.ComparisonOperator.GREATER_THAN_THRESHOLD,
                datapoints_to_alarm=1,
                evaluation_periods=1,  
                threshold=constants.THRESHOLD_LATENCY
                ))
    #link sns and sns subscription to alarm
            availability_alarm.add_alarm_action(actions_.SnsAction(topic))
            latency_alarm.add_alarm_action(actions_.SnsAction(topic))



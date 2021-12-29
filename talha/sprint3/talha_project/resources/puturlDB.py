import boto3

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

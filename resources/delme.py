from __future__ import print_function

import boto3
from botocore.exceptions import ClientError
import uuid
import json
import decimal
import constants as constants
import os
from encode import DecimalEncoder

class DynamoDB_Table:
    def __init__(self, ):
        self.dynamodb = boto3.resource('dynamodb')
    
    def putItem(self, alarmType, createdAt):
        ddb_table = self.dynamodb.Table(constants.TABLE_NAME)
        
        table_name = os.getenv('table_name')
        print(table_name, type(table_name))
        try:
            response = ddb_table.put_item(
                Item={
                    "Alarm_Type":"Latency"+createdAt,
                    "createdAt": createdAt,
                    # 'threshold': threshold,
                    }
                )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("PutItem succeeded:")
            print(json.dumps(response, indent=4, cls=DecimalEncoder))
            
    
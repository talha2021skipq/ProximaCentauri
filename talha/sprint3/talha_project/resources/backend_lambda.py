import json,os
from puturlDB import dynamoURLTablePutURLData
import constants as constants
def lambda_handler(events, context):
 print(events)
 db=dynamoURLTablePutURLData()
 opt=events['httpMethod']
 table_name= os.environ['table_name']
 
# if opt=='GET':
 # pass

 #elif opt=='DELETE':
 #pass
 if opt=='PUT':
  urls=events['body'].split()
  for url in urls:
   db.wdynamo_data(table_name,url)
   msg="The item has been successfully written."
   
 else: 
  print("select an appropriate option")
 
 datares={"Response" : msg, "httpMethod": events['httpMethod'], "body": events['body'] }
 return {'statusCode':200 , 'body':json.dumps(datares)}

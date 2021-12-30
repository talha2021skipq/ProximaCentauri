import json,os
import puturlDB as putdb
import constants as constants
def lambda_handler(events, context):
 print(events)
 db=putdb.dynamoTablePutURLData()
 opt=events['httpMethod']
 path=events['path']
 table_name= os.environ['tablesname']
 
# if opt=='GET':
 # pass

 #elif opt=='DELETE':
 #pass
 if opt=='PUT':
  urls=events['body']#.split()
  #for url in urls:
  db.wdynamo_data(table_name,urls)
  msg="The item has been successfully written."
 elif opt=='GET':
  urllist=db.rdynamo_data(table_name)
  msg="Your request is acknowledged"
  events['body']=urllist
 elif opt=='DELETE':
  print("Helooooooooooooooo")
  print(events['body'])
  return {'statusCode':200}
  #db.rdynamo_data(table_name,key)
   
 else: 
  print("select an appropriate option")
 
 datares={"Response" : msg, "httpMethod": events['httpMethod'], "body": events['body'] }
 return {'statusCode':200 , 'body':json.dumps(datares)}

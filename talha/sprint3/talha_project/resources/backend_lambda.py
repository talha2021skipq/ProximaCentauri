import json,os
import puturlDB as putdb
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
 msg=""
 if opt=='PUT':          ######///////PUT////////
  urls=events['body']#.split()
  #for url in urls:
  db.wdynamo_data(table_name,urls)
  msg="The item has been successfully written."
 elif opt=='GET':        ######////////GET///////
  urllist=db.rdynamo_data(table_name)
  msg="Your request is acknowledged"
  events['body']=urllist 
 elif opt=='DELETE':     ######///////DELETE///////
  urltodel=events['body']
  response=db.ddynamo_data(table_name,urltodel)
  print(response,"JWAB")
  msg="The Url has been deleted. Use GET method to check!"
  
 else: 
  print("Please select an appropriate option. Appropriate Options=[PUT, GET, DELETE]")
 #if opt=='PUT' or opt=='DELETE':
  #urldict=db.rdynamo_data(table_name)#returns a dictionary
  #db.Newcreate_alarm(urldict,os.environ['mytopic'])
  
  

           
  #pass
  
 datares={"Response" : msg, "httpMethod": events['httpMethod'], "body": events['body'] }
 return {'statusCode':200 , 'body':json.dumps(datares)}

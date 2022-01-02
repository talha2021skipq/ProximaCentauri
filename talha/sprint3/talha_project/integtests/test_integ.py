import datetime
import pytest
import requests
import json
from resources import puturlDB as putdb
BetaURLtable="Beta-infraStack-URLTable1792207E-1E3WEGLZJ0NFU"
db=putdb.dynamoTablePutURLData()
def test_integ():
    
    urllist=db.rdynamo_data(BetaURLtable)
    ##Getting the URLS in real time using API invoke link
    api_res=requests.get('https://4jd8g9kea3.execute-api.us-east-2.amazonaws.com/prod/')
    reply=json.loads(api_res.text)
    print("res from api", api_res)
    print("The reply=", reply)
    
    assert len(urllist) == len(reply['body'])
def realtime_test():
    start =datetime.datetime.now()
    api_put_res=requests.put('https://4jd8g9kea3.execute-api.us-east-2.amazonaws.com/prod/', data={"URL","dummy.com"})
    end=datetime.datetime.now()
    latency=end-start
    assert latency==2
     
     
    
    
    assert 2==2
# API invoke link: https://4jd8g9kea3.execute-api.us-east-2.amazonaws.com/prod/
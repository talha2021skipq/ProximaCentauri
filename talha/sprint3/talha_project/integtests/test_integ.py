import pytest
import requests
import json
from resources import puturlDB as putdb
BetaURLtable="Beta-infraStack-URLTable1792207E-1E3WEGLZJ0NFU"
def test_integ():
    db=putdb.dynamoTablePutURLData()
    urllist=db.rdynamo_data(BetaURLtable)
    ##Getting the URLS in real time using API invoke link
    api_res=requests.get('https://4jd8g9kea3.execute-api.us-east-2.amazonaws.com/prod/')
    reply=json.loads(api_res.text)
    print("res from api", api_res)
    print("The reply=", reply)
    
    assert len(urllist) == len(reply['body'])
    
     
     
    
    
    assert 2==2
# API invoke link: https://4jd8g9kea3.execute-api.us-east-2.amazonaws.com/prod/
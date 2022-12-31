import requests
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

API_URL="http://api.timezonedb.com/v2.1/convert-time-zone"

def res(curTime,prevTZ,curTZ):
    payload={
        'key': os.getenv('API_KEY'),
        'format':'json',
        'from':prevTZ.upper(),
        'to':curTZ.upper(),
    }
    res=requests.get(API_URL,params=payload)
    data=res.json()
    return ((curTime+data['offset']))
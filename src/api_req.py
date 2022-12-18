import requests
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

API_URL="http://api.timezonedb.com/v2.1/convert-time-zone"


def res(time,prevTZ,curTZ):
    payload={
        'key': os.getenv('API_KEY'),
        'format':'json',
        'from':'EST',
        'to':'UST',
        'time':time
    }
    res=requests.get(API_URL,params=payload)
    data=res.json()
    print(data['toTimestamp'])

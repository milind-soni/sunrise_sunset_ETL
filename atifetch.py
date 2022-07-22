import sqlite3
import json 
import requests
import datetime
import calendar 
from datetime import timedelta, datetime
import pandas
import urllib.request


SUN_DATA_URL = 'https://api.sunrise-sunset.org/json?lat=18.5204&lng=73.8567&date={}'
DB_PATH = '/home/milindsoni/Documents/atidiv/sun.db'


dates = pandas.date_range(datetime.date(datetime(2020,1,1)),datetime.date(datetime.now())-timedelta(days=1),freq='d')

for i in dates:
    
    fetchurl = SUN_DATA_URL.format(i.strftime('%Y-%m-%d'))

    with urllib.request.urlopen(fetchurl) as response:
        data = json.dumps(response.read().decode('utf-8'))
        data = json.loads(data)
        print(data)


# def get_data():

# response = requests.get(SUN_DATA_URL)
# data = response.json()
# print(data) 


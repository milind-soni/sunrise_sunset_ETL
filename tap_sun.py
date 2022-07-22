import singer 
import urllib.request
import datetime
import calendar 
from datetime import timedelta, datetime
import pandas
import requests

schema = {
  "type": "object",
  "properties": {
    "results": {
      "type": "object",
      "properties": {
        "sunrise": {
          "type": "string"
        },
        "sunset": {
          "type": "string"
        },
        "solar_noon": {
          "type": "string"
        },
        "day_length": {
          "type": "string"
        },
        "civil_twilight_begin": {
          "type": "string"
        },
        "civil_twilight_end": {
          "type": "string"
        },
        "nautical_twilight_begin": {
          "type": "string"
        },
        "nautical_twilight_end": {
          "type": "string"
        },
        "astronomical_twilight_begin": {
          "type": "string"
        },
        "astronomical_twilight_end": {
          "type": "string"
        }
      },
      "required": [
        "sunrise",
        "sunset",
        "solar_noon",
        "day_length",
        "civil_twilight_begin",
        "civil_twilight_end",
        "nautical_twilight_begin",
        "nautical_twilight_end",
        "astronomical_twilight_begin",
        "astronomical_twilight_end"
      ]
    },
    "status": {
      "type": "string"
    }
  },
  "required": [
    "results",
    "status"
  ]
}



SUN_DATA_URL = 'https://api.sunrise-sunset.org/json?lat=18.5204&lng=73.8567&date={}'


dates = pandas.date_range(datetime.date(datetime(2020,1,1)),datetime.date(datetime.now())-timedelta(days=1),freq='d')

for i in dates:
    fetchurl = SUN_DATA_URL.format(i.strftime('%Y-%m-%d'))
    response = requests.get(fetchurl)
    data = response.json()
    print(data)
    singer.write_schema('my_ss', schema, 'i')
    # singer.write_records('my_ss', [{'sunrise': data}])


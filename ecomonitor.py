import json
import requests
import datetime
import os
from hygrothermo import get_hygrothermo
from co2 import get_co2

def make_json(temperature, humidity, co2):
    dt = datetime.datetime.now()
    date = dt.isoformat()

    return json.dumps({
        "date":date,
        "temperature": temperature,
        "humidity": humidity,
        "co2": co2
    })

def post_data():

    url = os.getenv('ECOMONITOR_URL')

    temperature, humidity = get_hygrothermo()
    c = get_co2()

    response = requests.post(
        url,
        make_json(temperature, humidity, c),
        headers={'Content-Type': 'application/json'}
    )

if __name__=='__main__':
    post_data()

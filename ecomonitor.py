import json
import requests
import datetime
import os
import hygrothermo

def make_json(temperature, humidity):
    dt = datetime.datetime.now()
    date = dt.isoformat()

    return json.dumps({
        "date":date,
        "temperature": temperature,
        "humidity": humidity
    })

def main():

    url = os.getenv('ECOMONITOR_URL')

    temperature, humidity = hygrothermo.hygrothermo()

    response = requests.post(
        url,
        make_json(temperature, humidity),
        headers={'Content-Type': 'application/json'}
    )

if __name__=='__main__':
    main()

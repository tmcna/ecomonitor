import json
import requests
import datetime
import os
import hygrothermo
import co2

def make_json(temperature, humidity, co2):
    dt = datetime.datetime.now()
    date = dt.isoformat()

    return json.dumps({
        "date":date,
        "temperature": temperature,
        "humidity": humidity,
        "co2": co2
    })

def main():

    url = os.getenv('ECOMONITOR_URL')

    temperature, humidity = hygrothermo.hygrothermo()
    c = co2.co2()

    response = requests.post(
        url,
        make_json(temperature, humidity, c),
        headers={'Content-Type': 'application/json'}
    )

if __name__=='__main__':
    main()

import time
import board
import adafruit_dht
import statistics
import math
import sys

def get_hygrothermo():
    dhtDevice = adafruit_dht.DHT22(board.D23)
    temperature = []
    humidity = []
    INTERVAL = 2.0

    for i in range(10):
        try:
            temperature.append(dhtDevice.temperature)
            humidity.append(dhtDevice.humidity)

        except RuntimeError as error:
            print(error.args[0], file=sys.stderr)
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error

        time.sleep(INTERVAL)
    
    temperature_median = statistics.median(temperature)
    humidity_median = statistics.median(humidity)

    return temperature_median, humidity_median

if __name__=='__main__':
    t, h = get_hygrothermo()
    print(
        "Temp: {:.1f} C    Humidity: {}% ".format(t, h)
    )

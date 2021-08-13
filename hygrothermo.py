import time
import board
import adafruit_dht
import statistics
import math

def hygrothermo():
    dhtDevice = adafruit_dht.DHT22(board.D23)
    l_temp = []
    l_humidity = []

    for i in range(10):
        try:
            temperature_c = dhtDevice.temperature
            l_temp.append(temperature_c)
            # temperature_f = temperature_c * (9 / 5) + 32
            humidity = dhtDevice.humidity
            l_humidity.append(humidity)

        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error

        time.sleep(2.0)
    
    temperature_c_median = statistics.median(l_temp)
    humidity_median = statistics.median(l_humidity)

    return temperature_c_median, humidity_median

if __name__=='__main__':
    t, h = hygrothermo()
    print(
        "Temp: {:.1f} C    Humidity: {}% ".format(t, h)
    )

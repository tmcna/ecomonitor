import mh_z19
import time

def co2():
    r = mh_z19.read()
    return r['co2']

if __name__=='__main__':
    while True:
        r = co2()
        print(r)
        time.sleep(3)

import mh_z19
import time

def get_co2():
    r = mh_z19.read()
    return r['co2']

if __name__=='__main__':
    while True:
        r = get_co2()
        print(r)
        time.sleep(3)

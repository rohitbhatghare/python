import time
from threading import *

l = Lock()


def wish(name):
    l.acquire()
    for i in range(10):
        print("good evening:", end='')
        time.sleep(.50)
        print(name)
    l.release()


t1 = Thread(target=wish, args=("Dhoni",))
t2 = Thread(target=wish, args=("Yuvraj",))
t3 = Thread(target=wish, args=("Kohli",))
t1.start()
t2.start()
t3.start()

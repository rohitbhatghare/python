from threading import *
import time


def display():
    for i in range(10):
        print("seetha")
        time.sleep(2)


t = Thread(target=display)
t.start()
print(t.is_alive())
t.join()
print(t.is_alive())
for i in range(10):
    print("rama thread")

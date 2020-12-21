from threading import *


def job():
    print("child Thread")


t = Thread(target=job)
print(t.isDaemon())
t.setDaemon(True)
print(t.isDaemon())

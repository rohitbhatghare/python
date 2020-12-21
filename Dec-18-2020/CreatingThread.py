from threading import *


def dis():
    for i in range(1, 11):
        print("child class")


t = Thread(target=dis)
t.start()
for i in range(1, 11):
    print("main thread")

from threading import *


class Mythread(Thread):
    def run(self):
        for i in range(10):
            print("child class-1")


t = Mythread()
t.start()
for i in range(10):
    print("main thread-1")

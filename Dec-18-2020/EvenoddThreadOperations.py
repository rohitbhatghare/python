from threading import *


class even(Thread):
    def run(self):
        for i in range(10):
            if (i % 2 == 0):
                print(current_thread().getName(),i)


class odd(Thread):
    def run(self):
        for i in range(10):
            if (i % 2 == 1):
                print(current_thread().getName(),i)


a = even()
b = odd()
a.start()
b.start()
current_thread().setName("MainThread")
print(current_thread().getName())
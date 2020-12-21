from threading import *

class even(Thread):
    def run(self):
        for i in range(10):
            if(i%2==0):
                print("even",i)
class odd(Thread):
    def run(self):
        for i in range(10):
            if(i%2==1):
                print("odd",i)

a=even()
b=odd()
a.start()
b.start()
from threading import *


class Test:
    def dis(self):
        for i in range(10):
            print("child thread-2")


obj = Test()
t = Thread(target=obj.dis)
t.start()
for i in range(10):
    print("main thread-2")

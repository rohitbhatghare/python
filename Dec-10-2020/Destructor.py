import time
class test:
    def __init__(self):
        print("Object Initalization")
    def __del__(self):
        print("Fulfilling last wish and performing cleanup activities...")
t1=test()
t1=None
time.sleep(5)
print("End of application")
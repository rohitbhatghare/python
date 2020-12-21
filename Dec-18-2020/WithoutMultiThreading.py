from threading import *
import time
def doubles(numbers):
    for i in numbers:
        time.sleep(1)
        print("doubles",2*i)
def square(numbers):
    for n in numbers:
        time.sleep(1)
        print("square",n*n)
numbers=[1,2,3,4,5]
begintime=time.time()
doubles(numbers)
square(numbers)
print("the total time taken:",time.time()-begintime)
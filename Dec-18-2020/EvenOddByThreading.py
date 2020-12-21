from threading import *
import time
def even(numbers):
    for i in range(10):
        if (i % 2 == 0):
            print("even", i)
def odd(numbers):
    for i in range(10):
        if (i % 2 == 1):
            print("odd", i)
numbers=[1,2,3,4,5,6,7,8,9,10]
even(numbers)
odd(numbers)
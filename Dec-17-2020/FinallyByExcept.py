import os
try:
    print("Try")
    os._exit(0)
except NameError:
    print("Except")
finally:
    print("Finally")
from threading import *
print(current_thread().isDaemon())
print(current_thread().daemon)

print(current_thread().isDaemon())
current_thread().setDaemon(True)
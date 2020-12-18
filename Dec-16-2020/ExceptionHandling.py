print("Before")
a, b = 3, 4
print(a + b)
l = [1, 2, 3, 4, 5]

try:
    #c = 4 / 0
    for i in range(5):
        print(l[i])

except ZeroDivisionError as ob1:
    print("Zerodivisionerror occurred", ob1)
except IndexError as ob:
    print("IndexError generated", ob)

print("after")

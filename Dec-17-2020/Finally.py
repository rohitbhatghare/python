x= int(input("Enter the value of a"))
y= int(input("Enter the value of b"))
def divide(a, b):
    try:
        res = a // b
    except ZeroDivisionError:
        print("Error...You are dividing by Zero")
    finally:
        print("Finally Execution")



divide(x,y)
print("Division is ",divide)

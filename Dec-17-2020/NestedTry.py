try:
    print("outer try block")
    try:
        print("Inner try block")
        print(10/0)
    except ZeroDivisionError:
        print("Inner except block")
    finally:
        print("Inner finally block")
    print(2/0)
except ZeroDivisionError:
    print("Outer except block")
finally:
    print("outer finally block")

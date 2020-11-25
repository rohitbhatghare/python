def outer():
    print("outer function started")

    def inner():
        print("inner function started")

    print("outer calling inner function")
    return inner

f1=outer()
f1()
f1()
f1()
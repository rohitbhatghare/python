def outer():
    print("outer function started")

    def inner():
        print("inner function started")

    print("outer calling inner function")
    inner()


outer()

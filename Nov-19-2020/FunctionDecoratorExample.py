def check(func):
    def inside(a, b):
        print("Dividing", a, "and", b)
        if b == 0:
            print("Can't divide by zero")

        return func(a, b)

    return inside


@check
def div(a, b):
    print(a / b)


div(2, 5)
div(2, 0)

def wish(name):
    print("hello", name, "good morning")


def decor(fun):
    def inner(name):
        if name == "sunny" or name=="durga":
            print("hello", name," bad morning")
        else:
            fun(name)

    return inner


@decor
def wish(name):
    print("hello", name, "good morning")


wish("durga")
wish("ravi")
wish("sunny")

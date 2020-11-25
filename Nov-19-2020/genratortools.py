def mygen():
    yield "C"
    yield "B"
    yield "A"

g=mygen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
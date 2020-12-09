class demo:
    def _init_(self):
        self.a = 2
        self.b = 3


d = demo()
print(d.a)
print(d.b)
del d.a
print(d.a)

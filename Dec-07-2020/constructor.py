class One:
    """this is my first class"""

    def _init_(self):
        a = int(input("enter number : "))
        self.id = a
        print("this is constructor ", self.id)

    a = 2

    def set1(self):
        print("hi")


ob = One()
ob1 = One()
ob.set1()
ob1.set1()
print(ob.a)
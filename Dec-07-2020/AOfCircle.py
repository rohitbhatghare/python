import math


class circle:
    def _init_(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


r = int(input("Enter radius of circle: "))
obj = circle(r)
print("Area of circle:", obj.area())
print("Perimeter of circle:", obj.perimeter())
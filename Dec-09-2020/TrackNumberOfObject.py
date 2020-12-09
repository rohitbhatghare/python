class Student:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

        Student.counter += 1


    def printDetails(self):
        print(self.name, self.age, "years old")
student1 = Student('Tapu', 22)
student2 = Student('goli', 19)
student3 = Student('pinku', 13)


print("Total number of objects created: ", Student.counter)

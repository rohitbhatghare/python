class student:
    def setname(self,name):
        self.name=name

    def getname(self):
        return self.name

    def setmarks(self,marks):
        self.marks=marks

    def getmarks(self):
        return self.marks
n= int(input("Enter the number of students"))
for i in range(n):
    s=student()
    name= input("Enter name:")
    s.setname(name)
    marks=int(input("Enter the marks :"))
    s.setmarks(marks)
    print("Hi",s.getname())
    print("Your marks are:",s.getmarks())
    print()
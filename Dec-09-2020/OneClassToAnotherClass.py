class employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal

    def dis(self):
        print("Employe Number :",self.eno)
        print("Employee name",self.ename)
        print("Employee salary",self.esal)
class test:
    def modify(emp):
        emp.esal=emp.esal+10000
        emp.dis()
e=employee(100,"durga",10000)
test.modify(e)
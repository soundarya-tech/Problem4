class GLUGcompany:
    def _init_(self,name,age,id,salary,phone):
        self.name=name
        self.age=age
        self.id=id
        self.salary=salary
        self.phone=phone

    def getEmployeeDetails(self):
        print("name:"+self.name)
        print("Age:",self.age)
        print("ID:",self.id)
        print("Phone:",self.phone)
        print("Salary:",self.salary)
        

Vcom=GLUGcompany("Soundarya",24,1001,9893758374,100000)
Vcom.getEmployeeDetails()

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
        print("Salary:",self.salary)
        print("Phone:",self.phone)

Vcom=GLUGcompany("Barathi",20,1005,650000,8124814525)
Vcom.getEmployeeDetails()

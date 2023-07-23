class employee:
    company = "Apple"
    def showdetails(self):
        print(f"the name is {self.name} and company is {self.company}")
    @classmethod
    def changecompany(self,newcompany):
        self.company = newcompany

e1 =employee()
e1.name= "george"
e1.company="tesla"
e1.changecompany("tesla")     
e1.showdetails()
print(employee.company) 
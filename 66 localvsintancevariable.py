class Employee:
    companyname="APPLE"
    def __init__(self,name):
        self.name= name
        self.raise_amount= 0.02
    def showdetails(self):
        print(f"the name of employee is {self.name} and the raise amount is {self.companyname} is {self.raise_amount}")

emp1=Employee("george")
emp1.raise_amount=0.3
emp1.companyname='google'
emp1.showdetails()
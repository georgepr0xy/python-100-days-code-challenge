class employee():
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showdetails(self):
        print(f"the employee {self.id} is {self.name}")

class programmer(employee):
    def showlang(self):
      print("Default python")

e1=employee("george",66)
e1.showdetails()
e2=programmer("province",100)
e2.showlang()
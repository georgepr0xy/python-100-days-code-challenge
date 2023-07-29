class employee:
   def __init__(self,name):
       self.name=name
class dancer:
    def __init__(self,dance):
        self.dance = dance

class DancerEmployee(employee,dancer):
        def __init__(self, name,dance):
           self.name=name 
           self.dance=dance
        def show(self):
            print(f"the name is {self.name} and the dance is {self.dance}")
o= DancerEmployee("george","kathak")
print(o.name)
print(o.dance)   
o.show()  
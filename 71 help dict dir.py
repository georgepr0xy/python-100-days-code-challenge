# x = [2,4,5,6]
# print(dir(x))
# print(x.__add__)




class employee:
    def __init__(self,name ,age):
        self.name = name
        self.age= age

emp1=employee("george",12000)       
print(emp1.__dict__)


print(help(str))
print(help(int))
print(help(float))

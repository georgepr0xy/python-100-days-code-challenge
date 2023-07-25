# class parentclass:
#     def parent_method(self):
#         print("this is the parent method")

# class childclass(parentclass):
#     def parent_method(self):
#         print("george")
#         super().parent_method()

#     def child_method(self):
#         print("this is a child method")
#         super().parent_method()



# child_obeject = childclass()
# child_obeject.child_method()                  
# child_obeject.parent_method()                  





#----another example ----------->
class employee:
    def __init__(self,name , id):
        self.name=name
        self.id = id 

class programmer(employee):
    def __init__(self, name, id,lang):
        super().__init__(name, id)
        self.lang= lang        

a=employee("rohan",23)
b=programmer("george",342,"python")

print(a.name)
print(b.lang)
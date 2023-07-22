class person:
    
   def __init__(self,n,o): 
    print("i am person")

    self.name=n
    self.occ=o
     
    # name="George"
    # occ="hr"
   def info(self):
        print(f"{self.name} is a {self.occ}")


a=person("pranjal","hr")
b=person("harshit","manager")

# b=person()
# a=person()   
# a.name="province"
# a.occ="HR"
a.info()
b.info()    


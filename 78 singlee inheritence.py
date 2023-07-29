class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def make_sound(self):
        print("sound made by animal")
        
class cat(Animal):
    def __init__(self, name,breed):
        Animal.__init__(self,name,species="cat")
        self.breed=breed
    def make_sound(self):
        print("meo")    

class dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="dog")
        self.breed=breed

    def make_sound(self):
        print("bark")

c=cat("cat","black")
c.make_sound()

d=dog("dog","husky")
d.make_sound()
a=Animal("dog","dog")
a.make_sound()               
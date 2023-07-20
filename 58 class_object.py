class person:
    name = "Harry"
    occupation = "software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person()
a.name="George"
a.occupation="Data scientist"
a.networth=1000000

b=person()
b.name="pranjal"
b.occupation="HR"
b.networth=1382900

a.info()
b.info()

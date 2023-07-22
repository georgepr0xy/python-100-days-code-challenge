class myclass:
    def __init__(self,value):
       self._value = value 

    def show(self):
        print(f"the value is {self._value}") 
    @property
    def value(self):
        return 10*self._value 
    
    @value.setter
    def value(self,new_value):
        self._value=new_value/10
        


obj=myclass(10)
print(obj.value)
obj.value=67
obj.show()               
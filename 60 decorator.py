def designer(fx):
    def mfx(*args,**kwargs):
        print("what are you doing")
        fx(*args,**kwargs)
        print("how are you now")

    return mfx

# @designer                    #----------here designer is decorater
# def hello():
#      print("hellow world")

# hello()     

@designer
def add(a,b):
    print(a+b)

add(3,5)    


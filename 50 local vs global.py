# x = 5 
# print(x)
  
  
# def hello():
#     y = 10 
#     print(y)
#     print(x)
#     print("ths is loacal vs global variable example")


# hello()


x = 5 
print(x)
  
  
def hello():
    y = 10 
    global x
    x = 55
    print(y)
    print(x)
    print("ths is loacal vs global variable example")


hello()
print(x)
#------------map----------->
# def cube(x):
#     return x*x*x

# print(cube(2))

# l=[1,2,4,6,4,8,3]
# newl=[]
# for item in l:
#     newl.append(cube(item))
# newl=list(map(cube,l))  #-------->iin place of cube we can use lambda
# print(newl)    

#-------------------filter----->

# def filter_function(a):
#     return a>2

# l=[1,2,4,6,4,8,3]

# newlist=list(filter(filter_function,l))
# print(newlist)

#----------reduce----------->
from functools import reduce

l=[2,3,4,4,5]
def mysum(x,y):
    return x+y

sumup=reduce(mysum,l)
print(sumup)

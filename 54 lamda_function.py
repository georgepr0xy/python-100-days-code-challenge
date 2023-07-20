def apply(fx,value):
    return 6+fx(value)


cube =lambda x:x*x*x
sqaure = lambda x:x*x
double =lambda x:x*2
avg = lambda x,y,z:(x+y+z)/2


# print(F"the cube of 2 is {cube(2)}")
# print(sqaure(3))
# print(double(4))
# print(avg(2,3,4))
print(apply(lambda x:x *x*x,2))

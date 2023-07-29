class base():
    pass
class derived1(base):
    pass
class derived2(base):
    pass
class derived3(derived1,derived2):
    pass

#--------------Hybrid inheritence------------------>

#------below is hierarchical inheritence----------->
class base():
    pass
class m1(base):
    pass
class m2(base):
    pass
class m3(base):
    pass

#----dervive from M1----->
class m1_1(m1):
    pass
class m1_2(m1):
    pass

#----dervive from M2----->
class m2_1(m2):
    pass
class m2_2(m2):
    pass


#----dervive from M3----->
class m3_1(m3):
    pass
class m3_2(m3):
    pass


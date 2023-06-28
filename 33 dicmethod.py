ep1={1:"abc",2:"george",3:"provine",4:556,5:985}
ep2={7:32,8:345,9:1023,10:389}

print(ep1)
ep1.update(ep2)
ep1.popitem()
del ep1[4]
ep1.clear()
print(type(ep1))
print(ep1)
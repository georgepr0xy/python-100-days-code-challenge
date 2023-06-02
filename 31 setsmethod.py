s1 ={1,2,3,7,8,13}
s2 ={3,4,9,10,11,12}
print(s1.issubset(s2))
print(s1.issuperset(s2))
s1.clear()
print(s1)
#del s1   it will delete the set s1


#s1.pop()  pop any
#s1.add(20)
#s1.remove(13)
#s1.remove(5)    it thow an error bro! 5 is not there in s1
#s1.discard(5)    it does not throw error still there is not any 5
#print(s1)
'''print(s1.isdisjoint(s2))
print(s1.union(s2))
print(s1.difference(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))

s1.update(s2)
print(s1)
print(s1.intersection(s2))'''
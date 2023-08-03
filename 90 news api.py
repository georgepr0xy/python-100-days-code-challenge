def generators():
 for i in range(5000):
     yield i

gen= generators()
# print(next(gen))   
# print(next(gen))   
# print(next(gen)) 
# print(next(gen)) 
# print(next(gen)) 
for j in gen:
   print(j)

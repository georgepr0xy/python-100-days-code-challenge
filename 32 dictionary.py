dic = {
    1 : "Karan",
    2 : "george",
    3 : "province",
    4 : "pranjal",
    5 : "Mayank",
}
'''print(dic[1])
print(dic[2])
print(dic[3])
print(dic[4])
print(dic[5])'''

#print(dic[25])    ---->  it will give an error
#print(dic.get(25))  ----> it will give NONE as output

for key in dic.keys():
    #print(dic[key])  # ---> it will give values of all key
  #  print(key) -----> it will give key only
   print(f"the value of {key} is {dic[key]}")
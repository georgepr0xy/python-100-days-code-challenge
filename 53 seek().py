# with open("myfile.txt","r") as f:
#     f.seek(4)

#     data= f.read(15)
#     print(data)    
#     print(f.tell())

with open('myfile.txt','w') as f:
    f.write("hellow george procince")
    f.truncate(4)


with open('myfile.txt','r') as f:
    print(f.read())    
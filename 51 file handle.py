#----------TO read the file---------------------->

# f=open('myfile.txt','r')
# text=f.read()
# print(text)


#---------TO Write the file------------------->

# f=open('myfile.txt','w')
# text=f.write("hello bro")
# f.close()

#-------------To append the fie------------------>
f=open("myfile.txt","a")
text=f.write("appended the text")
f.close()



with open("myfile.txt","a") as f:
    f.write("with statement is used")

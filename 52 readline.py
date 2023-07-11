# f=open('myfile.txt','r')
# i=0
# while True:
#     i= i+1
    
#     line=f.readline()
#     if not line:
#      break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"The marks of the student {i}in maths is:{m1}")
#     print(f"The marks of the student {i}in science is:{m2}")
#     print(f"The marks of the student {i} in sst  is:{m3}\n")
#---------------------------------------------------------------------->


#using write lines below---------------->
f=open('file.txt','w')
lines=["line1\n","line2\n","line3\n"]
f.writelines(lines)
f.close()
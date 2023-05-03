num=int(input("enter the number:"))
if(num<0):
    print("the number is negative")
elif(num>0):
    if(num<=10):
        print("the number is between from 1 to 10")
    elif(num>10 and num<=20):
        print("the number is between from 11 to 20")
    else:
        print("the number is greater than 20")
else:
     print("the number is zero")


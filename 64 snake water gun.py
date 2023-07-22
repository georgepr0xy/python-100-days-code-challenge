import random
def check(comp,user):
    if(comp==user):
        return 0
    elif(comp == 0, user ==1):
        return -1
    elif(comp == 1,user==2):
        return -1
    elif(comp == 2,user==0):
        return -1
    else:
        return 1
     

comp = random.randint(0,2)
user=int(input("0 for snake, 1 for Water and 2 for Gun :"))

print(f"computer:{comp} and user:{user}")
result=check(comp,user)
print(result)

if(result==0):
    print("Match Draw")
elif(result==-1):
    print("You Loose")
elif(result==1):
    print("You Won")        
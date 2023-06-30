def fun1():
    try:
        l=[22,34,56,78]
        i = int(input("enter index:"))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0 
    finally:
        print("i am always excuted")

x = fun1()
print(x)
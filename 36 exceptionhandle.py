'''a = input("enter the number:")
print(f"multiplication of {a} is :")

try:
  for i in range(1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
print("some important lines of code")
print("end of the program")    '''

a=[33,45,57]
try:
   num = int(input("enter an integer value:"))
   print(a[num])
except ValueError:
      print("number is not an integer")
except IndexError:
     print("index not found")      
a="george is a good boy ;;;;;;;;"
print(a.upper())
print(a.lower())
print(a.rstrip("boy ;;;;;;;;"))
print(a.replace("george","pranjal"))
print(a.split(" "))
blogheading="this is the heading oF My blog"
print(blogheading)                   #withput captalize method 
print(blogheading.capitalize())
str1="wlecom to the vs code"
print(len(str1))
print(str1.center(100))
print(len(str1.center(100)))
print(blogheading.count("is"))
print(a.endswith(";;"))
print(blogheading.endswith("is",0,7))
print(blogheading.endswith("is",0,6))
print(str1.find("o"))
print(str1.find("e"))
print(str1.find("z"))
#print(str1.index("z"))    it gives an error 
print(str1.islower())     #throw false if atleast a upper case character is present
print(str1.isprintable())
str1="we wish you a merry christmas\n"
print(str1.isprintable())
print(str1.startswith("we"))
print(str1.startswith("wish"))
print(str1.startswith("z"))
print(str1.title("w"))

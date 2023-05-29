letter  = "hey my name is {} and i am from {}"
country= "india"
name = "George"
print(letter.format(name,country))
print(f"hey my name is {name} and i am from {country}")

price=49.495999
txt=f"for only{price:.2f}dollars"
print(txt)
print(type(f"{3*50}"))
print(f"my name{name} also my name {{name}}")
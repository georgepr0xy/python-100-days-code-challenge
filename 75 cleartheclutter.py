import os
files=os.listdir("clutteredfolder")
i=1
for file in files:
    if file.endswith(".png"):
     print(file)
     
     os.rename(f"clutteredfolder/{file}",f"clutteredfolder/{i}.png")
     i= i+1
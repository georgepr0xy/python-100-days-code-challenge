import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timestamp=int(time.strftime('%H'))
print(timestamp)
if(timestamp>=0 and timestamp<12):
   print("Good morning")
elif(timestamp>=12 and timestamp<=17):
    print("Good Afternoon")
elif(timestamp>=18 and timestamp<=21):
    print("Good Evening")
else:
     print("goodninght")

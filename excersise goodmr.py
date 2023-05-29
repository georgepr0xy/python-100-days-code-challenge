import time 
t = time.strftime("%H:%M:%S")
print(t)
hour = int(time.strftime('%H'))

if(hour>=0 and hour<12):
    print('Good morning')
elif(hour>=12 and hour<18):
    print('good afternoon')
if(hour>=18):
 print('good night') 

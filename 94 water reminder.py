import time
import win32com.client
t=time.strftime("%H:%M:%S")
print(t)

minute=int(time.strftime("%M"))
print(minute)

if minute==15 or minute==30 or minute==45 or minute==19:
 print("Drink water")

speaker = win32com.client.Dispatch("SAPI.SpVoice")
if minute==15 or minute==30 or minute==45 or minute==19:
 speaker.speak("Drink Water")
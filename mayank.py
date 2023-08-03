import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
list = ["Mayank","Tunnu","my son","manku"]
for i in list:
    speaker.Speak(f"Happy birthday to you {i}")
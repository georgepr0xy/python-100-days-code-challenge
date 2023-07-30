import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
list = ["harry","george","Divya prakash","pranjal seth"]
for i in list:
    speaker.Speak(f"shoutout! to {i}")
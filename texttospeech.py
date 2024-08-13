import pyttsx3

engine=pyttsx3.init()
"""voices=engine.getProperty("voices")
for voice in voices:
    print(voice.id)

"""
with open('python1.txt','r') as f:
   lines=f.read().replace("\n"," ")

engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.setProperty('rate',140)
engine.setProperty('volume',0.7)
engine.say(lines)
engine.runAndWait()

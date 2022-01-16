#To convert text to speech
# pip install gTTS to install this module
from gtts import gTTS
  
speech = input("Enter text to be convert in speech(English) : ")
myobj = gTTS(text=speech, lang = 'en' , slow=False)
myobj.save("speech.mp3")
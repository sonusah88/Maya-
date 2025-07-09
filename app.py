import speech_recognition as sr
import pyttsx3

#initializing..
engine=pyttsx3.init()
r=sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

print("Listening...")
with  sr.Microphone() as source:
    audio=r.listen(source)
    word=r.recognize_google(audio)
    print("You said: {word}")
speak(word)


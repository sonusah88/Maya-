import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import pywhatkit
from googlesearch import search
import sys

r=sr.Recognizer()
engine= pyttsx3.init()
def speak(a):
    engine.say(a)
    engine.runAndWait()

def process(word):
    if "play" in word.lower():
        pywhatkit.playonyt(word)
    elif "open google" in word.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in word.lower():
        webbrowser.open("https://www.facebook.com")
    elif "search" in word.lower():
        query = word
        for result in search(query, num_results=1):
            print(result)
            webbrowser.open(result)
    elif "send message" in word.lower():
        print("speak your message...")
        with sr.Microphone() as source:
            audio= r.listen(source,timeout=3,phrase_time_limit=5)
            a= r.recognize_google(audio) 
        pywhatkit.sendwhatmsg_instantly(
        phone_no="+9779817712881",
        message=a,
        wait_time=10,  # Seconds to wait before sending
        tab_close=True,
        close_time=2  # Close browser tab after sending
    )   

if __name__=="__main__":
    l=["exit","bye","stop","chup","i hate u","bhai"]
    while True:
        try:
            with sr.Microphone() as source:
                audio= r.listen(source)
                word= r.recognize_google(audio) 
            speak(word)
            print(word)
            process(word)
        except:
            print("Something went wrong....")

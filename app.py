import speech_recognition as sr
import pyttsx3
import pywhatkit

# Initialize speech engine and recognizer
engine = pyttsx3.init()
r = sr.Recognizer()

# Speak function with slow female voice
print("Listening...")
def speak(text):
    engine.setProperty('rate', 130)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # female voice
    engine.say(text)
    engine.runAndWait()

#task that should be added

def task(text):
    if "play" in text.lower():
        song = text.lower().replace("play", "").strip()
        pywhatkit.playonyt(song)
    elif "stop" in text:
        exit()

# Main loop
if __name__ == "__main__":
    while True:
        try:
            with sr.Microphone() as source:
                print("Say something...")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
                word = r.recognize_google(audio)
                print(f"You said :{word}")
                if "stop" in word:
                    break
                if "baby" in word.lower() or "hello baby" in word.lower():
                    speak("Yes baby ")
                    print("🫶🏻🥹❤️‍🩹")
                    with sr.Microphone() as source:
                        print("Listening Darling...")
                        audio = r.listen(source, timeout=3, phrase_time_limit=2)
                        word1 = r.recognize_google(audio)
                        print(f"You said: {word1}")
                        task(word1)
                else:
                    print("🥺🥺🥺😡")

        except Exception as e:
            print("!!! Something went wrong !!!")
            print(e)

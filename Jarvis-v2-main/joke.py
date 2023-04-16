import requests
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def tell_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
    if response.status_code == 200:
        joke = response.json()['joke']
        print(joke)
        speak(joke)
    else:
        print("Sorry, I couldn't find any jokes at the moment Abhishek.")
        speak("Sorry, I couldn't find any jokes at the moment Abhishek.")
        

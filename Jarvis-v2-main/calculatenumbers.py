import wolframalpha
import pyttsx3
import speech_recognition
import requests

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening ... ")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
        try:
            print("Understanding")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said : {query} \n")
        except Exception as e:
            print("Say that again :(")
            return "None"
        return query


def calculate():
    try:
        speak("Enter the expression Abhishek: ")
        expression = str(input('Enter the expression : '))
        result = eval(expression)
        print(f"{result} is the answer abhishek" )
        speak(f'{result} is the answer abhishek')
    except:
        return "Sorry, I couldn't calculate that."
    



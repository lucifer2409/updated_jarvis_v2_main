import pywhatkit
import pyttsx3
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime


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
        audio = r.listen(source,0,4)
        try:
            print("Understanding")
            query = r.recognize_google(audio,language='en-in')
            print(f"You said : {query} \n")
        except Exception as e:
            print("Say that again :(")
            return "None"
        return query


strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes=1)).strftime("%M"))

def sendmessage():
    speak("Who do you want to message : ")
    person = int(input('''
    Press 1 for person 1 , 2 for person 2 and so on ... \n
    person_1 : Abhishek wagh \n
    person_2 : Maa \n
    person_3 : Papa \n
    person_4 : Deep \n
    person_5 : vikram
    '''))
    if person == 1:
        speak('whats the message ? ')
        message =str(input('Enter the message:'))
        pywhatkit.sendwhatmsg("+918369233037",message,time_hour=strTime,time_min=update)
    elif person ==2 :
        speak('whats the message ? ')
        message =str(input('Enter the message:'))
        pywhatkit.sendwhatmsg("+919167824794",message,time_hour=strTime,time_min=update)
    elif person ==3:
        speak('whats the message ? ')
        message =str(input('Enter the message:'))
        pywhatkit.sendwhatmsg("+919820738277",message,time_hour=strTime,time_min=update)
    elif person==4:
        speak('whats the message ? ')
        message =str(input('Enter the message:'))
        pywhatkit.sendwhatmsg("+918356937907",message,time_hour=strTime,time_min=update)
    elif person==5:
        speak('whats the message ? ')
        message =str(input('Enter the message:'))
        pywhatkit.sendwhatmsg("+919137847616",message,time_hour=strTime,time_min=update)
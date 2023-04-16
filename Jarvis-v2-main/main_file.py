import pyttsx3
from plyer import notification
import speech_recognition
import requests
import datetime
import os
import requests
import pyautogui
from bs4 import BeautifulSoup


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


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


 
def alarm(query):
    timehere = open('Alarmtext.txt','a')
    timehere.write(query)
    timehere.close
    os.startfile('alarm.py')

if __name__ == "__main__":
    while True:
        query = takecommand().lower()
        if 'wake up' in query:
            from greetme import GreetMe
            GreetMe()
        while True:
            query = takecommand().lower()
            if 'go to sleep' in query:
                speak(
                    "ok abhishek i am going to sleep , you can call me anytime you need me !!")
                exit()
            elif "goodbye zeera" in query:
                speak("GoodBye Abhishek , Call me anytime you need me")
                exit
            elif 'hello' in query:
                speak("Hello abhishek , Good to see you back !!")
            elif "goodbye" in query:
                speak("Good bye abhishek , Have a nice time")
                exit()
            elif 'name' in query:
                speak("My name is Jarvis how can i help you sir")
            elif "how are you" in query:
                speak("I am good Abhishek Nice to hear from you !!")
            elif "thank you" in query:
                speak("You are welcome abhishek ")
            elif 'joke' in query:
                from joke import tell_joke
                tell_joke()
            elif "open" in query:
                query = query.replace("open",'')
                print(query)
                from openapps import open_application
            elif "close" in query:
                query = query.replace('close','')
                from openapps import close_application
                close_application(query)
            elif 'bye' in query:
                speak("Bye abhishek !!")
                exit()
            elif "google" in query:
                from SearchNow import searchgoogle
                searchgoogle(query)
            elif "youtube" in query:
                from SearchNow import searchyoutube
                searchyoutube(query)
            elif "wikipedia" in query:
                from SearchNow import searchwikipedia
                searchwikipedia(query)
            elif "weather" in query or "temperature" in query:
                speak("Temperature of which place do you want to know ?")
                query = takecommand().lower()
                url = f"http://api.openweathermap.org/data/2.5/weather?q={query}&appid=d43ca36d57f9e0c9b15b3761854d5e56&units=metric"
                response = requests.get(url)
                data = response.json()
                temperature = data["main"]["temp"]
                speak(f"The temperature in {query} is {temperature} degrees.")
                print(f"The temperature in {query} is {temperature} degrees.")

            elif "set an alarm" in query:
                print('Input the time : ')
                speak('Set the time')
                a = input('Please tell the time')
                alarm(a)
                speak('done sir')

            elif "the time" in query:
                strtime = datetime.datetime.now().strftime("%H:%M")
                speak(f"Abhishek the time is : {strtime}")
            elif "the date" in query:
                from date import get_date
                get_date()
            elif "okay" in query:
                speak("Yes abhishek , please feel free to ask me anything you want help with")
            elif "pause" in query:
                pyautogui.press("k")
                speak("Video paused")
            elif "play" in query:
                pyautogui.press("k")
                speak("Video played")
            elif "mute" in query:
                pyautogui.press("m")
                speak("video muted")
            elif "volume up" in query:
                from keyboard_1 import volumeup
                speak("Turning volume up , Abhishek")
                volumeup()
            elif "volume down" in query:
                from keyboard_1 import volumedown
                speak("Turning volume down , Abhishek")
                volumedown()
            elif "remember that" in query:
                rememberMessage = query.replace("remember that", "")
                rememberMessage = query.replace("jarvis", "")
                speak(f"You told me to : {rememberMessage}")
                remember = open("Remember.txt", "a")
                remember.write(rememberMessage)
                remember.write("\n")
                remember.close()
            elif "what do you remember" in query:
                remember = open("Remember.txt", "r")
                speak(f"You told me to : " + remember.read())
            elif "battery" in query:
                from battery_status import battery_status
                battery_status()
            elif "news" in query:
                from NewsRead import get_news
                get_news()
            elif "calculate" in query:
                from calculatenumbers import calculate
                calculate()
            elif 'whatsapp' in query:
                from Whatsapp import sendmessage
                sendmessage()
            elif "shutdown system" in query:
                speak("Are you sure you want to shut down the system ?")
                shutdown = input(
                    "Do you wish to shutdown your computer ? (yes/no)").lower()
                if shutdown == "yes":
                    os.system("shutdown /s /t 1")
                elif shutdown == "no":
                    break

            elif "schedule my day" in query:
                tasks = []  # empty list
                speak("Do you want to clear the old tasks ? , please speak yes or no")
                query = takecommand().lower()
                if 'yes' in query:
                    file = open('tasks.txt', "w")
                    file.write("")
                    file.close()
                    no_tasks = int(input('Enter the number of tasks : '))
                    i = 0
                    for i in range(no_tasks):
                        tasks.append(input('Enter the task : \n'))
                        file = open("tasks.txt", "a")
                        file.write(f"{i}.{tasks[i]} \n")
                        file.close()

                elif 'no' in query:
                    no_tasks = int(input('Enter the number of tasks : '))
                    i = 0
                    for i in range(no_tasks):
                        tasks.append(input('Enter the task : \n'))
                        file = open("tasks.txt", "a")
                        file.write(f"{i}.{tasks[i]} \n")
                        file.close()
                else :
                    query = takecommand.lower()
            elif "what's my schedule for today" in query:
                file = open("tasks.txt", "r")
                content = file.read()
                speak(content)
                file.close()

                notification.notify(
                    title="My schedule :- ",
                    message=content,
                    timeout=15
                )
            
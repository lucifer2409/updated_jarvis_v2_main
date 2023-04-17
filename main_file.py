import pyttsx3
from plyer import notification
import speech_recognition
import requests
import datetime
import os
import requests
import pyautogui
from bs4 import BeautifulSoup
from pynput.keyboard import Key,Controller
from time import sleep
from win10toast import ToastNotifier
import datetime
import time
keyboard = Controller()
strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes=1)).strftime("%M"))
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)
def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)
def tell_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
    if response.status_code == 200:
        joke = response.json()['joke']
        print(joke)
        speak(joke)
    else:
        print("Sorry, I couldn't find any jokes at the moment Abhishek.")
        speak("Sorry, I couldn't find any jokes at the moment Abhishek.")
def get_date():
    now = datetime.datetime.now()
    date_string = now.strftime("%A, %B %d, %Y")
    speak(f"The current date is {date_string}.")
def battery_status():
    battery = psutil.sensors_battery()
    percent = battery.percent
    speak(f'The battery percentage is : {percent} %')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def GreetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<=12:
        speak("Good Morning, Abhishek")
    elif hour>12 and hour<=18:
        speak("Good afternoon, Abhishek")
    else:
        speak("Good Evening,Abhishek")

    speak("Please tell me , how can i help you abhishek ")
def get_news():
    speak('Enter the category : ')
    category = str(input('Enter the category :'))
    speak('Enter the query such as specific interest')
    query = str(input('Enter the query : '))
    apikey = "a1efb2316ff8406de89f19918288d9cc"
    speak("Enter the country from which you want the news : ")
    country = str(input("Enter the country from which you want the news : "))
    url = (f"https://gnews.io/api/v4/top-headlines?category={category}&q={query}&lang=en&country={country}&max=3&apikey={apikey}")
    encoded_url = urllib.parse.quote(url, safe=':/&?=')
    with urllib.request.urlopen(encoded_url) as response:
        data = json.loads(response.read().decode("utf-8"))
        articles = data["articles"]

        for article in articles:
            print(f"Title: {article['title']}")
            speak(f"Title : {article['title']}")
            print(f"Description: {article['description']}")
            speak(f"Description: {article['description']}")
def open_application(application_name):
    if application_name.lower() == " notepad":
        speak('opening notepad sir')
        os.startfile("notepad.exe")
        print("Opening Notepad...")
    elif application_name.lower() == " calculator":
        os.startfile("calc.exe")
        speak('opening calclulator sir')
        print ("Opening Calculator...")
    elif application_name.lower() == " chrome":
        speak('opening chrome sir')
        os.startfile("chrome.exe")
        print ("Opening Chrome...")
    elif application_name.lower() == " terminal":
        speak('opening terminal sir')
        os.startfile("cmd.exe")
        print ("Opening terminal...")
    elif application_name.lower() == " settings":
        speak('opening settings sir')
        os.startfile("ms-settings:")
        print ("Opening settings...")
    elif application_name.lower() == " vs code":
        speak('opening vs code sir')
        os.startfile(" code")
        print ("Opening Visual studio code...")
    else:
        print ("Application not found.")
def close_application(application_name):
    speak(f'closing {application_name} sir')
    os.system(f"taskkill /f /im { application_name}.exe")
def set_alarm(alarm_time):
    # get the current time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    # calculate the number of seconds until the alarm time
    time_diff = (datetime.datetime.strptime(alarm_time, "%H:%M:%S") - datetime.datetime.strptime(current_time, "%H:%M:%S")).total_seconds()

    if time_diff < 0:
        print("Invalid time entered")
        return

    # wait for the specified time
    time.sleep(time_diff)

    # show a Windows toast notification at the alarm time
    toaster = ToastNotifier()
    toaster.show_toast("Alarm", "Wake up!", duration=10, threaded=True)
def calculate():
    try:
        speak("Enter the expression Abhishek: ")
        expression = str(input('Enter the expression : '))
        result = eval(expression)
        print(f"{result} is the answer abhishek" )
        speak(f'{result} is the answer abhishek')
    except:
        return "Sorry, I couldn't calculate that." 
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
def searchgoogle(query):
    if 'google' in query:
        query = query.replace("zira","")
        query = query.replace("google search","")
        query = query.replace("google","")
        query = query.replace("hey","")
        query = query.replace("for","")
        query = query.replace("search","")
        query = query.replace("on","")
        query = query.replace("in","")
        speak("This is what i found on google ")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)
        except:
            speak("No speakable output available")
def searchyoutube(query):
    if 'youtube' in query:
        speak("This is what i found for your search !")
        query = query.replace("youtube","")
        query = query.replace("search","")
        query = query.replace("zira","")
        query = query.replace("hey","")
        query = query.replace("for","")
        query = query.replace("on","")
        query = query.replace("in","")
        query = query.replace("play","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done,sir")
def searchwikipedia(query):
    if 'wikipedia' in query:
        speak("Searching from wikipedia...")
        query = query.replace("wikipedia","")
        query = query.replace("search","")
        query = query.replace("for","")
        query = query.replace("on","")
        query = query.replace("in","")
        query = query.replace("zira","")
        query = query.replace("hey","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia : ")
        print(results)
        speak(results)
def alarm(query):
    timehere = open('Alarmtext.txt','a')
    timehere.write(query)
    timehere.close
    os.startfile('alarm.py')

if __name__ == "__main__":
    while True:
        query = takecommand().lower()
        if 'wake up' in query:
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
                tell_joke()
            elif "open" in query:
                query = query.replace("open",'')
                print(query)
                open_application(query)
            elif "close" in query:
                query = query.replace('close','')
                close_application(query)
            elif 'bye' in query:
                speak("Bye abhishek !!")
                exit()
            elif "google" in query:
                searchgoogle(query)
            elif "youtube" in query:
                searchyoutube(query)
            elif "wikipedia" in query:
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
         
                speak("Turning volume up , Abhishek")
                volumeup()
            elif "volume down" in query:
               
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
             
                battery_status()
            elif "news" in query:
                get_news()
            elif "calculate" in query:
               
                calculate()
            elif 'whatsapp' in query:
            
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
            
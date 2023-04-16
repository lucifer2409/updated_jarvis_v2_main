import os
import pyttsx3
import speech_recognition
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


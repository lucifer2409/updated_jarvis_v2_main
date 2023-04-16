import speech_recognition
import pyttsx3
import pywhatkit
import webbrowser
import wikipedia
import wikipedia as googleScrap

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
        audio = r.listen(source,0,3)
        try:
            print("Understanding")
            query = r.recognize_google(audio,language='en-in')
            print(f"You said : {query} \n")
        except Exception as e:
            print("Say that again :(")
            return "None"
        return query
    

query = takecommand().lower()

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
        
        



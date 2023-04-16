import datetime
import pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_date():
    now = datetime.datetime.now()
    date_string = now.strftime("%A, %B %d, %Y")
    speak(f"The current date is {date_string}.")



import psutil
import pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def battery_status():
    battery = psutil.sensors_battery()
    percent = battery.percent
    speak(f'The battery percentage is : {percent} %')

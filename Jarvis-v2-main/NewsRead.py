import urllib.parse
import json
import speech_recognition as sr
import pyttsx3
import urllib.request

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

get_news()
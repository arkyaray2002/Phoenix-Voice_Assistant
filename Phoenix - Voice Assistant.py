import speech_recognition as sr
from ecapture import ecapture as ec
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import requests


listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def weatherReport():
    place = 'Kolkata'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={place}&units=metric&appid=858f54c9786e8dab5e2306b06f55df26'

    data = requests.get(url)
    data = data.json()

    talk('Your city is')
    talk(data['name'])
    talk(f"is {round(data['main']['temp'])} degree centigrade")
    talk(f" and humidity  {round(data['main']['humidity'])} percent")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        talk("Good Afternoon Sir !")

    else:
        talk("Good Evening Sir !")


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            wishMe()
            talk('I am Phoenix, your Personal Voice Assistant, made with Artificial Intelligence. How can I help you ?')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Phoenix' in command:
                command = command.replace('Phoenix', '')
                print(command)
    except:
        pass
    return command


def run_Phoenix():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)
    elif 'date' in command:
        today = datetime.datetime.now().strftime("%A %d %B %Y")
        talk('Today is ' + today)
    elif 'your name' in command:
        talk('My name is Phoenix, your Personal Voice Assistant, made with Artificial Intelligence.')
    elif "who made you" in command:
        talk("I am your virtual assistant PHOENIX, created by ARKYA RAY")
    elif "why you came to world" in command:
        talk("Thanks to ARKYA, who created me. further It's a secret")
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'open whatsapp' in command:
        talk("Here you go to WhatsApp Web\n")
        webbrowser.open("web.whatsapp.com")
    elif 'open youtube' in command:
        talk("Here you go to Youtube\n")
        webbrowser.open("youtube.com")
    elif 'open google' in command:
        talk("Here you go to Google\n")
        webbrowser.open("google.com")
    elif "camera" in command or "take a photo" in command:
        ec.capture(0, "Jarvis Camera ", "img.jpg")
    elif 'marry me' in command:
        talk('No, I think Single life is the Best Time of life. Here you have full freedom to do anything')
    elif 'are you single' in command:
        talk('No, I am in a relationship with your PC')
    elif 'what is love' in command:
        talk("It is 7th sense of human, that destroy all other senses")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif "weather" in command:
        weatherReport()
    else:
        talk('Please say the command again.')


while True:
    run_Phoenix()

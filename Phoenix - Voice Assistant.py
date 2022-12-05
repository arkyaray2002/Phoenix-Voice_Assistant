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
    elif 'date' in command:
        today = datetime.date.today()
        talk('Today is ' + today)
    elif 'your name' in command:
        talk('My name is Phoenix, your Personal Voice Assistant, made with Artificial Intelligence.')
    elif "who made you" in command:
        talk("I am your virtual assistant PHOENIX, created by ARKYA RAY")
    elif "why you came to world" in command:
        talk("Thanks to ARKYA. further It's a secret")
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
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

        # Google Open weather website
        # to get API of Open weather
        api_key = "Api key"
        base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
        talk(" City name ")
        print("City name : ")
        city_name = take_command()
        complete_url = base_url + "appid =" + api_key + "&q =" + city_name
        response = requests.get(complete_url)
        x = response.json()

        if x["code"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print(" Temperature (in kelvin unit) = " + str(current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(weather_description))
        else:
            talk(" City Not Found ")
    else:
        talk('Please say the command again.')


while True:
    run_Phoenix()
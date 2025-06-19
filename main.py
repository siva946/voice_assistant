import pyttsx3 #pip install pyttsx3
import datetime
import pyaudio #pipwin install pyaudio
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import psutil
import pyjokes
import pyautogui
import random
import requests
from pprint import pprint
# pprint is part of the Python standard library and does not require installation.


MASTER = "Siva Subramani"
print("Initializing zudo...")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak('The current time is')
    speak(Time)

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak('The Current date is')
    speak(date)
    speak(month)
    speak(year)

def wishme():
   speak("Welcome back sir!")
   #speak("the current time is")
   time()
   #speak("it's the")
   date()
   hour = datetime.datetime.now().hour
   if hour >= 0 and hour<12:
       speak("Good Morning" + MASTER)
   elif hour >=12 and hour<18:
        speak("Good Afternoon" + MASTER)
   elif hour >=18 and hour <24:
        speak("Good evening" + MASTER)
   else:
        speak("Good Night" + MASTER)
   speak("Zudo at your service. Please tell me how can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        # Recognize speech in English only
        try:
            query = r.recognize_google(audio, language='en-US')
        except sr.UnknownValueError:
            speak("Sorry, I could not understand.")
            return "None"
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return  "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yormail@gmail.com', 'zxcvbnm,./123')
    server.sendmail("sender@gmail.com", to, content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)

def battery():
    battery = psutil.sensors_battery()
    if battery is not None:
        speak(f'Battery is at {battery.percent} percent')
        if battery.power_plugged:
            speak('The charger is plugged in.')
        else:
            speak('The charger is not plugged in.')
    else:
        speak('Unable to get battery information.')

def joke():
    speak(pyjokes.get_joke())

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/SIVA/OneDrive/screenshot.png')

def who_am_i():
     speak('You are ' + MASTER + ', a brilliant person. I love you!')

def where_born():
    speak('I was created by a creator named Siva subramani, in Karaikudi.')

def how_are_you():
    speak('I am fine, thank you. How can help you Sir?')


def process_query(query):
    query = query.lower()
    if 'time' in query:
        time()

    elif 'date' in query:
        date()
    
    elif 'who am i' in query:
        who_am_i()
    
    elif 'where were you born' in query:
        where_born()
    
    elif 'how are you' in query:
        how_are_you()

    elif 'wikipedia' in query:
        speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak('According to Wikipedia...')
        print(results)
        speak(results)
    
    elif 'send email' in query:
        try:
            speak('What should I send...')
            content = takeCommand()
            speak('Who is the Receiver Sir?')
            receiver = input("Enter Receiver's Email :")
            to = receiver
            sendEmail(to, content)
            speak('Email sent Successfuly')

        except Exception as e:
            print(e)
            speak('Unable to send Email')
    
    elif 'open chrome' in query:
        speak('What should I Search?')
        chrome_path = r'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

        search = takeCommand().lower()
        webbrowser.get(chrome_path).open_new_tab(search+'.com')
    
    elif 'open youtube' in query:
        speak('What should I Search?')
        search_term = takeCommand().lower()
        speak("Opening YOUTUBE!")
        webbrowser.open('https://www.youtube.com/results?search_query='+search_term)
    
    elif 'weather details' in query: #weathermap Api
        speak('Which City Sir!')
        weather_up = takeCommand().lower()
        speak('Getting Weather Update for '+ weather_up)
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={API KEY}&units=metric'.format(weather_up)
        
        resi = requests.get(url)
        data = resi.json()
        temp = data['main']['temp'],
        wind_speed = data['wind']['speed'],
        latitude = data['coord']['lat'],
        longitude = data['coord']['lon'],
        description = data['weather'][0]['description']

        speak('Temperature is at: {} degree celcius'.format(temp))
        speak('Wind Speed is at: {} Micro Seconds'.format(wind_speed))
        speak('Latitude is : {}'.format(latitude))
        speak('Longitude is : {}'.format(longitude))
        speak('Clouds Status are : {}'.format(description))
        #update = webbrowser.open('https://api.openweathermap.org/data/2.5/weather?q={}&appid={API KEY}'.format(weather_up))

    elif 'open google' in query:
        speak('What should I Search?')
        search_term = takeCommand().lower()
        speak('Searching...')
        url = 'google.com'
        chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        webbrowser.open('https://www.google.com/search?q='+search_term)
    
    elif 'open github' in query:
        speak('Opening Github Sir!')
        search_term = takeCommand().lower()
        speak('Opening your Account Sir!')
        url = 'github.com'
        webbrowser.open('https://www.github.com/siva946')
    
    elif 'cpu' in query:
        cpu()
    
    elif 'joke' in query:
        joke()
    
    elif 'go offline' in query:
        speak('Going Offline Sir!')
        quit()
    
    elif 'open word' in query:
        speak('Opening MS Word....')
        ms_word = r'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office/WINWORD.EXE'
        os.startfile(ms_word)
    
    elif 'open downloads' in query:
        speak('Opening Downloads....')
        downloads = r'C:/Users/Tech/Downloads'
        os.startfile(downloads)
    
    elif 'open python' in query:
        speak('Opening PyCharm....')
        pycharm = r'C:/Program Files/JetBrains/PyCharm Community Edition 2020.1.2/bin/pycharm64.exe'
        os.startfile(pycharm)
    
    elif 'open visual code' in query:
        speak('Opening Visual Code....')
        pycharm = r'C:/Program Files/Microsoft VS Code/Code.exe'
        os.startfile(pycharm)
    
    elif 'write a note' in query:
        speak("What Should i write, Sir?")
        notes = takeCommand()
        file = open('notes.txt','w')
        speak("Sir Should I include Date and Time?")
        ans = takeCommand()
        if 'yes' in ans or 'sure' in ans:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            file.write(strTime)
            file.write(':-')
            file.write(notes)
            speak("Done taking Notes, Sir!")
        else:
            file.write(notes)
    
    elif 'show notes' in query:
        speak('Showing Notes')
        file = open('notes.txt','r')
        print(file.read())
        speak(file.read())

    elif 'screenshot' in query:
        screenshot()
    
    elif 'play music' in query:
        songs_dir = 'song directory'
        music = os.listdir(songs_dir)
        speak('What should I play?')
        speak('Select a number......')
        answer = takeCommand().lower()
        while('number' not in answer and answer != 'random' and answer != 'you choose'):
            speak('I could not understand you. Please Come up again')
            answer = takeCommand().lower()
        if 'number' in answer:
            no = int(answer.replace('number',''))
        elif 'random' or 'you choose' in answer:
            no  = random.randint(1,100)
        os.startfile(os.path.join(songs_dir,music[no]))
    
    elif 'who are you' in query:
        speak("I am Zudo, The Smart Assistant of Siva subramani, Developed to help him around with his work and makes his life easier with his machine")
    else:
        speak("Sorry, I didn't understand that command.")
        print("Sorry, I didn't understand that command.")

def run_assistant():
    wishme()
    while True:
        query = takeCommand().lower()
        if query == "none":
            continue
        process_query(query)

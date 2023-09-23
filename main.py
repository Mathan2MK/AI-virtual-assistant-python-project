import speech_recognition as sr
import pyaudio
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import wolframalpha
import ctypes
import subprocess
import time
import pyjokes
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def Start():
    print("Hi i am moon")
    speak("hi i am moon")
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        print("Hello Mathan, Good Morning")
        speak("Hello Mathan, Good Morning")
        speak("")
    elif hour>=12 and hour<18:
        print("Hello Mathan, Good Afternoon")
        speak("Hello Mathan, Good Afternoon")
    else:
        print("Hello Mathan, Good Evening")
        speak("Hello Mathan, Good Evening")

def instructions():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening now...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"You asked: {statement}\n")

        except Exception as e:
            print("i con not understund")
            speak("i con not understund, please say that again")
            return "None"
        return statement

Start()#-----------

if __name__ == '__main__':
    clear=lambda:os.system('cls')
    clear()

    while True:
        speak("How can I help you")
        statement = instructions().lower()
        if statement == 0:
            continue

        if 'what is' in statement:
            statement = statement.replace('wikipedia' and 'who' and 'what', '')
            info = wikipedia.summary(statement, 2)
            print(info)
            speak(info)


        elif 'who is' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("who is", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab('https://www.youtube.com')
            speak("Youtube is opened")
            time.sleep(1)

        elif 'open youtube music' in statement or "play music" in statement:
            webbrowser.open_new_tab('https://music.youtube.com')
            speak("Youtube Music is opened")
            time.sleep(1)

        elif 'play' in statement:
            song = statement.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)
            time.sleep(1)

        elif 'open google' in statement:
            webbrowser.open_new_tab('https://www.google.com/')
            speak("Google Chrome is opened")
            time.sleep(1)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail is opened")
            time.sleep(1)

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"the time is {strTime}")

        elif 'date' in statement:
            date = datetime.datetime.now().strftime('%d:%m:%y')
            print(date, '')

        elif "open leetcode" in statement:
            webbrowser.open_new_tab('https://leetcode.com/problemset/all/')
            speak("Here is leetcode, Have a great time solving problems!")

        elif 'news' in statement:
            news = webbrowser.open_new_tab('https://news.google.co.in/')
            speak('Here are some headlines from Google News. Happy reading')
            time.sleep(1)

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(1)

        elif 'joke' in statement:
            speak(pyjokes.get_joke())

        elif 'open chrome' in statement:
            speak("open chrome")
            codepath = r'C:\\Program Files\\Google\\Chrome\\Application\\chrome'
            os.startfile(codepath)

        elif 'open pycharm' in statement:
            speak("open pycharm")
            codepath = r'C:\\Users\\Mathan\\AppData\\Local\JetBrains\\PyCharm Community Edition 2023.1\\bin\\pycharm64'
            os.startfile(codepath)

        elif 'open this pc' in statement:
            speak("open pycharm")
            codepath = r'C:\\Users\\Mathan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\This PC'
            os.startfile(codepath)

        elif 'lock my system' in statement:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shut down my system' in statement or 'off my system' in statement :
            speak(" hut downing your system ")
            subprocess.call('shutdown / p /f')

        elif "restart" in statement:
            speak("restarted")
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in statement or "sleep" in statement:
            speak("system going sleep")
            subprocess.call("shutdown / h")

        elif "where is" in statement:
            statement = statement.replace("where is", "")
            location = statement
            speak("User asked to Locate")
            speak(location)
            webbrowser.open('https://www.google.nl / maps / place/' + location + "")

        elif "calculate" in statement:
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = statement.lower().split().index('calculate')
            statement = statement.split()[indx + 1:]
            res = client.statement (' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'exit' in statement:
            speak("Thanks for giving me your time")
            exit()
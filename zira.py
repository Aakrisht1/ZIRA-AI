import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyautogui
import keyboard
import time
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Zira Sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold=17500
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("According to wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'play music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=4u6bWs-ZG0o&list=RD4u6bWs-ZG0o&start_radio=1")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open spotify' in query:
            webbrowser.open("https://www.spotify.com/in-en/")

        elif 'open github' in query:
            webbrowser.open("https://github.com/")

        elif 'open slack' in query:
            webbrowser.open("https://slack.com/intl/en-in/")

        elif 'open geeks for geeks' in query:
            webbrowser.open("https://www.geeksforgeeks.org/")

        elif 'open calculator' in query:
            codePath = "C:\\Windows\\System32\\calc.exe"
            os.startfile(codePath)

        elif 'open notepad' in query:
            codePath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(codePath)

        elif 'open android studio' in query:
            codePath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(codePath)

        elif 'bluetooth' in query:
            keyboard.press_and_release('windows+a')
            time.sleep(3)
            pyautogui.click(x=1681, y=571)

        elif 'open discord' in query:
            webbrowser.open("https://discord.com/")

        elif 'open classroom' in query:
            webbrowser.open("https://classroom.google.com/u/1/h")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'check my task' in query:
            webbrowser.open("https://calendar.google.com/calendar/u/0/r?pli=1")

        elif 'open google meet' in query:
            webbrowser.open("https://meet.google.com/?hs=197&pli=1&authuser=0")

        elif 'exit' in query:
            speak("Sure Sir")
            exit()

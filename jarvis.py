import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello! How can I assist you today?")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recoginizing...")
        query=r.recognize_google(audio, language="en-in")
        print(f"user said : {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    return query


if __name__ == "__main__" :
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results.encode('utf-8'))
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")
        elif "open google" in query:
            webbrowser.open("https://www.google.com/")
        elif "open netflix" in query:
            webbrowser.open("https://netflix-clone-b9b3e.web.app")
        elif 'play music' in query:
            music_dir='D:\\Music-Player' 
            songs=os.listdir(music_dir)
            print(songs)
            random_song=random.choice(songs)
            os.startfile(os.path.join(music_dir,random_song))
        elif "the time" in query:
            strTime =datetime.datetime.now().strftime('%H:%M:%S')
            print(f"Generated response: Shyam, the time is {strTime}")
            speak(f"Shyam, the time is {strTime}")
        elif "open chrome" in query:
            browser="C:\\Users\\Public\\Desktop\\Google Chrome.lnk"
            os.startfile(browser)

        


        











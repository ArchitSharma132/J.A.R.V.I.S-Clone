import pyttsx3,datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from PyDictionary import PyDictionary

engine= pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    greeting = ""
    if 0 <= hour < 12:
        greeting = "good morning !"
    elif 12 <= hour < 18:
        greeting = "good afternoon !"
    elif hour >= 18:
        greeting = "good night !"
    else:
        greeting = "good evening !"

    final_greeting = greeting + " I am JARVIS sir, please tell me how may i help u"
    speak(final_greeting)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio=r.listen(source)
    try:
        print("Recognising...")
        query=r.recognize_google(audio, language= 'en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Say that again please...")
        return "None"
    return query


if __name__=="__main__":
    new_rate = 220
    engine.setProperty('rate', new_rate)
    wishMe()
    while True:
        query= takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching results....")
            query=query.replace("wikipedia", "")
            if query =="":
                speak("Please mention what u want to search for")
                query=takeCommand().lower()
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'college manager' in query:
            webbrowser.open("students.cuchd.in")
        elif 'lms' in query:
            webbrowser.open("lms.cuchd.in/login/index.php")
        elif 'chat gpt' in query:
            webbrowser.open("chatgpt.com")
        elif 'gmail' in query:
            webbrowser.open("mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
        elif 'outlook' in query:
            webbrowser.open("outlook.office.com/mail")
        elif 'open fitgirl' in query:
            webbrowser.open("fitgirl-repacks.site/popular-repacks")
        elif 'open dodi' in query:
            webbrowser.open("dodi-repacks.site")
        elif 'leetcode' in query:
            webbrowser.open("leetcode.com/explore")
        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{strtime}")
        elif 'brave' in query:
            b_path="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(b_path)
        elif 'repeat after me' in query:
            speak(f"{query}")
        elif 'define' in query:
            speak("Searching results....")
            query=query.replace("define", "")
            if query =="":
                speak("Please mention what u want to search for")
                query=takeCommand().lower()
            results=wikipedia.summary(query, sentences=3)
            speak("According to Internet")
            speak(results)
            webbrowser.open(f"https://www.dictionary.com/browse/{query}")

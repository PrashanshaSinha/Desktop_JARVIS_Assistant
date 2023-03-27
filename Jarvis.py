import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print(voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")

    elif hour>=12 and hour<=16:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Zira, your assistant. How may I help you")

def takeCommand():            
# It takes microphone input from the user and return string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sinhaprashansha12@gmail.com', 'Connectup@12')
    server.sendmail('sinhaprashansha12@gmail.com', to, content)
    server.close()
    
if __name__ == "__main__":
    wishMe()
    while True:
 # you need to say Open "Anything you want to search" in wikipedia then only ZIRA will work searching in wikipedia

            query = takeCommand().lower()
            if 'wikipedia' in query:
                speak('Searching Wikipedia....')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif "open youtube" in query:  
                webbrowser.open("https://www.youtube.com/")

            elif 'open google' in query:
                webbrowser.open("https://www.google.com/")

            elif 'open gmail' in query:
                webbrowser.open("https://www.gmail.com/")

            elif 'open github' in query:
                webbrowser.open("https://www.github.com/")

            elif "the time" in query:
                startime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"mam, the time is {startime}")

            elif "open code" in query:
                code_path = "C:\\Users\\Prashansha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(code_path)

            elif "open" in query:
                query = query.split(" ")
                search = query[1:]
                search = "+".join(search)
                url = f"https://www.google.com/search?q={search}"
                webbrowser.open(url)

            elif "email to self" in query:
                try:
                    speak("what should i say?")
                    content = takeCommand()
                    to = "sinhaprashansha12@gmail.com"
                    sendEmail(to, content)
                    speak("email has been sent!")
                except Exception as ex:
                    print(ex)
                    speak("sorry my friend, I am not able to sent this email right now, please check!!")

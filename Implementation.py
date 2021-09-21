import webbrowser

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sivaji")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sivaji")
    else:
        speak("Good evening sivaji")
    speak("I am Your Friend MR sivaji please tell me How can i help you")

def takeCommand():#With the help of the takeCommand() function, our A.I.
     # assistant will be able to return a string output by taking microphone input from us.
    #it takes microphone input from the user and returns the string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
    try:
        print("Recognizing..........")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        #print(e)
        print("say that again please....")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('koppisettisivaji@gmail.com','password')
    server.sendmail('koppisettisivaji@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('seaching wikipedia......')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'what the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")

        elif 'play music' in query:
            music_dir='E:\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'open kotlin' in query:
            codepath="C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.3.3\\bin\\idea64.exe"
            os.startfile(codepath)

        elif 'open power point' in query:
            codepath="C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
            os.startfile(codepath)

        elif 'email to sundar' in query:
            try:
                speak("what should i say....")
                content=takeCommand()
                to="ganeshbestliker143@gmail.com"
                sendEmail(to,content)
                speak("email has been sent..")
            except Exception as e:
                print(e)
                speak("sorry sivaji i am not able sent email.....")

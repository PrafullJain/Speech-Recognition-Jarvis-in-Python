import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import os
import webbrowser
import smtplib
import random


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

url="https://www.google.com"
cp="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(cp),1)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good AfterNoon!")
    else:
        speak("Good Evening!")
        
    speak("I'm  Jarvis sir. Please tell how may I help you")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
       #speak("Please Wait...")
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print("User Said: ",query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("praffuljaincp@gmail.com",'godisfail')
    server.sendmail('praffuljaincp@gmail.com',to,content)
    server.close()
    
if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching in Wikipedia...")
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia..")
            print(results)
            speak(results)
            break
        elif 'open youtube' in query:
            webbrowser.get('chrome').open_new_tab("https://www.youtube.com")
            break
        elif 'open google' in query:
            webbrowser.get('chrome').open_new_tab("https://google.com")
            break 
        elif 'open gmail' in query:
            webbrowser.get('chrome').open_new_tab("https://gmail.com")
            break 
        elif 'open twitter' in query:
            webbrowser.get('chrome').open_new_tab("https://twitter.com")
            break
        elif 'open news' in query:
            webbrowser.get('chrome').open_new_tab("https://timesofindia.com")
            break
        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open_new_tab("https://stackoverflow.com")          
            break
        elif 'play music' in query:
            speak("Music is Loading ,Please Wait...!")
            music_dir='D:\Downloads\\Music'
            songs=os.listdir(music_dir)
            speak("Music is playing now..")
            x=random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[x]))
            print(songs)
            break
        elif 'what is current time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir,the time is:")
            speak(strTime)
            break
        elif 'open eclipse' in query:
            codePath="D:\\Softwares\\eclipse\\eclipse.exe"
            os.startfile(codePath)
            break
        elif 'send email to anyone' in query:
            try:
                speak("Please tell the receiver email-address")
                toem=takeCommand()
                to=toem
                speak('What should I say?')
                content=takeCommand()
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend,we are not able to send the email ,please try after sometime..")
            break

           
    
    

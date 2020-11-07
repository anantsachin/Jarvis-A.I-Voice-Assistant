import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!") 

    speak ("I am Jarvis Sir. Please tell me how may I help you")

def takecommand():
     
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")   
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")                  

    except Exception as e:
        # print(e)   
        print("Say that again please...")   
        return "None"    
    return query

def sendEmail(do, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(#Your Email, #Password)) 
    server.sendmail(#Your Email, to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        # logic 
        if "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open cube' in query:
            webbrowser.open("play.google.com/store/apps/details?id=com.Gamezlab.Cube.io")

        elif 'open blue ridge parents portal' in query:
            webbrowser.open("ict.blueridgepublicschool.com")

        elif 'open siemens' in query:
            webbrowser.open("siemens.com")


        elif 'play music' in query:
            music_dir = 'C:\\Users\\ntpriv\Music\\favsongs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir< songs[0]))
        

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
        
        elif 'open unity' in query: 
            unityPath = "C:\\Program Files\\Unity Hub\\Unity Hub.exe"
            os.startfile(unityPath)

        elif 'open code' in query: 
            codePath = "C:\\Users\\ntpriv\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'who made you' in query:
            speak("i am made by Anant upadhyay he is a game developer and ethical hacker. he is also the ceo and founder of gamezlab.")

        elif 'how to use tik tok' in query:
            speak("Abe saale abhi band kiya aur terako chalu karvana he maar tu saale")

        elif 'send email to anant' in query:
            try:
                speak("what should i say")
                content = takecommand()
                to = # Reciver's email
                sendEmail(to, content)
                speak("Email has been send!")
            except Exception as e:
                print(e)
                speak("Sorry my friend anant bhai. I am not able to send this email")
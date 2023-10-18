import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import pywhatkit
assistant = pyttsx3.init('sapi5')
voices=assistant.getProperty('voices')
assistant.setProperty('voices',voices[1].id)
assistant.setProperty('rate',170)

def speak(audio):
    print(" ")
    assistant.say(audio)
    print(f":{audio}")

    assistant.runAndWait()

def Takecommand():
    command=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        command.pause_threshold =1
        audio = command.listen(source)

        try:
            print("recognizing...")
            query = command.recognize_google(audio,language='en=hi')
            print(f"you said:{query}")

        except Exception as error:
            return "None"
        return query.lower()

def taskExe():

    while True:
        query = Takecommand()

        if 'hello' in query:
            speak("'hello sir , i am jarvis")
            speak("your personal AI assistant")
            speak(" how can i help you")

        elif 'how are you' in query:
            speak("i am fine sir ")
            speak("what about you")
        
        elif 'take a break' in query:
            speak("ok sir")
            break

        elif 'tell me a joke' in query:
            speak("why tigers can't hide")
            speak("because they are spotted")

        
 
        elif 'youtube' in query:
            query=query.replace("jarvis","")
            query=query.replace("youtube search","")
            webbrowser.open("https://www.youtube.com/results?search_query="+query)
            speak("done sir")

        elif 'google' in query:
            speak("this is what i found")
            query=query.replace("jarvis","")
            query=query.replace("google search","")
            pywhatkit.search(query)
            speak("done sir")
        elif 'shutdown' in query:
             os.system("shutdown /s /t 1")
taskExe()



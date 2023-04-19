
from jarvisUI import  Ui_Dialog
from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType 
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import sys
assistant = pyttsx3.init('sapi5')
voices=assistant.getProperty('voices')
assistant.setProperty('voices',voices[1].id)
assistant.setProperty('rate',170)

f=True

def speak(audio):
   
    print(" ")
    assistant.say(audio)
    print(f":{audio}")

    assistant.runAndWait()

class MainThread(QThread):

    def __init__(self):
       super(MainThread,self).__init__()

    

   
    def Takecommand(self):
     command=sr.Recognizer()
     with sr.Microphone() as source:
        print("listening...")
        command.pause_threshold =1
        audio = command.listen(source)

        try:
            print("recognizing...")
            self.query = command.recognize_google(audio,language='en=hi')
            print(f"you said:{self.query}")

        except Exception as error:
            return "None"
        return self.query.lower()

    def taskExe(self):
       
     speak("hello sir i am jarvis")
     while f:
        self.query = self.Takecommand()

        if 'hello' in self.query:
            speak("'hello sir , i am jarvis")
            speak("your personal AI assistant")
            speak(" how can i help you")

        elif 'how are you' in self.query:
            speak("i am fine sir ")
            speak("what about you")
        
        elif 'take a break' in self.query:
            speak("ok sir")
            break

        elif 'tell me a joke' in self.query:
            speak("why tigers can't hide")
            speak("because they are spotted")

        elif 'i love you ' in self.query:
            speak("i love you too")
            speak("but as a friend")
 
        elif 'youtube' in self.query:
            self.query=self.query.replace("jarvis","")
            self.query=self.query.replace("youtube search","")
            webbrowser.open("https://www.youtube.com/results?search_query="+self.query)
            speak("done sir")

        elif 'google' in self.query:
            speak("this is what i found")
            self.query=self.query.replace("jarvis","")
            self.query=self.query.replace("google search","")
            pywhatkit.search(self.query)
            speak("done sir")
        

startFunctions = MainThread()

class Gui_Start(QMainWindow):

  def __init__(self):
    super().__init__()
    self.jarvisUi = Ui_Dialog()
    self.jarvisUi.setupUi(self)

    self.jarvisUi.pushButton.clicked.connect(self.startFunc)
    self.jarvisUi.pushButton_2.clicked.connect(self.close)
  
  def startFunc(self):
     
     self.jarvisUi.movie = QtGui.QMovie("Iron_Template_1.gif")
     self.jarvisUi.label_2.setMovie(self.jarvisUi.movie)
     self.jarvisUi.movie.start()

     self.jarvisUi.movie = QtGui.QMovie("7kmF.gif")
     self.jarvisUi.label_3.setMovie(self.jarvisUi.movie)
     self.jarvisUi.movie.start()
      

     self.jarvisUi.movie = QtGui.QMovie("Code_Template.gif")
     self.jarvisUi.label_4.setMovie(self.jarvisUi.movie)
     self.jarvisUi.movie.start()

     self.jarvisUi.movie = QtGui.QMovie("Earth.gif")
     self.jarvisUi.label_5.setMovie(self.jarvisUi.movie)
     self.jarvisUi.movie.start()
     startFunctions.taskExe()

     

 

Gui_App = QApplication(sys.argv)
Gui_jarvis = Gui_Start()
Gui_jarvis.show()

exit(Gui_App.exec_())
f=False

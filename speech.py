import speech_recognition as sr# Its use to listen audio and convert into text
import pyttsx3# It is use to speak the text
import webbrowser#It is use to connect with the web pages
import pyjokes#It is use to provide the jokes 
import datetime#Its provide the infomation of time
import pyaudio
from flask import request
from flask import render_template
from flask import Flask
import time
#Initalize speech_recognition class as r
r=sr.Recognizer()
#Using Flask for web pages
speech=Flask(__name__)

def spktxt():
#use microphone as a source
      with sr.Microphone() as source:
            print("Listning")
            r.adjust_for_ambient_noise(source)#remove listen time noise capture
            audio=r.listen(source)
            try:
                  print("recognizing...")
                  text=r.recognize_google(audio,language="en-in")# Use google recognizer
                  print("User said:",text)
                  return text
            except sr.UnknownValueError:
                  print("Sorry,Couldn't understand audio")
                  return None
def speechtxt(text):
      #Initalize pyttsx3 class as engine
      engine=pyttsx3.init()
      #There are two types of voice:1.Man 2.Women (get voice property)
      voices=engine.getProperty("voices")
      #Set the voice as man for index[0] and for women index[1]
      engine.setProperty("voice",voices[1].id)
      #Set the speed of speak text
      rate=engine.getProperty("rate")
      engine.setProperty('rate',150)
      #Speak the text
      engine.say(text)
      engine.runAndWait()
#Connect with web page
@speech.route('/',methods=["POST","GET"])
def index():
      output = ""
      spoken_text=""
      if request.method == "POST":
        
        spoken_text = spktxt()
        if spoken_text is None:
            output = "Sorry, I didn't catch that."
        else:
            data = spoken_text.lower()
            if "your name" in data:
                output = "I am a large language model Electronic Machine"
            elif "open youtube" in data:
                output = "Opening YouTube"
                webbrowser.open('https://www.youtube.com/')
            elif "joke" in data:
                output = pyjokes.get_joke(language="en", category="neutral")
            elif "time" in data:
                #datetime.datetime.now() defines the current time
                #strftime search the different categories here %I=hours,%M=minutes,%p=pm or am
                output = datetime.datetime.now().strftime("%I:%M %p")
            elif "exit" in data:
                output = "Thank you. Goodbye!"
            else:
                output = "Command not recognized."
            speechtxt(output)
      return render_template('index.html', response=output,sptext=spoken_text)
      time.sleep(5)



if __name__ == '__main__':
     speech.run(debug=True)
      
#       while True:
#             data=spktxt().lower()
#             if "your name" in data:
#                   name="My name is real world problem solver electronic machine"
#                   speechtxt(name)
#             elif "open youtube" in data:
#                   webbrowser.open('https://www.youtube.com/')
#             elif "joke" in data:
#                   py_joke=pyjokes.get_joke(language="en",category="neutral")
#                   print(py_joke)
#                   speechtxt(py_joke)
#             elif "time" in data:
                  
#                   time=datetime.datetime.now().strftime("%I%M%p")
#                   print(time)
#                   speechtxt(time)
#             elif "exit" in data:
#                   speechtxt("Thank you")
#                   break
      

# else:
#       print("Speech recognition failed")


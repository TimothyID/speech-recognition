import speech_recognition as sr
import time
import os
import random
import datetime
import webbrowser
import sys

jokes = ["Did you hear about the restaurant on the moon? Great food, no atmosphere.", "What do you call a fake noodle? An Impasta.",
"How many apples grow on a tree? All of them.", "Want to hear a joke about paper? Nevermind it's tearable."]

r = sr.Recognizer()

def web():
    send = webbrowser.open('reddit.com')
with sr.Microphone() as source:
    while(1):
        print ('What do you want me to do?')
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
        if text == 'exit' or text == 'stop':
            os.system("espeak 'Bye Bye!'")
            sys.exit()
        if text == 'joke':
            print(random.choice(jokes))
            os.system("espeak 'Bye Bye!'")
        if text == 'time':
            print(datetime.datetime.now().time())
            os.system("espeak 'Bye Bye!'")
        if text == 'date':
            print(datetime.datetime.now().date())
            os.system("espeak 'Bye Bye!'")
        print('Done!')
        time.sleep(2)

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
    while(1):import speech_recognition as sr
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
            os.system('clear')
        if text == 'joke':
            randJoke = random.choice(jokes)
            print(randJoke)
            os.system("espeak '{}'".format(randJoke))
            os.system('clear')
        if text == 'time':
            time = datetime.datetime.now().time()
            print(time)
            os.system("espeak '{}'".format(time)
            os.system('clear')
        if text == 'date':
            date = datetime.datetime.now().date()
            print(date)
            os.system("espeak '{}'".format(date))
            os.system('clear')
        print('Done!')
        time.sleep(2)

        print ('What do you want me to do?')
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
        if text == 'exit' or text == 'stop':
            os.system("espeak 'Bye Bye!'")
            sys.exit()
        if text == 'joke':
            randJoke = random.choice(jokes)
            print(randJoke)
            os.system("espeak '{}'".format(randJoke))
        if text == 'time':
            time = datetime.datetime.now().time()
            print(time)
            os.system("espeak '{}'".format(time))
        if text == 'date':
            date = datetime.datetime.now().date()
            print(date)
            os.system("espeak '{}'".format(date))
        print('Done!')
        time.sleep(2)

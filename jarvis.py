from tkinter import *
import speech_recognition as sr
import time
import os
import random
import datetime
import webbrowser
import sys
from currency_converter import CurrencyConverter

jokes = ["Did you hear about the restaurant on the moon? Great food, no atmosphere.", "What do you call a fake noodle? An Impasta.",
"How many apples grow on a tree? All of them.", "Want to hear a joke about paper? Nevermind it's tearable."]

r = sr.Recognizer()

c = CurrencyConverter()

def button_clicked():
    with sr.Microphone() as source:
        print ('What do you want me to do?')
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
        if text == 'help':
            os.system("espeak 'Commands, joke, date, time, help, exit'")
        if text == 'exit' or 'stop' or 'exit app' or 'stop app':
            os.system("espeak 'Bye Bye!'")
            sys.exit()
        if text == 'date' or 'tell the date' or 'tell me the date' or 'what is the date':
            date = str(datetime.datetime.now().date())
            os.system("espeak '{}'".format(date))
        if text == 'time' or 'what is the time' or 'what time is it':
            time = str(datetime.datetime.now().time())
            os.system("espeak '{}'".format(time))
        if text == 'jokes' or 'tell me a joke':
            randJoke = random.choice(jokes)
            os.system("espeak '{}'".format(randJoke))
            

root = Tk()

root.geometry('500x600')

button1 = Button(root, bg='blue', text='Speak!', command=button_clicked, height=2, width=25)
button1.place(x='140', y='270')

os.system("espeak 'Hey! My name is Andrew! I can help you with basic tasks! Say HELP for commands list'")


root.mainLoop()

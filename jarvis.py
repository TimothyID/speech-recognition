from tkinter import *
import speech_recognition as sr
import time
import os
import random
import datetime
import webbrowser
import sys

jokes = ["Did you hear about the restaurant on the moon? Great food, no atmosphere.", "What do you call a fake noodle? An Impasta.",
"How many apples grow on a tree? All of them.", "Want to hear a joke about paper? Nevermind it's tearable."]

nets = ['.com', '.net', '.ru', '.io', '.eu']

r = sr.Recognizer()

root = Tk()

def button_clicked():
    with sr.Microphone() as source:
        print ('What do you want me to do?')
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
        if text == 'help':
            help = 'Commands, joke, date, time, exit'
            os.system("espeak '{}'".format(help))
        elif text == 'exit':
            ex = 'Bye bye!'
            os.system("espeak '{}'".format(ex))
            sys.exit()
        elif text == 'date':
            date = str(datetime.datetime.now().date())
            os.system("espeak '{}'".format(date))
        elif text == 'time':
            time = str(datetime.datetime.now().time())
            os.system("espeak '{}'".format(time))
            labe1 = label(root, textvariable=time)
        elif nets in text:
            print('Success')
        elif text == 'website':
            url = 'reddit.com'
            opr = 'Opening Reddit!'
            os.system("espeak '{}'".format(opr))
            webbrowser.get('firefox').open(url)
        elif text == 'jokes' or 'tell me a joke':
            randJoke = random.choice(jokes)
            os.system("espeak '{}'".format(randJoke))


root.geometry('500x600')

button1 = Button(root, bg='blue', text='Speak!', command=button_clicked, height=2, width=25)
button1.place(x='140', y='270')

root.mainloop()

#os.system("espeak 'Hey! My name is Andrew! I can help you with basic tasks! Say HELP for commands list'")

root.mainLoop()

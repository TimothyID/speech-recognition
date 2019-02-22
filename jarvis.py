#1).  make calculator

from tkinter import *
import speech_recognition as sr
import time
import os
import random
import datetime
import webbrowser
import sys
import re
from pygame import mixer

jokes = ["Did you hear about the restaurant on the moon? Great food, no atmosphere.", "What do you call a fake noodle? An Impasta.",
"How many apples grow on a tree? All of them.", "Want to hear a joke about paper? Nevermind it's tearable."]

headsTails = ['Heads', 'Tails']

h

r = sr.Recognizer()

root = Tk()

root.title('Syava Bot')

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
        elif text == 'heads or tails':
            ht = random.choice(headsTails)
            os.system("espeak '{}'".format(ht))
        elif text == 'date':
            date = str(datetime.datetime.now().date())
            os.system("espeak '{}'".format(date))
        elif text == 'time':
            time = str(datetime.datetime.now().time())
            os.system("espeak '{}'".format(time))
            labe1 = label(root, textvariable=time)
        elif '.com' in text:
            print('Success')
            url = text
            sub = re.sub('\.com$', '', url)
            opr = 'Opening ' + sub
            os.system("espeak '{}'".format(opr))
            webbrowser.get('firefox').open(url)
        elif '.net' in text:
            print('Success')
            url = text
            sub = re.sub('\.net$', '', url)
            opr = 'Opening ' + sub
            os.system("espeak '{}'".format(opr))
            webbrowser.get('firefox').open(url)
        elif '.eu' in text:
            print('Success')
            url = text
            sub = re.sub('\.eu$', '', url)
            opr = 'Opening ' + sub
            os.system("espeak '{}'".format(opr))
            webbrowser.get('firefox').open(url)
        elif text == 'f*** you':
            fuck = 'fuck you'
            os.system("espeak '{}'".format(fuck))
            root.destroy()
            print('............/´¯/)..............(\¯`\...... ......')
            print('............/....//..............\\....\...........')
            print('.........../....//................\\....\..........')
            print('....../´¯/..../´¯\............/¯` ....\¯`\.....' )
            print('..././.../..../..../.|_....._|.\....\....\...\.\..')
            print('(.(....(....(..../.)..).....(..(.\....)....)....).)')
            print('.\................\/.../....\...\/................/')
            print('....\..............(............)............../...')
            print('......\.............\.........../............./....')
            print('                    yo mum gei')
        elif text == 'mad':
            url = 'https://www.youtube.com/watch?v=10yrPDf92hY'
            mad = 'Opening the clip mad city'
            os.system("espeak '{}'".format(mad))
            webbrowser.get('firefox').open(url)
        elif text == 'jokes' or 'tell me a joke':
            randJoke = random.choice(jokes)
            os.system("espeak '{}'".format(randJoke))
        elif text == 'hello':
            hello = random.choice(helloo)
            os.system("espeak '{}'".format(hello))

root.geometry('500x600')

C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "syava.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

button1 = Button(root, bg='blue', text='Speak!', command=button_clicked, height=2, width=25)
button1.place(x='140', y='270')

mixer.init()
mixer.music.load('syavapro.mp3')
mixer.music.play()

root.mainloop()

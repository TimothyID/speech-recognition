import speech_recognition as sr
import time
import os

r = sr.Recognizer()

with sr.Microphone() as source:
    while(1):
        def speech():
            time.sleep(2)
            print ('What do you want me to do?')
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
            if text == 'joke':
                print('chicken')
            print('Done!')

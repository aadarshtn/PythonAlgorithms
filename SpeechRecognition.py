# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 22:40:41 2019

@author: ADARSH
"""

import speech_recognition as sr

a_f=("speech.wav")

r = sr.Recognizer()

with sr.AudioFile(a_f) as source:
    audio=r.record(source)
    
try:
    print("Audio file contains : " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError:
    print("Couldnt get the results from google soeech recognition")
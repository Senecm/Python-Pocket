from PyDictionary import PyDictionary
from tkinter import *
import tkinter as tk
import pyttsx3
import speech_recognition as sr
#import json
win = Tk()
win.geometry("600x500")
win.title("Dictionary")

def relaySound(word):
    eng = pyttsx3.init()
    eng.say(word)
    eng.runAndWait()
    
def findMeaning(word):
    dic = PyDictionary()
    try: 
        defi = dic.meaning(word)
        #json.loads(defi)
        txtare = Text(win, height=10, width=70)
        txtare.grid(column=0, row=8)
        print(defi)
        txtare.insert(tk.END, str(defi))
        btnb = Button(win, text="Listen", bg="black", fg="white", command = lambda: relaySound(txtare.get("1.0", END)))
        btnb.grid(column=0, row=7)
    except Exception as e:
        print(e)

def speechMeaning():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        output = r.recognize_google(audio)
    dic = PyDictionary()
    try:
        defi = dic.meaning(output)
        lblc = Label(win, text="Activated!", font=("Arial Bold", 10))
        lblc.grid(column=0, row=11)
        txtarea = Text(win, height=10, width=70)
        txtarea.grid(column=0, row=13)
        txtarea.insert(tk.END, defi)
        btnb = Button(win, text="Listen", bg="black", fg="white", command = lambda: relaySound(txtarea.get("1.0", END)))
        btnb.grid(column=0, row=11)
    except Exception as e:
        print(e)

lbl = Label(win, text="Tkinter Dictionary", font=("Comic Sans Ms", 50))
lbl.grid(column=0, row=0)
lbla = Label(win, text="Enter a word to search for a meaning:", font=("Arial Bold", 15))
lbla.grid(column=0, row=1)
ent = Entry(win, width=50)
ent.grid(column=0, row=6)
btn = Button(win, text="Find Meaning", bg="blue", fg="white", command = lambda: findMeaning(ent.get()))
btn.grid(column=0, row=7)
lblb = Label(win, text="Say a word to search for a meaning:", font=("Arial Bold", 15))
lblb.grid(column=0, row=9)
enta = Entry(win, width = 50)
enta.grid(column=0, row=10)
btna = Button(win, text="Activate", bg="blue", fg="white", command = lambda: speechMeaning())
btna.grid(column=0, row=12)
win.mainloop()
from PyDictionary import PyDictionary
from tkinter import *
import pyttsx3
import speech_recognition as sr
win = Tk()
win.geometry("600x500")
win.title("Dictionary")
def findMeaning(word):
    dic = PyDictionary()
    output = Label(win, text=word, font=("Helvetica", 10))
    try: 
        print(word)
        print(dic.meaning(word))
    except IndexError:
        print("Could not find your word!")
lbl = Label(win, text="Tkinter Dictionary", font=("Comic Sans Ms", 50))
lbl.grid(column=0, row=0)
lbla = Label(win, text="Enter a word to search for a meaning:", font=("Arial Bold", 15))
lbla.grid(column=0, row=1)
ent = Entry(win, width=50)
ent.grid(column=0, row=6)
btn = Button(win, text="Find Meaning", bg="blue", fg="white", command = lambda: findMeaning(ent.get()))
btn.grid(column=0, row=7)
win.mainloop()

'''
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("Roger that, relaying information...")
        print(f"You said {text}")
    except sr.UnknownValueError:
        print("Could not understand what your saying")
    except Exception as e:
        quit(e)
'''
'''
dictionary = PyDictionary()
print(dictionary.meaning("big"))
'''
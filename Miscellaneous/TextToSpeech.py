__author__ = "Gordan"
import pyttsx3
#import speech_recognition as sr
engine = pyttsx3.init()
con = engine.runAndWait()
engine.say("Hello!")
engine.runAndWait()
engine.say("Give me some text to say back to you!")
engine.runAndWait()
user_input = input("Enter Text: ")
engine.say(user_input)
engine.runAndWait()
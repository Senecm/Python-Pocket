__author__ = "Gordan"
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Adjusting for ambiant noise...")
    r.adjust_for_ambient_noise(source)
    print(f"New energy threshold is {r.energy_threshold}")
    print("say something")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    try:
        text = r.recognize_google(audio)
        print("Roger that, relaying information...")
        print(f"You said {text}")
    except sr.UnknownValueError:
        print("Could not understand what your saying")
    except Exception as e:
        quit(e) #code above was helped in part by sebby37
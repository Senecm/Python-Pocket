import pyttsx3
import pitch
from pitch import *

e = pyttsx3.init()
i = pitch.voice()
i.listVoice()
i.setVoice(0)
e.say("egg")
e.runAndWait()
e.stop()
i.setVoice(1)
e.say("egg")
e.runAndWait()
e.stop()
i.setVoice(2)
e.say("egg")
e.runAndWait()
e.stop()
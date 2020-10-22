import pyttsx3

class voice:
    def listVoice(self):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:
            print(voice, voice.id)
            engine.setProperty('voice', voice.id)
            engine.say('Hello World')
            engine.runAndWait()
            engine.stop()
    def setVoice(self, option=0):
        engine = pyttsx3.init()
        voiceEn = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
        voiceAm = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
        VoiceRu = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'
        if option == 0:
            engine.setProperty('voice', voiceEn)
            engine.runAndWait()
            engine.stop
        elif option == 1:
            engine.setProperty('voice', voiceAm)
            engine.runAndWait()
            engine.stop()
        elif option == 2:
            engine.setProperty('voice', VoiceRu)
            engine.runAndWait()
            engine.stop()

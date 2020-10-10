import speech_recognition as sr
import os

r = sr.Recognizer()

for filename in os.listdir(os.getcwd()):
    if os.path.splitext(filename)[1].lower() == '.wav':
        test = sr.AudioFile(filename)
        with test as source:
            audio = r.record(source, duration=2)
        #try:
        result = r.recognize_sphinx(audio)
        newname = os.path.splitext(filename)[0] + '-' + result + os.path.splitext(filename)[1]
        print (newname)
        os.rename(filename, newname)
        #except:
        #    pass

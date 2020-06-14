import speech_recognition as sr
recon = sr.Recognizer()

with sr.Microphone() as source:
    print('diga algo para teste:')
    audio = recon.listen(source)

def method_name():
    return print(recon.recognize_sphinx(audio))

method_name()
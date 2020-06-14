import speech_recognition as sr
#biblioteca usada para arquivo de voz

recon = sr.Recognizer()

#variavel que irá reproduzir o arquivo de audio FALA.WAV que foi gravado
PATH = 'fala.wav'

with sr.AudioFile(PATH) as source:
    audio = recon.record(source)

print(recon.recognize_sphinx(audio))
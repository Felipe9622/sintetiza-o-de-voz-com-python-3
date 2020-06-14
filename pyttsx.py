import pyttsx3
from time import sleep

en = pyttsx3.init()

en.setProperty('rate', 155)
en.setProperty('volume', 2)
en.say("Olá, chefe , meu nome é, amdromeda")

sleep(2)

en.setProperty('rate', 150)
en.setProperty('volume', 1)
en.say("Para verificar se, está , tudo certo, quer fazer algum teste, ?")

en.runAndWait()

# RATE = velocidade
# volume = volume vai de 0 a 1
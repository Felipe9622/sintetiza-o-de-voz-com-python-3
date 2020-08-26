import pyttsx3
from time import sleep
from datetime import datetime
from googletrans import Translator
from googletrans.gtoken import TokenAcquirer

translator = Translator()
agora = datetime.now()
som = pyttsx3.init()




som.setProperty('rate', 150)
som.setProperty('volume', 2)
som.say("Olá, meu nome é, Amdromeda, ")
sleep(2)
som.say("Sou seu sistema, de tradução, de idiomas")
sleep(2)
som.say("antes de continuarmos, que tipo, de modo deseja fazer ?")
som.runAndWait()
print("""[1] comando de voz 
[2] texto""")
escolha = input("opção:")
if escolha == '1':
    teste = input('Quer fazer um teste para verificar se esta tudo ok ? S/N:').upper()
    if teste == 'S':
        nome = input("nome:")
        hora = agora.hour
        minuto = agora.minute

        som.setProperty('rate', 150)
        som.setProperty('volume', 1)
        texts1 = "Olá " + str(nome) + ",seja bem vindo, agora são " + str(hora) + "horas e" + str(minuto) + "minutos"
        sleep(2)


        som.say(texts1)

        som.setProperty('rate', 150)
        som.setProperty('volume', 1)
        som.say("digite uma frase")
        som.runAndWait()
        som.runAndWait()
    else:
        som.setProperty('rate', 150)
        som.setProperty('volume', 1)
        som.say("Digite uma frase")
        som.runAndWait()
else:
    som.setProperty('rate', 150)
    som.setProperty('volume', 1)
    som.say("Digite uma frase")
    som.runAndWait()
r = 'S'
while r == 'S':
    texto_pt = input("frase: ")

    acquirer = TokenAcquirer()
    acquirer.do(texto_pt)

    texto_en = translator.translate(texto_pt,src="pt", dest="en")

    print("Original text:", texto_pt)
    print("translation:", texto_en.text)
    r = str(input("Quer continuar ? [S/N]: ")).upper()

print('Fim')




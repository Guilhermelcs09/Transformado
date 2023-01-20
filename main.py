import pyttsx3


usuario = input('Qual arquivo vai ser tranformado em audio? ')
ler_arquivo = open(usuario, 'r', encoding='utf8')
texto = ler_arquivo.read()

# iniciando o programa
iniciar = pyttsx3.init()


voices = iniciar.getProperty('voices')

iniciar.setProperty('voice', voices[0].id)
rate = iniciar.getProperty('rate')
iniciar.setProperty('rate', rate+20)


print(texto)
iniciar.say(texto)
iniciar.runAndWait()

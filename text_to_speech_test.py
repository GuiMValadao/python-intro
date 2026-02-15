import pyttsx3

engine = pyttsx3.init()  # Criação do objeto/inicialização do módulo
engine2 = pyttsx3.init()

# Velocidade de fala
rate = engine.getProperty("rate")  # obtem detalhes da velocidade atual
print(rate)  # exibe a velocidade atual
engine.setProperty("rate", 100)  # define uma nova velocidade


# VOLUME
volume = engine.getProperty("volume")  # obtém o volume atual (min=0 and max=1)
print(volume)  # exibe o volume atual
engine.setProperty("volume", 0.8)  # define o volume, entre 0 and 1

# VOICE
voices = engine.getProperty("voices")  # obtém a lista de todas as vozes disponíveis
print(voices)
# Alterar índices para mudar as vozes.
# 0: feminina brasileira; 1: feminina inglesa; 2: feminina japonesa; 3: masculina inglês
engine.setProperty("voice", voices[0].id)
frase1 = " 1 2 3 teste "
frase2 = " 4 5 6 teste"
engine.say(frase1 + frase2)

engine2.runAndWait()

#------------------------------------------------------------
# Cap 8 - Jogo de adivinhacao
# Cap 11 - Dividir o jogo de adivinhaçao em funçoes menores.
# Cap 12 - Utilizar variaveis globais para simplificar o programa
#------------------------------------------------------------
import random

jogo = True
adivinhacao = 0
# Funçao para iniciar/reiniciar o jogo
def replay():
    global jogo
    if jogo == 's':
        jogo = True
        return jogo
    else:
        jogo = False
        return jogo

# Funçao para iniciar/reiniciar o jogo
def inicio(i = 0):
    global jogo
    if i == 0:
        i += 1
        print('Bem-vindo ao jogo de adivinhação de números!')
        jogo = str(input('Quer jogar? (s/n)'))
        comecar = replay()
        return comecar, i
    else:
        i += 1
        jogo = str(input('Quer jogar novamente? (s/n)'))
        comecar = replay()
        return comecar, i

# Funçao para obter input do usuario
def tentativa(resposta):
    global adivinhacao
    adivinhacao = input('Dê seu palpite entre 1 e 20: ')
    chec_num()
    # Para roubar, obtendo a resposta sem perder uma chance
    if adivinhacao == '-1':
        adivinhacao = cheat(resposta)
    return adivinhacao

# Funçao para garantir que foi inserido um numero e que le esta entre 0 e 21.
def chec_num():
    global adivinhacao
    while not((adivinhacao.isnumeric() and
                0 < int(adivinhacao) <= 20) or
        adivinhacao == '-1'):
        adivinhacao = input('Por favor, insira um numero inteiro de 1 a 20: ')
    return adivinhacao


# Funçao que define o cheat
def cheat(resposta):
    global  adivinhacao
    if adivinhacao == '-1':
        print('o numero correto e ', resposta)
        adivinhacao = input('Dê seu palpite entre 1 e 20: ')
        chec_num()
        cheat(resposta)
        return adivinhacao
    return None


# Funçao que verifica se o usuario acertou
def vitoria(resposta, chances, guess):
    if guess == resposta:
        print('Parabéns! Você acertou!')
        print('Você precisou de', 5 - chances,
              'tentativas para vencer!')
        return True
    else:
        return False

# Funçao que verifica se o usuario errou
def errado(chances, teste2, resposta):
    chances -= 1
    if chances == 0:
        print('Que pena, você perdeu... ')
        print('O número correto era ', resposta)
        return chances
    elif ((teste2 == resposta - 1) or
          (teste2 == resposta + 1)):
        print('Errado. Sua adivinhação passou perto.')
        return chances
    elif teste2 < resposta:
        print('Errado. Tente um número maior.')
        return chances
    else:
        print('Errado. Tente um número menor.')
    return chances

# Funçao definindo o loop principal do jogo
def loop_jogo():
    global jogo
    jogo = inicio()[0]
    while jogo == True:

        resposta = random.randint(1, 20)
        chances = 4

        # Permite ao usuario tentar novamente ate ficar sem chances
        while chances > 0:
            guess = int(tentativa(resposta))

            # Verifica se o jogador adivinhou corretamente.
            if not vitoria(resposta, chances, guess):
                chances = errado(chances, guess, resposta)
            else:
                break
        jogo = inicio(1)[0]

# Codigo rodando o jogo
loop_jogo()
print('Fim de jogo.')
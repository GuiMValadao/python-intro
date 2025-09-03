#------------------------------------------------------------
# Divida o jogo de adivinhaçao de numeros em funçoes menores.
#------------------------------------------------------------
import random

# Funçao para iniciar/reiniciar o jogo
def replay(jogo):
    if jogo == 's':
        jogo = True
        return jogo
    else:
        jogo = False
        return jogo

# Funçao para iniciar/reiniciar o jogo
def inicio(i=0):
    if i == 0:
        i += 1
        print('Bem-vindo ao jogo de adivinhação de números!')
        jogo = input('Quer jogar? (s/n)')
        comecar = replay(jogo)
        return comecar, i
    else:
        i += 1
        jogo = input('Quer jogar novamente? (s/n)')
        comecar = replay(jogo)
        return comecar, i

# Funçao para obter input do usuario
def tentativa(resposta):
    adivinhacao = int(input('Dê seu palpite entre 1 e 20: '))
    # Para roubar, obtendo a resposta sem perder uma chance
    if adivinhacao == -1:
        adivinhacao = cheat(adivinhacao, resposta)
    return adivinhacao

# Funçao que define o cheat
def cheat(teste, resposta):
    if teste == -1:
        print('o numero correto e ', resposta)
        adivinhacao = int(input('Dê seu palpite entre 1 e 20: '))
        return adivinhacao

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
    jogo = inicio()[0]
    while jogo == True:

        resposta = random.randint(1, 20)
        chances = 4

        # Permite ao usuario tentar novamente ate ficar sem chances
        while chances > 0:
            guess = int(tentativa(resposta))

            # Verifica se o jogador adivinhou corretamente.
            if vitoria(resposta, chances, guess) == False:
                chances = errado(chances, guess, resposta)
            else:
                break
        jogo = inicio(1)[0]

# Codigo rodando o jogo
loop_jogo()
print('Fim de jogo.')
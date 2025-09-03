#-----------------------------------------------------
# PSEUDOCODIGO
# Iniciar um loop para permitir jogar novamente
    # Gerar numeros aleatorios para serem adivinhados
    # Iniciar loop do jogo:
    # Pedir input do usuario para adivinhar o número
    # Permitir que o usuario roube, obtendo a resposta
    # sem perder uma chance ao digitar '-1'.
    # Comparar o input com o número aleatorio gerado
        # Se o input e '-1', retorna a resposta certa para
        # o usuario e pede nova adivinhaçao sem perder uma chance.
        # Se o input e numero gerado forem iguais, usuario venceu
        # Caso contrario, usuario errou.
            # Se chances = 0, usuario perdeu.
            # Se não, comparar se o número adivinhado e menor ou maior e
            # dizer ao usuario
            # Retornar ao início para pedir novo input
            # e diminuir numero de chances em 1.
    # Perguntar se o usuario quer jogar novamente.
    # Se sim ('s')
#---------------------------------------------------------------
# CODIGO
# Importa a biblioteca 'random', que gera numeros em uma sequência pseudo-aleatoria.
import random

jogo = True

# Inicia primeiro um loop que permite novo jogo seguido
# pelo loop para iniciar a adivinhaçao
while jogo == True:
    print('Bem-vindo ao jogo de adivinhação de números!')
    resposta = random.randint(1, 20)
    chances = 4

    while chances > 0:
        adivinhacao = int(input('Dê seu palpite entre 1 e 20: '))
        # Para roubar, obtendo a resposta sem perder uma chance
        if adivinhacao == -1:
            print('o numero correto e ', resposta)
        # Verifica se o jogador adivinhou corretamente.
        elif adivinhacao == resposta:
            print('Parabéns! Você acertou!')
            print('Você precisou de', 5 - chances,
                  'tentativas para vencer!')
            break
        # Se o usuario errou a adivinhaçao, remove uma chance
        # e se chances = 0, informa que o usuario perdeu e a
        # resposta correta:
        else:
            chances -= 1
            if chances == 0:
                print('Que pena, você perdeu... ')
                print('O número correto era ', resposta)
                break
            elif ((adivinhacao == resposta - 1) or
                  (adivinhacao == resposta + 1)):
                print('Errado. Sua adivinhação passou perto.')
            elif adivinhacao < resposta:
                print('Errado. Tente um número maior.')
            else:
                print('Errado. Tente um número menor.')

    # Pergunta se o usuario que jogar novamente.
    # Se retornar 's', recomeça o jogo, caso contratio termina.
    jogo = input('Quer jogar novamente?(s/n) ')
    if jogo == 's':
        jogo = True
    else:
        jogo  = False

print('Fim de jogo.')

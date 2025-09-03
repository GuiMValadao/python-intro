# Loop while
#contagem = 0
#print('Começando')
#while contagem < 10:
#    print(contagem, ' ', end='')    # Parte do loop while. end='' faz com que o proximo valor continue na mesma linha
#    contagem += 1                   # Tambem parte do loop
#print()     # nao e parte do loop
#print('Pronto')

#print('Exibe valores dentro de um alcance')     # Faz o mesmo que o codigo acima, mas usando o loop 'for', e a funçao 'range()'
#for i in range(0, 10):
#    print(i, ' ', end='')
#print()
#print('Pronto')

#print('Exibe valores dentro de um alcance aumentando de 2 em 2')
#for i in range(0, 10, 2):
#    print(i, ' ', end='')
#print()
#print('Pronto')

#for _ in range(0,10):       # Usando uma variavel anonima '_'. Quando nao importa a contagem de loops, apenas que ocorram.
#    print('.', end='')
#print()

#------------------------------------------------------
#Declaraçao para quebrar um loop (break)
#print('Apenas exiba o codigo se todas as iteraçoes forem completadas')
#num = int(input('Entre o numero a ser procurado: '))
#for i in range(0, 6):
#    if i == num:
#        break
#    print(i, ' ', end='')
#print('Pronto')

#for i in range(0, 10):
#    print(i, ' ', end='')
#    if i % 2 == 1:
#        continue
#    print('hey its an even number')
#    print('we love even numbers')
#print('Done')
#-------------------------------------
# 'For' loop com 'else'
# Apenas imprima o codigo se todas as iteraçoes forem completadas.
# print('Apenas imprima o codigo se todas as iteraçoes forem completadas')
# num = int(input('Entre o numero a ser procurado: '))
#for i in range(0,6):
#    if i == num:
#        break
#    print(i, ' ', end='')
#else:
#    print()
#    print('Todas as iteraçoes foram processadas')
#-----------------------------------------------------
# Jogo de dados
#import random       #importa o modulo random
#MIN = 1
#MAX = 6
#roll_again = 'y'
#while roll_again == 'y':
#    print('Lançando os dados...')
#    print('Os valores sao:')
#    dado1 = random.randint(MIN, MAX)
#    print(dado1)
#    dado2 = random.randint(MIN, MAX)
#    print(dado2)
#    roll_again = input('Jogar os dados novamente? (y/n): ')


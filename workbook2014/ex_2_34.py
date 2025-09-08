#-------------------------------------------
# Par ou impar
#-------------------------------------------
#
def get_int():
    num = input('Digite um numero inteiro: ')
    while not num.isnumeric():
        print('Valor digitado nao reconhecido. '
              'Digite um  numero inteiro: ')
        num = input('Digite um numero inteiro: ')
    return num

def checagem(valor):
    if int(valor) % 2 == 0:
        return 'par'
    else:
        return 'impar'

entrada = get_int()
verificacao = checagem(entrada)
print('O numero e', verificacao)

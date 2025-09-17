#--------------------------------------
# Média
#--------------------------------------

# Inicia a lista e a variável de entrada com um valor temporário.
lista = []
entrada = 1

# Loop que obtém valores do usuário e adiciona na lista.
while entrada != 0:
    entrada = float(input('Insira um valor para calcular a média:'))
    if entrada != 0:
        lista.append(entrada)

# Calcula e exibe a média usando a soma dos valores
# e o comprimento total da lista.
media = sum(lista)/len(lista)
print('-'*30)
# Exibe a média com duas casas decimais.
print(f'O valor médio é {media:.2f}')
print('-'*30)
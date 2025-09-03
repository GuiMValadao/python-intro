#----------------------------------------
# Soma dos primeiros n inteiros positivos
#----------------------------------------

# Insere o número final da soma
n = int(input('Insira um número inteiro positivo: '))

#  Calcula a soma
soma = int(n*(n+1)/2)

# Exibe o resultado
print('A soma de 1 até {} é {}'.format(n, soma))
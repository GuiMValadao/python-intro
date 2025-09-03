#---------------------------
# Depósitos de garrafas
#---------------------------

# Pergunta o número de garrafas para o usuário
garrafa = [float(input('Quantas garrafas de 1 litro ou menos você tem?')),
           float(input('Quantas garrafas de mais de 1 litro você tem?'))]
price = [0.10, 0.25]

# Calcula o preço de retorno
retorno = garrafa[0]*price[0] + garrafa[1]*price[1]

# Exibe o resultado.2 casas decimais. %.2f. faz com que retorno tenha
# apenas 2 casas decimais
print('O retorno será de R$ %.2f.'%retorno)
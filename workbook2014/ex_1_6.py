#------------------------------
# Imposto e gorjeta
#------------------------------

# Aqui deve ser inserido o preço da refeição e o programa calcula
# o imposto e gorjeta
preco = float(input('Preço da refeição: R$ '))
imposto = 0.10 * preco
gorjeta = 0.18 * preco

# Exibe o resultado
print('O imposto é de R$ %.2f, a gorjeta é de R$ %.2f e o Total é R$ %.2f'\
      %(imposto, gorjeta, preco + imposto + gorjeta))
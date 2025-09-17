#-------------------------------------
# Tabela de desconto
#-------------------------------------

# Tabela de preços e valor do desconto
precos = [4.95, 9.95, 14.95, 
          19.95, 24.95]
desconto = 0.6
print('Preço original | ' \
'Valor do desconto | Preço com desconto')
for item in range(0, len(precos)):
    print(f'{precos[item]:.2f}', ' '*15, 
          f'{precos[item]*desconto:.2f}', ' '*15,\
          f'{(precos[item]*(1-desconto)):.2f}')
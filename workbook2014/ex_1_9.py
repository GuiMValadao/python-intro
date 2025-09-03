#-----------------------------------------
# Juros compostos
#-----------------------------------------

# Inserir a quantidade inicial de dinheiro
grana = float(input('Insira o aporte inicial: '))

# Calcular e exibir o valor apos 1, 2 e 3 anos
grana = grana + 0.04 * grana
print('O valor na conta apos 1 ano e de R$ %.2f'%grana)
grana = grana + 0.04 * grana
print('O valor na conta apos 2 anos e de R$ %.2f'%grana)
grana = grana + 0.04 * grana
print('O valor na conta apos 3 anos e de R$ %.2f'%grana)

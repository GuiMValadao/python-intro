#--------------------------------------------
# Dispositivos e engenhocas
#--------------------------------------------

# Define o peso em gramas de cada tipo
peso_dispo = 75
peso_engen = 112

# Pergunta ao usuario a quantidade de cada tipo
quant_dispo = int(input('Qual o número de dispositivos? '))
quant_engen = int(input('Qual o número de engenhocas? '))

# Calcula o peso total e imprime a resposta
peso = peso_dispo * quant_dispo + peso_engen * quant_engen
print('O peso total da encomenda é', peso, 'gramas.')
valores = (input("Digite os valores para calcular a média: ")).split(" ")
i = 0
print(valores)
for valor in valores:
    valores[i] = float(valor)
    i += 1
valores_total = sum(valores)
media = valores_total / len(valores)
print(media)

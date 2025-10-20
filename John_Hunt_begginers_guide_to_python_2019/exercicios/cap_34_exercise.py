import collections as c

frase = input("Digite uma frase: ")
frase
contar_palavras = c.Counter(frase.split(" "))
print("Contador desordenado: \n", contar_palavras)
lista = sorted(contar_palavras.most_common())
palavras_ordenadas = c.OrderedDict(lista)
print("Contador ordenado: \n", palavras_ordenadas)

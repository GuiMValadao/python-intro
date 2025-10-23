# Capítulo 36 - Map, Filter, Reduce
#
# Python possui três funções que são amplamente utilizadas para implementar
# soluções no estilo de programação funcional em combinação com tipo
# de coleção containeres.
# Estas funções são conhecidas como funções de alta ordem que recebem
# uma coleção e uma função que serão aplicadas de várias formas àquela
# coleção. Este capítulo introduz três funções: map(), filter(), reduce().
# -----------------------------------------------
# Filter
# A função filter() é uma função de alta ordem que recebe uma função a ser
# usada para filtrar elementos de uma coleção. O resultado da função
# filter() é um novo iterável contendo aqueles elementos selecionados
# pela função teste. Isto é, a função passada para filter() é usada para
# testar todos os elementos na coleção que também é passada para filtrar.
# Aqueles cuja filtragem retorna True são incluídos na lista de valores
# retornados. O resultado retornado é um novo iterável consistindo de
# todos os elementos desta lista que satisfaz a função teste dada. A ordem
# dos elementos é preservada.
# A sintaxe é:
# filter(function, iterable)
# O segundo argumento é qualquer coisa que implemente o protocolo iterável,
# incluindo listas, tuplas, conjuntos, dicionários e muitos outros tipos.
# A função passada como primeiro argumento é a função teste; ela pode ser
# uma função lambda ou o nome de uma função existente.
# Aqui estão alguns exemplos da utilização de filter com uma lista de
# inteiros simples:
data = [1, 3, 5, 2, 7, 4, 10]
print("data:", data)
# d1 = list(filter(lambda i: i % 2 == 0, data))
# print("d1:", d1)


# def is_even(i):
#     return i % 2 == 0


# d2 = list(filter(is_even, data))
# print("d2:", d2)

# Isso retorna como resultado:
# data: [1, 3, 5, 2, 7, 4, 10]
# d1: [2, 4, 10]
# d2: [2, 4, 10]
# ---------------------------------------
# Map
# Map() é outra função de alta ordem disponível em Python. Ela aplica
# a função fornecida a todos os items no iterável passado a ela e retorna
# um novo iterável dos resultados gerados pela função aplicada.
# É um equivalente funcional de um loop for aplicado a um iterável onde os
# resultados de cada iteração do loop for são agrupados.
# A função map é amplamente usada no mundo da programação funcional.
# A sintaxe é:
# map(function, iterável, ...)
# O segundo argumento da função map é qualquer coisa que implementa o protocolo
# iterável.

# d1 = list(map(lambda i: i + 1, data))
# print("d1:", d1)


# def add_one(i):
#     return i + 1


# d2 = list(map(add_one, data))
# print("d2:", d2)

# Que retorna:
# data: [1, 3, 5, 2, 7, 4, 10]
# d1: [2, 4, 6, 3, 8, 5, 11]
# d2: [2, 4, 6, 3, 8, 5, 11]

# Mais de um iterável pode ser passado para a função map. Se múltiplos
# iteráveis são passados, então a função passada deve pegar tantos
# parâmetros quantos iteráveis presentes. Este recurso é útil se quiser
# fundir dados armazenados em duas ou mais coleções em uma única coleção.
# Por exemplo:
data1 = [1, 3, 7, 19]
data2 = [2, 4, 6, 8]
result = list(map(lambda x, y: x + y, data1, data2))
print(result)
# Que resulta em:
# [3, 7, 13, 27]
# --------------------------------------------------
# Reduce
# A função reduce() é a última função de alta ordem que pode ser usada com
# coleções que vamos olhar. Ela aplica uma função a um iterável e combina
# o resultado retornado para cada elemento em um único resultado. Esta
# função foi parte do coração da linguagem Python 2 mas não foi incluída no
# cerne de Python 3 pois sua aplicação é bem limitada. No entanto, onde
# ela é útil, é muito útil.
# Para usar reduce() em Python 3 é necessário importar o módulo functools.
# Um ponto que é às vezes incompreendido com reduce() é que a função passada
# a ela pega dois parâmetros, que são o resultado anterior e o próximo valor
# na sequência; então retorna o resultado de aplicar alguma operação a estes
# parâmetros.
# A sintaxe é:
# functools.reduce(função, iterável[, inicializador])~
# Note que opcionalmente você pode fornecer um inicializados que é usado
# para fornecer um valor inicial para o resultado. Um uso óbvio de reduce()
# é somar todos os valores de uma lista:
from functools import reduce

result = reduce(lambda total, value: total + value, data)
print(result)

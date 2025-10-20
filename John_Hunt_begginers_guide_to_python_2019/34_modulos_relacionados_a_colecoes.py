# Capítulo 34 - Módulos relacionados a coleções
# List comprehension é um mecanismo que pode ser usado para criar listas:
# [ <expressão> for item in iteravel <if condicao_opcional> ]

# A nova lista é formada dos resultados da expressão.
# Quando um list comprehension é executado, ele gera uma nova lista aplicando
# a expressão aos items de outra coleção.
# Qualquer coleção iterável pode ser usada para criar comprehension, como
# tuplas ou conjuntos. Outro recurso do list comprehension é filtrar
# valores passados à expressão usando o condicional opcional if.
# ---------------------------------------------
# O módulo Collections
# Este módulo estende recursos básicos dos tipos de dados orientados a coleção
# dentro de Python com tipos container de alto desempenho. Ele fornece muitos
# armazenadores úteis, como:

# Name              Purpose
#
# namedtuple()      Factory function for creating tuple subclasses with named fields
# deque             List-like container with fast appends and pops on either end
# ChainMap          Dict-like class for creating a single view of multiple mappings
# Counter           Dict subclass for counting hashable objects
# OrderedDict       Dict subclass that remembers the order entries were added
# Defaultdict       Dict subclass that calls a factory function to supply missing values
# UserDict          Wrapper around dictionary objects for easier dict subclassing
# UserList          Wrapper around list objects for easier list subclassing
# UserString        Wrapper around string objects for easier string subclassing

# Como exemplo, vamos usar o tipo Counter para contar eficientemente múltiplas
# cópias do mesmo elemento. Ele é eficiente pois apenas armazena uma cópia
# de cada elemento, mas mantém uma contagem do número de vezes que um elemento
# foi adicionado à coleção:
import collections

fruit = collections.Counter(
    [
        "maçã",
        "laranja",
        "pêra",
        "kiwi",
        "pêssego",
        "melancia",
        "manga",
        "maçã",
        "pêssego",
        "maçã",
        "laranja",
    ]
)
# print(fruit)
# print(fruit["maçã"])
# print(fruit["laranja"])

# Que tem a saída:
# Counter({'maçã': 3, 'laranja': 2, 'pêssego': 2, 'pêra': 1, 'kiwi': 1, 'melancia': 1, 'manga': 1})
# 3
# 2
# Pode ser usada, por exemplo, para descobrir o elemento com maior contagens.
# Isto é feito usando o método most_common. Ele pega um parâmetro que indica
# quantos dos elementos mais comuns devem ser retornados. Se esse valor é
# omitido (ou None), então retorna uma lista ordenada dos elementos.:
# print("fruit.most_common(1):", fruit.most_common(1))
# Que gera:
# fruit.most_common(1): [('maçã', 3)]
# Também pode-se realizar operações matemáticas com múltiplos objetos
# Counter. Por exemplo, pode-se somar e subtrair, obter uma combinação
# de contadores que combinam os valores máximos de dois objetos Counter,
# gerar uma interseção de dois Counters. Também pode-se acrescentar items
# a um Counter acessando o valor usando o item como chave:
fruit["morango"] = +1
# ------------------------------------------------
# Módulo Itertools
# Fornece um número de funções úteis que retornam iteradores construídos
# de diversas formas. Alguns exemplos são:
import itertools

# Connect two iterators together
r1 = list(itertools.chain([1, 2, 3], [2, 3, 4]))
print(r1)
# Create iterator with element repeated specified number of
# times (possibly infinite)
r2 = list(itertools.repeat("hello", 5))
print(r2)
# Create iterator with elements from first iterator starting
# where predicate function fails
values = [1, 3, 5, 7, 9, 3, 1]
r3 = list(itertools.dropwhile(lambda x: x < 5, values))
print(r3)
# Create iterator with elements from supplied iterator between
# the two indexes (use ‘None’ for second index to go to end)
r4 = list(itertools.islice(values, 3, 6))
print(r4)

# Que devolvem:
# [1, 2, 3, 2, 3, 4]
# ['hello', 'hello', 'hello', 'hello', 'hello']
# [5, 7, 9, 3, 1]
# [7, 9, 3]

# Capítulo 32 - Conjuntos
# Um conjunto é uma coleção desordenada e não-indexada de tipos qu não permite
# duplicatas.
# É definido usando chaves {}, por exemplo:
cesta = {'maçã', 'laranja', 'maçã', 'pêra',
         'laranja', 'banana'}
#print(cesta)
# Que tem a saída:
#{'maçã', 'pêra', 'banana', 'laranja'}
# Ou seja, os items duplicados na definição foram removidos. Além disso, não 
# tem uma ordem de exibição. Ao executar o print() novamente:
#{'pêra', 'maçã', 'banana', 'laranja'}
# A função construtora Set()
# Assim como com tuplas e listas, Python fornece uma função predefinida que 
# pode converter qualquer tipo iterável em um conjunto. Ela é:
#set(iterável)
dici = {'1':1, '2':2, '3':3}
set1 = set(dici)
#print(set1)
# Que resulta em {'1', '2', '3'}.
# Por serem desordenados, não se pode referir a 1 item específico em conjunto.
# No entanto, este tipo também é iterável. Portanto, pode-se usá-lo em laços
# for, como em:
#for fruta in cesta:
#    print(fruta)
# Que retorna:
#pêra
#banana
#maçã
#laranja
# Pode-se adicionar items a um conjunto com o método add():
cesta.add('ameixa')
# print(cesta)
# Não é possível alterar items já presentes em um conjunto.
# Pode-se remover um item com as funções remove() ou discard():
#cesta.remove('maçã')
#print(cesta)
#cesta.discard('caqui')
#print(cesta)
# pop() também remove um item do conjunto e o retorna como resultado da
# execução do método, mas como o conjunto é desordenado não se pode saber
# qual item será removido antes de usá-lo.
# Pode-se guardar qualquer item imutável dentro de um conjunto(tuplas, 
# strings, etc), mas não listas ou outros conjuntos. No entanto, frozensets,
# que são idênticos a conjuntos, mas imutáveis, podem ser aninhados em 
# conjuntos.
# O container conjunto também suporta operações como as de conjuntos(set like)
# como união (|), interseção (&), diferença(-) e diferença simétrica(^). 
# Todos eles são baseados na teoria de conjuntos simples.
# Method Description
# add()                 Adds an element to the set
# clear()               Removes all the elements from the set
# copy()                Returns a copy of the set
# difference()          Returns a set containing the difference between two or more sets
# difference_update()   Removes the items in this set that are also included in another, specified set
# discard()             Remove the specified item
# intersection()        Returns a set, that is the intersection of two other sets
# intersection_update() Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()          Returns whether two sets have a intersection or not
# issubset()            Returns whether another set contains this set or not
# issuperset()          Returns whether this set contains another set or not
# pop()                 Removes an element from the set
# remove()              Removes the specified element
# symmetric_difference() Returns a set with the symmetric differences of two sets
# symmetric_difference_update() inserts the symmetric differences from this set and another
# union()               Return a set containing the union of sets
# update()              Update the set with the union of this set and others
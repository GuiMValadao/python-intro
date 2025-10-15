# Capítulo 31 - Coleções, tuplas e listas
#
# Nos capítulos iniciais vimos alguns tipos embutidos em Python como
# string, int, float e bools. Existem outros tipos em Python, conhecidos
# coletivamente como tipos de coleção. Isto é pois eles representam uma
# coleção de outros tipos (como coleção de strings, ou inteiros).
# Uma coleção é um único objeto representando um grupo de objetos (como
# uma lista ou dicionário). Coleções também podem ser referidas como 
# containers(pois contém outros objetos). Estas classes de coleção são 
# frequentemente usadas como a base para estruturas e tipos de dados
# mais complexos ou específico de aplicações. Estes tipose de coleção 
# suportam diversos tipos de estruturas de dados (como listas e mapas)
# e modos de processar elementos dentro dessas estruturas. Este acpítulo
# introduz os tipos de Coleção em Python.
#------------------------------------------------
# Tipos de Coleção em Python
# Existem 4 tipos de classes em Python que fornecem este comportamento:
#   - Tuplas -  coleção de objetos ordenados e imutáveis. Permite duplicatas
#               e são indexados.
#   - Listas -  coleção de objetos ordenados e mutáveis, indexados e permite 
#               duplicatas.
#   - Conjuntos-coleção desordenada e não-indexada. São mutáveis mas não 
#               permitem duplicatas.
#   - Dicionário-Coleção desordenada indexada por chave(key) e valor(value).
#               Chaves duplicadas não são permitidas, mas valores duplicados
#               são. São containeres mutáveis.
#--------------------------------------------------
# Tuplas
# São definidas usando parênteses () em torno dos elementos que a compõe.
tup1 = (1, 3, 5, 7)
# São indexadas iniciando em 0
# A função tuple() também pode ser usada para criar uma nova tupla
# de um iterável. Isto significa que uma tupla pode ser criada de um conjunto,
# lista, dicionário ou qualquer tipo que implemente o protocolo iterável.
# A sintaxe é: tuple(iteravel)
list1 = [1, 2, 3]
t1 = tuple(list1)
#print(t1)
# Cada elemento de uma tupla pode ser acessado usando um índice entre 
# colchetes('[]').
#print('tup1[0]\t:', tup1[0])
#print('tup1[1]\t:', tup1[1])
#print('tup1[2]\t:', tup1[2])
# Também pode-se fazer o fatiamento com uma tupla. Isto cria uma nova tupla
# contendo um subconjunto da tupla inicial.
#print('tup1[1:3]:\t',tup1[1:3])
# Também pode-se reverter uma tupla usando a notação ::-1(retorna uma nova tupla)
#print('tup1[::-1]:\t', tup1[::-1])
# Podem conter tipos diferentes, como string e int.
# Pode-se iterar sobre o conteúdo de uma tupla usando o loop for:
tup3 = ('apple', 'pear', 'orange', 'plum', 'apple')
#for x in tup3:
#    print(x)
# Tuplas suportam diversas funções:
#print('len(tup3):\t', len(tup3)) # Exibe o número total de elementos na tupla.
#print(tup3.count('apple')) # Conta o número de elementos dado para count().
#print(tup3.index('pear')) # retorna o índice do primeiro valor pedido para index() na tupla.
# Note que index() e count() são métodos definidos na classe tupla enquanto
# len() é uma função a qual a tupla é passada. Isto é porque len() é uma função
# genérica e pode ser usada com outros tipos, como strings.
# Pode-se também checar se um elementos específico existe em uma tupla:
#if 'orange' in tup3:
#    print('orange is in the Tuple')
# Tuplas aninhadas:
# Tuplas podem ser aninhadas em outras tuplas, ou listas, dicionários, conjuntos.
tuple1 = (1, 3, 5, 7)
tuple2 = ['John', 'Denise', 'Phoebe', 'Adam']
tuple3 = {1:'A', 2:'B', 3:'C'}
tuple4 = (42, tuple1, tuple2, 5.5, tuple3)
#print(tuple4)
# com a saída:
#(42, (1, 3, 5, 7), ['John', 'Denise', 'Phoebe', 'Adam'], 5.5, {1: 'A', 2: 'B', 3: 'C'})
#-----------------------------------------
# Listas
# Listas suportam todos os recursos das tuplas citados acima, mas como são
# mutáveis também podem-se acrescentar, remover e modificar elementos.
# São criadas usando colchetes []

list1 = ['John', 'Paul', 'George', 'Ringo']
l1 = (1, 43.5, 'Phoebe', 21, True)
l2 = ['apple', 'orange', 31]
root_list = ['John', l1, l2, 'Denise']
#print(root_list)
# função construtora de listas
# Pode-se criar uma lista de um iterável usando list().
# list(iterable)
# Para adicionar um elemento usa-se:
# uma_lista.append(objeto)
# Para adicionar todos os items de uma lista em outra pode-se usar extend().
list1 = ['John', 'Paul', 'George', 'Ringo', 'Pete']
#print(list1)
list1.extend(['Albert', 'Bob'])
#print(list1)
list1 += ['Ginger', 'Sporty']
#print(list1)
# Pode inserir elementos em uma lista existente com insert().
# uma_lista.insert(indica, objeto)
# Duas listas podem ser concatenadas, usando lista1 + lista2.
# Pode-se remover elementos de uma lista com o método remove()..
# uma_lista.remove(objeto)
another_list = ['Gary', 'Mark', 'Robbie', 'Jason', 'Howard']
#print(another_list)
another_list.remove('Robbie')
#print(another_list)
# Método pop():
# lista.pop(index=-1)
# Este método difere de remove() em duas formas:
# - Pega um indice do item para ser removido
# - retorna o item que foi removido como resultado
list6 = ['Once', 'Upon', 'a', 'Time']
#print(list6)
#print(list6.pop(2))
#print(list6)
# Que gera:
#['Once', 'Upon', 'a', 'Time']
#a
#['Once', 'Upon', 'Time']
# Também pode-se usar a palavra chave del para remover elementos de uma lista.
my_list = ['A', 'B', 'C', 'D', 'E']
print(my_list)
del my_list[2]
print(my_list)
my_list = ['A', 'B', 'C', 'D', 'E']
del my_list[1:3]
print(my_list)
# Que resulta em:
#['A', 'B', 'C', 'D', 'E']
#['A', 'B', 'D', 'E']
#['A', 'D', 'E']
# Métodos de listas:
# Method     Description
# append()   Adds an element at the end of the list
# clear()    Removes all the elements from the list
# copy()     Returns a copy of the list
# count()    Returns the number of elements with the specified value
# extend()   Add the elements of a list (or any iterable), to the end of the current list
# index()    Returns the index of the first element with the specified value
# insert()   Adds an element at the specified position
# pop()      Removes the element at the specified position
# remove()   Removes the item with the specified value
# reverse()  Reverses the order of the list
# sort()     Sorts the list
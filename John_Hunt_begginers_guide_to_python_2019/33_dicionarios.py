# Capítulo 33 - Dicionários
# Um dicionário é um conjunto de associações entre uma chave e um valor que é
# desordenado, mutável e indexado. As chaves do dicionário devem ser únicas,
# mas os valores não precisam.
# Dicionários são criados usando chaves {} onde cada entrada é um par 
# chave: valor:
cidades = {'Paraná': 'Irati',
           'Santa Catarina': 'Florianópolis',
           'Rio Grande do Sul': 'Porto Alegre',
           'São Paulo': 'São Paulo'}
#print(cidades)
# Pode ser criado com a função dict() fornecendo um iterável ou uma sequência
# de valores chave:valor:
#dict(**kwarg)
#dict(mapping, **kwarg)
#dict(iterable, **kwarg)
# Esta é uma função sobrecarregada(overload) com três versões que podem pegar
# diferentes tipos de argumentos:
#   - A primeira opção pega uma sequência de pares chave:valor;
#   - A segunda pega um mapeamento e(opcionalmente) uma sequência de chave:valores
#   - A terceira pega um iterável de pares chave:valor e uma sequência opcional de chaves:valor
# Pode-se acessar os valores armazenados em um dicionário usando sua chave
# associada. Isto é especificado ou usando notação colchetes(com a chave
# dentro dos colchetes) ou o método get():
print('cidades[Paraná]:', cidades['Paraná'])
print('cidades.get(Santa Catarina:)', cidades.get('Santa Catarina'))
# Com a saída sendo:
# cidades[Paraná]: Irati
# cidades.get(Santa Catarina:) Florianópolis
# Pode-se adicionar uma nova entrada fornecendo a chave entre colchetes e
# o novo valor a ser atribuído para aquela chave:
cidades['Minas Gerais'] = 'Belo Horizonte'
# O valor associado com uma chave pode ser mudado reatribuindo um novo valor
# com a notação de colchetes:
cidades['Paraná'] = 'Curitiba'
# Uma entrada no dicionário pode ser removida usando um dos métodos pop()
# ou popitem() ou a palavra chave del;
#   -   O método pop(<chave>) remove a entrada com a chave especificada.
#       Este método retorna o valor da chave sendo apagada. Se a chave não
#       está presente, então um valor padrão (se foi definido usando 
#       setdefault()) será retornado. Se o padrão não tiver sido definido,
#       um erro será gerado.
#   -   O método popitem() remove o último item inserido no dicionário.
#       (Mas antes de Python 3.7 um item aleatório no dicionário era deletado!)
#       O par chava:valor é retornado do método.
#   -   A palavra chave del remove a entrada com a chave especificada do
#       dicionário. Ela só apaga o item, não retorna o valor. É, potencialmente,
#       mais eficiente que pop(<chave>).
#   -   clear() esvazia o dicionário de todas as entradas.
# Pode-se fazer loops por um dicionário usando o loop for. Ele processa cada
# uma das chaves do dicionário em sequência. Isto pode ser usado para acessar
# cada um dos valores associados com as chaves, por exemplo.
# Se quiser iterar sobre todos os valores diretamente, você pode fazê-lo
# usando o método values(). Ele retorna uma coleção de todos os valores,
# que podem então ser iterados.
#for e in cidades.values():
#    print()
# Valores, chaves e items
# Há três métodos que lhe permitem obter uma visualização dos conteúdos de um
# dicionário, sendo eles values(), keys(), e items(). Os dois primeiros
# são auto-explicativos, e items() retorna uma visualização dos items
# no dicionário (pares (chave,valor)).
# Uma visualização fornece uma janela dinâmica nas entradas do dicionário, 
# que significa que quando o dicionário muda, a visualização reflete esta
# mudança.
# Pode-se checar se uma chave é um membro de um dicionário usando a sintaxe
# in, por exemplo:
print(cidades)
print('São Paulo' in cidades)
print('Rio Grande do Sul' not in cidades)
# Dicionários podem ser aninhados. Em um dicionário, a chave e o valor devem
# ser um objeto; mas, em Python, tudo é um objeto e, portanto, pode ser usado
# como chave ou valor.
# Uma classe cujos objetos serão usados como chave dentro de um dicionário
# deveria considerar implementar dois métodos especiais, sendo eles
# __hash__() e __eq__(). O método hash é usado para gerar um número que pode
# ser usado pelo dicionário e o método igual é usado para testar se dois 
# objetos são iguais. Por exemplo:
# Python tem duas regras associadas a estes métodos:
#   * Se dois objetos são iguais, então seus números hash devem ser iguais.
#   * Para um objeto ser numerado(hashable), ele deve ser imutável;
# Também tem duas propriedades associadas com códigos hash de um objeto
# que deveriam ser aderidas:
#   * Se dois objetos tem o mesmo número hash, então eles são, provavelmente
#       o mesmo objeto.
#   * O número hash de um objeto deveria ser barato de computar.
# Para tipos embutidos em Python, não precisa se preocupar com isso, mas
# para classes e tipos definidos pelo usuário para serem chaves dentro de um
# dicionário então deve-se considerar implementar esses métodos. Isto é 
# porque um dicionário usa:
#   * O método 'hashing' para gerenciar como valores são organizados;
#   * O método 'igual a' para checar se uma chave já está presente no dicionário.
# Se quiser criar uma classe que não possa ser usada como chave em um dicionário,
# ou seja, não pode receber um número hash, pode definir isso definindo o método
# __hash__() como None:
# class NotHashableThing(object):
#     __hash__ = None
# Method Description
# clear()       Removes all the elements from the dictionary
# copy()        Returns a copy of the dictionary
# fromkeys()    Returns a dictionary with the specified keys and values
# get()         Returns the value of the specified key
# items()       Returns a list containing the tuple for each key value pair
# keys()        Returns a list containing the dictionary’s keys
# pop()         Removes the element with the specified key
# popitem()     Removes the last inserted key-value pair
# setdefault()  Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()      Updates the dictionary with the specified key-value pairs
# values()      Returns a list of all the values in the dictionary

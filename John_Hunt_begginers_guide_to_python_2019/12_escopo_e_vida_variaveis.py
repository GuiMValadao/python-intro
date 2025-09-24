# Escopo e tempo de vida de variaveis
# Nos exemplos anteriores foram definidas diversas variaveis, a maioria sendo chamadas variaveis 'globais'.
# Isto e, elas sao, potencialmente, acessiveis em qualquer lugar nos programas. Agora vamos olhar variaveis
# 'locais' como definidas dentro de uma funçao, variaveis globais e como elas podem ser referenciadas dentro de uma
# funçao e finalmente vamos considerar variaveis 'nao-locais'.
#-----------------------------------------------------------------
# Variaveis locais
# Na pratica, desenvolvedores tentam limitar o numero de variaveis globais em seus programas
# pois elas podem ser acessadas em qualquer lugar e podem ser modificadas em qualquer lugar,
# podendo resultar em comportamentos inesperados.
# Entretanto, nem todas as variaveis sao globais. Quando definimos uma funçao, podemos criar
# variaveis qujo alcance e apenas para aquela funçao e nao sao acessiveis ou visiveis
# fora da funçao. Essas variaveis sao referidas como variaveis locais.
#def my_function():
#    a_variable = 100
#    print(a_variable)

#my_function()          # ao executar a funçao, exibe o valor da variavel.

#print(a_variable)      # Se pedirmos para exibiir o valor da variavel fora da funçao, retorna erro.

#a_variable = 25         # Se a variavel e definida globalmente e em uma funçao, existem duas versoes
#my_function()           # completamente distintas e Python nao se confunde entre elas. Seria o mesmo
#print(a_variable)       # que dar-lhes nomes diferentes.
#-------------------------------------------------------------
# Palavra chave 'global'
#max = 100
#def print_max():
#    max = max+1             # Se a variavel global e definida e chamada dentro da funçao nao ha problema,
#    print(max)              # mas se a funçao tenta modificar a variavel, Python vai retornar um erro.
#print_max()
#
#max = 100
#def print_max():
#    global max          # Para poder modificar a variavel global dentro de uma funçao devemos usar a palavra chave
#    max = max+1         # 'global' junto com o nome da variavel. Isto permite que a funçao modifique o valor
#    print(max)          # de uma variavel global.
#print_max()
#print(max)
#-----------------------------------------------------------
# Variaveis nao-locais
# E possivel definir funçoes entro de outras funçoes. No entanto, nao se pode modificar
# variaveis da funçao parente na funçao 'filha', similar a funçao global em uma funçao.
# Alem disso, nao se pode usar a palavra-chave 'global' por a variavel e local.
#def outer():
#    title = 'original title'
#    def inner():
#        title = 'another title'
#        print('inner:', title)
#    inner()
#    print('outer:', title)
#outer()
# Ambas modificam a variavel 'title', mas ela nao e a mesma para ambas as funçoes; ambas tem sua versao da variavel 'title'.
# Para que a funçao interna 'inner()' modifique a variavel 'title', deve-se usar a palacra-chave 'nonlocal' na funçao 'inner()'.
# Fazendo isso, 'title' vai ser alterada para ambas as funçoes.
#def outer():
#    title = 'original title'
#    def inner():
#        nonlocal title
#        title = 'another title'
#        print('inner:', title)
#    inner()
#    print('outer:', title)
#outer()
#---------------------------------------------------
# Dicas
# Pontos a se notar sobre o alcance e tempo de vida das variaveis:
# 1 -   O alcance de uma variavel e parte de um programa onde a variavel e conhecida. Parametros e vvariaveis definidas
#       dentro de uma funçao nao sao visiveis fora dela. Logo, elas tem um alcance local.
# 2 -   O tempo de vida de uma variavel e o periodo pelo qual a variavel existe na memoria do programa Python.
#       O tempo de vida de variaveis dentro de uma funçao e tao longo quanto a funçao e executada. Estas variaveis locais sao destruidas
#       assim que a funçao retorna ou termina. Isto quer dizer que a funçao nao armazena os valores em uma variavel de uma chamada para outra.


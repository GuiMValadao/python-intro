# Funçoes de alta ordem
# Sao funçoes que pegam como um parametro, ou retorno (ou ambos), uma funçao.
#   * Funçoes podem ser vistas como blocos de codigo nomeados
#   * Sao definidas usando a palavra chave 'def' e sao compostas por cabeçalho e corpo
#   * Funçoes sao invocadas ou executadas usando seu nome seguido por parenteses
#     com ou sem parametros dependendo de sua definiçao.
#def get_msg():
#    return 'Hello Python World!'
#message = get_msg()
#print(message)
#print(type(get_msg))
#-------------------------------------------
# Funçoes como objetos
# Se '()' nao sao incluidos a funçao refere a si mesma em vez de ser executada.
# O valor que ela retorna e o nome da funçao e a localizaçao em hexadecimais
# na memoria.
# Assim como '1' e inteiro, 'John' e string e '42.6' e float, 'get_msg' e funçao.
#   ####################################
#   ??  Se um programa tiver muitas funçoes ele poderia ocupar espaço demais
#       na memoria?
#   ####################################
# Tambem pode-se usar variaveis para 'clonar' uma funçao
#another_reference = get_msg
#print(another_reference())
# Onde 'another_reference' agora faz o mesmo que a funçao 'get_msg'.
#
#def get_some_other_msg():
#    return 'Some other message!!!'
#get_msg = get_some_other_msg
#print(get_msg())
# Nomes de funçoes tambem podem ser usados como variaveis para referenciar
# outra funçao. Neste caso, get_msg executa a funçao 'get_some_other_msg'
# e a funçao get_msg ficou salva na variavel 'another_reference'.
#----------------------------------------------
# Conceitos de funçoes de alta ordem
# Assim como podemos atribuir uma referencia a uma funçao a uma variavel,
# tambem podemos atribuir uma referencia a uma  funçao como argumento
# para outra funçao, ou seja, uma funçao pode usar outra como parametro.
# Tais funçoes sao conhecidas como Funçoes de Alta-Ordem.
# Em Python, Funçoes de Alta-Ordem podem fazer pelo menos uma das duas coisas:
#   - Tomar uma ou mais funçoes como parametro.
#   - REtornar como resultado uma funçao.
# Todas as outras funçoes sao 'Funçoes de Primeira-Ordem'.
#---------------------------------------------
# Exemplo de funçao de alta ordem
# Exemplo abstrato, em pseudo-code
#def apply(x, function):
#    result = function(x)
#    return result
# E uma funçao de alta ordem pois depende da funçao passada para ela, 'function'.
#def mult(y):
#    return y*10.0
#print(apply(5,mult))
#---------------------------------------------
# Funçoes de alta ordem em Python

#def mult_by_two(num):
#    return num * 2
#def mult_by_five(num):
#    return num * 5
#def square(num):
#    return num * num
#def add_one(num):
#    return num + 1
#def apply(num, func):
#    return func(num)
#result = apply(10, mult_by_two)
#print(result)
#print(apply(10, mult_by_five))
#print(apply(10, square))
#print(apply(10, add_one))
#print(apply(10, mult_by_two))
#-------------------------------------------
# Usando funçoes de alta ordem
# A importancia de funçoes de alta ordem e observada
# quando sabemos que uma funçao devera ser fornecida como parametro,
# mas nao sabemos qual. A funçao sera providenciada em algum ponto
# no futuro. Assim, e criado um bloco de codigo que sera capaz
# de aplicar a funçao apropriada quando ela for conhecida.
# Por exemplo, se quisermos calcular a quantidade de omposto
# alguem deve pagar baseado em seu salario. No entanto, nao
# savemos como calcular o imposto pois e dependente de fatores
# externos. A funçao 'calculate_tax' poderia pegar uma funçao apropriada
# que performa o calculo e fornece o valor de imposto apropriado.
# As seguintes linhas de codigo aplicam essa abordagem.
#import math
#def simple_tax_calculator(amount):
#    return math.ceil(amount * 0.3)     # Funçao importada da biblioteca math.
#def calculate_tax(salary, func):
#    return func(salary)
#print(calculate_tax(45000.0, simple_tax_calculator))
#--------------------------------------------------
# Funçoes retornando funçoes
#
#def make_checker(s):
#    if s == 'even':
#        return lambda n: n%2 == 0
#    elif s == 'positive':
#        return lambda n: n >= 0
#    elif s == 'negative':
#        return lambda n: n < 0
#    else:
#        raise ValueError('Unknown request')
#f1 = make_checker('even')
#f2 = make_checker('positive')
#f3 = make_checker('negative')
#print(f1(3))
#print(f2(3))
#print(f3(3))
# A funçao 'make_checker' e uma fabrica de funçoes que podem ser criadas
# para realizar operaçoes especificas, no caso acima como checar
# se um valor e par, positivo ou negativo.
# Capítulo 29 - Decoradores
# A ideia por trás de Decoradores vem do livro de Design de padrões
# 'Gang of Four'. Neste livro, diversos objetos recorrentes da padrões
# de design orientados a objetos são apresentados. Um desses padrões
# de design é o padrão de design Decorator.
# O Decorator adressa a situação onde é necessário acrescentar comportamentos
# adicionais a objetos específicos. Um jeito de adicionar tal comportamento
# é decorar objetos criados com tipos que fornecem a funcionalidade extra.
# Estes decoradores cercam o elemento original mas apresentam exatamente
# a mesma interface para o usuário do elemento. Assim, o padrão de design
# Decorator extende o comportamento de um objeto sem usar subclasses.
# Esta decoração de um objeto é transparente para os clientes dos decoradores.
# Em Python, Decorators são funções que pegam outra função (ou outro objeto 
# chamável como um método) e retornam uma terceira função representando 
# o comportamento decorado. 
# -------------------------------------------
# O que são decoradores?
# Um Decorador é um pedaço de código, que é usado para marcar um objeto
# chamável (como uma função, método, classe ou objeto) tipicamente
# para melhorar ou modificar seu comportamento (potencialmente substituir.
# Assim, ele 'decora' o comportamento original.
# Decoradores são, de fato, objetos chamáveis também, e assim se comportam 
# como macros em outras linguagens que podem ser aplicados a objetos
# chamáveis que, então, retornam um novo objeto chamável (tipicamente
# uma nova função). A ideia básica é ilustrada no diagrama:
#  
#                       /------------------------------------------\
#                      |  decorador         /------------------\    |
#              -------------          -------------             |   |   
#             |  Interface  |        |  Interface  |    Função  |   |
#             |      da     |------- |      da     |  cercada   |   |
#             |    Função   |        |    Função   |            |   |
#              -------------          --------------            |   |
#                      |                    \------------------/    |               
#                       \------------------------------------------/
#
# Este diagrama ilustra um decorador cercando um objeto chamável,
# neste caso uma função. Note que o decorador apresenta exatamente a
# mesma interface que a função original apresentaria ao usuário, ou
# seja, pega os mesmos parâmetros e, ou retorna nada (None) ou algo.
# Deveria ser notado que o decorador também tem a liberdade de substituir
# completamente um objeto chamável em vez de apenar cercá-lo. É uma 
# decisão de design feita pelo implementador do decorador.
#------------------------------------------------
# Definindo um decorador
# Para definir um decorador, precisa, primeiro, definir um objeto
# chamável, como uma função que pega outra função como um parâmetro
# e retorna uma nova função. Um exemplo de definição de uma função
# de recordação (logger) bem simples é dado abaixo:
def logger(func):
    def inner():
        print('calling', func.__name__)
        func()
        print('called', func.__name__)
    return inner
# Neste caso, o decorador logger cerca a função original dentro de 
# uma nova função, chamada inner. Quando esta função é executada, uma 
# declaração é registrada antes e depois da função original ser executada.
# Toda função tem um atributo __name__ que fornece o nome da função,
# e isto é usado na função inner() acima para exibir a função atual
# que está para ser invocada. Note que a função inner() é definida dentro 
# da função logger(). Uma referência para a função inner() é, então, 
# retornada como o resultado da função logger(). A função inner() não
# é executada neste ponto. 
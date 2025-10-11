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
# -------------------------------------------
# Usando decoradores
# Para ver qual o efeito de aplicar um decorador é, é útil explorar a 
# abordagem básica(explícita) para usá-lo. Isto pode ser feito definindo 
# uma função (vamos chamá-la target) que exibe uma mensagem simples:
#def target():
#    print('In target function')
# Podemos aplicar o decorador logger explicitamente nesta função passando
# a referência à função target, por exemplo:
#t1 = logger(target)
#t1()
# Quando executamos esse código, executamos a função inner() que foi
# retornada pelo decorador. Esta função, por sua vez, exibe uma mensagem e
# chama a função passada para o logger. Uma vez que essa função passada
# foi executada, exibe outra mensagem. O efeito de executar a função t1() 
# é, portanto, chamar a função inner() que chama a função target, e exibe:
#calling target
#In target function
#called target
# Isto ilustra o que ocorre quando uma função de estilo decoradora é
# executada. Python fornece algum facilitador sintático que permite
# que a definição da função e associação com o decorador sejam declarados
# junto usando a sintaxe '@', por exemplo:
#@logger
#def target():
#    print('In target function')
#target()
# Isto tem o mesmo efeito que passar target para logger, mas ilustra o
# papel de logger de uma maneira mais Pythonica. É, portanto, o uso
# mais comum de Dcoradores.
#--------------------------------------------
# Funções com parâmetros
# Decoradores podem ser aplicados a funções que pegam parâmetros; entretanto,
# a função do decorador também deve pegar os mesmos parâmetros.
# Por exemplo, se você tivesse uma função como:
#@logger
#def my_func(x, y):
#    print(x, y)
#my_func(4, 5)

#Então o decorador também deve pegar dois parâmetros, por exemplo:
def registrador(func):
    def interior(x, y):
        print('calling', func.__name__, 'with', x, 'and', y)
        func(x, y)
        print('called', func.__name__)
    return interior
#@registrador
#def my_func(x, y):
#    print(x, y)
#my_func(4, 5)
#------------------------------------------
# Decoradores empilhados
# Decoradores podem ser empilhados, ou seja, mais de um decorador pode
# ser aplicado ao mesmo objeto chamável. Quando isto ocorre, cada função
# é cercada dentro de outra função; esta ideia é ilustrada no seguinte
# código:
def make_bold(fn):
    def makebold_wrapped():
        return"<b>" + fn() + "</b>"
    return makebold_wrapped

def make_italic(fn):
    def makeitalic_wrapped():
        return "<i>" + fn() + "</i>"
    return makeitalic_wrapped
@make_bold
@make_italic
def hello():
    return 'hello world'
#print(hello())

# Neste exemplo, a função hello é marcada com dois decoradores, 
# @make_bold e @make_italic. Isto significa que a função hello() é primeiro
# passada na função make_italic() e cercada pela função makeitalic_wrapped.
# Esta função é, então, retornada do decorador make_italic. makeitalic_wrapped
# é então passada para a função make_bold(), que então a cerca  dentro
# da função makebold_wrapped; que é retornada pelo decorador make_bold.
# O resultado é:
#<b><i>hello world</i></b>
#------------------------------------
# Decoradores parametrizados
# Decoradores também podem pegar parâmetros, mas a sintaxe para tais
# decoradores é um pouco diferente; há, essencialmente, uma camada extra de
# indireção. A função decoradora pega um ou mais parâmetros e retorna
# uma função que pode usar o parâmetro e pega o objeto chamável que está
# sendo cercado. Por exemplo:
def register(active=True):
    def wrap(func):
        def wrapper():
            print('Calling ', func.__name__, ' decorator param' \
            '', active)
            if active:
                func()
                print('Called ', func.__name__)
            else:
                print('Skipped ', func.__name__)
        return wrapper
    return wrap

@register()
def func1():
    print('func1')

@register(active=False)
def func2():
    print('func2')

#func1()
#print('-'*10)
#func2()

# Neste exemplo, a função cercada apenas será chamada se o parâmetro
# ativo é True. Este é o padrão, de modo que para func1() não é necessário
# especificar o parâmetro, mas note que agora o parâmetro precisa
# de parênteses. Para func2(), o decorador @register é definido com o
# parâmetro ativo como False. Isto significa que a função cercadora não
# chamará a função fornecida. 
#-------------------------------------
# Decoradores de método
# Métodos sem parâmetros
# Também é possível decorar métodos assim como funções (por eles também
# serem objetos chamáveis). Entretanto, é importante lembrar que métodos
# pegam o parâmetro especial 'self' como o primeiro parâmetro que é usado
# para referenciar o objeto ao qual o método está sendo aplicado. É, 
# portanto, necessário para o decorador levar este parâmetro em consideração;
# isto é, a função cercadora interior deve pegar pelo menos um parâmetro
# representando 'self':
def pretty_print(method):
    def method_wrapper(self):
        return"<p>{0}</p>".format(method(self))
    return method_wrapper

# O decorador pretty_print define uma função interna que pega como primeiro
# parâmetro(e único, neste caso) a referência ao objeto (que usa o 
# parâmetro 'self' por convenção). Isto é, então, passado para o método
# de fato quando é chamado.
# O decorador pretty_print pode agora ser usado com qualquer método que
# apenas pega o parâmetro self, por exemplo:
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    
    def print_self(self):
        print('Person -', self.name, ', ', self.age)
    
    @pretty_print
    def get_fullname(self):
        return self.name + " " + self.surname

# Na classe acima, o método get_fullname() é decorado com pretty_print.
# Se chamamos get_fullname() em um objeto, a string resultante será 
# cercada em <p> e </p>(que é marcação HTML de um parágrafo):
#print('Starting')
#p = Person('John', 'Smith', 21)
#p.print_self()
#print(p.get_fullname())
#print('Done')
#----------------------------------------------
# Métodos com parâmetros
# Assim como com as funções, métodos que pegam parâmetros em adição
# a self também podem ser decorados. Neste caso, a função retornada 
# do decorador deve pegar não apenas o parâmetro self, mas quaisquer
# parâmetros passados ao método. Por exemplo:
def trace(method):
    def method_wrapper(self, x, y):
        print('Calling', method.__name__, 'with', x, y)
        method(self, x, y)
        print('Called', method, 'with', x, y)
    return method_wrapper

# Agora este decorador tracer define uma função interna que pega o parâmetro
# self e dois parâmetros adicionais. Pode ser usado com quaisquer métodos
# que também pegam dois parâmetros como o método move_to() abaixo:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @trace
    def move_to(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return 'Point - ' + str(self.x) + ',' + str(self.y)

# Quando um objeto Point é criado abaixo, podemos chamar o método
# move_to() e ver o resultado:
#p = Point(1, 1)
#print(p)
#p.move_to(5, 5)
#print(p)

#-------------------------------------------------
# Decoradores de classe
# Além de possível decorar funções e métodos, também é possível decorar
# classes. Uma classe pode ser decorada para adicionar funcionalidades
# requisitadas que podes ser externas àquela classe.
# Como exemplo, um operação comum a nível de classe é querer indicar
# que uma classe deveria implementar o padrão de design singleton. 
# O 'Singleton Design Pattern' (novamente do livro Gang of Four Design
# Patterns') descreve um tipo que pode apenas ter um objeto construído
# para ele. Isto é, diferente de outros objetos não deveria ser possível
# obter mais que uma instância dentro do mesmo programa. Assim, o padrão
# de design Singleton garante que apenas uma instância de uma classe é
# criada. Todos os objetos que usam uma instância daquele tipo usam
# a mesma instância.
# Podemos definir um decorador que implementa este padrão, por exemplo:
def singleton(cls):
    print('In singleton for: ', cls) 
    instance = None

    def get_instance():
        nonlocal instance
        if instance is None:
            instance = cls()
        return instance
    return get_instance

# Este decorador retorna a função get_instance(). Esta função
# checa para ver se a variável instância é definida como None ou não;
# se é definida como None, ela instancia a classe passada ao decorador
# e salva isto na variável de instância. Então retorna a instância.
# Se a instância já é definida simplesmente retorna a instância.
# Podemos aplicar este decorador para classes inteiras como Service e Foo
# abaixo:
#@singleton
#class Service(object):
#    def print_it(self):
#        print(self)

#@singleton
#class Foo(object):
#    pass
# Agora podemos usar as classes Service e Foo normalmente; entretanto, 
# apenas uma instância de Serviço e de Foo serão criadas no mesmo
# programa.
#print('Starting')
#s1 = Service()
#print(s1)
#s2 = Service()
#print(s2)
#f1 = Foo()
#print(f1)
#f2 = Foo()
#print(f2)
#print('Done')
#--------------------------------------
# Quando um decorador é executado?
# Uma característica importante de decoradores é que eles são executados
# logo após a função decoradora ser definida. Isto é, geralmente, na 
# hora de importação (p. ex, quando um módulo é carregado por Python)
def logger(func):
    print('In Logger')
    def inner():
        print('In inner calling', func.__name__)
        func()
        print('In inner called', func.__name__)
    print('Finished Logger')
    return inner

#@logger
#def print_it():
#    print('Print It')

#print('Start')
#print_it()
#print('Done')

# Por exemplo, ao ser chamado como decorador da função print_it()
# 'In Logger' e 'Finished Logger' é exibido antes da execução da função
# interna ou da chamada da função print_it, tendo a saída:
#In Logger
#Finished Logger
#Start
#In inner calling print_it
#Print It
#In inner called print_it
#Done
# Isto ilustra a diferença entre o que Pythonistas chamam 'hora da 
# importação'(import time) e 'hora da execução'(runtime)
#---------------------------------------------------
# Decoradores embutidos
# Há diversos decoradores embutidos em Python 3, alguns que já usamos
# anteriormente como @classmethod, @staticmethod e @property. Também
# vimos alguns decoradores ao falar sobre métodos abstratos e propriedades.
# Também existem decoradores associados com teste unitário e operações
# assíncronas.
#------------------------------------------------
# FuncTools Wrap
# Um problema com funções decoradas pode se tornar aparente ao depurar
# ou tentar rastrear o que está acontecendo. O problema é que, por padrão,
# os atributos associados com a função sendo chamada são realmente aqueles 
# da função interna retornada pela função decoradora. Isto é, o name, doc
# e module da função são aqueles da função retornada pelo decorador.
# O name e documentação da função original, decorada, foram perdidos.
# Por exemplo, retornando ao decorador logger original temos:
#def logger(func):
#    def inner():
#        print('calling ', func.__name__)
#        func()
#        print('called ', func.__name__)
#    return inner


#print('name:', get_text.__name__)
#print('doc: ', get_text.__doc__)
#print('module; ', get_text.__module__)

# Ao executar este código, obtemos:
#name: inner
#doc:  None
#module;  __main__

# Isto faz parecer que a função get_text é chamada inner e não tem 
# docstring associada com isso. Entretanto, se olharmos à função
# ela deveria ser chamada get_text() e tem uma docstring 'returns some text'.
# Python incluiu o módulo functools (desde a versão 2.5) que contém
# o decorador functools.wraps que pode ser usado para circundar este
# problema. Wraps é um decorador que atualiza os atributos da função
# cercadora(inner) àqueles da função original (neste caso, get_text()):
from functools import wraps
def logger(func):
    @wraps(func)
    def inner():
        print('calling ', func.__name__)
        func()
        print('called ', func.__name__)
    return inner
@logger
def get_text(name):
    """ return some text"""
    return "Hello " + name

print('name:', get_text.__name__)
print('doc: ', get_text.__doc__)
print('module; ', get_text.__module__)
# Com isso, obtemos:
#name: get_text
#doc:  return some text
#module;  __main__
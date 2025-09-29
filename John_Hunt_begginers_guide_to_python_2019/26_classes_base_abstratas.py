# Capítulo 26 - Classes base abstratas
# Este capítulo apresente Classes base abstratas(também conhecidas
# como ABCs) que foram originalmente introduzidas em Python 2.6. 
# Uma Classe Base Abstrata é uma classe que não se pode instanciar
# e que é esperada que seja estendida por uma ou mais subclasses.
# Estas subclasses irão, então, preencher quaisquer lacunas deixadas
# pela classe base. Elas são muito úteis para criar hierarquias de
# classes com um alto nível de reutilização da classe raiz na 
# hierarquia.
# -----------------------------------------------
# Classes abstratas como um conceito
# Uma classe abstrata é uma classe da qual você não pode
# criar um objeto. Tipicamente estão ausentes um ou mais elementos
# necessários para criar um objeto completamente funcional.
# Em contraste, uma classe não-abstrata(ou concreta) não deixa
# nada indefinido e pode ser usada para criar um objeto funcional.
# Você poderia questionar qual a utilidade de uma classe abstrata?
# A resposta é que você pode agrupar elementos para serem compartilhados
# por um número de classes, sem fornecer uma implementação completa.
# Além disso, você pode forçar que subclasses providenciem métodos
# específicos garantindo que implementadores de uma subclasse pelo
# menos forneçam métodos nomeados apropriadamente. Você deveria, portanto,
# usar classes abstratas quando:
#   * você quer especificar dados ou comportamentos comuns a um conjunto de 
#       classes, mas insuficientes para uma única instância
#   * você quer forçar subclasses a fornecer comportamentos específicos.
# Em muitos casos, as duas situações ocorrem simultaneamente. Tipicamente,
# os aspectos da classe a ser definida como abstrata são específicos
# de cada classe, enquanto o que foi implementado é comum a todas as classes.
# --------------------------------------------------
# Classes base abstratas em Python
# ABCs não podem ser instanciadas por si só, mas podem ser extendidas 
# por subclasses. Estas subclasses podem ser classes concretas ou
# podem ser, elas também, ABCs (que extendem o conceito definido
# na ABC raiz).
# ABCs podem ser usadas para definir comportamento genérico (potencialmente
# abstrato) que pode ser misturado em outras classes Python e agem
# como uma raiz abstrata da hierarquia de classe. Eles podem também
# ser usados para fornecer um modo formal de especificar comportamento
# que deve ser fornecido por uma classe concreta.
# ABCs podem ter:
#   * Zero ou mais métodos ou propriedades abstratos (mas não são requiridas) 
#   * Zero ou mais métodos e propriedades concretas (não são requiridas)
#   * Ambos atributos privados e protegidos (seguindo as convenções de
#       barra única _ e barra dupla __)
# ABCs também podem ser usados para especificar uma interface específics
# ou protocolo formal. Se um ABC define quaisquer métodos ou propriedades
# abstratos, então as subclasses devem fornecer implementações para 
# todos os tais elementos abstratos.
# Há muitos ABCs embutidos em Python, incluindo:
#   * estruturas de dados (módulo collection),
#   * módulo numbers,
#   * streams (fluxos?)(módulo IO).
# De fato, ABCs são amplamente usadas internamente dentro do próprio Python
# e muitos desenvolvedores usam ABCs sem mesmo saber que elas existem
# ou entender como definí-las.
# Realmente, ABCs não são amplamente usadas por desenvolvedores 
# construindo sistemas com Python, apesar disso ser, em parte,
# porque elas são mais apropriadas para quem constrói bibliotecas,
# em particular aquelas que se esperam que sejam estendidas pelos
# próprios desenvolvedores.
# ---------------------------------------
# Subclassificando um ABC
# Tipicamente, uma ABC precisará ser importada do módulo
# em que é definida; claro, se a ABC é definida no módulo atual
# então isso não é necessário. Como um exemplo, a classe 
# collections.MutableSequence é uma ABC; esta é uma ABC para uma
# sequência de elementos que podem ser modificados (mutáveis) e 
# iterados sobre. Nós podemos usar isso como a classe base para
# nosso próprio tipo de coleção que chamaremos Bag, por exemplo:
# 
# from collections import MutableSequence
# class Bag(MutableSequence):
#   pass
# 
# Neste exemplo, estamos importando MutableSequence do módulo
# collections. Então definimos a classe Bag como extensão da ABC
# MutableSequence. Por hora, estamos usando a palavra chave especial
# de Python 'pass' como um reservador de espaço para o corpo da classe.
# Entretanto, isto significa que a classe Bag é, de fato, também uma classe
# abstrata como ela não implementa nenhum dos métodos abstratos na
# ABC MutableSequence. Entretanto, Python não valida isto na hora da
# importação; em vez disso, valida na hora da execução quando uma instância
# do tipo está para ser criada. Assim, se um programa tentar criar uma
# instância de Bag, o seguinte erro seria levantado:
# Traceback (most recent call last):
#
#File "/pythonintro/abstract/Bag.py", line 10, in <module>
#main()
#File "/pythonintro/abstract/Bag.py", line 7, in main
#bag = Bag()
#TypeError: Can't instantiate abstract class Bag with abstract
#methods __delitem__, __getitem__, __len__, __setitem__,
#insert 
# 
# Como pode ser visto, este é um requerimento bem formal; se você
# não implementar todos os métodos definidos como abstratos na classe
# mãe, então não pode criar uma instância da classe que está definindo
# (pois ela também é abstrata).
# Podemos definir um método para cada uma das classes abstratas a classe
# Bag e então seremos capazes de criar uma instância da classe. Por
# exemplo:
# 
# from collections import MutableSequence
# class Bag(MutableSequence):
#   def __getitem__(self, index):
#       pass
#   def __delitem__(self, index):
#       pass
#   def __len__(self):
#       pass
#   def __setitem__(self, index, value):
#       pass
#   def insert(self, index, value):
#       pass
# 
# Esta versão de Bag cumpre todos os requerimentos impostos sobre
# ela pela ABC MutableSequence; isto é, ela implementa cada um dos
# métodos especiais listados e o método insert. A classe Bag pode
# agora ser considerada como uma classe concreta. Entretanto, neste
# caso os métodos em si não fazem nada (usam novamente a palavra chavem
# de Python pass). Entretanto, agora podemos escrever:
# bag = Bag()
# E a aplicação não gerará uma mensagem de erro. Neste ponto poderíamos
# agora implementar cada método de modo que fornece uma implementação
# apropriada de Bag.
# -----------------------------------------------
# Definindo uma Classe Base Abstrata
# Uma ABC pode ser definida especificando que a classe tem uma
# metaclasse; tipicamente, ABCMeta. A metaclasse ABCMeta é fornecida pelo 
# módulo abc. A metaclasse é especificada usando o atributo metaclasse
# da lista de classe mãe. Isto vai criar uma classe que pode ser usada
# como uma ABC. Alternativamente, você pode extender a classe abc.ABC
# que especificou ABCMeta como sua metaclasse. Isto é exatamente como as 
# ABCs no arquivo _collections_abc.py são implementadas. O seguinte
# pedaço de código ilustra esta ideia. A classe ABCMeta é importada
# do módulo abc. É, então, usada com a classe Shape pelo atributo
# metaclass da lista de herança de classes:
# from abc import ABCMeta
# class Shape(metaclass=ABCMeta):
#   def __init__(self, id):
#       self.id = id
# Note que, neste ponto, apesar de Shape ser uma ABC, não define 
# nenhuma elemento abstrato e, assim, pode de fato ser instanciada
# como qualquer outra classe concreta. Entretanto, em seguida definiremos 
# alguns métodos abstratos para a ABC Shape.
# Para definir um método abstrato, precisamos também importar o decorador
# abstractmethod do módulo abc, (se quisermos definir uma propriedade
# abstrata então precisamos adicionar @property para um método abstrato
# apropriado). Importar o decorador abstractmethod é ilustrado abaixo:
# 
# from abc import ABCMeta, abstractmethod
# class Shape(metaclass=ABCMeta):
#   def __init__(self, id):
#       self._id = id
#
#   @abstractmethod
#   def display(self): pass
# 
#   @property
#   @abstractmethod
#   def id(self): pass
#
# A classe Shape é, agora, uma classe base abstrata e requer que 
# quaisquer subclasses devam fornecer uma implementação do método
# display() e a propriedade id (de outro modo a subclasse irá
# automaticamente tornar-se abstrata).
# A classe Circle é uma subclasse concreta da ABC Shape; assim ela
# fornece um método de inicialização __init__(), um método display e uma
# propriedade id:
# 
# class Circle(Shape):
#   def __init__(self, id):
#       super().__init__(id)
#   def display(self):
#       print('Circle: ', self._id)
#   @property
#   def id(self):
#       """ The id property """
#       return self._id
# 
# Agora podemos usar a classe Circle em uma aplicação:
# c = Circle('circle1')
# print(c.id)
# c.display()
# O output é:
# circle1
# Circle:  circle1 
# ------------------------------------
# Definindo uma interface
# Muitas linguagens como Java e C# tem o conceito de uma definição
# de interface; isto é um contrato entre os implementadores de uma
# interface e o usuário da implementação garantindo que certas
# instalações serão fornecidas. Python não tem explicitamente o
# conceito de contrato de interface (note que aqui interface se
# refere à interface entre uma classe e o código que a utiliza).
# Entretanto, Python tem Classes de Base Abstrata. Qualquer ABC
# que apenas tem métodos ou propriedades abstratos pode ser tratada
# como um contrato que deve ser implementado (ela pode, claro, ter
# métodos, propriedades e atributos concretos). Entretanto,
# como sabemos que Python garantirá que quaisquer instâncias 
# possam apenas serem criadas de classes concretas, podemos tratar
# uma ABC como se comportando como um contrato entre uma classe
# e aqueles usando aquela classe. Esta abordagem é adotada em diversos
# frameworks e bibliotecas dentro de Python.
# -------------------------------------
# Subclasses virtuais
# Na maioria das linguagens orientadas a objetos, para uma classe ser
# tratada como subclasse de outra classe, é necessário para a subclasse
# extender a classe mãe. Entretanto, Python tem uma abordagem mais
# relaxada à tipagem, como ilustrado pela ideia de 'Duck Typing' (discutida
# no próximo capítulo).
# Em algumas situações, no entanto, é útil ser capaz de confirmar que um tipo 
# é uma subclasse de outro ou que uma instância é uma instância de um tipo
# específico (que pode vir da hierarquia de classe do objeto) ao executar.
# De fato, em Python, não é necessário ser uma subclasse de fato de uma
# classe mãe para ser considerada uma subclasse - em vez disso, subclasses
# virtuais permitem que uma classe seja tratada como subclasse de outra 
# mesmo que não haja uma relação de hierarquia direta entre elas. A chave aqui
# é que a subclasse virtual deve corresponder a interface requerida
# apresentada oela classe mãe virtual. Isto é feito registrando uma classe como
# uma subclasse virtual de uma ABC. Isto é, a classe mãe virtual deve ser
# uma ABC e então a subclasse pode ser registrada (na execução) como uma
# subclasse virtual da ABC. Isto é feito usando um método chamado
# register().
# Uma vez que uma classe é registrada como uma subclasse de uma ABC,
# os métodos issubclass() e isinstance() retornarão True para aquela classe
# com respeito à classe mãe virtual. Por exemplo, dadas as seguintes
# duas classes independentes:
from abc import ABCMeta
class Person(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def birthday(self):
        print('Happy Birthday')

class Employee(object):
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
    def birthday(self):
        print('Its your birthday') 

# Se agoras checarmos para ver se Employee é uma subclasse
# de Person, obteremos False como retorno. 

#print(issubclass(Employee, Person))
#e = Employee('Megan', 21, 'MS123')
#print(isinstance(e, Person))

# Entretanto, se agora registrarmos a classe Employee como uma subclasse
# virtual da classe Person, os dois métodos de teste retornarão True.  

#Person.register(Employee)
#print(issubclass(Employee, Person))
#e = Employee('Megan', 21, 'MS123')
#print(isinstance(e, Person))

# Isto fornece um nível bastante útil de flexibilidade que pode ser
# explorado ao usar bibliotecas e frameworks existentes.
#------------------------------------------------
# Mixins
# Um mixin é uma classe que representa alguma (tipicamente concreta)
# funcionalidade que tem o potencial de ser útil em múltiplas
# situações mas por si só não é algo que seria instanciado.
# Entretanto, um mixin pode ser misturado em outras classes e pode 
# extender os dados e comportamentos daquele tipo e pode acessar dados 
# e métodos fornecidos por aquelas classes.
# Mixins são uma categoria comum de ABCs; apesar de serem implícitos em seu 
# uso (e nomeação) em vez de serem construtos completos na linguagem Python.
# Por exemplo, vamos definir uma classe PrinterMixing que fornece um método 
# de utilidade para ser usado com outras classes. Não é algo que queremos 
# que os desenvolvedores instanciem, então faremos isto uma ABC mas
# não define quaisquer métodos ou propriedades abstratos
from abc import ABCMeta
class PrinterMixin(metaclass=ABCMeta):
    def print_me(self):
        print(self)
class Person(object):
    def __init__(self, name):
        self.name = name
#class Employee(Person, PrinterMixin):
#    def __init__(self, name, age, id):
#        super().__init__(name)
#        self.age = age
#        self.id = id
#    def __str__(self):
#        return 'Employee(' + self.id + ')' + self.name + '['\
#                + str(self.age) + ']'
# Isto agora significa que quando instanciamos a classe Employee
# podemos chamar o método print_me() no objeto Employee

#e = Employee('Megan', 21, 'MS123')
#e.print_me()

# Uma coisa para se notar sobre PrinterMixin é que é completamente
# independente da classe em que foi misturado. Entretanto, mixins podem
# também impor algumas limitações nas classes em que eles são misturados.
# Por exemplo, IDPrinterMixin mostrado abaixo assume que a classe que será 
# misturada tem um atributo ou propriedade chamado id.
class IDPrinterMixin(metaclass=ABCMeta):
    def print_id(self):
        print(self.id)
# Isto significa que não pode ser misturada com sucesso na classe Person.
# Por outro lado, a classe Employee tem um atributo id e assim,
# IDPrinterMixin pode ser misturado na classe Employee:
class Employee(Person, PrinterMixin, IDPrinterMixin):
    def __init__(self, name, age, id):
        super().__init__(name)
        self.age = age
        self.id = id
    def __str__(self):
        return 'Employee(' + self.id + ')' + self.name + '['\
                + str(self.age) + ']'
e = Employee('Megan', 21, 'MS123')
e.print_me()
e.print_id()
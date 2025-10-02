# Capítulo 27 - Protocolos, polimorfismo e descritores
# Neste capítulo vamos explorar a ideia de um contrato implícito
# entre um objeto e o código que usa aquele objeto. Como parte desta
# discussão vamos explorar o que significa Duck Typing. Seguindo
# isso vamos introduzir o conceito de Python conhecido como
# protocolo. Vamos eexplorar seu papel dentro da programação Python e
# olhar a dois protocolos que ocorrem comumente: o Protocolo Gerenciador
# de Context e o Protocolo Descritor.
# ------------------------------------------------
# Contratos implícitos
# Algumas linguagens de programação (mais notavelmente Java e C#)
# tem a ideia de um contrato explicito entre uma classe e o usuário
# daquela classe; este contrato fornece uma garantia dos métodos que
# serão providenciados e os tipos que serão usados por parâmetros e 
# valores de retorno destes métodos. Nestas linguagens, é útil garantir
# que um método é apenas chamado com o tipo apropriado de valores e apenas 
# em situações apropriadas. Um pouco confusamente, estes contratos são
# referidos como interfaces em Java e C#; mas são feitos para descrever 
# a interface de programação de aplicativos (application programming 
# interfaces, API's) apresentados pela classe.
# Python é uma linguagem muito mais flexível e de fluxo livre que tanto
# Java quanto C# e então não tem um conceito explícito de interface. No 
# entanto, isto pode tornar as coisas mais complexas com o tempo; por exemplo,
# considerando a classe muito simples Calculator dada abaixo:
#class Calculator:
# def add(self, x, y):
#      return x + y
# Quais são os valores válidos que podem ser passados para o método
# add e usados para os parâmetros x e y? Inicialmente poderia parecer
# que valores numéricos como 1, 2 e 3.4, 5.77 etc seriam as únicas
# coisas que poderiam ser usadas com o método add:
#calc = Calculator()
# print('calc.add(3, 4):', calc.add(3, 4))  
# print('calc.add(3, 4.5):', calc.add(3, 4.5))
# print('calc.add(4.5, 6.2):', calc.add(4.5, 6.2))
# print('calc.add(2.3, 7):', calc.add(2.3, 7))
# print('calc.add(-1, 4):', calc.add(-1, 4))
#
# Isto gera a seguinte saída:
#calc.add(3, 4): 7
#calc.add(3, 4.5): 7.5
#calc.add(4.5, 6.2): 10.7
#calc.add(2.3, 7): 9.3
#calc.add(-1, 4): 3
#
# Entretanto, isto realmente representa um contrato que os valores 
# passados para o método Calculator.add() suportará o operador plus.
# Em um capítulo anterior, exploramos uma classe Quantity que implementou
# este operador (entre outros) e assim podemos também usar os objetos ´
# Quantity com o método add() de Calculator.
# q1 = Quantity(5)
# q2 = Quantity(10)
# print(calc.add(q1, q2))
# 
# Que exibe:
# 
# Quantity(15)
# 
# Este contrato implícito diz que o método Calculator.add() irá
# funcionar com qualquer coisa que suporta o operador numérico 'add',
# ou, em outras palavras, qualquer coisa que é tipo números.
# Isto também é conhecido como Duck Typing; isto é descrito na próxima seção.
#
# ------------------------------------------------
# Duck Typing
# 
# Este termo meio estranho vem de um ditado antigo que diz:
# 'Se anda como um pato, nada como um pato e grasna como um pato, então é um Pato!'
#
# Em Python, Duck Typing (também conhecido como tipagem de forma ou 
# tipagem estrutural) implica que se um objeto pode performar um conjunto
# exigido de operações, então é apropriado usá-lo para o que você quer. 
# Por exemplo, se o seu tipo pode ser usado com operadores de adição, 
# multiplicação, divisão e subtração então pode ser tratado como um tipo 
# Numérico(mesmo que não seja).
# Este é um recurso poderoso de Python e permite que código escrito
# originalmente para funcionar com um conjunto específico de tipos, também seja
# usado com um conjunto completamente novo de tipos desde que eles cumpram
# o contrato implícito definido dentro do código.
# Também é interessante notar, que um conjunto particular de métodos pode ter um 
# 'super conjunto' de requerimentos em um tipo particular, mas você precisa
# apenas implementar a quantidade necessária para a funcionalidade que
# você vai usar. Por exemplo, vamos modificar a classe Calculator um
# pouco e adicionamos mais alguns métodos:
#class Calculator():
#    """ Simple Calculator class"""
#    def add(self, x, y):
#       return x + y
#    def subtract(self, x, y):
#       return x - y
#    def multiply(self, x, y):
#       return x * y
#    def divide(self, x, y):
#       return x / y
#
# À primeira vista, isto pode indicar que qualquer coisa sendo usada com
# a Calculator deve implementar todos os quatro operadores '+', '-', '/', '*'.
# Entretanto, isto é apenas verdade se você precisar executar todos os quatro
# métodos definidos na classe.
# Por exemplo, considere o tipo Distance:
#class Distance():
#    def __init__(self, d):
#        self.value = d
#    def __add__(self, other):
#        return Distance(self.value + other.value)
#    def __sub__(self, other):
#        return Distance(self.value - other.value)
#    def __str__(self):
#        return 'Distance[' + str(self.value) + ']'
#
# Isto define uma classe que implementa apenas os métodos __add__() 
# e __sub__() e apenas suportará os operadores '+' e '-'.
# Podem instâncias de Distance serem usadas com a classe Calculator?
# A resposta é que elas podem mas apenas com os métodos add e subtract
# (Como eles apenas cumprem parte do contrato implicado entre a classe
# Calculator e os tipos usados por ela.)
# Podemos, portanto, escrever:
#calc = Calculator()
#d1 = Distance(6)
#d2 = Distance(3)
#print(calc.add(d1, d2))
#print(calc.subtract(d1, d2))
# E obtemos:
#Distance[9]
#Distance[3]
# Entretanto, se tentarmos usar multiply() ou divide() obteremos um erro.
#------------------------------------------------------
# Protocolos
# Como mencionado acima, Python não tem nenhum mecanismo formal para
# declarar o que é exigido entre o fornecedor de alguma funcionalidade e
# o usuário ou consumidor da funcionalidade. Em vez disso, a abordagem
# muito menor formal chamada Duck Typing é adotada.
# Isto, entretanto, levanta a questão: como você sabe o que é requerido:
# Como você sabe que precisa fornecer operadores numéricos para um objeto
# a ser usado com a classe Calculator?
# A resposta é que um conceito conhecido como Protocolo é usado.
# Um Protocolo é uma descrição informal da interface do programador
# providenciada por alguma coisa em Python (por exemplo, uma classe mas
# poderia também ser um módulo ou um conjunto de funções independentes).
# É definido apenas via documentação (e, portanto, a classe Calculator 
# deveria ter uma string de documentação da classe definindo este protocolo).
# Baseado na informação fornecida pelo protocolo, se uma função ou método
# requer que um objeto forneça uma operação específica (ou método) então
# se tudo funcionar, ótimo; se não, um erro será lançado, e o tipo não
# é compatível. É um dos elementos chave de Python que permite o conceito
# da Orientação a Objetos 'Polimorfismo' operar.
#-------------------------------------------------------
# Um exemplo de protocolo
# Há muitos Protocolos comumente ocorrentes que podem ser encontrados em Python. 
# Por exemplo, há um protocolo para definir Sequências, como um container
# que pode ser acessado um item por vez.
# Este protocolo requer que qualquer tipo que será guardado no container
# deve fornecer os métodos __len__() e __getitem__().  
# Assim, qualquer classe que implementa estes dois métodos cumpre os
# requerimentos do protocolo. Entretanto, como estes protocolos são
# informais e não-impostas em Python, não é realmente necessário implementar
# todos os métodos em um protocolo (como vimos na seção anterior). Por exemplo,
# se é conhecido que uma classe será usada apenas com iteração, então pode
# ser necessário implementar apenas o método __getitem__().
# -----------------------------------------
# O Protocolo Gerenciador de Contexto
# Outro exemplo concreto é aquele do Protocolo Gerenciador de Contexto. Este
# protocolo foi introduzido em Python 2.5, sendo bem estabelecido agora.
# É associado com a declaração 'with as'. Esta declaração é tipicamente
# usada com classes que precisarão alocar, e liberar, os chamados 'recursos'.
# Estes recursos poderiam ser arquivos, ou conexões de bases de dados, etc.
# Em cada um desses casos, uma conexão precisa ser feita (por exemplo,
# para um arquivo ou uma base de dados) antes do objeto associado poder
# ser usado. 
# Entretanto, a conexão deveria, então, ser fechada e liberada antes
# de terminarmos de usar o objeto. Isto é porque conexões penduradas
# com coisas como arquivos e bases de dados podem se manter (hang around)
# e podem causar problemas posteriormente (por exemplo, tipicamente apenas um
# número limitado de conexões simultâneas são permitidas para um arquivo ou
# uma base de dados por cada vez e se não são fechada apropriadamente podem
# ficar sem conexões possíveis avaliáveis).
# A declaração 'with as' garante que quaisquer passos de preparação
# são realizadas antes de um objeto estar avaliável para uso e que
# qualquer comportamento de desligamento é invocado quando tiver terminado.
# A sintaxe para o uso de 'with as' é:
# with <managed object> as <localname>:
#   Code to use managed object via <localname>
# Por exemplo:
# with ContextManagedClass() as cmc:
#   print('In with block', cmc)
#   print('Existing')
# Note que neste caso, o objeto referido por cmc está apenas no alcance
# dentro das linhas indentadas após a declaração with as; depois disso,
# a variável cmc não é mais acessível. 
# Como isso funciona? De fato, o que a declaração 'with as' faz é
# chamar um método especial quando a declaração 'with as' é entrada
# (logo após o ':' acima); este método é o método __enter__(). Então
# chama outro método especial assim logo que o método 'with as' é saído
# (logo após a última declaração indentada). Este segundo método é
# o método __exit__().
#   * O método __enter__() é esperado que faça qualquer preparação/alocação
#       de recursos/fazer conexões etc. É esperado que retorne um objeto 
#       que será usado dentro do bloco de declarações que forma a declaração
#       'with as'. É comum retornar self apesar de não necessário (esta 
#       flexibilidade permite que o 'objeto gerenciado' aja como uma 
#       fábrica para outros objetos se requirido).
#   * O método __exit__() é chamado no 'objeto gerenciado' e é passado
#       informação sobre quaisquer exceções que possam ter sido geradas 
#       durante o corpo da declaração 'with as'. Note que o método __exit__()
#       é chamado seja uma exceção lançada ou não. O método __exit__() retorna
#       um booleano, se retornar True então qualquer exceção que tenha sido
#       gerada é engolida (isto é, suprimida e não passada para o código
#       de chamada). Se retorna False então, se houver uma exceção, também
#       é passada de volta para qualquer código chamado com a declaração 'with as'.
# Uma classe de exemplo que pode ser usado com a declaração 'with as'(mas que
# cumpre os requerimentos do Protocolo Gerenciador de Contexto) é dado abaixo:

#class ContextManagedClass(object):
#    def __init__(self):
#        print('__init__')
#    def __enter__(self):
#        print('__enter__')
#        return self
#    # Args exception type, exception value and traceback
#    def __exit__(self, *args):
#        print('__exit__:', args)
#        return True
#    def __str__(self):
#        return 'ContextManagedClass object'

# A classe acima implementa o Protocolo Gerenciador de Contexto 
# ao definir ambos os métodos __enter__() e o método __exit__().
# Podemos agora usar esta classe com a declaração eith as:
#print('Starting')
#with ContextManagedClass() as cmc:
#    print('In with block', cmc)
#    print('Exiting')
#print('Done') 

# A saída disto é:
#Starting
#__init__
#__enter__
#In with block ContextManagedClass object
#Exiting
#__exit__: (None, None, None)
#Done
# 
# Disto você pode ver que o método __enter__() é chamado antes
# do código no bloco e __exit__() é chamado após o código no bloco.
#--------------------------------------------------
# Polimorfismo
# É a habilidade de enviar a mesma mensagem pedido para um método executar(run))
# para diferentes objetos, cada qual parece realizar a mesma função. 
# Entretanto, o jeito em que a mensagem é lidada depende da classe do objeto.
# Polimorfismo é uma palavra que soa estranho, derivada do grego, para um 
# conceito relativamente simples. É essencialmente a habilidade de pedir que
# a mesma operação seja realizada por uma ampla gama de diferentes tipos de 
# coisas. Como o pedido é processado depende da coisa que recebe o pedido.
# O programados não precisa se preocupar com como o pedido é resolvido,
# apenas que é. Isto é ilustrado abaixo:
# def night_out(p):
#   p.eat()
#   p.drink()
#   p.sleep()
# Neste exemplo, o parâmetro passado para a função night_out() espera
# ser dado algo que responderá aos métodos eat(), drink() e sleep(). 
# Qualquer objeto que cumpre este requerimento podem ser usados com a
# função. Podemos definir múltiplas classes que cumprem este contrato 
# informal, por exemplo, podemos definir uma hierarquia de classe que
# fornece esses métodos, ou separar completamente classes que implementam
# esses métodos. No caso da hierarquia de classe, os métodos podem ou não 
# sobrescrever aqueles da classe mãe.
# Efetivamente, isto significa que você pode pedir muitas coisas diferentes
# para realizar a mesma ação. Por exemplo, você poderia pedir uma gama de objetos 
# para fornecer uma string exibível descrevendo elas mesmo. De fato, em Python
# isto é exatamente o que acontece. Por exemplo, se você pedir uma 
# instância da classe Manager, um objeto compilador ou um objeto base de dados
# para retornar tal string, você usaria o mesmo método (__str__(), em Python).
# As seguintes classes todas cumprem o contrato implicado pela função night_out(): 
#class Person:
#    def eat(self): print('Person - Eat')
#    def drink(self): print('Person - Drink')
#    def sleep(self): print('Person - Sleep')
#class Employee(Person):
#    def eat(self): print('Employee - Eat')
#    def drink(self): print('Employee - Drink')
#    def sleep(self): print('Employee - Sleep')
#class SalesPerson(Employee):
#    def eat(self): print('SalesPerson - Eat')
#    def drink(self): print('SalesPerson - Drink')
#class Dog:
#    def eat(self): print('Dog - Eat')
#    def drink(self): print('Dog - Drink')
#    def sleep(self): print('Dog - Sleep')
#
# Isto significa que intâncias de todas as classes podem ser usadas com
# a função night_out(). Note que a classe SalesPerson cumpre o contrato
# implicado parcialmente pela herança (sleep() é herdada de Employee).
# ------------------------------------------------------
# O Protocolo Descritor
# Outro protocolo é o descritor. Descritores podem ser usados para
# criar o que é conhecido como atributos gerenciados. Um atributo
# gerenciado é um atributo de um objeto que é controlado (ou protegido)
# de acesso externo direto por código externo pelo descritor. O descritor
# pode, então, tomar qualquer ação que seja apropriada como validar o dado,
# checar o formato, fazer o log da ação, atualizar um atributo relacionado, etc.
# O protocolo descritor define quatro métodos (como de costume, eles são
# considerados métodos especiais e assim começam com sublinhado duplo):
#   * __get__(self, instance, owner) Este método é chamado quando o valor
#   de um atributo é acessado. 'instance' é a instância sendo modificada
#   e owner é a classe que define o objeto. Este método deveria retornar 
#   o valor do atributo (computado) ou levantar uma exceção AttributeError.
#   * __set__(self, instance, value) Este é chamado quando o valor de um 
#   atributo está sendo definido. O parâmetro value é o novo valor sendo
#   sendo definido.
#   * __delete__(self, instance) Chamado para deletar o atributo.
#   * __set_name__(self, owner, name) Chamado quando a classe owner 
#   é criada. O descritor foi atribuído para name. Este método foi 
#   adicionado ao protocolo em Python 3.6.
# A seguinte classe Logger implementa o protocolo Descritor. Ela pode,
# portanto, ser usado com outras classes para fazer o log da criação, 
# acessar e atualizar qualquer atributo seja aplicado sobre.
class Logger(object):
    """ Logger class implementing the descriptor protocol """ 
    def __init__(self, name):
        self.name = name
    def __get__(self, inst, owner):
        print('__get__:', inst, 'owner', owner,
              ', value', self.name, '=',
              str(inst.__dict__[self.name]))
        return inst.__dict__[self.name]
    def __set__(self, inst, value):
        print('__set__:', inst, '-', self.name, '=', value)
        inst.__dict__[self.name] = value
    def __delete__(self, instance):
        print('__delete__', instance)
    
    def __set_name__(self, owner, name):
        print('__set_name__', 'owner', owner, 'setting', name)

# Cada um dos métodos definidos para o protocolo exibe uma mensagem
# de modo que aquele acesso por ser monitorado. A classe Logger pode ser
# usada com a classe Cursor:
class Cursor(object):
    # Set up the descriptors at the class level
    x = Logger('x')
    y = Logger('y')
    def __init__(self, x0, y0):
        # Initialise the attributes
        # Note use of __dict__ to avoid using self.x notation
        # which would invoke the descriptor behaviour
        self.__dict__['x'] = x0
        self.__dict__['y'] = y0
    def move_by(self, dx, dy):
        print('move_by', dx, ',', dy)
        self.x = self.x + dx
        self.y = self.y + dy
    def __str__(self):
        return 'Point[' + str(self.__dict__['x'])+\
            ', ' + str(self.__dict__['y']) + ']'

# Há diversas coisas para se notar sobre esta definição de classe incluindo:
# Os Descritores devem ser definidos no nível da classe, não no
# nível do objeto/instância. Por isso os atributos x e y do objeto Cursor
# são definidos como tendo descritores Logger dentro da classe (e não dentro
# do método __init__()). Se você tentar definí-los usando self.x e self.y
# os descritores não serão registrados.
# O método __init__() de Cursor usa o dicionário __dict__ para inicializar
# os atributos de instância/objeto x e y. Isto é uma abordagem alternativa
# para acessar os atributos de um objeto; é usado internamente por um
# objeto para manter os valores reais dos atributos. Ele sobrepõe
# o mecanismo de buscar o atributo normal invocado quando você usar a
# notação ponto (como cursor.x = 10). Isto significa que não será 
# interceptado pelo Descritor. Isto foi feito porque o logger usa o método 
# __str__() para exibir a instância que guarda o atributo que usa os
# valores atuais de x e y. Quando o valor de x é inicialmente definido
# não haverá um valor de y, e assim um erro poderia ser gerado por __str__().
# O método __str__() também usa o dicionário __dict__ para acessar os
# atributos como não é necessário logar este acesso. Isto também tornaria
# recursivo se o Logger também usasse o método para exibir a instância.
# Podemos agora usar instâncias de Cursor sem saber o que o descritor 
# interceptará o acesso aos atributos x e y:
cursor = Cursor(15, 25)
print('-' * 25)
print('p1:', cursor)
cursor.x = 20
cursor.y = 35
print('p1 updated:', cursor)
print('p1.x:', cursor.x)
print('-' * 25)
cursor.move_by(1, 1)
print('-' * 25)
del cursor.x

# A saída deste código ilustra como descritores interceptaram acesso aos
# atributos. Note que o método move_by() acessa tanto os métodos descritores
# getter quanto o setter como ele lê o valor atual dos atributos e então os
# atualiza.
 
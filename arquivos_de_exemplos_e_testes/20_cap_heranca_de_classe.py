# Herança de classe
# A herança de classe é um recurso central da OOP. Ela permite
# uma classe herdar dados ou comportamentos de outra e é um
# dos modos principais em que reuso é habilitado dentro de classes.
#####################################################
# Herança permite que recursos definidos em uma classe sejam
# herdados e reutilizados na definição de outra classe. Por exemplo,
# uma classe Pessoa poderia ter os atributos 'nome' e 'idade'. 
# Também poderia ter comportamento associado com uma 'Pessoa' como
# 'aniversário'. Poderíamos, então, decidir que queremos ter outra
# classe 'Empregado' e que empregados também tem 'nome' e 'idade'
# e terão aniversários. Entretanto, além disso, um 'Empregado' pode
# ter um atributo 'Id' e um comportamento 'calcular_pagamento()'.
# Neste ponto, poderíamos duplicar a definição dos atributos 'nome' 
# e 'idade' e do comportamento 'aniversário()' na classe 'Empregado'
# (por exemplo, copiando e colando o código entre as classes).
# Entretanto, isto não apenas é ineficiente como também pode
# causar problemas no futuro. Por exemplo, podemos perceber que há 
# um problema ou bug na implementação de 'aniversário()' e podemos
# corrigí-lo na classe 'Pessoa' mas esquecer de fazê-lo na classe 'Empregado'.
# Em um sistema orientado a objetos, podemos obter a reutilização de 
# dados ou comportamento por herança. Isto é, uma classe pode herdar
# recursos de outra classe.
# Uma classe que é definida como extensão de uma classe parente
# tem a seguinte sintaxe:

#class SubClassName (BaseClassName):
#   class-body

# Note que a classe parente é especificada fornecendo o nome
# dela entre parênteses após o nome da nova (filha) classe.
# Podemos definir a classe 'Pessoa'. 
# Podemos definir a classe 'Pessoa' em Python como antes:
#########################################################
class Pessoa:    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        print('Feliz aniversário! Você tinha', self.idade, 'anos.')
        self.idade += 1
        print('Agora você tem', self.idade)
    
    def __str__(self):                          
        return self.nome + ' tem ' + str(self.idade) + ' anos de idade.'

class Empregado(Pessoa):
    def __init__(self, nome, idade, id):
        super().__init__(nome, idade)
        self.id = id
    
    def calcular_salario(self, horas_trabalhadas):
        taxa_de_pagamento = 7.50
        if self.idade >= 21:
            taxa_de_pagamento += 2.50
        return horas_trabalhadas * taxa_de_pagamento

class Vendedor(Empregado):
    def __init__(self, nome, idade, id, regiao, vendas):
        super().__init__(nome, idade, id)
        self.regiao = regiao
        self.vendas = vendas
    
    def bonus(self):
        return self.vendas * 0.5

#########################################################

# Aqui temos várias coisas:
# 1 -   A classe é chamada 'Empregado' mas extende 'Pessoa'. Isto
#       é indicado ao incluir o nome da classe sendo herdada em 
#       parênteses após o nome da classe sendo definida na declaração de classe.
# 2 -   Dentro do método __init__ referenciamos o método __init__()
#       definido na classe 'Pessoa' e usada para inicializar
#       instâncias daquela classe (pelo super().__init__()) Isto 
#       permite qualquer inicialização é necessária para Pessoa
#       acontecer. Note que o super()__init__() pode aparecer
#       em qualquer lugar de Empregado.__init__(); mas, por convenção,
#       aparece primeiro para garantir que o que a classe 'Pessoa'
#       fizer durante a inicialização não sobrescreve o que a classe 'Empregado' faz.
# 3 -   Todas as instâncias da classe Pessoa tem um 'nome', 'idade' e o
#       comportamento 'aniversario()'.
# 4 -   Todas as instâncias da classe 'Empregado' tem um nome, idade
#       e id e tem os comportamentos 'aniversario()' e 'calcular_pagamento(horas_trabalhadas)'
# 5 -   O método 'calcular_pagamento()' definido na classe empregado
#       pode acessas os atributos 'nome' e 'idade' assim como pode
#       acessar o atributo 'id'. De fato, usa a idade do empregado para
#       determinar a taxa de pagamento.
# Podemos ir além criar uma subclasse de Empregado, por exemplo com 
# a classe 'Vendedor'.
# 
# Agora podemos dizer que a classe 'Vendedor' tem um 'nome', 'idade',
# 'id', assim como 'regiao' e um total de vendas. Ela também tem os
# métodos 'aniversario()', 'calcular_pagamento(horas_trabalhadas)'
# e 'bonus()'
# Neste caso, o método Vendedor.__init__() chama 'Empregado'.__init__()
# como esta classe é a próxima na hierarquia, assim queremos executar 
# o comportamento de inicialização daquela classe antes de definirmos
# a classe 'Vendedor'.
# Podemos agora escrever código como:
#print('Pessoa')
#p = Pessoa('John', 54)
#print(p)
#print('-'*25)

#print('Empregado')
#e = Empregado('Denise', 51, 7468)
#e.aniversario()
#print('e.calcular_salario(40):', e.calcular_salario(40))
#print('-'*25)

#print('Vendedor')
#v = Vendedor('Phoebe', 21, 4712, 'UK', 30000.0)
#v.aniversario()
#print('v.calcular_salario(40):', v.calcular_salario(40))
#print('v.bonus():', v.bonus())

# Note que não Empregado e Vendedor não interferem em nada
# da classe Pessoa, assim como Vendedor não interfere em Pessoa e
# Empregado. Em termos de comportamento, todas as três classes
# podem executar o método aniversario(), mas apenas Empregado
# e Vendedor podem executar o método calcular_pagamento()
# e apenas Vendedor pode executar bonus().
#------------------------------------------------------
# Terminologia em torno de herança
# - Classe: Define uma combinação de dados e procedimentos que 
#           operam naqueles dados.
# - Subclasse:  Classe que herda de outra classe. Por exemplo, um
#           Empregado pode herdar de uma classe Pessoa. Qualquer
#           classe pode ter qualquer número de subclasses.
# - Superclasse:É parente de uma classe. Classe da qual a classe
#           atual herda. Por exemplo, Pessoa pode ser a superclasse
#           de Empregado. Em Python uma classe pode ter qualquer número
#           de superclasses.
# - Herança única ou múltipla: Refere-se ao número de superclasses da
#           qual uma classe herda. Por exemplo, Java é um sistema
#           de herança única, no qual uma classe pode apenas herdar 
#           de uma classe. Python, so contrário, é um sistema de 
#           herança múltipla em que uma classe pode herdar de uma ou mais
#           classes.
# Note que um conjunto de classes, envolvidas em uma hierarquia de herança,
# são normalmente nomeadas a partir da classe raiz (topo) da hierarquia,
# que no caso das classes definidas acima seria Pessoa.
# Tipos de Hierarquia
# Na maioria de sistemas OO, há dois tipos de hierarquia: uma refere-se 
# à herança(única ou múltipla), e a outra refere-se à instanciação(instantiation)
# hierarquia de herança já foi descrita, sendo o modo em que uma classe herda
# características de uma superclasse.
# A hierarquia de instanciação é relacioanada a instâncias ou objetos
# em vez de classes e é importante durante a execução do objeto.
# Há dois tipos de relação de instância: um indica uma relação do tipo 
# 'parte de' (part-of), enquanto a outra é relacionada a relação 'usando'
# (using)(é referida como uma relação 'é um'(is-a)).
#
#   is-a        Estudante -----> Pessoa
#
#   part-of     Motor----------> Carro
# 
# A diferença entre uma relação is-a e uma relação part-of
# é, frequentemente, confusa para novos programadores. O esquema 
# acima ilustra que um Estudante 'é um' tipo de Pessoa enquanto 
# um motos é 'parte de' um carro.
# Em Python, relações de herança são implementadas pelo mecanismo
# de subclasses. Em contraste, relações 'parte de' são implementadas
# usando atributos de instância em Python.
# O problema com classes, herança e relações 'é um' é que, na superfície,
# elas parecem capturar um conceito similar. No esquema seguinte, 
# as hierarquias todas capturam algum aspecto do uso da frase 'é um'.
# Entretanto, todas pretendem capturar uma relação diferente.
# A confusão é devido ao fato que em Inglês moderno, tendemos 
# sobreutilizar o temo 'é um'. No entanto, em classes de Python
# como Empregado e Pessoa e um objeto como Andrew são coisas diferentes.
# Podemos distinguir entre os diferentes tipos de relação sendo mais
# precisos sobre nossas definições em termos de uma linguagem
# de programação, como Python.
# 
#   is-a        Carro esportivo ----->  Carro   ----->  Veículo    
#
#   subclasse   Carro esportivo ----->  Carro   ----->  Veículo
#
#   Instância/  Porsche 911     ----->  Carro
#   Objeto

#----------------------------------------------------------
# O objeto de classe e herança
# Toda classe em Python extende uma ou mais superclasses. Isto
# é verdade mesmo para a classe Person definida abaixo:
#class Person:
#   def __init__(self,name,age):
#       self.name = name
#       self.age = age
# Isto ocorre pois, se não especificamos uma superclasse explicitamente,
# Python automaticamente adiciona a classe 'object' como classe parente.
# Assim o de cima é exatamente o mesmo que a definição de Person abaixo,
# que explicita a classe object como superclasse de Person:
#class Person(object):
#   def __init__(self,name,age):
#       self.name = name
#       self.age = age
# De fato, entre Python 2.2 e Python 3 era necessário usar
# a forma mais longa para garantir que as classes do 'novo estilo'
# estavam sendo usadas (oposto ao modo mais antigo em que classes
# eram definidas antes de Python 2.2).
#---------------------------------------------------
# A classe embutida 'object'
# A classe 'object' é a classe base(raíz) para todas as classes em
# Python. Ela tem métodos que, portanto, estão disponíveis para todos
# os objetos Python. Ela define um conjunto comum de métodos
# especiais e atributos intrínsecos. Os métodos incluem os métodos
# especiais __str__(), __init__(), __eq__()(equals) e __hash__()(método
# hash). Também define atributos como __class__, __dict__, __doc__ e __module__.
#---------------------------------------------------
# Propósito de subclasses
# As subclasses são usadas para refinar o comportamento e estrutura
# de dados de uma superclasse. Uma classe parente pode definir atributos
# e métodos genéricos/compartilhados; eles podem, então, ser herdados e 
# reusados por muitas outras (sub) classes que adicionam atributos e comportamentos
# específicos daquela subclasse.
# De fato, há apenar um pequeno número de coisas que uma subclasse deveria 
# fazer em relação a sua classe parente (superclasse). Se uma subclasse
# proposta não faz nenhuma dessas coisas, então sua classe parente escolhida
# não é a superclasse mais apropriada para usar.
# Uma subclasse deveria modificar o comportamento de sua classe parente 
# ou extender os dados armazenados por sua classe parente. Esta modificação
# deveria refinar a classe em um ou mais dos seguintes modos:
#   *   Mudanças ao protocolo externo ou interface da classe, isto é,
#       deveria extender o grupo de métodos ou atributos fornecidos pela classe.
#   *   Mudanças na implementação dos métodos; isto é, no modo em que o
#       comportamento fornecido pela classe está implementado.
#   *   Comportamento adicional que referencia o comportamento herdado.
# Se uma subclasse não fornece um ou mais dos citados acima, então
# está incorretamente colocada. Por exemplo, se uma subclasse implementa
# um novo conjunto de métodos, mas não refere nenhum dos atributos ou
# métodos da classe parente, então a classe não é realmente uma subclasse da parente.
#--------------------------------------------------
# Substituindo(overriding) métodos
# A substituição ocorre quando um método é definido em uma classe
# (por exemplo, Pessoa), e também em uma das subclasses(por exemplo,
# Empregado). Significa que instâncias de Pessoa e Empregado ambas respondem a 
# solicitações para este método ser executado mas cada um tem sua 
# própria implementação.
# Por exemplo, vamos assumir que definimos o método __str__() nessas classes.
# A definição em pseudocódigo de Person poderia ser:
#def __str__(self):
#   return 'Person ' + self.name + ' is ' + str(self.age)
# E em Employee poderia ser:
#def __str__(self):
#   return 'Employee(' + str(self.id) + ')'

# O método em Employee substitui a versão em Person para todas as instâncias
#-----------------------------------------------
# Extendendo métodos de superclasse
# No entanto, tivemos que duplicar o código de Pessoa para que Empregado
# pudesse converter os atributos 'nome' e 'idade' em strings. Podemos 
# evitar esta duplicação invocando o método da classe parente de dentro
# da versão da classe filha (como fizemos de fato para o inicializador
# __init__()).
# Por exemplo:
#class Person:
#   def __init__(self, name, age):
#       self.name = name
#       self.age = age
# 
#   def __Str__(self):
#       return self.name + ' is ' + str(self.age)
#
#class Employee(Person):
#   def __init__(self, name, age, id):
#       super().__init__(name,age)
#       self.id = id
#
#   def __str__(self):
#       return super().__str__() + '-id(' + str(self.id) + ')'

# Nesta versão do código a versão do método __str__() da classe Employee
# primeiro chama a versão da classe parente deste método e então adiciona
# a informação local à string retornada dela. Isto significa que apenas
# temos um local que converte name e age para uma string.
# ---------------------------------------
# Convenções de nomeação orientada por herança
# Há duas convenções de nomeação para se estar ciente com respeito
# a classes em Python. Elas são:
# * Convenção de barra única 
#       Métodos ou variáveis/atributos de instância (acessados
#       através de 'self.') cujos nomes começam
#       com uma única barra (_) são considerados como 'protegidos', 
#       isto é, são privados à classe mas podem ser acessados de qualquer
#       subclasse. Seu alcance é, portanto, a classe e subclasses.
# * Convenção de barra dupla
#       Métodos ou variáveis/atributos de instância (acessados por
#       'self.') cujos nomes começam com uma barra dupla deveriam ser 
#       considerados 'privados' àquela classe e não deveriam ser
#       chamadas de fora da classe. Isto inclui qualquer subclasse;
#       privado significa privado para a classe e apenas aquela classe.
# Qualquer identificador na forma __somename(pelo menos duas barras
# no início e no máximo uma barra no final) é textualmente substituído 
# com _classname __somename, onde classname é o nome da classe atual 
# sem a barra inicial.
# Python faz o que é chamado como codificação/distorção de nomes(name mangling)
# para fornecer algum suporte a métodos que começam com uma barra dupla.
# Esta distorção é feita sem consideração à posição sintática do identificador,
# de modo que pode ser usado para definir como privadas instâncias e 
# variáveis de classe, métodos, variáveis armazenadas em globais e mesmo 
# variáveis armazenadas em instâncias.
#----------------------------------------
# Python e herança múltipla
# Python suporta a ideia de herança múltipla, isto é, uma classe pode
# herdar de uma ou mais classes. A ideia é ilustrada no diagrama seguinte:
#                           object
#                             /\ 
#                            /  \
#                           /    \
#                         Car  |  Toy
#                           \      /
#                            \    /
#                             \  /
#                              \/
#                             ToyCar
#
# Neste caso, a classe 'ToyCar' herda da classe Car
# e da classe 'Toy'. Por sua vez, as classes Car e Toy
# herdam da (padrão) classe base 'object'.
# A sintaxe para definir herança múltipla em Python permite múltiplas
# superclasses serem listadas na lista de classes parente (definida 
# pelos braquetes após o nome da classe). Cada classe parente é separada
# por uma vírgula. A sintaxe é, assim:
#class SubClassName(BaseClassName1, BaseClassName2, ...
#BaseClassNameN):
#   class-body
#
# Por exemplo:
#
#class Car:
#   """ Car """
#
#class Toy:
#   """ Toy """ 
#
#class ToyCar(Car, Toy):
#   """ A Toy Car """
#
# Podemos dizer que a classe ToyCar herda todos os atributos(dados)
# e métodos(comportamento) definidos nas classes Car, Toy e object.
# Uma das questões fundamentais que isto gera é a herança de comportamento
# gerenciada dentro de uma hierarquia de herança múltipla. O desafio que
# herança múltipla possui é ilustrado adicionando alguns métodos à
# hierarquia de classes que estamos olhando. Neste exemplo adicionamos
# o método 'move()' para tanto a classe Car quanto Toy:
#                           object
#                             /\ 
#                            /  \
#                           /    \
#                         Car  |  Toy
#                        move()| move()
#                           \      /
#                            \    /
#                             \  /
#                              \/
#                             ToyCar
#
# A questão aqui é qual versão do método 'move()' será executado quando uma
# instância da classe ToyCar é instanciada e chamamos toy_car.move()?
# Isso ilustra uma versão simples do problema chamado 'herança diamante'.
# O problema é que com multiplas classes base da qual atributos
# ou métodos podem ser herdados, há frequentemente ambiguidade que precisa
# ser resolvida. Aqui, quando criamos uma instância da classe ToyCar, e
# chamamos o método move(), isto invoca o método herdade da clase base Car 
# ou da classe base Toy?
# A resposta é que em Python 3, uma procura 'largura primeiro'(breadth first)
# é usada para encontrar métodos definidos em classes parentes; isto
# significa que quando o método 'move()' é chamado em ToyCar, primeiro
# olharia em Car; então olharia em Toy se não pudesse encontrar um 
# método 'move()' em 'Car'; então olharia em Toy se não pudesse encontrar
# um método move() em Car. Se não puder encontrar o método em Carro nem
# em Toy olharia na classe object.
# Como resultado, irá encontrar a versão de Car primeiro e usar aquela versão.
# Isto é mostrado abaixo:
class Car:
   def move(self):
       print('Car-move()')

class Toy:
   def move(self):
       print('Toy - move()')

class ToyCar(Car, Toy):
   """ A Toy Car """

# A saída disto é:
# Car - move()
# Entretanto, se alteramos a ordem na qual ToyCar herda da classe 
# parente tal que trocamos Toy e Car:
class ToyCar(Toy, Car):
    """ A Toy Car """

#tc = ToyCar()
#tc.move()

# Então a classe Toy é procurada primeiro e a saída é alterada para
# Toy - move(). Isto mostra que a ordem em que uma classe herda de
# múltiplas classes é 'significante' em Python.
#----------------------------------
# Herança múltipla considerada prejudicial
# À primeira vista, herança múltipla em Python poderia parecer
# particularmente útil pois permite misturar múltiplos conceitos em 
# uma única classe muito facilmente e rapidamente. Isto é certamente 
# verdade e pode ser um recurso muito útil se usado com cuidado.
# Entretanto, a palavra 'cuidado' é usada aqui e deve ser levada em conta.
# Múltiplas heranças podem também ser muito perigosas e são um 
# tópico contingencioso para programadores e para aqueles projetando
# linguagens de programação. Poucas coisas em programação são inherentemente
# ruins mas herança múltipla pode resultar em um nível de complexidade
# (e comportamento inesperado) que pode prender desenvolvedores em nós.
# Parte do problema destacado por aqueles protestando contra herança 
# múltipla se resume à complexidade aumentada e ambiguidade que pode 
# ocorrer com árvores de heranças múltiplas que podem interconectar entre
# as classes diferentes. Um jeito de pensar nisso é que se uma classe herda
# de múltiplas classes, então aquela classe pode ter as mesmas classes
# múltiplas vezes na hierarquia de classes, isto pode tornar difícil 
# determinar qual versão de um método pode executar e isto poderia permitir 
# bugs ficarem intocados ou introduzir problemas esperados devido 
# diferentes interações entre os métodos. Isto é exacerbado quando os métodos
# herdados chamam super() usando o mesmo nome de método como:
#def get_data(self):
#   return super().get_data() + 'FData'
# O diagrama da pág. 226 mostra um exemplo de herança múltipla mais ou
# menos convolutos onde os nomes de classe A-X foram usadas de modo que não 
# há significado semântico atribuível para as classes herdadas. Classes 
# diferentes definem muitos métodos comuns (print_info()) e get_data())
# Todas as classes na hierarquia definem um método __str__()  que
# retorna o nome da classe; se a classe extende uma classe diferente da
# 'object', então a versão super de __str__() também é invocada.
# O código para a hierarquia de classe do diagrama á mostrado abaixo:

class A:
    def __str__(self):
        return 'A'
    def print_info(self):
        print('A')

class B:
    def __str__(self):
        return 'B'

class C:
    def __str__(self):
        return 'C'
    def get_data(self):
        return 'CData'

class D:
    def __str__(self):
        return 'D'
    def print_info(self):
        print('D')

class E:
    def __str__(self):
        return 'E'
    def print_info(self):
        print('E')

class F(C, D, E):
    def __str__(self):
        return super().__str__() + 'F'
    def get_data(self):
        return super().get_data() + 'FData'
    def print_info(self):
        print('F' + self.get_data())

class G(C, D, E):
    def __str__(self):
        return super().__str__() + 'G'
    def get_data(self):
        return super().get_data() + 'GData'

class H(F, G):
    def __str__(self):
        return super().__str__() + 'H'
    def print_info(self):
        print('H' + self.get_data())

class J(H):
    def __str__(self):
        return super().__str__() + 'J'

class I(A, J):
    def __str__(self):
        return super().__str__() + 'I'

class X(J, H, B):
    def __str__(self):
        return super().__str__() + 'X'

# Podemos agora usar a classe X em um programa simples Python:

x = X()
print('print(x):', x)
print('-' * 25)
x.print_info()

# A saída deste código simples é
#print(x): CGFHJX
#-------------------------
#HCDataGDataFData
#
# No entanto, se trocamos a ordem da herança de classe de 'H' de (F, G)
# para (G, F), então a saída muda.
#print(x): CFGHJX
#-------------------------
#HCDataFDataGData
#
# Isto é, claro, por causa da ordem de procura pela hierarquia de classes 
# agora é diferente.
# Note que esta mudança ocorreu não por causa de uma modificação à classe 
# que instanciamos (neste caso a X), mas à ordem de classes que uma de suas 
# parentes herda.
# Obviamente, Python não é ambíguo nem se confunde; é o desenvolvedor humano
# que pode se confundir e surpreender com o comportamento que é, então,
# apresentado. De fato, se tentar definir uma hierarquia de classes que
# Python não pode resolver em uma estrutura consistente, você será informado.
# O que pode ser confuso é que a habilidade de Python de produzir um
# estrutura consistente também pode ser dependente na ordem da herança.
# Por exemplo, se modificamos as classes que 'X' herda de forma que a 
# ordem é 'I' e 'J':
#class X(I, J):
#   def __str__(self):
#       return super().__str__() + 'X'
#
# Então isto compila e pode ser usado com o código anterior(apesar 
# que com saída diferente)
#print(x): AIX
#-------------------------
#A
#
# Entretanto, se mudarmos a ordem das classes parentes de modo que
# trocamos 'I' e 'J':
#class X(J, I):
#   def __str__(self):
#       return super().__str__() + 'X'
# 
# Recebos uma exeção TypeError:
#Traceback (most recent call last):
#File "multiple_inheritance_example.py", line 73, in <module>
#class X(J, I):
#TypeError: Cannot create a consistent method resolution
#order (MRO) for bases J, I
#
# Portanto, em geral, é necessário ter cuidado quando
# usando herança múltipla; mas isto não quer dizer que tais situações
# não são úteis. Em alguns casos, você quer que uma classe herde
# da parente que tem hierarquia completamente diferentes hierarquias
# e são completamente separadas uma da outra; tais situações herança
# múltipla pode ser muito útil - esses chamados 'comportamentos
# ortogonais' são uns dos melhores usos de herança múltipla e não 
# deveriam ser ignorados simplesmente devido preocupações de complexidade
# aumentada.
#
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
print('Pessoa')
p = Pessoa('John', 54)
print(p)
print('-'*25)

print('Empregado')
e = Empregado('Denise', 51, 7468)
e.aniversario()
print('e.calcular_salario(40):', e.calcular_salario(40))
print('-'*25)

print('Vendedor')
v = Vendedor('Phoebe', 21, 4712, 'UK', 30000.0)
v.aniversario()
print('v.calcular_salario(40):', v.calcular_salario(40))
print('v.bonus():', v.bonus())

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
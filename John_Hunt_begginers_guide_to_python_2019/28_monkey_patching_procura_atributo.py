# Capítulo 28 - Monkey Patching e Procura de atributo
# Monkey Patching se relaciona à habilidade em Python de estender
# a funcionalidade associada com uma classe/tipo na hora da execução.
# Apesar de não diretamente relacionado com Monkey Patching, como
# Python procura atributos e como este processo pode ser controlado
# é um aspecto útil de se entender. Em particular, como lidar com atributos 
# desconhecidos pode ser muito útil em controlar situações em que 
# Monkey Patching poderia ser usado para resolver uma incompatibilidade
# de atributo inicial.
#---------------------------------------------------
# Monkey Patching é a ideia que é possível acrescentar comportamento
# para um objeto existente, na hora da execução, para cumprir 
# algum requerimento que originalmente o tipo não cumpria. Isto
# pode acontecer, por exemplo, como não há exigência para uma classe
# de implementar um protocolo completamente; em muitos casos, uma 
# classe pode apenas implementar o mínimo de um protocolo exigido
# para cumprir as necessidades atuais; se, em um momento posterior,
# outros elementos de um protocolo são requeridos então eles podem 
# ser adicionados.
# Claro, se esta é uma ocorrência que provavelmente seja comum, então
# os recursos podem ser adicionados para a classe ser usada por todos;
# se não, então aqueles recursos podem ser adicionados dinamicamente
# na hora da execução de um objeto em si. Isto evita que a interface 
# pública do tipo se torne bagunçada com recursos/funcionalidades
# raramente utilizadas.
#------------------------------------------------------
# Como Monkey Patching funciona?
# Python é uma linguagem dinâmica que permite que a definição de um tipo
# mude na hora da execução. Como métodos em objetos são, de fato, 
# apenas outro atributo de uma classe, apesar de um que pode ser 
# executado, é possível adicionar novas funcionalidades para uma classe
# definindo novos atributos que irão manter referências ao novo comportamento.
# ----------------------------------------------
# Exemplo de Monkey Patching
# A seguinte classe, Bag, implementa um método de inicialização,
# __init__(), __str__() e __getitem__() usados para suportar
# acesso indexado a um tipo container(ou coleção).
#class Bag():
#    def __init__(self):
#        self.data = ['a', 'b', 'c']
#    def __getitem__(self, pos):
#        return self.data[pos]
#    def __str__(self):
#        return 'Bag(' + str(self.data) + ')'
#b = Bag()
#print(b) 

# Isto cria um objeto Bag e exibe os conteúdos. No entanto, se 
# tentarmos executar 'print(len(b))' vamos receber um erro:
# Traceback (most recent call last):
#File "Bag.py", line 12, in <module>
#print(len(b))
#TypeError: object of type 'Bag' has no len()
# Isto é porque a função len() espera que o objeto passado a ela 
# implemente o método __len__() que é usado para obter o comprimento.
# Neste caso, a classe Bag não implementa este método. No entanto,
# podemos definir uma função separada que se comporta do modo
# que precisaríamos a Bag para calcular seu comprimento, por exemplo:
#def get_length(self):
#    return len(self.data)
# Esta função pega um único parâmetro que chamamos self. Então usa
# este parâmetro para referenciar um atributo chamado data que
# usa len() para retornar o comprimento dos items associados ao dado.
# No presente, esta função não tem relação com a classe Bag a não
# ser o fato que assume o que quer que seja passado a ela terá um
# atributo chamado data, que a classe Bag tem.
# De fato, a função get_length() é compatível com qualquer classe que 
# tem um atributo chamado 'data' que pode ser usado para determinar
# seu comprimento. Podemos, agora, associá-la com a classe Bag;
# isto pode ser feito atribuindo a referência da função(na prática, 
# seu nome), para um atributo apropriado na classe Bag. Como a função
# len() espera uma classe para implementar o método __len__(), podemos
# atribuir a função get_length() para o atributo __Len__(). Isto
# efetivamente adiciona um novo método para a classe Bag com a 
# assinatura __len__(self):
# Monkey patching
#Bag.__len__ = get_length
# Agora podemos chamar:
#print(len(b))
# Agora fizemos o Monkey Patch da classe Bag de modo que o método
# faltando se torna disponível.
#-----------------------------------------
# O parâmetro self
# Uma das razões Monkey Patching funciona é porquê todos os métodos
# recebem o primeiro parâmetro especial (chamado self por convenção)
# representando o próprio objeto. Isto significa que qualquer função
# que trata o primeiro parâmetro como sendo uma referência para um
# objeto pode potencialmente ser usado para definir um método em uma
# classe. Se uma função não assume que o primeiro parâmetro é uma
# referência para um objeto(o que guarda o método) então não pode
# ser usado para adicionar uma nova funcionalidade para uma classe. 
#------------------------------------------
# Adicionando novos dados para uma classe
# Monkey patching não é apenas limitado para uma funcionalidade; é
# também possível adicionar novos dados de atributos para uma classe.
# Por exemplo, se queremos cada Bag tenha um nome, então poderíamos
# adicionar um novo atributo para a classe que tenha seu 'name':
#Bag.name = 'My Bag'
#print(b.name)
# Que exibe a string My Bag que agora age como um valor padrão
# do nome de qualquer Bag. Uma vez o atributo é adicionado podemos
# então mudar o nome desta instância particular de uma Bag:
# Por exemplo, se estendemos o exemplo acima:
#Bag.name = 'My Bag' 
#print(b.name)

#b.name = 'Johns Bag'
#print(b.name)

#b2 = Bag()
#print(b2.name)
#------------------------------------------------
# Procura de atributo
# Como mostrado acima, Python é bastante dinâmico e é fácil adicionar
# atributos e métodos para uma classe, mas como isto funciona?
# É válido considerar como Python controla a procura de método e
# atributo por um objeto.
# Classes em Python podem ter tanto atributos orientados a classe
# quanto instância, por exemplo, a seguinte classe Student tem um 
# atributo de classe count (que é associado com a própria classe)
# e um atributo de instância ou objeto name. Assim, cada instância da
# classe Student terá seu próprio atributo name.
#class Student:
#    count = 0
#    def __init__(self, name):
#        self.name = name
#        Student.count += 1
# Sempre que uma instância da classe Student é criada, o atributo 
# Student.count aumentará em 1.
# Para controlar estes atributos, Python mantém dicionários internos;
# um para atributos de classe e um para atributos de objeto. Estes
# dicionários são chamados __dict__ e podem ser acessados ou pela
# classe <class>.__dict__ (para atributos de classe) ou de uma
# instância da classe <instance>__dict__ (para atributos de objeto).
# Por exemplo:
#student = Student('John')
# Dicionário de atributo de classe:
#print('Student.__dict__:', Student.__dict__)
# Dicionário de atributo de instância/objeto:
#print('student.__dict__:', student.__dict__)
# Para procurar um atributo, Python faz o seguinte para atributos de classe:
#   1.  Procura o Dicionário de classe por um atributo
#   2.  Se o atributo não é encontrado no passo 1 então procura os 
#       dicionários de classes pais
# Para atributos de objeto, Python primeiro procura o dicionário de 
# instância e repete os passos acima, tomando assim esses passos:
#   1.  Procurar o dicionário do objeto/instância;
#   2.  Se o atributo não foi encontrado no passo 1, procurar no
#       dicionário da classe pelo atributo.
#   3.  Se o atributo não é encontrado no passo 2, então procurar
#       no dicionário da classe pai.

#print('Student.count:', Student.count) # class lookup
#print('student.name:', student.name) # instance lookup
#print('student.__dict__:', student.__dict__)
#print('student.count:', student.count) # lookup finds class attribute

# Como os dicionários usados para guardar os atributos de classe e 
# objeto são apenas dicionários, eles fornecem outro jeito de acessar 
# os atributos de uma classe como Student. Isto é, você pode escrever
# código que irá acessar um valor de atributo usando o __dict__ apropriado,
# em vez da mais usual notação ponto, por exemplo, o seguinte é equivalente:
# procura de classe
#print('Student.count:', Student.count)
#print("Student.__dict__['count']:", Student.__dict__['count'])

# procura de instância/objeto
#print('student.name:', student.name)
#print("student.__dict__['name']:", student.__dict__['name'])

# Em ambos os casos, o resultado final é o mesmo, ou o atributo de classe
# count é acessado ou o atributo de objeto name é acessado.
# Entretanto, acessar atributos por __dict__ não ativa um processo de
# busca; em vez disso, é uma procura direta no container do dicionário
# associado. Assim, se você tentar acessar uma variável de classe pelo
# __dict__ do objeto, então você terá um erro. Isto é ilustrado abaixo, 
# onde tentamos acessar a variável de classe count pelo objeto student
# Tenta procurar uma variável de classe através de um objeto
#print('student.name:', student.name)
#print("student.__dict__['count']:", student.__dict__['count'])
#-----------------------------------------------
# Lidando com acesso de atributo desconhecido
# Monkey patching é muito flexível e útil quando você sabe o que
# precisar fornecer; entretanto, o que acontece quando uma referência
# a um atributo (ou invocaçâo de método) ocorre quando não é esperada? 
# Por padrão, um erro é gerado como o AtributeError:
#student = Student('John')
#res1 = student.dummy_attribute
#print('p.dummy_attribute:', res1)
#
# O que gera um erro de atributo AtributeError:
# Traceback (most recent call last):
#File "d:\programacao\python-intro\John_Hunt_begginers_guide_to_python_2019\28_monkey_patching_procura_atributo.py", line 188, in <module>
#   res1 = student.dummy_attribute
#           ^^^^^^^^^^^^^^^^^^^^^^^
#AttributeError: 'Student' object has no attribute 'dummy_attribute'
#
# Você pode pegar AtributeError se quiser; mas isto significa cercar
# o código em um bloco try. Uma alternativa é definir um método chamado
# __getattr__(); este método será chamado quando um atributo não é 
# encontrado no __dict__ do objeto(e classe). Este método pode, então, 
# realizar qualquer ação é apropriada como fazer o registro(logging)
# de uma mensagem ou exibir um valor padrão etc.
# Por exemplo, se modificamos a definição da classe Student para incluir
# um método __getattr__() de modo que um valor padrão é retornado:  
#class Student:
#    count = 0
#    def __init__(self, name):
#        self.name = name
#    Student.count += 1
    # Method called if attribute is unknown
#    def __getattr__(self, attribute):
#        print('__getattr__: ', attribute)
#        return 'default'

# Agora, ao tentar acessar dummy_attribute em um objeto student vamos
# receber a string'default':

#student = Student('John')
#res1 = student.dummy_attribute
#print('p.dummy_attribute:', res1)

# Perceba que o método __getattr__() é apenas chamado para atributos
# desconhecidos como Python procura primeiro em __dict__ e, assim,
# se o atributo é encontrado, não é feita a chamada para __getattr__().
# Além disso, se um atributo é acessado diretamente do __dict__, então
# o método __getattr__() nunca é invocado.
#-------------------------------------------
# Resolvendo invocações de método desconhecidos
# __getattr__() também é invocado se um método desconhecido é chamado.
# Por exemplo, se chamamos dummy_method() em um objetod Student, então
# um erro é levantado (novamente será AttributeError). Entretanto, se
# definimos um método __getattr__() podemos retornar uma referência a
# um método para usar um padrão. Por exemplo, se modificamos o método 
# __getattr__() para retornar uma referência a um método:
#class Student:
#    count = 0
#    def __init__(self, name):
#        self.name = name
#        Student.count += 1
#    # Method called if attribute is unknown
#    def __getattr__(self, attribute):
#        print('__getattr__: ', attribute)
#        return self.my_default
#    def my_default(self):
#        return 'default'
# Agora, quando um método indefinido é invocado, __getattr__() será
# chamado. Este método retornará uma referência a my_default().
#student = Student('John')
#res2 = student.dummy_method()
#print('student.dummy_method():', res2)
#--------------------------------------------
# Interceptando a busca de atributo
# Também é possível sempre interceptar buscas de atributo usando a
# notação ponto implementando o método __getattribute__(). Este método
# sempre será chamado em vez de procurar atributos no dicionário do
# objeto. O método __getattr__() será apenas chamado se for gerado
# um AttributeError ou se o método __getattribute_() chamá-lo explicitamente.
# O método __getattribute__() deveria, portanto, retornar um valor de
# atributo(que pode ser um valor padrão) ou gerar um AttributeError
# se apropriado. É importanto evitar implementar código que chamará 
# si próprio recursivamente (por exemplo, chamar self.name dentro
# de __getattribute__() resultará em uma chamada recursiva dessa função). 
# Para evitar isto a implementação do método deveria ou acessar a pasta
# __dict__ ou chamar o método __getattribute__() de classes base.
# Um exemplo é dado abaixo de um método __getattribute__() simples
# que recorda a chamada de um método e então passa a invocação para a
# implementação da classe base:
#class Student:
#    count = 0
#    def __init__(self, name):
#        self.name = name
#        Student.count += 1
#    # Method called if attribute is unknown
#    def __getattr__(self, attribute):
#        print('__getattr__: ', attribute)
#        return 'default'
    # Method will always be called when an attribute
    # is accessed, will only called __getattr__ if it
    # does so explicitly or if an AttributeError is raised
#    def __getattribute__(self, name):
#        print('__getattribute__()', name)
#        return object.__getattribute__(self, name)
#    def my_default(self):
#        return 'default'
#student = Student('Katie')
#print('student.name:', student.name) # instance lookup
#res1 = student.dummy_attribute # invoke missing attribute
#print( ' student.dummy_attribute:', res1)

# Este código retorna:
#__getattribute__() name
#student.name: Katie
#__getattribute__().dummy_attribute
#__getattr__:  dummy_attribute
#student.dummy_attribute: default

# Onde __getattribute__() é invocado para student.name e student.dummy_attribute
# mas __getattr__() é invocado apenas quando dummy_attribute é acessado.
# __getattribute__() é apenas invocado para acesso a atributos e não para
# métodos, diferente de __getattr__().
#-----------------------------------------------
# Interceptando a atribuição de um atributo
# Também é possível interceptar a atribuição de atributos de objeto/instância
# quando a notação ponto está sendo usada. Isto pode ser feito implementando
# o método __setattr__(). Este método é invocado em vez da atribuição.
# O método __setattr__() pode realizar qualquer ação requerida incluindo
# salvar o valor fornecido. Entretanto, para fazer isso deveria ou inserir
# o valor diretamente no dicionário do objeto ou, preferivelmente, chamar
# o método da classe base __setattr__(), por exemplo, object.__setattr__(self, name, value)
# como mostrado abaixo:
class Student:
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1          
    # Method will always be called when an attribute is set
    def __setattr__(self, name, value):
        print('__setattr__:', name, value)
        object.__setattr__(self, name, value)
    
student = Student('John')
student.name = 'Bob'
print('student.name:', student.name) # instance lookup
# Gerando: 
#__setattr__: name John
#__setattr__: name Bob
#student.name: Bob
# Algumas coisas para se observar nessa saída:
#   * Primeiro, a atribuição de name para o objeto da classe Student
#       dentro do método __init__() também invoca o método __setattr__().
#   * Segundo, a atribuição da variável de classe count não invoca 
#       o método __setattr__().
#   * Terceiro, a atribuição de student.name obviamente invoca __setattr__().

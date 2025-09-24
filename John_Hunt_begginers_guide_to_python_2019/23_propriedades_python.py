# Capítulo 23 - Propriedades Python
# Muitas linguagens orientadas a objetos tem o conceito explícito
# de encapsulação; isto é, a habilidade de esconder dados dentro de um 
# objeto e apenas fornecer portais específicos para aqueles dados.
# Estes portais são métodos definidos para pegar (get) ou atribuir(set)
# o valor de um atributo. Isto permite mais controle sobre o acesso
# ao dado; por exemplo, é possível checar que apenas um inteiro
# positivo acima de zero, mas abaixo de 120, é usado para a idade
# de uma pessoa, etc.
# Em muitas linguagens como Java e C#, atributos pode ser escondidos
# de acesso externo usando palavras-chave específicas (como private)
# que indicam que os dados deveriam ser tornados privados ao objeto.
# Python não tem explicitamente o conceito de encapsulação; em vez disso
# depende de duas coisas; uma convenção padrão usada para indicar que um 
# atributo deveria ser considerado privado e um conceito chamado
# uma propriedade que permite atribuidores (setter) e pegadores (getter)
# serem definidos para um atributo.
#---------------------------------------------
# Atributos em Python
# Todos os atributos de um objeto são avaliáveis publicamente em 
# Python; isto é, eles são todos visíveis a qualquer código usando 
# o objeto. Por exemplo, dada a seguinte definição da classe Pessoa
# ambos 'nome' e 'idade' são parte da interface pública da classe Pessoa;
#class Pessoa:
#    def __init__(self, nome, idade):
#        self.nome = nome
#        self.idade = idade
#
#    def __str__(self):                          
#        return str(self.nome) + ' tem ' + str(self.idade) + ' anos de idade.'

# Como 'nome' e 'idade' são parte da interface pública da classe 
# significa que podemos escrever
#pessoa = Pessoa('John', 54)
#pessoa.nome = 42
#pessoa.idade = -1
#print(pessoa)

# Podemos indicar que queremos tratar idade e nome como privados
# ao objeto prefixando os nomes de atributo com uma barra ('_')
# como mostrado abaixo:
#class Pessoa:
#    def __init__(self, nome, idade):
#        self._nome = nome
#        self._idade = idade
#
#    def __str__(self):                          
#        return (str(self._nome) + ' tem ' + str(self._idade) +  
#    ' anos de idade.')

# Isto diz a Python que queremos considerar _nome e _idade como sendo
# privados. Entretanto, deveria ser notado que isto é apenas uma convenção; 
# apesar de fortemente aderida. Não há nada impedindo que alguém escreva:
#pessoa = Pessoa('John', 54)
#pessoa._idade = -1
#print(pessoa)
# No entanto, o desenvolvedor da classe Pessoa tem a liberdade de 
# mudar o interno da classe (como _idade) sem aviso e a maioria
# consideraria que qualquer um que ignorou a convenção e agora
# tem um problema pode culpar só a si próprio.
#----------------------------------------------------
# Métodos de estilo de definidores e pegadores
# Isso gera a questão: como obtemos o 'nome' e 'idade' de uma 
# Pessoa de um modo aceitável?
# A resposta é que um desenvolvedor deveria fornecer métodos
# de pegadores e definidores que podem ser usados para acessar os valores.
# Podemos atualizar a classe Pessoa com alguns métodos pegadores
# e um únido método definidor:

#class Pessoa:
#    def __init__(self, nome, idade):
#        self._nome = nome
#        self._idade = idade
#
#    def get_idade(self):
#        return self._idade
#
#    def set_idade(self, nova_idade):
#        if (isinstance(nova_idade, int) and nova_idade > 0 and
#            nova_idade < 120):
#            self._idade = nova_idade
#
#    def get_nome(self):
#        return self._nome
#    def __str__(self):                          
#        return (str(self._nome) + ' tem ' + str(self._idade) +  
#    ' anos de idade.')

# Os dois métodos pegadores tem o formato de get_ seguidos pelo
# nome do atributo que eles estão pegando. Assim, temos
# get_idade e get_nome. Tipicamente, tudo que pegadores fazem é retornar
# o atributo sendo usado (como é o caso aqui).
# O único método atribuidor é um pouco diferente; isto valida 
# os dados que foram fornecidos para checar que são apropriados (isto
# é, um inteiro usando isinstance(nova_idade, int) e que é um valor
# acima de zero mas abaixo de 120). Apenas se os dados passarem estas 
# checagens são usados como o novo valor da idade da pessoa, por exemplo,
# se tentarmos definir uma idade como -1:
#person = Pessoa('John', 54)
#person.set_idade(-1)
#print(person)
# OUTPUT: John tem 54 anos de idade.
# Como -1 não obedece às definiçoes de set_idade a slteração é ignorada.
# Deve-se notar que isso poderia ser considerado como uma falha
# silenciosa; isto é, tentamos definir a idade a falhamos mas 
# ninguém sabe disso. Em muitos casos, em vez de falhar silenciosamente,
# preferiríamos notificar alguém do erro fornecendo alguma forma de objeto
# Erro; isso será discutido próximo capítulo.
# Você poderia então perguntar onde está o atribuidor para o atributo _nome?
# A resposta é que queremos fazer o atributo _nome um atributo apenas de
# leitura e, portanto, não criamos um método do estilo atribuidor.
# Este é um idioma comum seguido em Python - você pode ter atributos 
# leitura-escrita e atributos apenas-leitura dependendo se eles tem
# métodos atribuidores e pegadores ou não. Também é possível escrever
# atributos escrever-apenas, mas é muito raro e tem poucos casos de utilização.
# ----------------------------------------------
# Interface pública de propriedades
# Apesar de agora termos uma interface mais formal para os atributos 
# armazenados por uma instância da classe Pessoa, é um pouco desajeitada:
#pessoa = Pessoa('John', 54)
#print(pessoa)
#print(pessoa.get_nome())
#print(pessoa.get_idade())
# Acabamos escrevendo uma quantidade maior de código e, apesar de ter
# um argumento que torna o código mais óbvio, é um pouco prolixo.
# Para contornar isto um conceito conhecido como Propriedades foi
# introduzido em Python 2.2. Na sintaxe original para isto era 
# possível adicionar uma linha de código adicional à classe que 
# dizia a Python que você queria fornecer uma nova propriedade
# e que métodos específicos deveriam ser usados para atribuir e obter
# os valores desta propriedade.
# A sintaxe para definir uma propriedade deste modo é:
#
# <property_name> = property(fget=None, fset=None, fdel=None, doc=None)
# 
# Onde fget indica a função pegadora, fset a função atribuidora,
# fdel a função a ser usada para deletar um valor e doc fornece
# a documentação da propriedade (sendo todos eles opcionais).
# Podemos modificar nossa classe Pessoa de forma que 'idade' é, agora
# uma propriedade (note que uma convenção comum é que o atributo
# é nomeado _idade, os métodos são nomeados get_idade e set_idade e
# a propriedade será chamada idade):
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def get_idade(self):
        return self._idade
    def set_idade(self, nova_idade):
        if (isinstance(nova_idade, int) and nova_idade > 0 and
            nova_idade < 120):
            self._idade = nova_idade
    idade = property(get_idade, set_idade,doc='Uma propriedade idade')

    def get_nome(self):
        return self._nome
    nome = property(get_nome, doc='Uma propriedade nome')

    def __str__(self):                          
        return (str(self._nome) + ' tem ' + str(self._idade) +  
    ' anos de idade.')

person = Pessoa('John', 54)
print(person)
print(person.idade)
print(person.nome)
person.idade = 21
print(person)

# Note que agora podemos escrever pessoa.idade e pessoa.idade = 21; em
# ambos os casos estamos acessando a propriedades idade que resulta no método
# get_idade() e set_idade() sendo executados, respectivamente.
# Assim, o atribuidor ainda está protegendo a atualização para o 
# atributo adjacente _idade que é, de fato, usado para salva o valor atual.
# Também note que, se um método não é fornecido para um dos fget, fset, fdet
# métodos, isto não é um erro; apenas indica que a propriedade não 
# suporta aquele tipo de acessador. Assim, a propriedade nome é uma 
# propriedade apenas de leitura pois não define o método atribuidor.
# Um método deletor pode ser usado para liberar a memória associada com 
# atributo; no caso de um int não é necessário, mas pode ser necessário
# para tipos mais complexos, definidos pelo usuário.
# Podemos, portanto, escrever:
#def del_nome(self):
#       del self.nome
#nome = property(get_name, fdel=del_name, doc='Uma propriedade de nome)
# Note que estamos usando um palavra-chave de referência para o método
# deletor como pulamos o método atribuidor e não podemos, portanto,
# depender de argumentos posicionais.
#------------------------------------------
# Definições mais concisas de propriedades
# O exemplo acima funciona, mas ainda é um pouco prolixo; enquanto
# isto está no lado do escritor da classe, ainda parece meio pesado.
# Para superar isso, uma opção mais concisa está disponível desde Python 2.4.
# Esta abordagem usa o que são conhecidos como decoradores. Decoradores 
# representam metadados (isto é, informação sobre seu código que o interpretador 
# Python pode usar para entender o que você quer fazer com certas coisas).
# Python 2.4 introduziu três novos decoradores: @property, @<property-name>.setter
# e @<propertyname>.deleter. Estes decoradores são adicionados ao início da
# definição de um método para indicar que o método deveria ser usado para
# fornecer acesso a uma propriedade (e definir aquela propriedade), definir um
# atribuidor para a propriedade ou um deletor para a propriedade.
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    @property
    def age(self):
        """ The docstring for the age property """
        print('In age method')
        return self._age
    @age.setter
    def age(self, value):
        print('In set_age method')
        if isinstance(value,int) & value > 0 & value < 120:
            self._age = value
    @property
    def name(self):
        print('In name')
        return self._name
    @name.deleter
    def name(self):
        del self._name
    def __str__(self):
        return 'Person[' + str(self._name) +'] is ' + str(self._age)

# Note três coisas importantes neste exemplo:
#   *   O nome dos métodos não são mais set_age e get_age; em
#       vez disso, ambos métodos são, agora, apenas age e o
#       decorador diferencia seus papeis. Note também que não
#       precisamos mais ter uma declaração separada que declara a
#       propriedade, agora está implícito no uso do decorador @property
#       e no nome do método associado.
#   *   O decorador @property é usado para definir o nome da propriedade
#       (neste caso, idade) e definir decorações posteriores que serão
#       nomeadas pela propriedade com um elemento .setter ou .deletter
#   *   A string de documentação agora é definida no método associado
#       com o decorador @property.
p1 = Person('Joao', 24)
print(p1)
print(p1.age)
p1.age = 25     # define novo valor à idade pela existência do atribuidor
print(p1.age)
del p1.name     # deleta o nome devido a propriedade criada
print(p1.name)  # resulta em erro, pois o nome foi deletado

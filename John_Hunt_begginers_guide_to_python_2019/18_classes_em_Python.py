# Classes em Python
# Em Python, tudo é um objeto e, portanto, exemplo de um tipo de classe
# de coisas. Por exemplo, inteiros são um exemplo da classe 'int',
# números reais exemplos de 'float' etc. No entanto, não se é 
# restrito apenas a tipos(classes) pré-construídos (build-in types);
# também é possível criar classes definidas pelo usuário. Estas
# podem ser usadas para criar suas próprias estruturas de dados,
# próprios tipos de dados, próprias aplicações etc.
#----------------------------------------------------------------
# Definições de classe
# A definição de uma classe em Python tem o seguinte formato:
#class nameOfClass(SuperClass) :
#    _init_
#    attributes
#    methods

# Mas você deve notar que pode alterar a ordem da definição
# dos atributos e métodos conforme requerido em uma classe.
# O seguinte código é um exemplo da definição de uma classe:
print(' '*50)
print('#'*50)
#######################################################3
class Pessoa:
    """ Um exemplo de classe que salva
        o nome e idade de uma pessoa"""
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):                          
        return self.nome + ' tem ' + str(self.idade) + ' anos de idade.'
    
    def aniversario(self):
        print('Feliz aniversário! Você tinha', self.idade, 'anos,')
        self.idade += 1
        print('agora você tem', self.idade, 'anos.')

    def calcular_pagamento(self, horas_trabalhadas):
        taxa_de_pagamento = 7.50
        if self.idade >= 21:
            taxa_de_pagamento += 2.50
        return horas_trabalhadas*taxa_de_pagamento
    
    def e_adolescente(self):
        return self.idade < 20
    
#######################################################    
# Apesar de não ser uma regra mandatória nem rápida, é comum definir uma
# classe em um arquivo nomeado pela classe. Por exemplo, o código acima
# poderia ser salvo em um arquivo chamado Pessoa.py; isto torna mais fácil
# encontrar o código associado a uma classe.
# A classe 'Pessoa' tem dois atributos (ou variáveis de instância)
# chamados 'nome' e 'idade'. Também há um método especial definido chamado
# __init__. Este é um inicializador(também chamado construtor) para classe.
# Ele indica quais dados devem ser fornecidos quando uma instância 
# da classe Pessoa é criada e como os dados são salvos internamente.
# Neste caso, um 'nome' e uma 'idade' devem ser fornecidos quando uma
# instância da classe Pessoa é criada.
# Os valores fornecidos serão, então, salvos dentro de uma instância
# da classe (representada pela variável especial 'self') em 
# variáveis/atributos de intâncisa self.nome e self.idade. Note que 
# os parâmetros do método __init__ são variáveis locais e desaparecerão
# quando o método finalizar, mas self.nome e self.idade são variáveis
# de instância e existirão enquanto o objeto estiver avaliável.
# Vamos olhar à variável especial self. Este é o primeiro
# parâmetro passao em qualquer método. No entanto, quando um método
# é chamadao, não passamos um valor para este parâmetro; Python o faz.
# Ele é usado para representar o objeto dentro do qual o método está
# executando. Ele fornece o contexto dentro do qual o método executa
# e permite ao método acessar os dados guardados pelo objeto. Portanto,
# self é o objeto em si.
# Um método é o nome dado para o comportamento que está conectado
# diretamente à classe Pessoa; não é uma função livre mas parte da 
# definição da classe Pessoa. Historicamente, esse nome vem da 
# linguagem Smalltalk, usada inicialmente para simular uma planta
# de produção e um método representava algum comportamento que poderia 
# ser usado para simular uma mudança na linha de produção.
#--------------------------------------------------------
# Criando exemplos da Classe Pessoa
# Novas instâncias/objetos da classe Pessoa podem ser criados usando
# o nome da classe e passando valores a serem usados para os parâmetros
# do método de inicialização. Por exemplo:
p1 = Pessoa('João', 25)
p2 = Pessoa('Maria', 16)
# As duas variáveis guardam instâncias (ou exemplos) separados
# da classe Pessoa. Cada instância também tem seu identificador
# único - que mostra que mesmo se os valores de atributo forem
# os mesmos para dois objetos, ainda são instâncias separadas
# de uma determinada classe. Este identificador pode ser acessado
# usando a função id():
#print('id(p1):', id(p1))
#print('id(p2):', id(p2))
#------------------------------------------------------
# Tenha cuidado com atribuições
# Dado que no exemplo acima, p1 e p2 referenciam instâncias diferentes
# da classe Pessoa; o que acontece quando p1 ou p2 são atribuídos a
# outra variável?
px = p1
# O que acontece é que p1 não é o objeto em si, mas o 'endereço'
# do objeto Pessoa. Ao atribuir px = p1, fazemos uma cópia completa
# do endereço do objeto Pessoa de p1. Isto pode ser observado olhando
# para os identificadores de p1 e px:
#print('id(p1):', id(p1))
#print('id(px):', id(px))
# Por conseguinte, se mudarmos a atribuição de p1 agora, por exemplo
# fazendo p1 = p2, px não tem sua atribuição alterada, continua
# se referindo ao antigo objeto a que p1 se referia, enquanto p1 agora 
# se refere ao objeto atribuído a p2, assim como o próprio p2.
#------------------------------------------------------
# Exibindo(Printing) objetos
# Se usamos, agora, a função print() para exibir os objetos guardados por
# p1 e p2, vamos obter o nome da classe e o número hexadecimal de onde
# a classe está guardada na memória. 
#print(p1)
#print(p2)
# Acessando atributos de objeto
# Podemos acessar os atributos de p1 e p2 usando a notação ponto(dot).
# Ela nos permite seguir a variável guardando o objeto com um ponto 
# e o atributo de interesse. Por exemplo, para acessar o nome de um
# objeto Pessoa usamos p1.nome ou sua idade, p1.idade.
#print(p1.nome, 'é', p1.idade)
#print(p2.nome, 'é', p2.idade)
# Também podemos atualizar os atributos de um objeto diretamente,
# por exemplo:
#p1.nome = 'Henrique'
#p1.idade = 24
#print(p1.nome, 'é', p1.idade)
# Veremos em um capítulo posterior (Propriedades Python) que podemos restringir
# acesso a estes atributos tornando-os propriedades.
#----------------------------------------------------------------
# Definindo uma representação de string padrão
# Na seção anterior exibimos a informação do objeto da instância
# da classe Pessoa acessando seus atributos 'nome' e 'idade'.
# Entretanto, precisávamos conhecer a estrutura interna da classe
# Pessoa para exibir seus detalhes. Isto é, precisávamos saber
# que existiam atributos chamados 'nome' e 'idade' avaliáveis na classe.
# Podemos fazer a classe Pessoa converter a si mesma em uma string para
# ser exibida definindo um método que pode ser usado para converter
# um objeto em uma string para exibição.
# Este método é o método __str__. Deste método, é esperado o retorno
# de uma string que pode ser usada para representar a informação apropriada
# de uma classe. A assinatura do método é:
#def __str__(self)
# Métodos iniciando com a barra dupla ('__') são, por convenção,
# considerados especiais em Python e veremos muitos desses métodos posteriormente.
# Por hora, vamos focar apenas no método __str__().
# Podemos adicionar este método à classe Pessoa e ver como ele afeta a 
# saída gerada ao usar a função print().
#print(p1)
# Note que no método __str__ acessamos os atributos nome e idade
# usando o parâmetro self passado para o método pelo Python. Também note
# que é necessário converter o número 'idade' em uma string. Isto é pelo
# operador '+' fazer concatenação de strings, a não ser que um dos operandos
# seja um número, o que vai dear errado se o outro operando for uma string.
#----------------------------------------------------------
# Fornecendo um comentário de classe
# É comum fornecer um comentário para uma classe definindo o que a classe
# faz, seu propósito e quaisquer pontos de nota sobre ela.
# Isto pode ser feito fornecendo uma docstring para a classe logo após
# o cabeçalho da declaração da classe; pode-se usar aspas triplas para 
# criar múltiplas linhas.
# A docstring é acessível através do atributo __doc__ da classe. A
# ideia é tornar informação avaliável aos usuários da classe, mesmo
# na hora da execução. Também pode ser usado por IDE's para fornecer
# informação em uma classe.
#---------------------------------------------------------
# Adicionando um método aniversário
# Vamos agora adicionar um comportamento para a classe Pessoa. No exemplo
# seguinte, definimos um método chamado aniversário() que não pega parâmetros
# e aumenta o atributo idade em 1.
#def aniversario(self):
#   print('Feliz aniversário! Você tinha', self.idade, 'anos,')
#   self.idade += 1
#   print('Agora você tem', self.idade, 'anos.')
# Note que, novamente, o primeiro parâmetro passado para o método aniversario
# é self. Isto representa a instância (o exemplo da classe Pessoa) com o 
# qual este método será usado. Se criamos, agora, uma instância da classe
# Pessoa e chamamos aniversario() nela, a idade vai aumentar em 1, por exemplo:
#p3 = Pessoa('Gui', 28)
#print(p3)
#p3.aniversario()
#print(p3)
#--------------------------------------------------------------
# Definindo métodos de instância
# O método aniversário() mostrado acima é um exemplo do que é conhecido como
# método de instância; isto é, está ligado a uma instância da classe.
# Naquele caso, o método não pegou nenhum parâmetro, nem retornou
# nenhum parâmetro; no entanto, métodos de instância podem fazer ambos.
# Por exemplo, vamos assumir que a classe Pessoa também será usada
# para calcular o quanto alguém deveria ser pago. Vamos também assumir que
# a taxa é de R$ 7,50 se você tem menos de 21 anos, mas que tem 2,50 extra
# se tem 21 anos ou mais.
# Poderíamos definir um método de instância que irá pegar como entrada o
# número de horas trabalhadas e retornará a quantidade que alguém deveria
# ser pago:
#def calcular_pagamento(self, horas_trabalhadas):
#   taxa_de_pagamento = 7.50
#   if self.idade >= 21:
#       taxa_de_pagamento += 2.50
#   return horas_trabalhadas*taxa_de_pagamento
# Podemos invocar este método usando a notação ponto, por exemplo:
#pagamento = p2.calcular_pagamento(40)
#print('Pagamento', p2.nome, pagamento)
#pagamento = p1.calcular_pagamento(40)
#print('Pagamento', p1.nome, pagamento)
# Outro exemplo de um método de instância definido na classe Pessoa é
# e_adolescente(). Este método não pega parâmetros, mas retorna um valor
# Booleano dependendo do atributo 'idade':
#def e_adolescente(self):
#   return self.idade < 20
#---------------------------------------------------------------------
# A palavra-chave del
# Tendo, em algum ponto, criado um objeto de algum tipo (seja bool, int
# ou um tipo definido pelo usuário como Pessoa), pode ser necessário
# mais tarde deletar aquele objeto. Isto pode ser feito com a palavra-chave
# 'del'. Ela é usada para deletar objetos, o que permite que a memória 
# que estava sendo ocupada seja recuperada e usada por outras partes
# do programa. Por exemplo:
#p1 = Pessoa('João', 25)
#print(p1)
#del p1
# Não é necessário usar 'del' pois definir p1 como 'None' terá o mesmo 
# efeito. Além disso, so o código acima foi definido dentro de uma função
# ou método, então p1 terminará de existir assim que a função/método terminar,
# tendo o mesmo efeito de deletar o objeto.
#----------------------------------------------------
# Gerenciamento automático de memória
# A criação e exclusão de objetos (e sua memória associada) é administrada
# pelo Python Memory Manager. De fato, a provisão de um gerenciador de
# memória é uma das vantagens de Python ao comparar com linguagens como
# C e C++. 
# A maioria dos problemas associados com alocação de memória em linguagens 
# como C++ ocorre pois os programadores devem não apenas se concentar 
# na (geralmente complexa) lógica da aplicação, mas também no gerenciamento
# de memória. Eles devem garantir que atribuíram apenas a memória necessária
# e desatribuem quando não é mais necessário.
# ----------------------------------------------------
# Atributos intrínsecos
# Toda classe (e todo objeto) em Python tem um conjunto de atributos
# intrínsecos definidos pelo sistema de tempo de execução do Python. 
# Alguns desses atributos intrínsecos são dados abaixo para classes
# e objetos. Classes tem os seguintes atributos intrínsecos:
#   * __name__ o nome da classe
#   * __module__ o módulo(ou biblioteca) do qual ela foi carregada
#   * __bases__ uma coleção de suas classes base
#   * __dict__ um dicionário (conjunto de pares de valores chave) contendo todos os atributos (incluindo métodos)
#   * __dos__ a string de documentação
# Para objetos:
#   * __class__ o nome da classe do objeto
#   * __dict__ um dicionário contendo todos os atributos do objeto.
# Note que esses atributos intrínsecos todos começam e terminam com
# uma barra dupla - isto indica seu status especial dentro do Python.
# Um exemplo de exibir estes atributos para nossa classe Pessoa e uma 
# instância da classe são:
print('Atributos de classe')
print(Pessoa.__name__)
print(Pessoa.__module__)
print(Pessoa.__doc__)
print(Pessoa.__dict__)
print('Atributos de objeto')
print(p1.__class__)
print(p1.__dict__)





print('#'*50)
print(' '*50)
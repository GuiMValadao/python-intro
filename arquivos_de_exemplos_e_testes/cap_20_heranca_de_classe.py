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
# 
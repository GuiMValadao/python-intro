# Lado de classe e comportamento estático
# As classes em Python podem armazenar dados e comportamentos 
# que não fazem parte de uma instância ou objeto; em vez disso
# fazem parte da classe.
# --------------------------------------
# Em Python, classes também tem atributos; eles são referidos
# como variáveis ou atributos de classe (diferente de 
# variáveis ou atributos de instância). As variáveis são definidas
# dentro do alcance da classe, mas fora de quaisquer métodos,
# estando, portanto, ligadas à classe em vez de qualquer instância.
# Por exemplo, podemos atualizar a classe Pessoa para manter uma
# contagem de quantas instâncias da classe são criadas:
############################################
class Pessoa:
    """Uma classe de exemplo para guardar o nome e idade de uma pessoa"""
    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1

    def __init__(self, nome, idade):
        Pessoa.increment_instance_count()
        self.nome = nome
        self.idade = idade

    @staticmethod
    def static_function():
        print('Static method.')
###########################################
# A variável 'instance_count' não é parte de um objeto individual,
# mas é parte da classe e todas as instâncias da classe podem 
# acessá-la usando ela com o prefixo do nome da classe.
p1 = Pessoa('Jon', 23)
p2 = Pessoa('Carla', 26)
p3 = Pessoa('Marcos', 34)
p4 = Pessoa('Lonra', 93)
print(Pessoa.instance_count)
##########################################
# Métodos de class side
# Também é possível definir comportamento que está ligado
# à classe em vez de um objeto individual. Este comportamento
# é chamado método de classe
# Métodos de classe são escritod de maneira similar a qualquer
# outro método mas são 'decorados' com @glassmethod e pegam
# um primeirp parâmetro que representa a classe em vez de uma
# instância individual. Esta declaração é escrita antes da 
# declaração do método.
# O método de classe (alterado na classe Pessoa no começo do arquivo)
# aumenta a variável instance_count; note que essa variável é acessada
# pelo parâmetro cls passado para o método pelo Python. Como este é
# um método de classe, você não precisa prefixar o atributo de classe 
# com o nome da classe; em vez disso o primeiro parâmetro para
# o método de classe, cls, representa a classe em si. O método de 
# classe pode ser acessado prefixando-o com o nome da classe e usando
# a notação ponto para indicar qual método chamar. Isto é ilustrado 
# no corpo do método __init__().
#################################################
# Porque métodos de classe?
# Pode parecer incerto o que deveria normalmente ir em um
# método de instância ou em método de classe. No entanto, é importante
# lembrar que:
# * Métodos de instância definem o comportamento da instância/objeto.
# * Métodos de classe definem o comportamento da classe.
# Métodos de classe deveriam apenas realizar uma das funções seguintes:
# * CRIAÇÃO DE INSTÂNCIAS - Este papel é muito importante pois é
#   como você pode usar uma classe como uma fábrica para objetos e pode
#   ajudar a esconder uma grande quantidade de preparações e trabalho de
#   instanciações.
# * RESPONDER QUESTÕES SOBRE A CLASSE - Este papel pode fornecer 
#   objetos geralmente úteis, frequentemente derivados de variáveis
#   de classe. Por exemplo, eles podem retornar o número de instâncias
#   desta classe que foram criadas.
# * GERENCIAMENTO DE INSTÂNCIAS - Neste papel, métodos de classe 
#   controlam o número de instâncias criadas. Por exemplo, uma classe
#   pode apenas permitir uma única instância da classe ser criada;
#   isto é nomeado uma classe 'singleton'. Métodos de gerenciamento
#   de instâncias também podem ser usados para acessar uma istância
#   (p. ex aleatoriamente ou em um dado estado).
# * EXEMPLOS - Ocasionalmente, métodos de classe são usados para fornecer
#   exemplos úteis que explicam a operação de uma classe. Isto pode 
#   ser uma prática muito boa.
# * TESTES - Métodos de classe podem ser usados para suportar o teste
#   de uma instância de uma classe. Você pode usá-los para criar 
#   uma instância, realizar uma operação e comparar o resultado com 
#   um valor conhecido. Se os valores são diferentes, o método pode
#   reportar um erro. Isto é um modo muito útil de fornecer testes de regressão.
# * SUPORTE - para algum dos papeis acima.
# Quaisquer outras tarefas deveriam ser realizadas por um método
# de instância.
#####################################################
# Métodos estáticos
# Há mais um tipo de método que pode ser definido em uma classe;
# são os métodos 'estáticos'.
# Eles são definidos dentro de uma classe mas não são atrelados
# nem à classe nem a qualquer instância da classe; não recebem
# o primeiro parâmetro especial representando nem a classe (cls), nem
# as instâncias (self). São, efetivamente, o mesmo que funções livres
# mas são definidos dentro de uma classe frequentemente por conveniência
# ou para fornecer um jeito de agrupar estas funções juntas.
# Um método estático é um método que é decorado com o decorador
# @staticmethod. Um exemplo é colocado na classe no início do arquivo.
# Estes métodos são invocados pelo nome da classe em que são definidos,
# por exemplo:
#Pessoa.static_function()
# Nota para programadores Java e C#: tanto em Java quanto C#, o
# termo 'class side' e estático são usados intercambiavelmente.
# No entanto, em ambos casos aqueles métodos são o equivalente de 
# métodos de classe em Python. Em Python, 'class' methods e 'static'
# methods são muito diferentes.
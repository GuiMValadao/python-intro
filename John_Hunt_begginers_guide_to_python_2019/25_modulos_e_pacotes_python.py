# Capítulo 25 - Módulo e pacotes de Python
# Módulos e pacotes são dois construtos usados em Python
# para organizar programas maiores. Este capítulo introduz módulos
# em Python, como eles são acessados, definidos e como Python
# encontra módulos etc.
#------------------------------------------
# Módulos
# Um módulo lhe permite agrupar funções relacionadas, classes
# e código em geral. Você pode pensar em um módulo como sendo uma
# espécie de biblioteca de código (apesar de, na verdade,
# muitas bibliotecas são, elas mesmas, compostas de muitos
# módulos como, por exemplo, uma biblioteca pode ter extensões
# ou opcionais para sua funcionalidade central).
# É útil organizar seu código em módulos quando o código
# ou se torna grande ou quando você gostaria de reutilizar
# alguns elementos do código base em múltiplos projetos.
# Dividindo um corpo grande de código de um único arquivo lhe ajuda
# a simplificar a manutenção, compreensibilidade, teste, reutilização,
# e escopo do código. Esses são explicados abaixo:
#   * Simplicidade - Focar em um subconjunto de um problema geral
#       nos ajuda a desenvolver soluções que funcionam para o 
#       subconjunto e podem ser combinadas para resolver o problema
#       geral. Isto significa que módulos individuais podem ser
#       mais simples que a solução geral.
#   * Manutenção -  Módulos tipicamente tornam mais fácil definir limites
#       lógicos entre um corpo de código e outro. Isto significa que é
#       mais fácil ver o que compreende um módulo e verificar que
#       o módulo funciona de maneira apropriada mesmo quando modificado.
#       Também ajuda a distinguir um corpo de código de outro, tornando
#       mais fácil encontrar onde mudancas devreia ir
#   * Teste -   Como um módulo pode ser feito independente um do outro
#       há menos dependências e cruzamentos. Isto significa que um 
#       módulo pode ser testado em isolamento e mesmo antes de outros módulos,
#       e a aplicação geral, terem sido escritas.
#   * Reusabilidade -   Definir uma função ou classe em um módulo significa
#       que é mais fácil reutilizá-la em outro módulo, como os limites
#       entre um módulo e outro são claros.
#   * Escopo -  Módulos tipicamente também definem um espaço de nomes,
#       isto é, um escopo dentro do qual cada função ou classe são únicas.
#       Pense no espaço de nomes como algo parecido com um sobrenome. 
#       dentro de uma sala podem ter muitas pessoas com o primeiro
#       nome 'John', mas podemos diferenciar entre elas usando seu nome 
#       completo, por exemplo, 'John Hunt', 'John Jones', 'John Smith',
#       cada sobrenome neste exemplo fornece um espaço de nomes que 
#       garante que cada John é único.
#---------------------------------------
# Módulos Python
# Em Python, um módulo equivale a um arquivo contendo código Python.
# Um módulo pode conter:
#   * Funções
#   * Classes
#   * Variáveis
#   * Código executável
#   * Atributos associados com o módulo como seu nome.
# O nome de um módulo é o nome do arquivo em que é definido (removendo
# o sufixo '.py'). Por exemplo:
#      ---------------------------
#      | def printer(some_object):|
#      ==============-------------
#      | class Shape:|
#       -------------
#     arquivo: utils.py
#
# Assim, a função printer() e a classe Shape são definidas no módulo
# utils. Elas podem ser referenciadas pelo nome do módulo, utils.
# Como exemplo, vamos olhar a definição do módulo utils definido
# no arquivo util.py:
"""This is a test module"""
print('Hello I am the utils module')
def printer(some_object):
    print('printer')
    print(some_object)
    print('done')
class Shape:
    def __init__(self, id):
        self._id = id
    def __str__(self):
        return 'Shape - ' + self._id
@property
def id(self):
    """ The docstring for the id property """
    print('In id method')
    return self._id
@id.setter
def id(self, value):
    print('In set_age method')
    self._id = id
default_shape = Shape('square')
#
# O módulo tem um comentário que está no início do arquivo - esta é 
# uma documentação útil para quem for trabalhar com o módulo. Em 
# alguns casos, o comentário no início do módulo pode fornecer uma
# documentação extensa sobre o módulo como o que ele fornece, como usar
# seus recursos e exemplos que podem ser usados como referência.
# O módulo também tem algum código executável (a declaração print após 
# o comentário) que será executado quando o módulo é carregado/inicializado
# pelo Python. Isto acontecerá quando o módulo é primeiro referenciado na 
# aplicação.
# Uma variável default_shape também é inicializada quado o módulo
# é carregado e também pode ser referenciada fora do módulo de maneira similar
# à função e classe do módulo. Tais variáveis podem ser úteis em 
# preparar padrões ou dados predefinidos que podem ser usados por
# desenvolvedores trabalhando com o módulo.
#-----------------------------------------
# Importando módulos em Python
# Um módulo definido pelo usuário não é automaticamente acessível 
# por outro arquivo ou script; é necessário importar(import) o módulo.
# Importar um módulo faz com que as funções, classes e variáveis
# definidas dentro do módulo fiquem visíveis ao arquivo em que são
# importados.
# Por exemplo, para importar todos os conteúdos do módulo utils em um
# arquivo chamado my_app.py podemos usar:
# 
# import utils
# 
# Note que não damos o nome do arquivo, mas o nome do módulo para ser
# importado (que não inclui '.py').
# Uma vez que as definições dentro do módulo utils estão visíveis
# dentro de my_app.py, podemos usá-las como se tivessem sido definidas 
# dentro do arquivo atual. Note que, devido a alcance, a função,
# classe e variável definidas no módulo utils serão prefixadas pelo
# nome do módulo, isto é, utils.printer e utils.Shape etc.
# import utils
# utils.printer(utils.default_shape)
# shape = utils.Shape('circle')
# utils.printer(shape)
#
# Ao executar o arquivo 'my_app.py' produzimos a seguinte saída:
# Hello I am the utils module
# printer
# Shape - square
# done
# printer
# Shape - circle
# 
# Note que a primeira linha da saída é a saída da declaração print
# no início do módulo utils, o que ilustra a habilidade em Python
# de definir comportamentos que serão executados quando um módulo
# é carregado; tipicamente, isto poderia executar algum código de
# limpeza (housekeeping) ou definir comportamento requisitado pelo
# módulo. Deveria ser notado que o módulo é inicializado apenas 
# a primeira vez e assim, as declarações executáveis são executadas
# apenas uma vez.
# Se esquecermos de incluir a declaração import no início do arquivo,
# então Python não saberia que deveria utilizar o módulo utils. 
# Assim, geraríamos um erro indicando que o elemento utils não é 
# conhecido: NameError: name 'utils' is not defined.
# Podem haver qualquer quantidade de módulos importados em um arquivo.
# Eles podem ser importados por declarações import separadas ou 
# fornecendo uma lista separada por vírgula de módulos:
# import utils
# import support
# import module1, module2, module3
# Uma convenção comum é colocar todas as declarações de importação
# no início do arquivo; entretanto, isto é apenas uma convenção e
# declarações import podem ser feitas em qualquer lugar em um
# arquivo antes do local onde os recursos do módulo são usados.
# É uma convenção bastante comum, no entanto, que ferramentas como 
# PyCharm indicarão um problema de estilo se você não colocar 
# os imports no início do arquivo.
# --------------------------------------
# Importando de um módulo
# Um problema com o exemplo anterior é que tivemos que continuar
# nos referindo a instalações fornecidas pelo módulo utils como
# utils.<coisa de interesse>; o que, enquanto torna muito claro que
# esses recursos vem do módulo utils, é um pouco tedioso. Uma variante
# da declaração import nos permite importar tudo de um módulo em
# particular e remover a necessidade de prefixar as funções ou classes
# do módulo com o nome do módulo, por exemplo:
# from <module name> import *
# Que pode ser lido como 'de <nome do módulo> importe tudo' daquele
# módulo e torne diretamente disponível.
#from utils import *
#printer(default_shape)
#shape = Shape('circle')
#printer(shape)
#
# Como isto mostra que podemos referenciar 'default_shape', a função
# 'printer()' e a classe 'Shape' diretamete. Note que '*' aqui é 
# comumente referido como coringa; o que quer dizer que representa
# tudo no módulo.
# O problema com este tipo de import é que pode resultar em confronto
# de nomes por trazer no alcance todos os elementos definidos no 
# módulo utils. Entretanto, podemos apenas estar interessados na
# classe Shape; nesse caso, podemos escolher apenas aquele recurso,
# por exemplo:
#from utils import Shape
#s = Shape('Rectangle')
#print(s)
# Agora apenas a classe Shape foi importada no arquivo e feita
# diretamente avaliável. Você pode também dar um nome alternativo para
# um elemento sendo importado de um módulo usando a declaração
# import. Por exemplo:
# import <module_name> as <alternative_module_name>
# Por exemplo:
#import utils as utilities
#utilities.printer(utilities.default_shape)
# Também podemos renomear elementos individuais de um módulo,
# por exemplo uma função pode ser dada um apelido. A sintaxe é:
# from <module_name> import <element> as <alias>
# Por exemplo:
# from utils import printer as myfunc
# Neste caso, a função printer no módulo utils está sendo
# nomeada como myfunc e assim será conhecida como myfunc
# no arquivo atual. Podemos também combinar múltiplas importações
# from juntas com alguns dos elementos sendo importados tendo 
# apelidos:
# from utils import Shape, printer as myfunc
#  


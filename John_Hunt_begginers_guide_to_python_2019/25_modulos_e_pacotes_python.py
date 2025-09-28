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
#"""This is a test module"""
#print('Hello I am the utils module')
#def printer(some_object):
#    print('printer')
#    print(some_object)
#    print('done')
#class Shape:
#    def __init__(self, id):
#        self._id = id
#    def __str__(self):
#        return 'Shape - ' + self._id
#@property
#def id(self):
#    """ The docstring for the id property """
#    print('In id method')
#    return self._id
#@id.setter
#def id(self, value):
#    print('In set_age method')
#    self._id = id
#default_shape = Shape('square')
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
# s = Shape('oval')
# myfunc(s)
# -------------------------------------
# Escondendo alguns elementos de um módulo
# Por padrão, qualquer elemento em um módulo cujo nome começa
# com uma barra _ é escondido quando uma importação coringa é
# realizada. Deste modo, certos itens nomeados podem ser escondidos
# a menos que sejam explicitamente importados. Assim, se nosso
# módulo utils agora incluir uma função:
# """ This is a test module"""
# print('Hello I am the utils module')
# as before
# def _special_function():
#   print('Special fuction')
# E então tentamos importar o módulo inteiro usando a importação
# coringa e acessar _special_function:
# from utils import *
# _special_function()
# Obtemos um erro:  NameError: name '_special_function' is not defined
# Entretanto, se explicitamente importamos a função:
#from utils import _special_function
#_special_function()
# Podemos utilizá-la, obtendo:
#Hello I am the utils module
#Special function
# Isto pode ser usado para esconder recursos que são ou não
# planejados para serem usados fora do módulo ou para fazer
# recursos avançados avaliáveis apenas para aqueles que realmente
# os querem.
# ------------------------------------------------------
# Importando detro de uma função
# Em alguns casos pode ser útil limitar o escopo de um import
# para uma função; assim, evita-se qualquer uso desnecessário de,
# ou confronto de nomes com, recursos locais. Para fazer isso
# só precisa adicionar um impor ao corpo da função:
# def my_funs():
#   from util import Shape
#   s = Shape('line') 
#----------------------------------------------------
# Propriedades do módulo
# Todo módulo tem um conjunto de propriedades que podem ser usadas
# para encontrar quais recursos ele fornece, qual seu nome,
# qual(se existe) sua string de documentação etc.
# Estas propriedades são consideradas especiais como todas elas 
# iniciam e terminam com uma barra dupla('__'). Elas são:
#   * __name__: o nome do módulo
#   * __doc__:  a docstring do módulo
#   * __file__: o arquivo em que o módulo foi definido.
# Vocês também pode obter uma lista dos conteúdos de um módulo após
# ele ter sido importado usando a função dir(<module-name>). Por exemplo:
# import utils
# print(utils.__name__)
# print(utils.__doc__)
# print(utils.__file__)
# print(dir(utils)) 
# Que fornece:
# Hello I am the utils module
#utils
#This is a test module
#utils.py
#['Shape', '__builtins__', '__cached__', '__doc__', '__file__',
#'__loader__', '__name__', '__package__', '__spec__',
#'_special_function', 'default_shape', 'printer']
# Note que a declaração executável print ainda é executada como
# isto é executado quando o módulo é carregado pela execução atual
# do Python; mesmo que tudo que queremos fazer é acessar alguma das
# propriedades do módulo. A maioria das propriedades dos módulos são
# usadas por ferramentas para ajudar desenvolvedores; mas eles podem 
# ser uma referência útil quando você encontra um novo módulo pela primeira vez.
# ----------------------------------------------------
# Módulos padrões
# Python vem com muitos módulos embutidos assim como muitos outros 
# disponíveis de terceiros. De uso particular é o módulo sys, que
# contém um número de itens e funções de dados relacionados à plataforma
# de execução na qual um programa está sendo executado. 
# Alguns dos recursos do módulo sys são mostrado abaixo, incluindo
# sys.path(), que lista as partas (directories) que são procurados para 
# resolver um módulo quando uma declaração import é usada. Esta é uma
# variável escrevível (writable), permitindo um programa adicionar
# pastas (e, portanto, módulos) antes de tentar importar.
import sys
#print('sys.version:', sys.version)
#print('sys.maxsize:', sys.maxsize)
print('sys.path:', sys.path)
#print('sys.platform:', sys.platform)
#
# ----------------------------------------
# Caminho de busca de módulos Python
# Um pontos que passamos por cima até aqui é como Python encontra 
# esses módulos? A resposta é que ele usa um ambiente especial chamado
# PYTHONPATH. Esta é uma variável que pode ser definida antes de executar
# Python que diz onde procurar por quaisquer módulos nomeados. 
# Ele é insinuado na seção anterior onde a variável de caminho do módulo
# sys é exibida. Ao executar esse comando, foi obtido:  

#sys.path: ['', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\\python313.zip',
#  'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\\DLLs', 
# 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\\Lib', 
# 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0', 
# 'C:\\Users\\guimv\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python313\\site-packages', 
# 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\\Lib\\site-packages']

# Esta é, na verdade, uma lista dos locais em que Python procuraria para
# encontrar um módulo; Python vai procurar cada um desses locais em
# sequência em busca do módulo nomeado; vai usar o primeiro que encontrar. 
# O algoritmo de busca é:
#   * A pasta atual.
#   * Se o módulo não foi encontrado, então Python procura cada pasta na
#     variável PYTHONPATH
#   * Se tudo falhar, Python procura o caminho padrão.
# Um ponto a ser notado sobre esta ordem de busca é que é possível
# esconder um módulo fornecido pelo sistema criando um definido
# pelo usuário e dando o mesmo nome que o módulo do sistema;
# isto é porque o seu próprio módulo será encontrado antes e esconderá
# o fornecido pelo sistema.
# Neste caso PYTHONPATH será usado para encontrar módulos embutidos
# em Python sob a instalação Python, enquato os módulos definidos pelo 
# usuário serão encontrados nas pastas do espaço de trabalho.
# Também é possível sobrescrever a variável padrão PYTHONPATH. Isto
# é o que é conhecido como uma variável de ambiente e portanto pode ser
# definida como uma variável de ambiente do sistema operacional 
# Unix/Linux ou Windows que pode, então, ser pega pelo ambiente Python. 
# A sintaxe usada para definir PYTHONPATH depende no sistema operacional.
# Para o Windows:
# set PYTHONPATH = C:\python30\lib; 
# Para Unix\Linux:
# set PYTHONPATH = /usr/local/lib/python
#--------------------------------------------------
# Módulos como scripts
# Qualquer arquivo Python não apenas é um módulo mas também
# um script ou programa Python. Isto significa que pode ser executado
# diretamente se necessário. Por exemplo, o seguinte é o conteúdo
# de um arquivo chamado module1.py:
# """ This is a test module""" 
# print('Hello I am module 1')
# def f1():
#   print('f1[1]')
# def f2():
#   print('f2[1]')
# x = 1 + 2
# print('x is', x)
# f1()
# f2()
# Quando este arquivo é executado, ou carregado em um REPL Python,
# então o código livre será executado e a saída gerada será:
# Hello I am module 1
# x is 3
# f1[1]
# f2[1]
#
# Isto parece ok até você tentar usar module1 com o seu código; o
# código livre ainda irá executar se escrevermos:
# import module1
# module1.f1()
# A saída é:
#Hello I am module 1
#x is 3
#f1[1]
#f2[1]
#f1[1]
# As primeiras 4 linhas são executadas quando module1 é carregado 
# como elas são executáveis livres dentro do módulo. Podemos, claro,
# remover o código livre; mas e se quisermos de vez em quando executar module1
# como um script/programa e às vezes como um módulo importado em outros
# módulos?
# Em Python, podemos diferenciar entre quando um arquivo é carregado
# como um módulo e quando é executado como um programa/script. Isto é
# porque Python define a propriedade __name__ para o nome do módulo
# quando ele está sendo carregado como um módulo; mas se está sendo
# executado como um script então o __name__ é definido para a string 
# __main__. Isto é, parcialmente, porque historicamente main() tem
# foi o ponto de entrada para aplicações em diversas linguagens como
# C, C++, Java e C#.
# Podemos agora determinar se um módulo está sendo carregado ou executado 
# como um script/aplicação principal checando a propriedade __name__
# do módulo (que é diretamente acessível de dentro do módulo). Se
# o módulo é o ponto de entrada __main__ então executa algum código;
# se não, então faz outra coisa.
# Por exemplo,
# """ This is a test module""" 
# print('Hello I am module 1') 
# def f1():
#   print('f1[1]')
# def f2():
#   print('f2[1]')
# if __name__ == '__main__':
#   x = 1 + 2
#   print('x is', x)
#   f1()
#   f2()
# Agora o código dentro da declaração if será executado apenas quando
# este módulo é carregado como o ponto inicial de uma aplicação/
# script. Note que a declaração print no início do módulo irá ser
# executada em ambos os cenários; isto pode ser útil pois permite 
# o comportamento de inicialização ainda ser executado onde apropriado.
# Um padrão ou idioma comum é colocar o código a ser executado quando um
# arquivo está sendo carregado diretamente (em vez de como um módulo) em
# uma função chamada main() e chamar aquela função de dentro da declaração
# if. Isto ajuda a esclarecer qual comportamento se pretende executar e quando,
# assim a versão final de nosso módulo é:
# """ This is a test module""" 
# print('Hello I am module 1') 
# def f1():
#   print('f1[1]')
# def f2():
#   print('f2[1]')
# def main():
#   x = 1 + 2
#   print('x is', x)
#   f1()
#   f2()
#
# if __name__ == '__main__':
#   main()
# Esta versão é o que seria chamada agora de Python idiomático, ou estilo Pythonico.
#------------------------------------------------------
# Pacotes Python
# Organização de pacotes
# Python permite a desenvolvedores organizar módulos junto em pacotes,
# em uma estrutura hierarquica baseada em pastas. Um pacote é definido como:
#   * Uma 'pasta' contendo um ou mais arquivos fonte em Python e
#   * Um arquivo fonte 'opcional' chamado __init__.py. Este arquivo pode
#     também conter código que é executado quando um módulo é importado do pacote.
# Por exemplo, o seguinte esquema ilustra um pacote utils contendo dois
# módulos classes e funções:
#   v utils (pasta)  
#       __init__.py
#       classes.py
#       functions.py
# Neste caso, o arquivo __init__.py contém cóigo do nível de inicialização do pacote.
# print('utils package')
# O conteúdo do arquivo __init__.py serão executados uma vez, a primeira que 
# qualquer dos módulos dentro do pacote é chamado. O módulo functions então
# contém diversas definições de funções; enquanto o módulo classes contém diversas
# definições de classes.
# Nos referimos a elementos de um pacote relativo ao nome do pacote -
# como mostrado abaixo:
# from utils.functions import *
# f1()
# from utils.classes import *
# p = Processor()
# Aqui estamos importando ambas módulos functions e classes do pacote
# utils. A função f1() é definida no módulo functions enquanto a classe
# Processor é definido no módulo classes.
# Você pode usar todos os estilos from e import que já vimos, por
# exemplo você pode importar uma função de um módulo em um pacote
# e dar um apelido:
# from util.functions import f1 as myfunc
# myfunc()
# É possível importar todos os módulos de um pacote simplesmente
# importando o nome do pacote. Se você quer fornecer algum controle sobre
# o que é importado de um pacote quando isto ocorre você pode definir
# a variável 'all' no arquivo __init__.py que indicará o que será importado
# nesta situação.
#--------------------------------------------------
# Subpacotes
# Pacotes podem conter subpacotes a qualquer profundidade que você
# requerir. Por exemplo, o diagrama da página 296 ilustra essa ideia.
# No diagrama, utils é o pacote raiz (root), que contém dois 
# subpacotes file_utils e network_utils. O pacote file_utils tem um
# arquivo de inicialização e um módulo file_support. O pacote 
# network_utils também tem um arquivo de inicialização do pacote
# e dois módulos: network_monitoring e network_support. Claro, o pacote
# raiz também tem seu próprio arquivo de inicialização e seus dois módulos
# próprios, classes e functions.
# Para importar o subpacote, fazemos o mesmo que antes mas cada pacote no caminho
# para o módulo é separado por um ponto, por exemplo:
# import utils.file_utils.file.support
# ou
# from utils.file_utils.file_support import file_logger
#   

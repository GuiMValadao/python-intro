# Capítulo 24 - Erro e exceções
#
# Quando algo dá errado em um programa de computador, alguém
# precisa ficar sabendo. Uma maneira de informar outras partes
# de um programa (e possivelmente aquelas executando um 
# programa) é gerando um objeto erro e propagá-lo pelo código
# até algo lidar com o erro e arrumar as coisas ou no qual o
# programa inicia é encontrado.
# Se o erro propaga para fora do programa, então o usuário que
# executou o programa precisa saber que algo deu errado. Eles são 
# notificados de um problema por uma curta mensagem sobre o
# Erro que ocorreu e uma pedaço do código indicando onde ele pode
# ser encontrado. Em Python, os termos 'Erro'(Error) e 'Exceção'
# (Exception) são usados sinonimamente; no entanto, do ponto de
# vista do estilo, exceções poderiam ser usadas para representar 
# problemas com operações como exceções aritméticas e erros
# poderiam ser usados com problemas funcionais, como um arquivo
# não sendo encontrado.
#--------------------------------
# O que é uma exceção?
# Em Python, tudo é um tipo de objeto, incluindo inteiros, strings,
# booleanos e, de fato, exceções e erros. Os tipo Exception/Error
# são definidos em uma hierarquia de classe com a raiz dessa 
# hierarquia sendo o tipo BaseException. Todos os erros internos
# e exceções eventualmente extende do tipo BaseException. Esse tipo
# tem uma subclasse Exception, que é a raiz de todas as exceções
# definidas pelo usuário (assim como muitas exceções internas).
# Por sua vez, ArithmeticException é a classe base para todas
# as exceções internas associadas a erros aritméticos. Na pág.265
# é mostrado um diagrama da hierarquia de classes para alguns tipos
# comuns de erros e exceções.
# Quando uma exceção ocorre, isto é conhecido como levantar(raising)
# uma exceção, e quando é passada para o código lidar é conhecido
# como jogar(throwing) uma exceção. Estes termos se tornarão mais
# óbvios na sequência.
#---------------------------------
# O que é lidar com exceções?
# Uma exceção move o fluxo de controle de um lugar para outro. Na
# maioria das situações, isto é porque um problema ocorre que não
# pode ser resolvido localmente mas que pode ser resolvido em
# outra parte do sistema.
# O problema é, geralmente, algum tipo de erro (como divisão por
# zero), mas pode ser qualquer problema (por exemplo, identificar
# que o código postal especificado com um endereço não combinam)
# O propósitp de uma exceção, portanto, é lidar com uma condição
# de erro quando ela ocorre na execução.
# É válido considerar porque você deveria querer lidar com uma 
# exceção; no fim das contas, o sistema não permite que um erro
# passe batido. Por exemplo, se tentamos dividir por zero, então
# o sistema gera um erro para você. Isto pode significar que o
# usuário entrou um valor errado, e não queremos que os usuários 
# sejam apresentados a um diálogo sugerindo que eles entrem no
# depurador do sistema. Podemos, portanto, usar exceções para
# forçar o usuário a corrigir o erro e re-executar o cálculo.
# A seguinte tabela ilustra terminologia tipicamente usada
# com resolução de erros/exceções em Python.
# Exceção               | Um erro que é gerado durante execução
#-----------------------|--------------------------------------
# Levantar (raising)    | Gerando uma nova exceção
# uma exceção           |
#-----------------------|--------------------------------------
# jogar(throwing) uma   | Desencadeando uma exceção 
# exceção               |   gerada
#-----------------------|--------------------------------------
# # Resolver uma        | Processando código que resolve
# exceção               |   o erro
#-----------------------|---------------------------------------
# Resolvedor            | O código que lida com o erro (referido como 'catch block')
#-----------------------|---------------------------------------
# Sinal                 | Um tipo particular de exceção (como 'out of bounds' ou 'divide by zero')
#
# Diferentes tipos de erro produzem diferentes tipos de exceção. Por
# exemplo, se o erro é causado por dividir um inteiro por zero, então
# a exceção é uma exceção aritmética. O tipo de exceção é identificado por
# objetos e pode ser pego e processado por resolvedores de exceção.
# Cada resolvedor pode lidar com exceções associadas a sua classe 
# de erro ou exceção (e suas subclasses).
# Uma exceção é instanciada quando surge. O sistema procura através
# da pilha de execução (o conjunto de funções ou métodos que foram 
# invocados em ordem reversa) até encontrar um resolvedor que pode 
# lidar com a exceção. O resolvedor associado, então, processa a
# exceção, o que pode envolver alguma ação remedial ou terminar a 
# execução atual de maneira controlada. Em alguns casos, pode ser
# possível reiniciar a execução do código.
# Como um resolvedor pode apenas lidar com uma exceção de uma classe
# específica (ou sublcasse), uma exceção pode passar por um alguns
# blocos do resolvedor antes de encontrar um que possa processá-la.
#-------------------------------------
# Resolvendo uma exceção
# Você pode pegar uma exceção implementando o construto try-except.
# Este construto é dividido em três partes:
#   *   bloco try. Este bloco indica o código que é para ser monitorado
#       para as exceções listadas nas expressões except.
#   *   cláusula except. Você pode usar uma cláusula opcional except 
#       para indicar o que fazer quando certas classes de erro/exceção
#       ocorrem (p.ex, resolver o problema ou gerar uma mensagem de aviso).
#       Pode haver qualquer números de cláusulas except na sequência
#       de checagem para diferentes tipos de erros/exceções.
#   *   cláusula else. Esta é uma cláusula opcional que será executada se,
#       e apenas se, nenhuma exceção foi lançada no bloco try. Ela é
#       útil para código que deve ser executado se a cláusula try não gera
#       uma exceção.
#   *   cláusula finally. A cláusula opcional finally executa após o
#       bloco try termina (independentemente de uma exceção ser 
#       lançada ou não). Você pode usá-la para limpar quaisquer recursos,
#       fechar arquivos, etc.
# Como exemplo, considere a seguinte função que divide um número por
# zero; isto vai gerar o ZeroDivisionError quando é executado para
# qualquer número:
def runcalc(x):
    x/0
#runcalc(6)
# Entretanto, podemos lidar com isso cercando a chamada para runcalc
# dentro de uma declaração try e fornecendo uma cláusula except. 
# A sintaxe para uma declaração try com uma cláusula except é:
# try:
#   <código para monitorar>
# except <tipo de exceção para a qual é monitorado>:
#   <código para chamar se a exceção é encontrada>
# Um exemplo concreto disto é dado abaixo para uma declaração try
# que será usada para monitorar uma chamada de runcalc:
#try:
#    runcalc(6)
#except ZeroDivisionError:
#    print('oops')
# Que agora resulta na string 'oops' sendo exibida. Isto ocorre
# pois quando runcalc é chamada, o operador '/' lança o ZeroDivisionError
# que é passado de volta ao código que tem uma cláusula except especificando
# este tipo de exceção. Esta parta pega a exceção e executa o bloco
# de código associado que, neste caso, exibe 'oops'.
# De fato, não temos que ser tão preciso assim; a cláusula except pode 
# ser dada uma classe de exceção para procurar e vai combinar com 
# qualquer exceção que é daquele tipo ou é uma instância de uma 
# subclasse da exceção. Nós, portanto, também escrevemos:
#try:
#    runcalc(6)
#except Exception:
#    print('oops')
# A classe EXception é uma classe avó de ZeroDivisionError, que é subclasse.
# No entanto, se não quer um bloco em comum do código para resolver
# as exceções, você pode definir diferentes comportamentos para
# diferentes tipos de exceção. Isto é feito tendo uma série de
# cláusulas excepts; cada uma monitorando um tipo de exceção diferente:
#try:
#   runcalc(6)
#except ZeroDivisionError:
#   print('oops')
#except IndexError:
#   print('arr')
#except FileNotFoundError:
#   print('huh')
#except Exception:
#   print('duh')
#----------------------------------------------
# Acessando o objeto exceção
# É possível acessar o objeto excessão pego pela cláusula except
# usando a palavra chave 'as':
#try:
#    runcalc(6)
#except ZeroDivisionError as exp:
#    print(exp)
#    print('oops')
# O que vai gerar:
# division by zero
# oops
# Se há múltiplas cláusulas except, cada except pode decidir
# se vai ligar um objeto exceção a uma variável ou não (e cada variável pode
# ter um nome diferente). Apenas a exceção FileNotFoundError abaixo
# não atribui um nome à exceção correspondente:
#try:
#    runcalc(6)[1]
#except ZeroDivisionError as exp:
#    print(exp)
#    print('oops')
#except IndexError as e:
#    print(e)
#    print('arrgh')
#except FileNotFoundError as f:
#    print(f)
#    print('huh!')
#except Exception as exception:
#    print(exception)
#    print('Duh!')

#----------------------------------------------
# Pulando para resolvedores de exceção
# Uma das características interessantes da resolução de exceções em
# Python é que quando um erro ou exceção são levantados, são imediatamente
# lançados aos resolvedores de exceção (as cláusulas except). Quaisquer 
# declarações que seguem o ponto no qual a exceção foi lançada não são
# executados. Isto quer dizer que uma função pode ser terminada mais cedo
# e declarações seguintes no código chamando podem não ser executados.
# Como um exemplo, considere o seguinte código. Ele define uma função
# minha_funcao() que exibe uma string, realiza uma operação de divisão que
# causará o levantamento de ZeroDivisionError se o valor y é zero,
# e então tem uma declaração print na sequência. Esta função é chamada de 
# dentro de uma declaração try. Note que há uma declaração print de cada
# lado da chamada para minha_funcao().
def minha_funcao(x, y):
    print('entrada de minha função')
    result = x/y
    print('saída da minha função')
    return result
#print('Iniciando')
#Iniciando
#Antes da minha função
#entrada de minha função
#saída da minha função
#Após minha função
#feito

#try:
#    print('Antes da minha função')
#    minha_funcao(6, 0)
#    print('Após minha função')
#except ZeroDivisionError as exp:
#    print('oops')
#print('feito')
#Iniciando
#Antes da minha função
#entrada de minha função
#oops
#feito
# A diferença é que a segunda declaração 'print' em minha_funcao()
# não foi executada. Em vez disso, após o ponte onde o cálculo seria
# realizado e o erro surge, o código pula para a cláusula except.
# Isto é, parcialmente, porque o termo lançado(throwing) é usado
# a respeito da resolução de erros e exceções; pois o erro ou exceção
# surge em um lugar e é lançado para o ponto onde ele pode ser resolvido,
# ou é jogado para fora da aplicação se nenhuma cláusula except é
# encontrada para resolvê-lo.
#---------------------------------------
# Pegar qualquer exceção
# Também é possível especificar uma cláusula except que pode ser usada 
# para pegar qualquer tipo de erro ou exceção, por exemplo:
#try:
#   minha_funcao(6,0)
#except IndexErrot as e:
#   print(e)
#except:
#   print('Alguma coisa deu errado')
# 
# Ela deve ser a última cláusula except pois omite o tipo de exceção
# e assim age como um coringa. Pode ser usada para garantir que 
# você será notificado que um erro, de fato, ocorreu, mesmo sem saber
# qual tipo de erro foi; logo, deve-se usar esse recurso com cuidado.
#---------------------------------------
# A cláusula else
# A declaração try também tem uma cláusula opcional else. Se estiver presente,
# então deve vir após todas as cláusulas except. Ela será executada
# se nenhuma exceção foi levantada. Se alguma exceção foi levantada, 
# a cláusula else não será executada.
#try:
#   minha_funcao(6,2)
#except ZeroDivisionError as e:
#   print(e)
#else:
#   print('Tudo correu bem')
#Com a saída sendo:
#
#entrada de minha função
#saída da minha função
#Tudo correu bem

# Como pode ver, a declaração print na cláusula else foi executada.
# Se em vez de 2 colocamos zero, então o erro é pego e exibe 'division
# by zero', e a cláusula else não é executada.
#--------------------------------------------
# A cláusula finally
# Uma cláusula finally pode também ser fornecida com a declaração
# try. Esta cláusula é a última na declaração e deve vir após
# quaisquer cláusulas except e else. É usada para código que você
# quer executar independentemente de uma exceção ter ocorrido ou
# não. Por exemplo, na seguinte seção de código:
#try:
#    minha_funcao(6,2)
#except ZeroDivisionError as e:
#    print(e)
#else:
#    print('Tudo correu bem')
#finally:
#    print('Sempre executa')
#entrada de minha função
#saída da minha função
#Tudo correu bem
#Sempre executa
# A cláusula 'finally' pode ser bastante útil para atividades do tipo
# de limpeza(housekeeping) geral como desligar ou fechar quaisquer
# recursos que seu código pode estar usando, mesmo após um erro ocorrer.
#-----------------------------------------
# Levantando uma exceção
# Um erro ou exceção é levantado usando a palavra chave 'raise'. A sintaxe
# disso é:
#raise<Exception/Error type to raise>()
# Por exemplo:
#def function_bang():
#   print('function_bang in')
#   raise ValueError('Bang!')
#   print('function_bang')
# Na função acima a segunda declaração do corpo da função irá
# criar uma nova instância da classe ValueError e então levantá-la
# de modo que ela é jogada, permitindo que seja pega por quaisquer
# resolvedores de exceção que tenham sido definidos.
# Podemos lidar com esta exceção escrevendo um bloco 'try' com uma
# cláusula except para a classe ValueError. Por exemplo:
#try:
#   function_bang()
#except ValueError as ve:
#   print(ve)
# Isto gera a saída:
#function_bang in
#Bang!
# Note que se você apenas quer levantar uma exceção sem fornecer quaisquer
# argumentos construtores, então você pode apenas fornecer o nome da classe
# da exceção com a palavra-chave:
#raise ValueError # Forma curta para raise ValueError()
# Você também pode re-raise um erro ou exceção; isto pode ser útil
# se você simplesmente quer notar que um erro ocorreu e então
# relançá-lo de modo que ele pode ser resolvido mais adiante na aplicação:
#try:
#   function_bang()
#except ValueError:
#   print('oops')
#   raise
# Isto vai levanter novamente o ValueError pego pela cláusula except.
# Note aqui que não a atribuimos uma variável; poderíamos ter feito se quiséssemos:
#try:
#   function_bang()
#except ValueError as ve:
#   print(ve)
#   raise
#--------------------------------
# Definindo uma exceção customizada
# Você pode definir seus próprios erros e exceções, que podem lhe dar
# mais controle sobre o que acontece em circunstâncias em particular.
# Para definir uma exceção, você cria uma subclasse da classe Exception
# e gera uma mensagem apropriada:
#class InvalidAgeException(Exception):
#    """ Valid Ages must be between 0 and 120 """
#    def __init__(self, valor):
#        self.valor = valor
#    def __str__(self):
#       return 'InvalidAgeException(' + str(self.valor) + ')'

# Esta classe poderia ser usada para representar explicitamente um problema
# quando uma idade é definida em uma classe Pessoa que não está dentro
# da faixa de idades aceitável.
# Podemos usar isso com a classe Pessoa que definimos anteriormente; esta versão
# da classe Pessoa definiu idade como uma propriedade e tentou validar
# que uma idade apropriada foi definida:
#class Pessoa:
#    def __init__(self, nome, idade):
#        self._nome = nome
#        self._idade = idade
#    @property
#    def idade(self):
#        """ Docstring para a propriedade idade """
#        print('No método idade')
#        return self._idade
#    @idade.setter
#    def idade(self, valor):
#        print('No método set_idade(', valor, ')')
#        if isinstance(valor, int) & (valor > 0 & valor < 120):
#            self._idade = valor
#        else:
#            raise InvalidAgeException(valor)
#    @property
#    def nome(self):
#        print('Em nome')
#        return self._nome
#    @nome.deleter
#    def nome(self):
#        del self._nome
#    def __str__(self):
#        return 'Pessoa[' + str(self._nome) +'] é ' + str(self._idade)
    
# Note que o método definidor de idade agora lança InvalidAgeException,
# então escrevemos:
#try:
#   p = Pessoa('Adam', 21)
#   p.idade = -1
#except InvalidAgeException as iae:
#    print(iae)

# Podemos capturar o fato que uma idade inválida foi especificada.
# Entretanto, no resolvedor de exceções não sabemos o que a idade
# inválida era. Podemos, claro, fornecer esta informação incluindo-a
# nos dados armazenados por InvalidAgeException. Se modificarmos a definição
# da classe de forma que fornecemos um inicializador para permitir
# que parâmetros sejam passados para a nova instância de InvalidAgeException.
# Também definimos o método __str__() apropriado para converter a exceção
# em uma string para propósitos de exibição.
#----------------------------------------------
# Encadeamento de exceções
# Uma característica final que pode ser útil ao criar suas próprias
# exceções é encadeá-las a uma exceção adjacente genérica. Isto pode
# ser útil quando uma exceção genérica é levantada, por exemplo, por 
# alguma biblioteca ou pelo sistema Python em si, e você quer convertê-lo
# em uma aplicação de exceção mais significativa.
# Por exemplo, vamos dizer que queremos criar uma exceção para representar
# um problema específico com os parâmetros passados para uma função
# dividir, mas não queremos usar a genérica ZeroDivisionException, em vez
# disso, queremos usar nossa própria DivideByYWhenZeroException. Esta 
# nova exceção poderia ser definida como:
#class DivideByYWhenZeroException(Exception):
#    """ Sample Exception class"""
#def divide(x, y):
#    try:
#        result = x/y
#    except Exception as e:
#        raise DivideByYWhenZeroException from e
# Usamos as palavras chave raise e from quando estamos instanciando
# a DivideByYWhenZeroException. Isto encadeia nossa exceção à exceção 
# original que indica o problema por baixo.
# Podemos agora chamar o método divide como abaixo:
#divide(6,0)
#
# Como você pode ver, obtém informação sobre tanto a DivideByYWhenZeroException
# quanto a original ZeroDivisionError. Isto pode ser muito útil quando
# definindo tais exceções específicas da aplicação.
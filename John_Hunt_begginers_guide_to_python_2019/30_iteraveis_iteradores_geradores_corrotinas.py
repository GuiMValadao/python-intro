# Capítulo 30 - Iteráveis, iteradores, geradores e corrotinas
# Há dois protocolos que você provavelmente usará, ou precisará
# implementar em algum ponto: eles são os protocolos iterável e iterador.
# Eles são protocolos relacionados amplamente utilizados e suportados
# por um grande número de tipos.
# Uma das razões que iteradores e iteráveis são importantes é que podem
# ser usados com declarações 'for' em Python; isso os torna muito fáceis
# de integrar em código que necessita processar uma sequência de valores
# em sequência. Dois recursos tipo iteração de Python são Geradores e
# Corrotinas, que são discutidos no fim deste capítulo.
# -------------------------------------------------
# Iteração
# Iteráveis
# O protocolo Iterável (Iterable) é usado por tipos onde é possível processar
# seu conteúdo um de cada vez, em sequência. Um iterável é algo que irá
# fornecer um iterador que pode ser usado para realizar este processamento. 
# Logo, não é o iterador em si, mas o fornecedor do iterador.
# Há muitos tipos iteráveis em Python, incluindo listas, sonjuntos,
# dicionários, tuplas, etc. Eles são todos containers iteráveis que
# fornecerão um iterador.
# Para ser um tipo iterável é necessário implementar o método __iter__()
# (que é o único método no protocolo iterável). Este método deve fornecer
# uma referência ao objeto iterador. Esta referência poderia ser o tipo
# de dado em si ou poderia ser outro tipo que implementa o protocolo
# iterador.
#---------------------------------------------------------
# Iteradores
# Um iterador é um objeto que executará uma sequência de valores. Iteradores
# podem ser finitos em comprimento ou infinitos (no entanto, muitos 
# containeres orientados a iteradores fornecem um conjunto fixo de valores).
# O protocolo iterador especifica o método __next__(). Deste método, é 
# esperado retornar o próximo item na sequência para retornar ou 
# levantar a exceção StopIteration. É usado para indicar que o iterador
# terminou de fornecer valores.
#---------------------------------------------------------
# Métodos relacionados a iteração
# Sumarizando, temos:
#   * __iter__() do protocolo Iterável que é usado para retornar o objeto
#                 iterador.
#   * __next__() do protocolo Iterador que é usado para obter o próximo valor
#                   em uma sequência de valores.
# Qualquer tipo de dado pode ser tanto Iterável quanto Iterador, mas isso
# não é requerido. Um Iterável poderia retornar um objeto diferente que
# será usado para implementar o iterador ou pode retornar si próprio como o
# iterador - é uma escolha do designer.
#-----------------------------------------------------------------
# A Classe Iterável Pares
# Para ilustrar as ideias por trás de iteráveis e iteradores vamos implementar
# uma classe simples; esta classe será a classe Pares que é usada para
# fornecer um conjunto de valores pares de 0 a algum limite. Isto ilustra
# que não são apenas containeres de dados que podem ser iteráveis/iteradores.
# Também ilustra um tipo que é tanto iterável quanto iterador.

class Pares(object):
    
    def __init__(self, limite):
        self.limite = limite
        self.valor = 0

    # Torna a classe iterável
    def __iter__(self):
        return self
    
    # Torna a classe um iterador
    def __next__(self):
        if self.valor > self.limite:
            raise StopIteration
        else:
            valor_retornado = self.valor
            self.valor += 2
            return valor_retornado
    
# Algumas coisas para se observar nesta classe:
# O método __iter__() retorna self; este é um padrão muito comum e assume
# que a classe também implementa o protocolo iterador.
# O método __next__() ou retorna o próximo valor na sequência ou
# levanta a exceção StopIteration para indicar que não há mais valores
# disponíveis.
#----------------------------------------
# Usando a classe Pares em um laço for
print('Começando...')
for i in Pares(6):
    print(i, end=', ')
print('Terminou.')

# Que resulta em:
#--
# Começando...
# 0, 2, 4, 6, Terminou.
#--
# Isto faz parecer como se o tipo Pares fosse um tipo embutido pois pode
# ser usado com uma estrutura existente em Python; no entanto, o laço for
# simplesmente espera ser dado um iterável; por isso Pares é compatível.
#-------------------------------------------
# Móduto Itertools
# O módulo itertools fornece várias funções úteis que retornam 
# iteradores construídos de vários modos. Pode ser usado para fornecer
# um iterador sobre uma seleção de valores de um tipo de dado que é 
# iterável; pode ser usado para combinar iteráveis juntos, etc.
#--------------------------------------------
# Geradores
# Em muitos casos não é apropriado (ou possível) obter todos os dados
# a serem processados de antemão (por razões de performance, memória,
# etc.).
# Geradores são funções especiais que podem ser usadas para gerar
# uma sequência de valores para serem iterados sobre conforme a necessidade.
# em vez de por antemão.
# A única coisa que torna um gerador uma função geradora é o uso da 
# palavra chave 'yield'. Yield pode apenas ser usada dentro de uma 
# função ou método. Em sua execução, a função é suspensa, e o valor da
# declaração yield é retornado como o valor do 'ciclo' atual. Se isto
# é usado com um loop for, então o loop executa uma vez para esse valor.
# A execução da função gerador é, então, resumida após o loop completou
# um ciclo e o valor do próximo ciclo é obtido.
# A função gerador continuará fornecendo valores até ela retornar (que
# significa que uma sequência infinita de valores pode ser gerada).
#---------------------------------------------
# Definindo uma função gerador
# um exemplo muito simples de uma função gerador é dado abaixo:
def gerar_numeros():
    print('Começo')
    yield 1
    print('Continuação')
    yield 2
    print('Final')
    yield 3
    print('Término')
# Esta é uma função gerador pois possui pelo menos uma declaração yield.
# Cada vez que a função gerar_numeros é chamada dentro de uma declaração
# for ela retornará um dos valores associados com a declaração yield;
# ----------------------------------------------
# Usando uma função gerador em um laço for
for i in gerar_numeros():
    print(i)
# É comum para o corpo de um gerador ter algum tipo de loop dentro de si.
# Este laço(loop)é usado tipicamente para gerar valores que serão
# 'fornecidos' (yielded). No entanto, como é mostrado acima, isso não é 
# necessário. Note que a funcao gerar_numeros() é uma funcao mas é uma
# função especial pois retorna um objeto gerador. Isto é, uma função
# gerador retorna um objeto gerador que cerca a geração dos valores 
# requeridos mas está escondida do desenvolvedor.
# -------------------------------------------------
# Quando as declarações yield são executadas?
# É interessante considerar o que acontece dentro de uma função gerador;
# ela é, na verdade, suspensa toda vez que uma declaração yield fornece um
# valor e apenas volta quando a próxima solicitação por um valor é recebida.
# Isto pode ser visto adicionando algumas declarações print à função gerar_numeros():
# O resultado é:
#--
#Começo
#1
#Continuação
#2
#Final
#3
#Término
#--
#----------------------------------------------------
# Um gerador de números pares
# Poderíamos ter usado um gerador para produzir um conjunto de números
# pares até um limite especificado, como fizemos antes com a classe
# Pares, mas sem a necessidade de criar uma classe (e implementar
# dois métodos especiais). Por exemplo:
def pares_ate(limite):
    valor = 0
    while valor <= limite:
        yield valor
        valor += 2
#for i in pares_ate(6):
#    print(i, end=', ')
# Que resulta em:
#--
#0, 2, 4, 6,
#--
# O que ilustra o benefício potencial de um gerador sobre um iterador;
# a função pares_ate é muito mais simples e concisa que a classe iterável Pares.
#---------------------------
# Aninhando funções geradoras:
# Você também pode aninhar funções geradoras como cada chamada para a
# função geradora é encapsulada em seu próprio objeto gerador que captura
# todas as informações de estado precisadas por aquela invocação do gerador.
# Por exemplo:
for i in pares_ate(4):
    print('i:', i)
    for j in pares_ate(6):
        print('j:', j, end=', ')
    print('')
# Que retorna:
#--
#i: 0
#j: 0, j: 2, j: 4, j: 6,
#i: 2
#j: 0, j: 2, j: 4, j: 6,
#i: 4
#j: 0, j: 2, j: 4, j: 6,
#--
# Como pode ver deste laço, a variável i é presa aos valores
# produzidos pela primeira chamada de pares_ate() enquanto a
# variável do laço j é presa a valores produzidos pela segunda chamada a
# pares_ate().
#-----------------------------------
# Usando geradores fora de um laço for
# Você não precisa de um laço for para trabalhar com uma função gerador;
# o objeto gerador retornado de fato pela função gerador suporta a função
# next(). Esta função pega um objeto gerador e retorna o próximo valor
# na sequência:
pares = pares_ate(4)
print(next(pares), end=', ')
print(next(pares), end=', ')
print(next(pares))
# Que retorna:
#--
# 0, 2, 4
#--
# Chamadas subsequentes a next(pares) não retornam um valor; se preciso,
# o gerador pode lançar um erro/exceção.
#-----------------------------------------
# Corrotinas
# Foram introduzidas em Python 2.5 mas ainda são amplamente mal-entendidas.
# Muitas documentações introduzem corrotinas dizendo que elas são 
# similares a geradores, mas há uma diferença fundamental entre eles:
#   * geradores são produtores de dados;
#   * corrotinas são consumidores de dados.
# Isto é, corrotinas consomem dados produzidos por outra coisa; enquanto
# um gerador produz uma sequência de valores que outra coisa pode
# processar.
# A função send() é usada para enviar valores para uma corrotina. Estes
# itens de dados tornam-se disponíveis dentro da corrotina; que irá 
# esperar por valores sejam fornecidos a ela. Quando um valor é fornecido,
# então algum comportamento será disparado(triggered). Assim,
# quando uma corrotina consome um valor isto aciona algum comportamento
# para ser processado.
# Parte da confusão entre geradores e corrotinas é que a palavra chave
# yield é reutilizada dentro de uma corrotina; é usada dentro de uma
# corrotina para fazâ-la esperar até que um valor tenha sido enviado.
# Então fornecerá este valor para a corrotina.
# Também é necessário 'prime'(?) uma corrotina usando as funções
# next() ou send(None). Isto avança a corrotina para chamar yield onde 
# ela esperará até que um valor seja-lhe enviado.
# Uma corrotina pode continuar para sempre a menos que close() seja
# enviado a ela. É possível perceber a corrotina sendo fechada 
# pegando a exceção GeneratorExit; você pode ativar então algum 
# comportamento de desligamento se necessário.
# Como exemplo, é dada a função grep() abaixo:
def grep(padrao):
    print('Procurando', padrao)
    try:
        while True:
            linha = (yield)
            if padrao in linha:
                print(linha)
    except GeneratorExit:
        print('Saindo da corrotina')

# Esta corrotina vai esperar por dados de entrada; quando são enviados 
# a ela, então os dados serão atribuídos à variável linha. Então checará
# se o padrão usado para iniciar a corrotina está presente em linha; se
# estiver, exibirá a linha; então retornará ao início e esperará para o 
# próximo dado ser enviado à corrotina. Se, enquanto esperando, a corrotina 
# for fechada, então irá pegar a exceção GeneratorExit e exibir a mensagem
# apropriada.
print('Iniciando')
g = grep('Python')
# prime the coroutine
next(g)
# Envia dados para a corrotina
g.send('Java é maneiro')
g.send('C++ é maneiro')
g.send('Python é maneiro')
# Agora fecha a corrotina
g.close()
print('Feito')
# Com a saída:
#--
#Iniciando
#Procurando Python
#Python é maneiro
#Saindo da corrotina
#Feito
#--
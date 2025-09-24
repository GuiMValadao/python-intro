# Funçoes em python
# Um jeito em que as unidades menores podem ser definidas em Python sao funçoes.
# Em Python, funçoes sao grupos de declaraçoes relacionadas que podem ser chamadas juntas,
# que tipicamente executam uma tarefa especifica, e que podem ou nao pegar um conjunto de parametros ou retornar um valor.
# Funçoes podem ser definidas em um lugar e chamadas ou invocadas (invoked) em outro, o que ajuda a tornar o codigo mais modular e facil de entender.
# Tambem significa que a mesma funçao pode ser chamada multiplas vezes ou em multiplos lugares. Isto ajuda a garantir que, apesar de uma parte da funcionalidade
# ser usada em vaarios lugares, so precisa ser definida uma vez e apenas ser mantida e testada em um lugar.
#-----------------------------------------
# Como funçoes funcionam
# Quando uma funçao e chamada, o fluxo do controle do programa pula de onde a funçao e chamada para onde ela foi definida.
# O corpo da funçao e executado antes do controle retornar para onde ela foi chamada.
# Como parte deste processo, todos os valores que estavam no lugar quando a funçao foi chamada  sao armazenados
# (stored away) em uma coisa chamada 'stack' de modo que se a funçao define suas proprias versoes, elas nao sobrescrevem uma a outra.
# A invocaçao de uma funçao e ilustrada abaixo:
# def nome_funcao():
# ...                <--
# ...                  |
# # Inicio do programa |
# ...                  |
# ...                  |
# nome_funcao()>--------
# ...                  |
# nome_funcao() >-------
#-----------------------------------------
# Tipos de funçao
# Tecnicamente falando ha dois tipos de funçoes em Python: 'built-in' e 'user defined'.
# Funçoes built-in sao as fornecidas pela linguagem, como print() e input().
# User-defined sao as escritas por desenvolvedores.
#-----------------------------------------
# Definindo funçoes
# A sintaxe basica e ilustrada abaixo:
#   def nome_funcao(lista de parametros):
#       """docstring"""
#       declaracao
#       declaracao(s)
# 1 - Todas as funçoes (nomeadas) sao definidas usando a palavra chave 'def';
# ela indica o inicio da definiçao de uma funçao. Uma palavra chave e parte da
# sintaxe da linguagem Python, nao pode ser redefinida e nao e uma funçao.
# 2 - Uma funçao pode ter um nome que a identifica unicamente, mas tambem pode-se
# ter funçoes anonimas.
# 3 - As convençoes de nomeaçao para variaveis tambem se aplicam para funçoes,
# todas em minusculo e com diferentes elementos do nome da funçao separados por '_'.
# 4 - Uma funçao pode (opcionalmente) ter uma lista de parametros que permitem dados
# serem passados para a funçao.
# 5 - Dois pontos sao usados para marcar o fim do cabeçalho da funçao e o inicio
# do corpo da funçao.
# 6 - Uma string de documentaçao opcional (a 'docstring') pode ser fornecida
# que descreve o que a funçao faz. Tipicamente usamos aspas triplas, pois elas permitem
# a string da documentaçao ocupar multiplas linhas se necessario.
# 7 - Uma ou mais declaraçoes em Python compoem o corpo da funçao. Elas sao indentadas relativas
# a definiçao da funçao. Todas as linhas indentadas sao parte da funçao ate a linha
# que e indentada no mesmo nivel da linha 'def'.
# 8 - E comum usar 4 espaços (nao um tab) para determinar o quanto identar o corpo da funçao.
#--------------------------------------------
# Um exemplo de funçao
# Uma funçao simples:
#def print_msg():           # Funçao nomeada 'print_msg'
#    print('Ola, mundo!')   # Corpo da funçao
#print_msg()                # Chamada da funçao
# Podemos adicionar um parametro tornando-a mais geral e reutilizavel:
#def print_msg(msg):
#    print(msg)
#msg = input('Insira a frase desejada: ')
#print_msg(msg)
#---------------------------------------------
# Retornando valores das funçoes
# Para retornar um valor da funçao usa-se a declaraçao 'return'.
# Quando 'return' e alcançado na funçao, sua execuçao termina e returna o valor
# encontrado apos 'return'. Se tem um valor, torna-se avaliavel para o codigo que chamou a funçao.
# Pode-se retornar multiplas variaveis:
#def troca(a, b):
#   return b, a
#a = 2
#b = 3
#z = troca(a,b)
#print(z)
# P valor retornado pela funçao troca e chamado de 'tuple'.
#----------------------------------------------------------
# Docstring
# Conforme as funçoes tornam-se mais complexas, a documentaçao se torna mais importante.
# A docstring permite que a funçao forneça alguma orientaçao no que e esperado
# em termos de dados passados para os parametros, potencialmente o que vai acontecer se os dados sao incorretos
# assim como qual o proposito da funçao.
#def get_integer_input(message):
#    """
#    Esta funçao vai mostrar a mensagem ao usuario e pedir que um
#    inteiro seja fornecido.
#
#    Se o usuario colocar algo que nao e um numero entao o input
#    sera rejeitado e uma mensagem de erro sera mostrada.
#
#    O usuario sera pedido entao para tentar novamente."""
#    value_as_string = input(message)
#    while not value_as_string.isnumeric():
#        print('O valor deve ser inteiro')
#        value_as_string = input(message)
#    return int(value_as_string)
#age = get_integer_input('Por favor, digite sua idade: ')
#print('idade =', age)
#print(get_integer_input.__doc__)            # print(nome_funçao.__doc__) exibe a documentaçao
#--------------------------------------------------
# Parametros de funçao
# Um parametro e uma variavel definida como parte do cabeçalho da funçao
# e e usado para fazer dados avaliaveis dentro da funçao
# Um argumento e o valor ou dado de fato passados para a funçao quando
# ela e chamada. Os dados serao arquivados dentro dos parametros
# * Funçoes de multiplos parametros
# Dois ou mais parametros sao separados por virgula. Antes do Python 3.7 havia
# um limite de 256 parametros, mas este limite nao existe mais.
# * Valores de parametros padrao
# Quando se tem um ou mais parametros, pode-se querer fornecer valores padrao
# para um ou todos os parametros, especialmente para os que nao serao usados
# na maioria dos casos. Isto pode ser feito declarando o valor no cabeçalho da funçao
# junto com o nome do parametro. Se um valor for escolhido para o parametro,
# ele vai se sobrepor ao padrao. Se nao, o padrao sera usado.
#def cumprimentador(nome, mensagem = 'Vida Longa e Prospera'):
#    print('Bem-vindo', nome, '-', mensagem)
#cumprimentador('Guilherme')                                # Argumento vazio, retorna argumento padrao
#cumprimentador('Guilherme', 'Espero que goste de Python')  # Argumento fornecido para a funçao, sobrescreve o padrao
# 'nome' e um campo/parametro obrigatorio nesse caso, e 'mensagem' e um parametro opcional.
# Um ponto sutil e que qualquer quantidade de parametros podem possuir valores padrao,
# mas quando um parametro tem um valor padrao, todos os parametros restantes a direita dele
# tambem deverao ter valores padrao.
#---------------------------------------------
# Argumentos nomeados
# Pode-se definir e chamar nomes para atribuir argumentos aos parametros em vez de atribuir os
# argumentos de forma posicional. Pode-se misturar argumentos posicionais e nomeados,
# mas nao se pode colocar argumentos posicionais depois de um argumento nomeado.
#---------------------------------------------
# Argumentos arbitrarios
# Em agluns casos pode-se nao saber quantos argumentos serao fornecidos ao chamar uma funçao
# Python permite passar um numero arbitratio de argumentos para a funçao e entao
# processar esses argumentos na funçao.
# Para definir uma lista de parametros como tendo comprimento arbitrario,
# o parametro e marcado com um asterisco. Por exemplo:
# comprimentador(*args):
#    for nome in args:
#        print('Bem-vindo', nome)
#comprimentador('John', 'Denise', 'Phoebe', 'Adam','Gryff')
#----------------------------------------------
# Argumentos posicionais e palavras chave
# Algumas funçoes em Python sao definidas de modo que os argumentos para os metodos
# podem ser providenciados tanto usando um numero varial de argumentos posicionais
# quanto de argumentos nomeados(palavras-chave). Estas funçoes tem dois agumentos:
# *args e **kwargs (para argumentos posicionais e nomeados)
# Por exemplo, a funçao 'my_function' pega um numero variavel de ambos argumentos
# posicionais e nomeados:
#def my_function(*args, **kwargs):
#    for arg in args:
#        print('arg:', arg)
#    for key in kwargs.keys():
#        print('key:', key, 'has value: ', kwargs[key])
#my_function('John', 'Denise', daughter='Phoebe', son='Adam')
#print('-' * 50)
#my_function('Paul', 'Fiona', son_number_one='Andrew',
#son_number_two='James', daughter='Joselyn')
#------------------------------------------------------
# Funçoes anonimas
# Todas as funçoes definidas ate aqui tinham um nome pelo qual elas podiam
# ser referenciadas, como 'comprimentador' ou 'my_function', que as possibilitavam ser chamadas multiplas vezes.
# Entretanto, em alguns casos queremos criar uma funçao e usa-la apenas uma vez,
# e nomeando-a para essa unica vez pode 'poluir' o espaço de nomes do programa
# (ou seja, muitos nomes) e alguem poderia chama-la quando nao seria esperado.
# Para evitar isso, pode-se definir uma funçao anonima, que nao tem nome e so pode ser
# chamada no ponto em que eela e definida.
# Sao definidas usando a palavra-chave 'lambda', sendo  por isso conhecidas como funçoes lambda.
# A sintaxe e
#lambda arguments: expression
# Funçoes anonimas podem ter qualquer numero de argumentos mas apenas uma expressao,
# ou seja, uma declaraçao que retorna um valor, como corpo.
#double = lambda i: i * i
#print(double(10))
#print(double(4))


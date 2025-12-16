# Capítulo 22 - Expressões Regulares em Python
# Expressão Regular (Regular Expression) é um modo muito poderoso de se
# processar texto ao procurar por padrões recorrentes; são bastante usadas
# com dados armazenados em arquivos de texto plano (como logs), arquivos
# CSV e arquivos Excel.
# -----------------------------------------------------
# Uma Expressão Regular (também chamada regex ou apenas 're') é uma sequência
# de caracteres (letras, números e caracteres especiais) que formam um padrão
# que pode ser usado para buscar texto para ver se o texto contém sequências
# de caracteres que combinam com o padrão.
# Por exemplo, poderia ter um padrão definido como 3 caracteres seguido de
# 3 números. Este padrão poderia ser usado para procurar um padrão igual
# em outras strings. Assim, as strings seguintes ou combinam(contém) este
# padrão ou não:

# Abc123         Combina com o padrão
# A123A          Não combina com o padrão
# 123AAA         Não combina com o padrão

# Expressões regulares são amplamente utilizadas para encontrar informações
# em arquivos, por exemplo:
#   * encontrar todas as linhas em um arquivo de registro(log) associado
#       a um usuário específico ou uma operação específica,
#   * para validar entrada como checar que uma string é um endereço de e-mail
#       válido ou CEP etc.
# Suporte para expressões regulares é largamente espalhado dentro das linguagens
# de programação como Java, C#, PHP e particularmente Perl. Python não é exceção,
# e tem o módulo embutido re (assim como outros módulos) que suportam RegEx.
# ---------------------------------------------
# Padrões de Expressão Regular
# Você pode definir um padrão de expressão regular usando qualquer caractere
# ou número em ASCII. Assim, a string 'John' pode ser usada para definir
# um padrão regex que pode ser usado para combinar qualquer outra string que
# contém os caracteres 'J', 'o', 'h', 'n'. Assim, cada uma das strings seguintes
# combinarão com este padrão:
#   * 'John Hunt'
#   * 'John Jones'
#   * 'Andrew John Smith'
#   * 'Mary Helen John'
#   * 'John John John'
#   * 'I am going to visit John'
#   * 'I once saw a film by John Wayne'
# Mas as strings seguintes não combinariam com o padrão:
#   * 'Jon Davies' - neste caso, a ortografia de John é diferente.
#   * 'john williams' - neste caso, a letra maiúscula 'J' não combina com a minúscula 'j'.
#   * 'David James' - neste caso, não contém a string John.
# Regexs usam caracteres especiais para permitir a descrição de padrões mais
# complexos. Por exemplo, podemos usar os caracteres especiais '[]' para
# definir um conjunto de caracteres que pode combinar. Por exemplo, se queremos
# indicar que J pode ser maiúsculo ou minúsculo, podemos escrever '[Jj]', que
# indica que ou 'J' ou 'j' pode combinar com a primeira letra.
#   * [Jj]ohn - isto declara que o padrão pode começar com letra maiúscula e minúscula, seguido por 'ohn'.
# ---------------------------------------------------
# Metacaracteres de padrão
# Há vários caracteres especiais (muitas vezes chamados metacaracteres) que
# tem um significado específico dentro de um padrão regex, listados na tabela:

# Caractere  | Descrição                                 | Exemplo
# -----------|-------------------------------------------|-------------------------------------------
# []         | Conjunto de caracteres                    | [a-d] caracteres na sequência de 'a' até 'd'
# -----------|-------------------------------------------|-------------------------------------------
# \          | Indica uma sequência especial (também     | '\d' indica que o caractere deveria ser um inteiro
#            | usado para escapar caracteres especiais)  |
# -----------|-------------------------------------------|-------------------------------------------
# .          | Qualquer caractere exceto de nova linha   | 'J.hn' indica que qualquer caractere pode estar entre 'J' e 'h'
# -----------|-------------------------------------------|-------------------------------------------
# ^          | Indica que a string deve começar com o    | '^hello' indica que a string deve começar
#            | seguinte padrão                           | com 'hello'
# -----------|-------------------------------------------|-------------------------------------------
# $          | Indica que a string deve termina com      | 'world$' indica que a string deve terminar
#            | o padrão precedente                       | com 'world'
# -----------|-------------------------------------------|-------------------------------------------
# *          | Zero ou mais ocorrências do padrão        | 'Python*' indica que procuramos por zero ou
#            | precedente                                | mais vezes que Python está em uma linha
# -----------|-------------------------------------------|-------------------------------------------
# +          | Uma ou mais ocorrências do padrão         | 'info+' indica que devemos encontrar 'info'
#            | precedente                                | na string pelo menos uma vez
# -----------|-------------------------------------------|-------------------------------------------
# ?          | Zero ou 1 ocorrência do padrão precedente | 'john?' indica zero ou 1 instância de 'john'
# -----------|-------------------------------------------|-------------------------------------------
# {}         | Exatamente o número de ocorrências        | 'John{3}' indica que esperamos ver 'John na
#            | especificado                              | string 3 vezes. '. 'X{1,2}' indica que pode haver 1 ou 2 'X' próximos entre si na string.
# -----------|-------------------------------------------|-------------------------------------------
# |          | Um ou outro                               | 'True|OK' indica que procuramos ou por True ou OK
# -----------|-------------------------------------------|-------------------------------------------
# ()         | Agrupa uma regex; pode aplicar outro      |'(abc|xyz){2}' indica que procuramos por abc ou xyz repetidos duas vezes.
#            | operador ao grupo todo                    |

# -----------------------------------------------------------------
# Sequências especiais
# Uma sequência especial é uma combinação de '\' seguido por uma combinação
# de caracteres que tem significado especial. A seguinte tabela lista as
# sequências mais comuns usadas para Regex:

# Sequência | Descrição                                 | Exemplo
# ----------|-------------------------------------------|-------------------------------------------
# \A        | Retorna uma combinação se os seguintes    | "\AThe" deve começar com 'The'
#           | caracteres estão no início da string      |
# ----------|-------------------------------------------|-------------------------------------------
# \b        | Retorna uma combinação onde os caracteres | "\bon" ou "ou\b" indica que
#           | especificados estão no começo ou fim de   | uma string deve iniciar ou terminar com 'on'
#           | uma palavra                               |
# ----------|-------------------------------------------|-------------------------------------------
# \B        | Indica que os seguinte caracteres devem   | r"\Bon" ou r"on\B" não deve começar
#           | estar presentes em uma string, mas não no | ou terminar com 'on'
#           | fim ou começo de uma palavra              |
# ----------|-------------------------------------------|-------------------------------------------
# \d        | Retorna uma combinação onde a string tem  | "\d"
#           | dígitos (números de 0 a 9)                |
# ----------|-------------------------------------------|-------------------------------------------
# \D        | Retorna uma combinação onde a string não  | "\D"
#           | contém dígitos                            |
# ----------|-------------------------------------------|-------------------------------------------
# \s        | Retorna uma combinação onde a string tem  | "\s~"
#           | caractere de espaço em branco             |
# ----------|-------------------------------------------|-------------------------------------------
# \S        | Retorna uma combinação onde a string não  | "\S"
#           | contém espaço em branco                   |
# ----------|-------------------------------------------|-------------------------------------------
# \w        | Retorna uma combinação onde a string tem  | "\w"
#           | qualquer caractere de palavra (caracteres |
#           | de a a Z, dígitos 0-9 e sublinhado '_'    |
# ----------|-------------------------------------------|-------------------------------------------
# \W        | Retorna uma combinação onde a string não  | "\W"
#           | contém nenhum caractere de palavra        |
# ----------|-------------------------------------------|-------------------------------------------
# \Z        | Retorna uma combinação se os seguintes    | "Hunt\Z"
#           | caracteres estão no final da string       |
# ----------|-------------------------------------------|-------------------------------------------

# -------------------------------------------------------------------
# Conjuntos
# Um conjunto é uma sequência de caracteres dentro de chaves que tem significados
# específicos. A seguinte tabela tem alguns exemplos:
# Conjunto  | Descrição
# ----------|-------------------------------------------
# [jeh]     | Retorna uma combinação onde um dos caracteres especificados (j, e ou h) estão presentes
# [a-x]     | Retorna uma combinação para qualquer caractere minúsculo, alfabeticamente entre a e x
# [^zxc]    | Retorna uma combinação para qualquer caractere exceto z, x e c
# [0123]    | Retorna uma combinação onde qualquer dos dígitos indicados está presente
# [0-9]     | Retorna uma combinação para qualquer dígito entre 0 e 9
# [0-9][0-9]| Retorna uma combinação para qualquer número de dois dígitos entre 00 e 99
# [a-zA-Z]  | Retorna uma combinação para qualquer caractere alfabeticamente entre a e z ou A e Z

# ---------------------------------------------------------------
# O módulo re de Python
# Este módulo é embutido no Python para trabalhar com regex. Você poderia,
# também, examinar o módulo regex, que tem compatibilidade retroativa com o
# padrão re, mas fornece recursos adicionais.
# --------------------------------------------------------------
# Trabalhando com RegEx
# Usando Strings Brutas (Raw)
# Um ponto importante sobre muitas das strings usadas para definir os padrões
# de expressões regulares é que eles são precedidos por 'r', por exemplo, r'/bin/sh$'.
# O 'r' antes da string indica que ela deve ser tratada como uma string bruta.
# Uma string bruta é uma string em Python na qual todos os caracteres são tratados
# como caracteres individuais. Significa que a barra ('\') é tratada como um
# caractere literal em vez de um caractere especial que é usado para escapar
# o próximo caractere. Por exemplo, em uma string padrão, '\n' representa uma
# nova linha, por exemplo:
# s = "Hello \n World"
# print(s)
# # Obtemos:
# # Hello
# #  World
# # No entanto, se prefixarmos a string com r:
# s = r"Hello \n World"
# print(s)
# Obtemos:
# Hello \n World
# Isto é importante para expressões regulares pois caracteres como '\' são
# usados dentro de padrões para ter significados especiais em expressões
# regulares e assim não queremos que Python os processe do modo usual.
# ---------------------------------------------------------
# Exemplo simples

# import re

# texto1 = "john williams"
# padrao = "[Jj]ohn"
# print("procurando em", texto1, "pelo padrão", padrao)
# if re.search(padrao, texto1):
#     print("Combinação encontrada")

# A função re.search(padrao, texto) retorna None(ou False pela declaração if)
# ou um objeto Match(que sempre tem valor Booleano True). Tanto o objeto Match
# quando o método search serão descritos em mais detalhes na sequência.
# ------------------------------------------------
# Objeto Match
# Objetos Match são retornados pelas funções search() e match(). Sempre tem valor
# Booleano True. Essas funções retornam None quando não é encontrada uma combinação
# e um objeto Match quando é. Portanto, pode-se usar um objeto Match com uma
# declaração if:
# import re

# pattern = r"[Dd]ia"
# string = "Um dia desses, vai chover. Diante disso, temos que esperar."

# match = re.search(pattern, string)
# if match:
#     process(match)

# Objetos Match suportam vários método e atributos, incluindo:
#   * match.re: O objeto expressão regular cujo método match() ou search() produziu
#       esta instância match.
#   * match.string: A string passada para match() ou search().
#   * match.start([group]) / match.end([group]): Retorna os índices de início e
#       fim da substring combinada por grupo.
#   * match.group(): retorna a parte da string onde houve uma combinação.
#
# ---------------------------------------------------
# A função search()
# Essa função procura a string por uma combinação, e retorna um objeto Match se
# encontrar. A assinatura da função é:
# re.search(pattern, string, flags=0)
# Esses parâmetros significam:
#   * pattern é a expressão regular a ser usada no processo de combinação.
#   * string é a string a ser procurada
#   * flags: estas flags (opcionais) podem ser usadas para indicar quaisquer
#       comportamentos opcionais associados com o padrão. Elas incluem:
# Flag          | Descrição
# re.IGNORECASE | Performa a combinação ignorando a caixa (maiúscula ou minúscula)

# re.LOCALE     | Interpreta palavras de acordo com o local atual. Esta interpretação
#               | afeta o grupo alfabético (\w e \W), assim como comportamento de contorno (\b e \B)

# re.MULTILINE  | Faz com que $ combine com finais de linha (e não apenas strings) e
#               | faz ^ combinar com o início de qualquer linha.

# re.DOTALL     | Faz com que o caractere ponto combine om qualquer caractere, incluindo nova linha.

# re.UNICODE    | Interpreta letras de acordo com o conjunto de caracteres do Unicode;
#               | afeta o comportamento de \w, \W, \b, \B.

# re.VERBOSE    | Ignora espaços em branco dentro do padrão (exceto dentro de um
#               | conjunto [] ou quando escapado com uma barra \) e trata '#' não
#               | escapado como marcador de comentário.

# Se houver mais de uma combinação, apenas a primeira ocorrência será retornada:

# import re

# line1 = 'The price is 23.55'
# containsIntegers = r'\d+'
# if re.search(containsIntegers, line1):
#     print('Line 1 contains an integer')
# else:
#     print('Line 1 does not contain an integer')

# ------------------------------------------
# A função match()
# Esta função tenta combinar um padrão de expressão regular no início de uma
# string. A assinatura dessa função é:
# re.match(pattern, string, flags=0)
# Os parâmetros são equivalentes aos da função search, e match() também retorna
# um objeto Match se houver combinação ou None se não.
# ----------------------------------------------------
# A diferença entre match() e search()
#    * match() checa por uma combinação apenas no início da string
#   * search() checa por uma combinação em qualquer lugar da string.
# ----------------------------------------------------
# A função findall()
# A função findall() retorna uma lista contendo todas as combinações. A assinatura
# dessa função é:
# re.findall(patter, string, flags=0)
# Ela retorna todas as combinações não-sobrepostas de pattern na string, como
# uma lista de strings. A string é scanneada da esquerda para a direita, e combinações
# são retornadas na sequência em que são encontradas. Se um ou mais grupos estão
# presentes no padrão, então uma lista de grupos é retornada; ela será uma lista
# de tuplas se o padrão tem mais de um grupo. Se nenhuma combinação for encontrada,
# uma lista vazia é retornada.
# Um exemplo de usar a função findall() é dado abaixo. Este exemplo busca por uma
# substring iniciando com duas letras seguidas por 'ai' e um único caractere.
# É aplicada a uma frase e retorna apenas a substring 'Spain' e 'plain':
# import re

# str = "The rain in Spain stays mainly on the plain"
# results = re.findall("[a-zA-Z]{2}ai.", str)
# print(results)
# for s in results:
#     print(s)
# A saída desse programa é:
# ['Spain', 'plain']
# Spain
# plain
# ------------------------------

# A função finditer()
# Esta função retorna um iterador fornecendo(yielding) objetos combinados para a
# regex patter na string fornecida. A assinatura dessa função é:
# re.finditer(pattern, string, flags=0)
# A string é scanneada da esquerda para a direita, e combinações são retornadas na
# ordem encontradas. Combinações vazias são incluídas no resultado. Flags podem ser
# usadas para modificar as combinações.
# ------------------------------------------------------------
# A função split()
# Essa função retorna uma lista onde a string foi dividida em cada combinação.
# A sintaxe é:
# re.split(pattern, string, maxsplit=0, flags=0)
# O resultado é a divisão da string pelas ocorrências de pattern. Se os parênteses
# de captura são usados na regex pattern, então o texto de todos os grupos em
# pattern também são retornados como parte da lista resultante. Se maxsplit não
# é zero, no máximo maxsplit divisões ocorrem, e o restante da string é retornada
# como o elemento final da lista. Flags podem, novamente, serem usadas para modificar
# as combinações.
# import re

# str = "It was a hot summer night"
# x = re.split(r"\s", str)
# print(x)

# Que retorna:
# ['It', 'was', 'a', 'hot', 'summer', 'night']

# ------------------------------------------
# A função sub()
# Essa função substitui ocorrências do padrão regex na string com a string repl.
# re.sub(pattern, repl, string, count=0)
# Este método substitui todas as ocorrências do padrão da regex na string com
# repl, substituindo todas as ocorrências se count não for definido. Este método
# retorna a string modificada.
# import re

# pattern = r"(England|Wales|Scotland)"
# input = "England for footbal, Wales for Rugby and Scotland for the Highland games"
# print(re.sub(pattern, "Brazil", input))

# Que gera:
# Brazil for footbal, Brazil for Rugby and Brazil for the Highland games

# Você pode controlar o número de substituições especificando o parâmetro count:
# import re

# pattern = r"(England|Wales|Scotland)"
# input = "England for footbal, Wales for Rugby and Scotland for the Highland games"
# print(re.sub(pattern, "Brazil", input, count=2))

# Com a saída:
# Brazil for footbal, Brazil for Rugby and Scotland for the Highland games

# Você também pode obter quantas substituições foram feitas usando a função subn().
# Esta função retorna a nova string e o número de substituições em uma tupla:
# import re

# pattern = r"(England|Wales|Scotland)"
# input = "England for footbal, Wales for Rugby and Scotland for the Highland games"
# print(re.subn(pattern, "Brazil", input))

# Que gera:
# ('Brazil for footbal, Brazil for Rugby and Brazil for the Highland games', 3)
#
# -------------------------------------------------------
# A função compile()
# A maioria das operações de expressões regulares estão disponíveis tanto como
# funções a nível de módulo(como descrito acima) quando como métodos em um objeto
# de regex compilado.
# As funções de nível-módulo são, tipicamente, simplificadas ou modos padronizados
# de usar a regex comopilada. Em muitos casos, essas funções são suficientes, mas se
# controle mais refinado é necessário, então uma regex compilada pode ser usada.
# re.compile(pattern, flags=0)
# A função compile() compila um padrão de regex em um objeto regex, que pode ser
# usado para combinar usando seus métodos match(), search() e outros descritos abaixo.
# O comportamento da expressão pode ser modificado especificando flags.
# As declarações:
# prog = re.compile(pattern)
# result = prog.match(string)
# São equivalentes a:
# result = re.match(pattern, string)
# mas usar re.compile e salvar o objeto regex resultante para reutilização é mais eficiente
# quando a expressão será usada várias vezes em um único programa. Objetos regex compilados
# suportam os seguintes métodos e atributos:
#   * Pattern.search(string, pos, endpos): Scaneia pela string procurando o primeiro
#       local onde a regex produz uma combinação e retorna o objeto Match correspondente.
#       Retorna None se nenhuma posição da string combina com o padrão. Inicia
#       em pos e termina em endpos se fornecidos (se não, processa toda a string).
#   * Pattern.match(string, pos, endpos): Se zero ou mais caracteres no início
#       da string combinam esta regex, retorna o objeto Match correspondente. Retorna
#       None se a string não combina com o padrão. Os parâmetros pos e endpos são
#       opcionais e especificam os limites do processamento.
#   * Pattern.split(string, maxsplit = 0): Idêntico à função split().
#   * Pattern.findall(string[,pos[,endpos]]): Similar à função findall(), mas
#       também aceita parâmetros opcionais pos e endpos que limitam a região.
#   * Pattern.finditer(string[,pos[,endpos]]): Similar à finditer.
#   * Pattern.sub(repl, string, count=0): Idêntico a sub()
#   * Pattern.subn(repl, string, count=0): Idêntico a subn()
#   * Pattern.pattern: a string padrão da qual o objeto padrão foi compilado.
# Um exemplo de utilização da função compile é dado abaixo. O padrão a ser
# compilado é definido como contendo 1 ou mais dígitos (0 a 9):
# import re

# line1 = "The price is 23.55"
# containsIntegers = r"\d+"
# rePattern = re.compile(containsIntegers)
# matchLine1 = rePattern.search(line1)
# if matchLine1:
#     print("Line 1 contains a number")
# else:
#     print("Line 1 does not contain a number")

# p = re.compile(r"\W+")
# s = "20 High Street"
# print(p.split(s))

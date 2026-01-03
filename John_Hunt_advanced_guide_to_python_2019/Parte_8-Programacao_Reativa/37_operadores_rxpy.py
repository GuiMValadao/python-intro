# Capítulo 37 - Operadores RxPy

# Operadores da Programação Reativa
# Por trás da interação entre um Observável e um Observador está um fluxo de dados.
# Isto é, o Observável fornece um fluxo de dados a um Observador que consume/
# processa aquele fluxo. É possível aplicar um operador a estes fluxo de dados
# que pode ser usado para filtrar, transformar e geralmente refinar como e
# quando o dado é fornecido ao Observador.
# Os observadores são, em maioria, definidos no módulo rx.operators, por exemplo,
# rx.operators.average(). Entretanto, é comum usar um apelido para isto, chamando
# o módulo operators como op:
# from rx import operators as op
# Isto permite uma forma mais curta para usar ao referenciar um operador, como
# op.average().
# Muitos dos operadores RxPy executam ums função que é aplicada a cada um dos
# items de dados produzidos por um Observável. Outros podem ser usados para criar
# um Observável inicial (já vimos esses operadores na forma do operador from_list()).
# Outro conjunto de operadores podem ser usados para gerar um resultado baseado
# em dados produzidos pelo Observável (como o operador sum()).
# Os operadores de RxPy podem ser categorizados como:
#   * Criacionais
#   * Transformacionais
#   * Combinatoriais
#   * Filtros
#   * Manipuladores de erros
#   * Operadores condicionais e booleanos
#   * Matemáticos
#   * Conectáveis
# --------------------------------------------------------
# Operadores de Piping
# Para aplicar um operador diferente dos criacionais a um Observável é necessário
# criar uma pipe. Ume Pipe é, essencialmente, uma série de uma ou mais operações
# que podem ser aplicadas ao fluxo de dados gerado pelo observável. O resultado
# da aplicação da Pipe é que um novo fluxo de dados é gerado que representa os
# resultados produzidos seguindo a aplicação de cada operador em sequência. Isto
# é ilustrado na figura pipe.png.
# Para criar uma pipe, o método Observable.pipe() é usado. Este método pega uma
# lista separada por vírgulas de um ou mais operadores e retorna um fluxo de dados.
# Então, os observadores podem se inscrever ao fluxo de dados da pipe. Isto pode
# ser visto nos exemplos dados no resto deste capítulo.
# ------------------------------
# Operadores criacionais
# Você já viu um exemplo de um operador criacional nos exemplos apresentados
# no capítulo 36, pois o rx.from_list() é um exemplo deles, sendo usado para
# criar um novo Observável baseado em dados armazenados em uma estrutura similar à
# de listas(list like).
# Uma versão mais genérica de from_list() é o operador from_(). Ele pega um
# iterável e gera um Observável baseado nos dados fornecidos pelo iterável.
# Qualquer objeto que implementa o protocolo iterador pode ser usado, incluindo
# tipos definidos pelo usuário. Também existeum operador from_iterable().
# Todos os três operadores fazem a mesma coisa, e pode escolher qual usar baseado
# em qual possui o melhor significado semântico baseado no contexto.
# source = rx.from_([2, 3, 5, 7])
# source = rx.from_iterable([2, 3, 5, 7])
# source = rx.from_list([2, 3, 5, 7])
# Outro operador criacional é o rx.range(). Ele gera um observável para
# uma faixade números inteiros. A faixa pode ser especificada com ou sem um
# valor inicial e com ou sem um passo. Entretanto, o valor máximo na faixa deve sempre
# ser indicado, por exemplo:
# obs1 = rx.range(10)
# obs2 = rx.range(0, 10)
# obs3 = rx.range(0, 10, 1)
# --------------------------------------------
# Operadores Transformacionais
# Existem vários operadores transformacionais, incluindo rx.operators.map() e
# rx.operators.flat_map(). O primeiro aplica um função a cada item de dado
# gerado perlo observável, enquando o segundo, além de aplicar uma função,
# aplica, na sequência, uma operação de achatamento(flatten) ao resultado.
# Por exemplo, se o resultado é uma lista de listas, flat_map transformará
# uma única lista.
# O operador rx.operators.map() é geralmente usado para realizar algum tipo
# de transformação dos dados que recebe. Isso poderia ser acrescentar um a
# todos os valores inteiros, converter o formato dos dados de XML para JSON,
# enriquecer os dados com informações adicionais como a hora em que foi adquirido
# e quem o forneceu etc.
# No exemplo dado abaixo, transformamos o conjunto de valores inteiros fornecidos
# pelo Observável original em strings. Este é um uso típico de um operador
# de transformação, isto é, transformar dados de um tipo para outro ou acrescentar
# informações aos dados.

# import rx
# from rx import operators as op

# source = rx.from_list([2, 3, 5, 7]).pipe(op.map(lambda value: "'" + str(value) + "'"))

# source.subscribe(
#     lambda value: print(
#         "Lambda recebido", value, "é uma string", isinstance(value, str)
#     )
# )

# Com a saída:
# Lambda recebido '2' é uma string True
# Lambda recebido '3' é uma string True
# Lambda recebido '5' é uma string True
# Lambda recebido '7' é uma string True
# --------------------------------------------------
# Operadores combinatoriais
# Esses operadores combinam múltiplos items de dados de alguma maneira. Um exemplo
# é o operador rx.merge(). ESte operador junta os dados produzidos por dois
# observáveis em um único fluxo de dados Observável.
# import rx

# source1 = rx.from_list([2, 3, 5, 7])
# source2 = rx.from_list([10, 11, 12])

# rx.merge(source1, source2).subscribe(lambda v: print(v, end=","))

# Que retorna:
# 2,3,5,7,10,11,12,
# ---------------------------------------
# Operadores de filtragem
# Esta categoria tem vários operadores, entre eles rx.operators.filter(),
# rx.operators.first(), rx.operators.last() e rx.operators.distinct().
# O operador filter() apenas permite que passem aqueles items de dados que
# passarem por alguma expressão teste definida pela função passada ao filtro.
# Esta função deve retornar True ou False. Qualquer item de dado que faça a
# função retornar True é permitida passar pelo filtro.
# Por exemplo, vamos assumir que a função passada ao filter() é projetada
# para permitir que apenas números pares passem. Se o fluxo de dados contem os
# números 2, 3, 5, 7, 4, 9 e 8, apenas os números 2, 4 e 8 passarão:
# import rx
# from rx import operators as op

# source = rx.from_list([2, 3, 5, 7, 4, 9, 8]).pipe(
#     op.filter(lambda value: value % 2 == 0)
# )

# source.subscribe(lambda value: print("Lambda recebido", value))

# Que retorna:
# Lambda recebido 2
# Lambda recebido 4
# Lambda recebido 8

# Os operadores first() e last() emitem apenas o primeiro e último item de
# dado publicado pelo Observável. O operador distinct() suprime items duplicados
# de serem publicados pelo Observável. Por exemplo, na seguinte lista usada como
# dado para o Observável, os números 2 e 3 são duplicados:
# import rx
# from rx import operators as op

# source = rx.from_list([2, 3, 5, 2, 4, 3, 2]).pipe(op.distinct())

# source.subscribe(lambda value: print("Recebido", value))

# Com a saída:
# Recebido 2
# Recebido 3
# Recebido 5
# Recebido 4

# ---------------------------------------------------
# Operadores matemáticos
# Operadores matemáticos e agregados realizam cálculos no fluxo de dados
# fornecido pelo Observável. Por exemplo, o rx.operators.average() pode ser usado
# para calcular a média de um conjunto de números publicados por um Observável.
# De modo similar, rx.operators.max() pode selecionar o valor máximo, rx.operators.min()
# o valor mínimo e rx.operators.sum() somará todos os números publicados etc.
# import rx
# from rx import operators as op

# rx.from_list([2, 3, 5, 7]).pipe(op.sum()).subscribe(lambda v: print(v))
# Que exibe a soma, 17.

# No entanto, em alguns casos pode ser útil receber notificação do total
# intermediário durante a soma assim como o valor final para que operadores
# mais abaixo na corrente possam reagir aos subtotais. Isto pode ser feito
# usando rx.operators.scan(). Ele é, na verdade, um operador transformacional
# mas pode ser usado nesse caso para fornecer uma operação matemática.
# O operador scan() aplica uma função a cada item de dado publicado por um
# Observável e gera seu próprio item de dado para cada valor recebido. Cada
# valor gerado é passado à próxima invocação de scan() assim como publicado
# ao fluxo de dados do Observável. O total acumulado pode, assim, ser gerado
# do subtotal anterior e do novo valor obtido.
# import rx
# from rx import operators as op

# rx.from_([2, 3, 5, 7]).pipe(op.scan(lambda subtotal, i: subtotal + i)).subscribe(
#     lambda v: print(v)
# )

# Com a saída:
# 2
# 5
# 10
# 17

# -------------------------------------------
# Operadores de encadeamento
# Um aspecto interessante da abordagem RxPy a processamento do fluxo de dados é
# que é possível aplicar múltiplos operadores ao fluxo de dados produzido por
# outro Observável. Os operadores discutidos acima, a verdade, retornam outro
# Observável. Este novo Observável pode fornecer seu próprio fluxo de dados baseado
# no fluxo original e o resultado da aplicação de um operador. Isto permite que
# outro operador seja aplicado em sequência ao dado produzido pelo novo Observável.
# Isto permite que os operadores sejam acorrentados juntos para fornecer
# processamento sofisticado dos dados publicados pelo Observável original.
# Por exemplo, poderíamos iniciar filtrando a saída de um Observável de modo
# que apenas certos items de dados são publicados. Poderíamos, então, aplicar
# uma transformação na forma de um operador map() àqueles dados:
# 2 |           | 2 |           | '2'
# 3 |           |   |           |
# 5 |           |   |           |
# 7 |---Filtro--|   |----map----|
# 4 |           | 4 |           | '4'
# 9 |           |   |           |
# 8 |           | 8 |           | '8'

# Note a ordem com que os operadores foram aplicados; primeiro, os dados que
# não são de interesse são removidos e a transformação aplicada no que resta.
# Isto é mais eficiente que aplicar os operadores ao contrário pois, no exemplo
# acima, não precisamos transformar os valores ímpares. Portanto, é comum tentar
# colocar operadores de filtro o mais acima da corrente que for possível.
# O código usado para gerar o conjunto acorrentado de operadores é dado abaixo.
# Neste caso, usamos funções lambda para definir a funçao filter() e map(). Os
# Operadores são aplicados ao Observável obtido da lista fornecida. O fluxo de
# dados gerado pelo Observável é processado por cada um dos operadores definidos
# na pipe. Como existem, agora, dois operadores, a pipe contém ambos e age
# como um cano no qual os dados fluem.
import rx
from rx import operators as op

source = rx.from_list([2, 3, 5, 7, 4, 9, 8])
pipe = source.pipe(
    op.filter(lambda value: value % 2 == 0),
    op.map(lambda value: "'" + str(value) + "'"),
)

pipe.subscribe(lambda value: print("Recebido", value))

# Que retorna:
# Recebido '2'
# Recebido '4'
# Recebido '8'

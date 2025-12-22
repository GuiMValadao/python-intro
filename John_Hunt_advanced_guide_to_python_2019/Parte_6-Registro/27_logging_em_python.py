# Capítulo 27 - Logging em Python
# Python vem com um módulo para registro embutido desde Python 2.3. Este
# módulo, logging, define funções e classes que implementam um framework
# de logging flexível que pode ser usado em qualquer aplicativo/script/
# bibliotecas/módulos em Python.
# Apesar de diferentes frameworks de logging diferirem apenas nos detalhes
# específicos do que oferecem, quase todos tem os mesmos elementos centrais.
# Os elementos centrais do módulo logging de Python são mostrados na figura
# logging.png, e descritos abaixo:
#   * Log Message: É a mensagem a ser registrada da aplicação.
#   * Logger: Fornece aos programadores um ponto de entrada/interface
#       ao sistema de registro. A classe Logger tem vários métodos que
#       podem ser usados para registrar mensagens em diferentes níveis.
#   * Handler: Determinam para onde enviar uma mensagem de registro,
#       manipuladores padrão envolvem manipuladores de arquivos que enviam
#       mensagens a um arquivo e manipuladores HTTP que enviam mensagens a
#       um servidor da web.
#   * Filter: É um elemento opcional na pipeline de logging. Podem ser
#       usados para filtrar a informação a ser registrada fornecendo
#       controle refinado de quais mensagens registradas são retornadas(por exemplo, para um arquivo de log).
#   * Formatter: São usados para formatar a mensagem de registro conforme
#       necessário. Isto pode envolver acrescentar estampas temporais, informação
#       de módulo e função/método etc à mensagem de registro original.
#   * Configuration Information: O logger (e handlers, filters e formatters
#       associados) podem ser configurados ou programaticamente em Python ou
#       por arquivos de configuração. Estes arquivos podem ser escritos usando
#       pares chave-valor ou em um arquivo YAML(Yet Another Markup Language).
# É válido notar que grande parte do framework de logging está escondido do
# desenvolvedor que apenas precisa ver o logger; o restante da pipeline de
# logging é ou configurada por padrão ou por informação deconfiguração de log
# tipicamente na forma de um arquivo de configuração de logs.
# ------------------------------------------------
# O Logger
# Esta classe fornece uma interface à pipeline de logging. É obtido da função
# getLogger() definida no módulo logging. A seguinte seção de código ilustra
# a aquisição do logger padrão e sua utilização para registrar uma mensagem
# de erro.
# import logging

# logger = logging.getLogger()
# logger.error("Isto deveria ser usado com algo inesperado")

# A saída é registrada no console como configuração padrão.
# ---------------------------------------------------
# Controlando a quantidade de informações registradas
# Mensagens de log são, na verdade, associadas com um nível de registro.
# Estes níveis de registro tem a finalidade de indicar a seriedade da
# mensagem sendo registrada. Existem 6 diferentes níveis associados com
# o framework logging do Python:
#   * NOTSET: neste nível, nenhum registro é feito.
#   * DEBUG: Este nível fornece informações detalhadas, tipicamente de interesse
#       quando um desenvolvedor está diagnosticando um bug ou problemas com um aplicativo.
#   * INFO: Este nível dá menos detalhes que o nível DEBUG.
#   * WARNING: Usado para fornecer informações sobre eventos inesperados
#       ou indicação de algum problema provável que um desenvolvedor ou
#       administrador do sistema poderiam querer investigar mais a fundo.
#   * ERROR: Fornece informação sobre algum problema sério que a aplicação
#       não conseguiu resolver e, provavelmente, significa que a aplicação
#       não pode funcionar corretamente.
#   * CRITICAL: É o nível mais alto de problema e é reservado para situações
#       críticas como aquelas em que o programa não pode continuar executando.
#
# Os níveis de log são relativos em com o outro e definidos em uma hierarquia.
# Cada nível de log tem um valor numérico associado com ele(apesar de você
# não deveria nunca usar os números).
# CRITICAL  50
# ERROR     40
# WARNING   30
# INFO      20
# DEBUG     10
# NOTSET    0
# Associado com o nível de log ao qual uma mensagem foi registrada, um logger
# também tem um nível de log associado com ele. O logger processará todas
# as mensagens que estão no nível do logger ou acima daquele nível. Assim,
# se um logger tem um nível WARNING, então ele registrará todas as mensagens usando
# os níveis warning, error e critical.
# De modo geral, uma aplicação não usará o nível DEBUG em produção. Isto é
# geralmente considerado inapropriado pois sua finalidade é apenas cenários
# de debug. O nível INFO pode ser considerado apropriado, mas é provável que
# produza grandes quantidades de informação pois tipicamente guarda a execução
# de funções e métodos. Se um aplicativo foi bem testado e verificado, então
# apenas avisos e erros que deveriam ocorrer/preocupar. Portanto, não é
# incomum padronizar para o nível WARNING em sistemas de produção.
# Se olharmos agora para o seguintes código, que obtém o objeto logger padrão
# e então usa vários métodos diferentes do logger, podemos ver o efeito dos
# níveis de log na saída:
# import logging

# logger = logging.getLogger()
# logger.debug("Este serve para ajudar com o debugging")
# logger.info("Apenas para informação")
# logger.warning("Este é um aviso!")
# logger.error("Isto deveria ser usado com algo inesperado")
# logger.critical("Alguma coisa séria")

# Como o nível padrão do logger é definido como WARNING, apenas as três últimas
# são exibidas, e os dois níveis menores ignorados.
# Entretanto, o objeto Logger nos permite alterar o nível de registro programaticamente
# usando o método setLevel(), por exemplo, logger.setLevel(logging.DEBUG)
# ou por logging.basicConfig(level=logging.DEBUG); ambas irão definir
# o nível do logger para DEBUG.
# Além disso, pode-se desligar o logging definindo seu nível como NOTSET:
# logger.setLevel(logging.NOTSET)
# ou
# logging.Logger.disabled = True
# -------------------------------------------------
# Métodos Logger
#   * setLevel(level)
#   * getEffectiveLevel(): retorna o nível de log do logger
#   * isEnabledFor(level): checa se o logger está habilitado para o nível especificado.
#   * debug(message): registra mensagens no nível de debug
#   * info(message): registra mensagens no nível info
#   * warning(message): registra mensagens no nível warning
#   * error(message): registra mensagens no nível error
#   * critical(message): registra mensagens no nível critical
#   * exception(message): registra um mensagem no nível erro. Entretanto,
#       pode apenas ser usado dentro de um resolvedor de exceções e inclui um
#       stack trace de qualquer exceção associada, por exemplo:


# import logging

# logger = logging.getLogger()

# try:
#     print("iniciando")
#     x = 1 / 0
#     print(x)
# except:
#     logger.exception("mensagem de exceção")
# print("Terminado")

#   * log(level, message): registra mensagens no nível de registro especificado.
# Adicionalmente, também tem vários métodos usados para gerenciar handlers e filters:
#   * addFilter(filter): acrescenta o filtro especificado ao logger.
#   * removeFilter(filter): remove o filtro especificado do objeto logger.
#   * addHandler(handler): o handler especificado é acrescido ao logger
#   * removeHandler(handler): remove o handler especificado do logger.
# ----------------------------------------------
# Logger padrão
# Um logger padrão (ou raiz/root)sempre está disponível do framework de logging.
# Ele pode ser acessado pelas funções definidas no módulo logging. Elas permitem
# que mensagens sejam registradas em níveis diferentes usando métodos como
# info(), error(), warning() mas sem a necessidade de obter uma referência
# ao objeto logger primeiro. Por exemplo:
# import logging

# # Define o nível do logger raiz
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("Para ajudar com debugging")
# logging.info("Apenas informação")
# logging.warning("Aviso")
# logging.error("Algo inesperado")
# logging.critical("Algo sério")

# Que retorna:
# DEBUG:root:Para ajudar com debugging
# INFO:root:Apenas informação
# WARNING:root:Aviso
# ERROR:root:Algo inesperado
# CRITICAL:root:Algo sério

# Perceba que o formato padrão exibido pelo logger root exive o nível de
# log, o nome do log gerando a saída e a mensagem.

# ----------------------------------------------
# Loggers de nível módulo

# A maioria dos módulos não usará o logger root para registrar informações,
# mas usará um logger nomeado(named) ou de nível módulo(module level).
# Tais loggers podem ser configurados independentemente do logger root.
# Isto permite que os desenvolvedores ativem o registro apenas para um
# módulo em vez de para a aplicação inteira. Isto pode ser útil se um
# desenvolvedor quer investigar um problema que está localizado dentro de um
# único módulo. Exemplos de código anteriores neste capítulo usaram a função
# getLogger() sem parâmetros para obter o objeto logger. Isto é apenas outro
# modo de obter uma referência ao logger root que é usado por funções de
# log isoladas como logging.info() ou logging.debug().
# No entanto, é possível criar um logger nomeado. Este é um objeto separado
# que tem seu próprio nome e pode, potencialmente, ter seu próprio nível de
# log, handlers, formatters etc. Para obter um logger nomeado, deve-se passar
# uma string com o nome para o método getLogger():
# logger1 = logging.getLogger('meu logger')
# Isto retorna um objeto logger com o nome 'meu logger'. Note que isto pode
# ser um objeto logger novo, mas se qualquer outro código dentro do sistema atual
# requisitou anteriormente um logger chamado 'meu logger', então aquele objeto
# será retornado no código atual. Assim, múltiplas chamadas a getLogger() com
# o mesmo nome sempre retornarão uma referência ao mesmo objeto Logger.
# É uma prática comum usar o nome do módulo como o nome do logger; como apenas
# um módulo com um nome específico deveria existir dentro de um sistema
# em particular. O nome do módulo não precisa ser 'hard coded' pois pode ser
# obtido usando o atributo do módulo __name__, sendo comum:
# logger2 = logging.getLogger(__name__)

# Podemos ver o efeito de cada tipo de declaração exibindo cada logger:
# import logging

# logger = logging.getLogger()
# print("Root logger:", logger)

# logger1 = logging.getLogger("meu logger")
# print("Logger nomeado:", logger1)

# logger2 = logging.getLogger(__name__)
# print("Logger de módulo:", logger2)

# Que retorna:

# Root logger: <RootLogger root (WARNING)>
# Logger nomeado: <Logger meu logger (WARNING)>
# Logger de módulo: <Logger __main__ (WARNING)>

# Isto mostra que cada logger tem seu próprio nome (o código foi executado
# no módulo principal(main), por isso logger 2 tem o nome __main__) e todos
# os três loggers tem um nível de log efetivo WARNING, que é o padrão.

# --------------------------------------
# Hierarquia de logs
# Existe, de fato, uma hierarquia de loggers com o logger root no topo.
# Todos os loggers nomeados estão abaixo do root. O nome de um logger pode
# ser um valor hierárquico separado por ponto como util, util.lib, util.lib.printer.
# Loggers que estão mais abaixo da hierarquia são filhos de loggers mais acima.
# A hierarquia de nome de loggers é análoga a hierarquia de pacotes Python, e
# idêntica a ela se você organizar os loggers em uma base por-módulo usando
# a construção recomendada logging.getLogger(__name__).
# Esta hierarquia é importante ao considerar o nível de log. Se um nível de
# log não foi definido para o logger atual, então procurará no pai para ver se
# aquele logger tem um nível de log definido, usando o valor encontrado ou
# continuando a procurar por uma definição explícita até chegar ao root,
# com um nível de log padrão WARNING.
# Isto é útil por não é necessário explicitamente definir o nível de log para
# cada objeto logger usados em uma aplicação. Em vez disso, é apenas necessário
# definir o nível de log da raiz (ou para uma hierarquia de módulos um ponto
# apropriado na hierarquia). Este valor pode, então, ser sobrescrito quando necessário.
# -----------------------------------------
# Formatadores
# Existem dois nívels nos quais você pode formatar as mensagens registradas,
# eles estão dentro da mensagem de log passada para um método de registro (como
# info() ou warn()) e pela configuração de nivel topo que indica qual informação
# adicional pode ser acrescentada à mensagem de log individual.
# -----------------------------------------
# Formatando Mensagens de Log
# A mensagem de log pode ter caracteres de controle que indicam quais valores
# deveriam ser colocados dentro da mensagem, por exemplo:

# logger.warning('%s is set to %d', 'count', 42)

# Isto indica que a string de formato espera ser dada uma string(%s) e um
# número (%d). Os parâmetros a serem substituídos na string de formatação
# seguem a string de formatação como uma lista de valores separada por vírgulas.
# ------------------------------------------
# Formatando a Saída de Logs

# A pipeline de logging pode ser configurada para encorporar informação
# padrão com cada mensagem de log. Isto pode ser feito globalmente para todos
# os handlers. Também é possível definir programaticamente um formatador
# específico em um handler individual; isto será discutido mais à frente.
# Para definir globalmente o formato de saída para mensagens de log usa-se
# a função logging.basicConfig() usando o parâmetro nomeado format.
# Este parâmetro pega uma string que pode conter atributos LogRecord organizados
# como você achar melhor. Existe uma lista compreensiva de atriburtos LogRecord
# que pode ser encontrada em  <https://docs.python.org/3/library/logging.html#logrecord-attributes>.
# Os principais atributos são:
#   * args: uma tupla listando os argumentos usados para chamar a função/método associada.
#   * asctime: indica a hora em que a mensagem de log foi criada.
#   * filename: nome do arquivo contendo a declaração de log.
#   * module: o nome do módulo (a porção nome do nome do arquivo).
#   * funcName: o nome da função ou método contendo a declaração de log.
#   * levelName: o nível de log da declaração de log.
#   * message: a mensagem de log em si fornecida pelo método de log.
# O efeito de alguns deles é mostrado abaixo:
# import logging

# logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG)
# logger = logging.getLogger(__name__)


# def fazer_algo():
#     logging.debug("Para ajudar com debugging")
#     logging.info("Apenas informação")
#     logging.warning("Aviso")
#     logging.error("Algo inesperado")
#     logging.critical("Algo sério")


# fazer_algo()

# Estão seção de código exibe:
# 2025-12-21 21:39:33,864 Para ajudar com debugging
# 2025-12-21 21:39:33,865 Apenas informação
# 2025-12-21 21:39:33,865 Aviso
# 2025-12-21 21:39:33,866 Algo inesperado
# 2025-12-21 21:39:33,866 Algo sério

# Entretanto, poderia ser útil saber o nível de registro associado com as
# declarações de log, assim como a função da qual as declarações foram
# chamadas. É possível obter essa informação alterando a string de formato
# passada à função logging.basicConfig():
# logging.basicConfig(format="%(asctime)s [%(levelname)s] #(funcName)s: %(message)s", level=logging.DEBUG)

# Pode-se também controlar o formato da informação de hora-data associada com
# a declaração de log usando o parâmetro datafmt da função logging.basicConfig():
# logging.basicConfig(format="%(asctime)s %(message)s", datefmt='%d%m%Y %I:%M:%S %p level=logging.DEBUG)
# Esta string de formato usa as opções de formatação usadas pela função
# datetime.strptime():
#   * %m - Mês como número preenchido com 0: 01, 02 ... 11, 12
#   * %d - Dia do mês preenchido com zero: 01, 02... 30, 31
#   * %Y - Ano com século como número decimal: 2025
#   * %I - Hora (relógio 12-h): 01, 10...
#   * %M - Minuto, 00, 01, 59...
#   * %S - Segundo, 00, 01, 49...
#   * %p - ou AM ou PM.

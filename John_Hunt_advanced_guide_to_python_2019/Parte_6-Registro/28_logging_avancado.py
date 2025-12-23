# Capítulo 28 - Logging avançado
# Handlers
# Dentro da pipeline de logging, são os handlers que enviam as mensagens a
# seus destinos finais. Por padrão, o handler é configurado para direcionar
# a saída para o console/terminal associado com o programa em execução. Entretanto,
# isto pode ser alterado para enviar as mensagens de log para um arquivo, serviço
# de e-mail, servidor web etc. ou mesmo para qualquer combinação desses pois
# é possível ter múltiplos handlers configurados para um logger. Isto é
# ilustrado para o diagrama da figura handlers.png.
# No diagrama acima, o logger foi conofigurado para enviar todas as mensagens
# oara 4 handlers diferentes, que permitem que uma mensagem de log seja
# escrita para o console, servidor web, um arquivo e um serviço de e-mail.
# Este tipo de comportamento pode ser necessário pois:
#   * O servidor web permitirá que desenvolvedores acessem uma interface web
#       que lhes permitirá ver os arquivos de log mesmo se não tiverem permissão
#       de acessar um servidor de produção.
#   * O arquivo log garante que todos os dados de log estejam armazenados
#       permanentemente dentro do depósito de arquivos.
#   * Uma mensagem de e-mail pode ser enviada a um sistema de notificação
#       para que alguém deja notificado que houve um problema que precisa
#       ser investigado.
#   * O console pode, ainda, estar disponível aos administradores do sistema que
#       podem querer ver a mensagem de log gerada.
# O framework de logging do Python possui vários handlers:
#   * logging.StreamHandler: envia mensagem às saídas como stdout, stderr etc.
#   * logging.FileHandler: envia os logs para arquivos. Há vários tipos de
#       Handlers de arquivos além do básico FileHandler, incluindo logging.handlers.RotatingFileHandler
#       (que rotacionará os arquivos de log baseado em um tamanho de arquivo máximo) e
#       logging.handlers.TimeRotatingFileHandler(que rotacionará o arquivo de log
#       em intervalos de tempo específicos, p.ex , diariamente).
#   * logging.handlers.SocketHandler: que envia mensagens a um TCP/IP socket
#       onde pode ser direcionado a um servidor TCP.
#   * logging.handlers.SMTPHandler: que envia mensagens pelo SMTP(Simple Mail Transfer Protocol) para um servidor de e-mail.
#   * logging.handlers.SysLogHandler: que envia mensagens de log para um programa Unix syslog.
#   * logging.handlers.NTEventLogHandler: que envia uma mensagem a um log de evento do Windows.
#   * logging.handlers.HTTPHandler: envia para um servidor HTTP.
#   * logging.NullHandler: Não faz nada com as mensagens de erro. Isto é bastante
#       usado por desenvolvedores de bibliotecas que querem incluit logging em
#       suas aplicações mas esperam que desenvolvedores preparem um handler
#       paropriado quando usarem a biblioteca.
# ----------------------------------------------------------
# Definindo o Handler de saída de root
# O seguinte exemplo usa a função logging.basicConfig() para preparar o
# logger root para usar um FileHandler que escreverá as mensagens de log em
# um arquivo chamado 'exempl.log':

# import logging

# logging.basicConfig(filename="exemplo.log", level=logging.DEBUG)

# logger = logging.getLogger(__name__)

# logging.debug("Para ajudar com debugging")
# logging.info("Apenas informação")     # Nota: a saída é em ASCII, de modo que acentos como ã ou ç exibirão caractere desconhecido no arquivo.
# logging.warning("Aviso")
# logging.error("Algo inesperado")
# logging.critical("Algo sério")

# Como pode ser visto com isto, o formatador padrão está configurado
# para um FileHandler. Ele acrescenta o nível da mensagem de log antes
# da mensagem em si.
# ------------------------------------------
# Definindo o Handler programaticamente
# Também pode-se criar programaticamente um handler e configurá-lo para
# o logger. Isto é feito instanciando uma das classes handler existentes(ou
# criando uma subclasse de um handler existente como o root Handler ou FilheHandler etc).
# O handler instanciado pode, então, ser adicionado como um handler ao logger.

# import logging

# logging.basicConfig()
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# file_handler = logging.FileHandler("detalhado.log")

# logger.addHandler(file_handler)


# def faz_algo():
#     logger.debug("mensagem debug")
#     logger.info("mensagem informativa")
#     logger.warning("mensagem de aviso")
#     logger.error("mensagem de erro")
#     logger.critical("mensagem crítica")


# logger.info("Iniciando")
# faz_algo()
# logger.info("Terminado")


# Dado que isto é bem mais código que usar a função basicConfig(), poderia
# se perguntar 'por que usar isso?'. A resposta é:
#   * Você pode ter diferentes handlers para diferentes loggers em vez de definir
#       o handler a ser usado centralmente
#   * Cada handler pode ter seu formato próprio de modo que registrar em um arquivo
#       tem um formato diferente de registrar para o console.
# Podemos definir o formato do handler instanciando a classe logging.Formatter
# com uma string de formatação apropriada. O objeto formatados pode, então,
# ser aplicado a um handler usando o método setFormatter() no objeto handler.
# Por exemplo, podemos modificar o código acima para incluir um formatador que
# será, então, definido no handler do arquivo como mostrado abaixo:
# file_handler = logging.FileHandler('detalhado.log')
# formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(message)s')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)
# -----------------------------------------------
# Múltiplos handlers
# Como comentado na seção anterior, podemos criar múltiplos handlers para enviar
# mensagens de log para locais diferentes; por exemplo, do console para aquivos
# ou mesmo servidores de e-mail. O seguinte programa ilustra a preparação de
# ambos handlers para arquivo e console para um logger de nível módulo.
# Para fazer isso, criamos dois handlers, o file_handler e o console_handler.
# Como efeito colateral, podemos também dar-lhes níveis de log e formatadores
# diferentes. Neste caso, file_handler herda o nível de log do próprio logger
# (que é DEBUG) enquanto o console handler tem seu nível de log definido como
# WARNING. Também preparamos diferentes formatadores em cada handler; neste caso,
# o formatador do logger para handler de arquivo dá mais informações que o
# formatador para o console.


# import logging

# logging.basicConfig(handlers=[logging.NullHandler()])
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# file_handler = logging.FileHandler("detalhado.log")
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.WARNING)

# fh_formatter = logging.Formatter(
#     "%(asctime)s [%(levelname)s] %(name)s.%(funcName)s: %(message)s",
#     datefmt="%d-%m-%Y %I:%M:%S %p",
# )
# file_handler.setFormatter(fh_formatter)

# console_formatter = logging.Formatter(
#     "%(asctime)s - %(funcName)s - %(message)s", datefmt="%d-%m-%Y %I:%M:%S %p"
# )
# console_handler.setFormatter(console_formatter)

# logger.addHandler(console_handler)
# logger.addHandler(file_handler)


# def faz_alguma_coisa():
#     logger.debug("mensagem debug")
#     logger.info("mensagem info")
#     logger.warning("mensagem aviso")
#     logger.error("mensagem erro")
#     logger.critical("mensagem critica")


# logger.info("Iniciando")
# faz_alguma_coisa()
# logger.info("Terminado")

# A saída dessa seção de código para o console é:
# 22-12-2025 05:32:23 PM - faz_alguma_coisa - mensagem aviso
# 22-12-2025 05:32:23 PM - faz_alguma_coisa - mensagem erro
# 22-12-2025 05:32:23 PM - faz_alguma_coisa - mensagem critica
# E para o arquivo é:
# 22-12-2025 05:32:23 PM [INFO] __main__.<module>: Iniciando
# 22-12-2025 05:32:23 PM [DEBUG] __main__.faz_alguma_coisa: mensagem debug
# 22-12-2025 05:32:23 PM [INFO] __main__.faz_alguma_coisa: mensagem info
# 22-12-2025 05:32:23 PM [WARNING] __main__.faz_alguma_coisa: mensagem aviso
# 22-12-2025 05:32:23 PM [ERROR] __main__.faz_alguma_coisa: mensagem erro
# 22-12-2025 05:32:23 PM [CRITICAL] __main__.faz_alguma_coisa: mensagem critica
# 22-12-2025 05:32:23 PM [INFO] __main__.<module>: Terminado
# -----------------------------------------------------------
# Filtros
# Filtros podem ser usados por Handlers para fornecer um controle refinado
# da saída do log. Um filtro pode ser adicionado a um logger usando o método
# logger.addFilter(). Um Filter pode ser criado extendendo a classe logging.Filter
# e implementando o método filter(). Este método pega uma gravação de log. Esta
# gravação pode ser validada para determinar se ela deveria ser exibida ou não.
# Se sim, retorna True, mas se deve ser ignorada, retora False.
# No seguinte exemplo, um filtro chamado MyFilter é definido que filtrará
# todas as mensagens de log contendo a string 'John'. É adicionado como um
# filtro ao logger e então as duas mensagens de log são geradas.
# import logging


# class MyFilter(logging.Filter):
#     def filter(self, record):
#         if "John" in record.msg:
#             return False
#         else:
#             return True


# logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG)
# logger = logging.getLogger()
# logger.addFilter(MyFilter())
# logger.debug("Este serve para ajudar com debugging")
# logger.info("Aqui tem informação sobre John")

# Apenas o log de debug é exibido, pois o info contém a string 'John'.
# ------------------------------------------
# Configuração de Log
# Todos os exemplos até aqui usaram a configuração programatica do framework
# de logging. Isto é razoável, como visto, mas requer alteração de código se
# quiser alterar o nível de logging para um logger particular, ou alterar onde
# um handler em particular envia as mensagens de log.
# Para a maioria dos sistemas de produção, uma solução melhor é usar um arquivo
# de configuração externo que é carregado quando a aplicação é executada e usado
# para configurar dinamicamente o framework de logging. Isto permite que administradores
# de sistema e outros alterem o nível de log, o destino das mensagens, o formato etc.
# sem precisar alterar o código.
# O arquivo de configuração de logging pode ser escrito usando diversos formatos
# padrão desde JSON(Java Script Object Notation) até YAML(Yet Another Markup
# Language), ou como um conjunto de pares chave-valor de um arquivo .config.
# Neste livro, é explorado brevemente o formato YAML:

############
# version: 1
# formatters:
# myformatter:
# format: '%(asctime)s [%(levelname)s] %(name)s.%(funcName)s:
# %(message)s'
# handlers:
# console:
# class: logging.StreamHandler
# level: DEBUG
# formatter: myformatter
# stream: ext://sys.stdout
# loggers:
# myLogger:
# level: DEBUG
# handlers: [console]
# propagate: no
# root:
# level: ERROR
# handlers: [console]
# ################

# Este código YAML acima é armazenado em um arquivo chamado logging.config.yaml,
# entretanto pode chamar o arquivo de qualquer coisa significativa.
# O arquivo YAML sempre inicia com um número de versão. Ele é um valor inteiro
# representando a versão do schema YAML. Todas as outras chaves no arquivo são
# opcionais, e incluem:
#   * formatters - lista um ou mais formatadores; cada um tem um nome que age como
#       uma chave e um valor formato que é a string definindo o formato da mensagem de log.
#   * filters - é uma lista de nomes de filtros e um conjunto de suas definições.
#   * handlers - é uma lista de handlers nomeados. Cada definição de handler
#       é feita de um conjunto de pares chave-valor onde as chaves definem
#       a classe usada para o filtro(obrigatório), o nível de log do filtro (opcional)
#       o formatador para usar com o handler (opcional) e uma lista de filtros (opcional)
#   * loggers - um ou mais loggers nomeados. Cada logger pode indicar o nível de log
#       (opcional) e uma lista de handlers (opcional). A opção propagate pode
#       ser usada para parar a propagação de mensagens para um logger pai (definindo-a como False).
#   * root - configuração do logger root.
# Este arquivo pode ser carregado em uma aplicação Python usando o módulo
# PyYAML. Ele fornece um parser YAML que pode carregar arquivos desse tipo
# com uma estrutura de dicionário que pode ser passada à função logging.config.dictConfig().
# Como é um arquivo, deve ser aberto e fechado para garantir que o recurso seja
# resolvido apropriadamente; portanto é desejável que seja gerenciado pela
# declaração with-as:
# with open('logging.config.yaml', 'r') as f:
#   config = yaml.safe_load(f.read())
#   logging.config.dictConfig(config)
# Isto abrirá o arquivo YAML no modo somente-leitura e o fechará após as
# duas declarações terem sido executadas.

#######################################
# import logging
# import logging.config
# import yaml

# with open("logging.config.yaml", "r") as f:
#     config = yaml.safe_load(f.read())
#     logging.config.dictConfig(config)

# logger = logging.getLogger("meuLogger")


# def faz_algo():
#     logger.debug("mensagem debug")
#     logger.info("mensagem info")
#     logger.warning("mensagem aviso")
#     logger.error("mensagem erro")
#     logger.critical("mensagem critica")


# logger.info("Iniciando")
# faz_algo()
# logger.info("Terminado")
#######################################

# Considerações de performance
# O desempenho durante logging sempre deve ser considerado. Em geral, deve-se evitar
# realizar qualquer trabalho desnecessário quando o logging está desabilitado
# (ou desabilitado para o nível em uso). Isto pode parecer óbvio, mas pode
# ocorrer de várias maneiras inesperadas.
# Um exemplo é na concatenação de strings. Se uma mensagem a ser registrada
# envolve a concatenação, então ela sempre será realizada quando um método de
# log está envolvido. Por exemplo:
# logger.debug('Count: ' + count + ', total: ' + total)
# Isto sempre resultará na string sendo gerada para count e total antes da
# chamada ser feita para a função debug; mesmo se o nível de debug não está
# ativado. Entretanto, usar uma string de formatação evita isso. A formatação
# envolvida será realizada somente se a string for usada em uma mensagem de log.
# Você deveria, portanto, sempre usar formatação de string para preencher
# mensagens de log. Por exemplo:
# logger.debug('Count: %d, total: %d ', count, 42)
# Outra otimização potencial é usar logger.isEnabledFor(level) como uma guarda
# contra a execução da declaração de log. Isto pode ser útil quando uma operação
# associada precisa ser realizada para suportar a operação de logging mas a operação
# é computacionalmente cara.
# if logger.isEnabledFor(logging.DEBUG):
#   logger.debug('Message with %s, %s', expensive_func1(), expensive_func2())

# Capítulo 24 - Python DB-API

# O padrão para acessar uma base de dados em Python é Python DB-API. Ele
# especifica um conjunto de interfaces padrão para módulos que permitem
# que Python acesse uma base de dados específica. O padrão é descrito no
# PEP 249 (PEP = Python Enhancement Proposal).
# Quase todos os módulos de acesso a base de dados em Python aderem a esse
# padrão. Isto significa que se você trocar de uma base de dados para outra,
# ou tentar transferir um programa Python de uma base de dados para outra,
# então os APIs que encontrar deveriam ser muito similares (apesar de SQL processado
# por diferentes bases de dados poderem diferir). Existem módulos disponíveis
# para a maioria das bases de dados comuns como MySQL, Oracle, Microsoft SQL
# Server etc.
# -------------------------------------------------
# A DB-API
# Existem vários elementos-chave na DB_API, sendo eles:
#   * A função connect(): É usada para conectar com uma base de dados e retorna
#       um objeto Connection.
#   * Objetos Connection: Dentro do DB-API, o acesso a uma base de dados
#       é atingido por objetos Connection. Eles dão acesso a objetos cursores.
#   * Objetos cursores: São usados para executar declarações SQL na base de dados.
#   * O resultado de uma execução: São os resultados que podem ser buscados
#       como uma sequência de sequências (como uma tupla de tuplas). O padrão
#       pode, assim, ser usado para selecionar, inserir ou atualizar na base de dados.
# Estes elementos são ilustrados na figura db-elements.png.
# O padrão especifica um conjunto de funções e objetos a serem usados para
# conectar com uma base de dados. Eles incluem a função connection, o objeto
# Connection e o objeto Cursor. Os elementos acima são descritos com mais
# detalhes na sequência.
# -------------------------------------------------
# A Função connect
# É definida como:
# connect(parameters...)
# É usada para fazer a conexão inicial à base de dados. A conexão retorna
# um Objeto Connection. Os parâmetros requeridos pela função são dependentes
# da base de dados.
# ------------------------------------------
# Objeto Connection
# É retornado pela função connect(). Fornece diversos métodos, incluindo:
#   * close(): para fechar a conexão quando não for mais necessária.
#   * commit(): usada para enviar (commit) uma transação pendente
#   * rollback(): usada para desfazer todas as mudanças feitas à base de
#       dados desde o envio da última transação (opcional pois nem todas
#       as bases de dados tem suporte a transações).
#   * cursor(): retorna um novo objeto Cursor para usar com a conexão.
# ---------------------------------------------
# Objeto Cursor
# É retornado do método connection.cursor(). Representa um cursor na base
# de dados, que é usado para gerenciar o contexto de uma operação de busca ou
# a execução de um comando de base de dados. Cursores suportam uma variedade
# de atributos e métodos:
#   * cursor.execute(operation, parameters): prepara e executa uma operação de
#       base de dados (como uma declaração de consulta ou comando de atualização.)
#       Parametros podem ser dados como uma sequência ou mapeamento e serão
#       presos às variáveis na operação. Variáveis são especificadas em uma
#       notação específica da base de dados.
#   * cursor.rowcount: atributo somente leitura que dá o número de linhas
#       que a última chamada cursor.execute() retornou (para declarações do
#       estilo SELECT) ou afetou (para atualização ou inserção)
#   * cursor.description: atributo somente leitura fornecendo informação
#       sobre as colunas presentes em quaisquer resultados retornados
#       de uma operação SELECT.
#   * cursor.close() fecha o cursor. Depois deste ponto, o cursor não é mais utilizável.
# Além disso, o objeto Cursor também fornece vários métodos do tipo busca.
# Eles são usados para retornar os resultados de uma consulta de base de dados.
# Os dados retornados são compostos por uma sequência de sequências onde cada
# sequência interna representa uma única linha retornada pela declaração
# SELECT. Os métodos de busca(fetch) definidos pelo padrão são:
#   * cursor.fetchone(): Pega a próxima linha do conjunto de resultados da consulta,
#       retornando uma única sequência, ou None quando não há mais dados disponíveis.
#   * cursor.fetchall(): Pega todas as linhas (restantes) do resultado de uma
#       consulta, retornando-as como uma sequência de sequências.
#   * cursor.fetchman(size): Busca o próximo conjunto de linhas do resultado
#       de uma consulta, retornando uma sequência de sequências. Uma sequência
#       vazia é retornada quando não há mais linhas disponíveis. O número de
#       linhas buscadas por chamada é especificado pelo parâmetro.
# -----------------------------------------------
# Mapeamentos de Tipos da Base de Dados para Tipos do Python
# O padrão DB-API também especifica um conjunto de mapeamentos dos tipos
# usados em uma base de dados para os tipos usados em Python, com os principais
# incluindo:
# Date(year, month, day)        - Representa uma data na base de dados
# Time(hour, minute, second)    - Representa um valor de tempo na base de dados
# Timestamp(year,month,day,hour,- Armazena um valor de data/hora
#           minute, second)
# String                        - Usado para representar dados tipo string (como VARCHARs) em bases de dados
#
# -----------------------------------------------
# Gerando erros
# O padrão também especifica um conjunto de exceções que podem ser lançadas
# em diferentes situações. Elas são apresentadas na figura excecoes.png.
# O diagrama ilustra a hierarquia de herança para os erros e avisos associados
# com o padrão.Note que o DB-API Warning e Error ambos estendem a classe
# Exception do Python padrão; entretanto, dependendo da implementação específica,
# podem haver uma ou mais classes adicionais na hierarquia entre essas classes.
# Por exemplo, no módulo PyMySQL existe uma classe MySQLError que estende
# Exception e é, então, estendida por ambos Warning e Error. Note também que
# Warning e Error não tem relação entre si. Isto ocorre pois Warnings não são
# considerados Errors e, portanto, tem hierarquias separadas.
# Uma descrição de cada classe Warning e Error são dadas abaixo:
#   * Warning: Usada para avisar de problemas como truncamentos de daos durando inserção etc

#   * Error: Classe base para todas as outras exceções de erro.

#   * InterfaceError: Exceção levantada para erros relacionados à interface
#                       da base de dados em vez da BD em si.

#   * DatabaseError: erros relacionados à base de dados.

#   * DataError: erros por problema com os dados como divisão por zero, números fora da faixa permitida etc.

#   * OperationalError: Erros relacionados à operação da BD, como deconexão inesperada.

#   * IntegrityError: Quando a integridade relacional da BD é afetada.

#   * InternalError: Quando a BD encontra um erro interno, como o cursor não ser mais válido ou a transação fora de sincronia etc.

#   * ProgrammingError: Erros de programação, como tabela não encontrada, erro de sintaxe
#                       na declaração do SQL etc.

#   * NotSupportedError: Quando um método ou API da BD foi usada mas não é
#                       suportada pela BD, como pedir um rollback() em uma
#                       conexão que não suporta transações.

# --------------------------------------------------------------
# Descrições de linhas
# O objeto Cursor tem um atributo description que fornece uma sequência de
# sequências; cada subsequência dá uma descrição de um dos atributos dos
# dados retornados pela declaração SELECT. A sequência descrevendo o atributo
# é feita de até 7 items, que incluem:
#   * name
#   * type_code - indica que tipo Python o atributo foi mapeado
#   * display_size - tamanho usado para exibir o atributo
#   * internal_size - tamanho usado internamente para representar o valor
#   * precision - se um valor numérico real, a precisão suportada pelo atributo
#   * scale - indica a escala do atributo
#   * null_ok - indica se o atributo pode ter valores nulos
# Os dois primeiros(name e type_code) são obrigatórios, os outros opcionais
# e definidos como None se não tem valores significativos dados.
# ------------------------------------------------------
# Transações em PyMySQL
# No PyMySQL, as transações são gerenciadas pelo objeto Connection. Ele
# possui os seguintes métodos:
#   * connection.commit().
#   * connection.rollback().
# O padrão não especifica como uma interface de base de dados deveria gerenciar
# ligar ou desligar transações. Entretanto, MySQL permite transações e pode
# trabalhar em doir modos; um suporta o uso de transações como já descrito;
# o outro usa um modo de envio(commit) automático. No modo automático, cada
# comando enviado à base de dados é tratado como uma transação independente
# e quaisquer alterações são enviadas automaticamente no final da declaração.
# Ele pode ser ligado em PyMySQL usando:
#   * connection.autocommit(True) para ligar, (False) para desligar e é o padrão.
# Outros métodos associados inclulem:
#   * connection.get_autocommit() que retorna um booleano indicando se o autocommit está ligado ou não
#   * connection.begin() para explicitamente iniciar uma nova transação.

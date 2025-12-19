# Capítulo 25 - Módulo PyMySQL
# Este módulo fornece acesso a uma base de dados MySQL através de Python.
# Ele implementa o Python DB-API v2.0. Este módulo é uma interface de
# base de dados puramente em Python, sendo portável através de diferentes sistemas
# operacionais; isto é notável pois alguns módulos de interface de base de
# dados são simples encapsuladores de outras implementações (nativas) que
# podem ou não estar disponíveis em diferentes sistemas operacionais. Por
# exemplo, um módulo de interface de base de dados nativo de Linux pode não
# estar disponível para Windows.
# Para usar o módulo PyMySQL é necessário instalá-lo no computador:
# pip install PyMySQL
# ----------------------------------------------
# Trabalhando  com o módulo PyMySQL
# Para usar PyMySQL para acessar uma base de dados é necessário seguir os
# seguintes passos:
#   1. Importar o módulo.
#   2. Fazer uma conexão com a máquina host executando a base de dados e com
#       a base de dados a ser usada.
#   3. Obter um objeto cursor do objeto Connection.
#   4. Executar algum SQL usando cursor.execute().
#   5. Pegar os resultados do SQL usando o objeto cursor.
#   6. Fechar a conexão com a base de dados.
# Estes passos são os fundamentais, que sempre serão usados ao acessar uma
# base de dados por PyMySQL. Vamos avaliar cada um deles em sequência.
# ---------------------------------------------
# Importar o módulo
# Deve-se atentar à caixa das letras, para importar o módulo usa-se pymysql
# com todas as letras minúsculas:
# import pymysql
# ----------------------------------------------
# Conectar com a base de dados
# Cada módulo de base de dados terá suas especificidades para conectar com
# o servidor da base de dados; eles geralmente envolverão especificar a máquina
# em que a base de dados está executando, o usuário a ser utilizado para a conexão
# e qualquer informação de segurança necessária como senha e a instância da
# base de dados com a qual será feita a conexão. Na maioria dos casos, uma
# base de dados é gerenciada por um sistema de gerenciamento de base de dados
# (DBMS) que pode cuidar de múltiplas instâncias de base de dados e, portanto,
# é necessário especificar qual instância deve ser acessada.
# Para MySQL, o sevidor da base de dados MySQL é um DBMS que pode cuidar de
# múltiplas instâncias. A função pymysql.connect, portanto, precisa das
# seguintes informações ao conectar com uma base de dados:
#   * O nome da máquia onde o servidor da base de dados está, dbserver.mydomain.com.
#       Se você que conectar com a mesma máquina em que o programa Python está
#       executando, então pode usar localhost. Este é um nome especial
#       reservado para a máquina local e evita a necessidade de se preocupar
#       com o nome do computador local.
#   * O nome de usuario para a conexão. A maioria das bases de dados limitam
#       o acesso a usuários nomeados. Eles não são estritamento usuários
#       humanos que entram em um sistema mas entidades que tem permissão de
#       conectar com a base de dados e realizar certas operações. Por exemplo,
#       um usuário pode apenas ser capaz de ler dados da base enquanto outro
#       pode inserir novos dados.
#   * A senha do usuário
#   * A instância da base de dados a ser conectada. Como mencionado acima,
#       um DBMS pode gerenciar múltiplas instâncias da base de dados.
# Por exemplo:
# # Abrir conexão com a base de dados
# connection = pymysql.connect('localhost', 'username', 'password', 'uni-database')

# Neste caso, a máquina com que estamos conectando é 'localhost', o usuário é
# 'username', a senha 'password' e a instância da base de dados é 'uni-database';
# ----------------------------------
# Obtendo o objeto cursor
# cursor - connection.cursor()
# ----------------------------------
# Usando o objeto cursor
# O seguinte exemplo usa uma declaração SELECT simples para pegar todos os
# atributos da tabela students para todas as linhas atualmente armazenadas:
# cursor.execute('SELECT * FROM students')
# Note que este método executa a declaração SELECT mas não retorna o conjunto
# de resultados diretamente. Em vez disso, retorna um inteiro indicando o
# número de linhas ou afetadas pela modificação ou retornadas como parte da
# consulta. No caso de uma declaração SELECT, o número retornado pode ser usado
# para determinar que tipo de método de busca usar.
# ---------------------------------
# Obtendo informação sobre os resultados
# O objeto Cursor também pode ser usado para obter informações sobre os resultados
# a serem buscados como quantas linhas tem e qual é o tipo de cada atributo nos
# resultados:
#   * cursor.rowcount() é uma propriedade somente leitura que indica o número
#       de linhas retornados pela declaração SELECT ou afetadas por uma declaração
#       UPDATE ou INSERT.
#   * cursor.description() é uma propriedade somente leitura que fornece uma
#       descrição de cada atributo no conjunto de resultados. Cada descrição
#       fornece o nome do atributo e uma indicação do tipo (via type_code)
#       assim como informações sobre se o valor pode ser nulo ou não e para
#       números, a escala, precisão e tamanho.
# Um exemplo de utilização dessas duas propriedades é:
# print('cursor.rowcount', cursor.rowcount)
# print('cursor.description', cursor.description)

# Um exemplo de possível saída desses comando poderia ser:
# cursor.rowcount 6
# cursor.description (('id', 3, None, 11, 11, 0, False),
# ('name', 253, None, 180, 180, 0, False), ('surname', 253,
# None, 180, 180, 0, False), ('subject', 253, None, 180, 180,
# 0, False), ('email', 253, None, 180, 180, 0, False))

# -----------------------------------------------
# Buscando resultados
# Agora que a declaração SELECT foi executada com sucesso, podemos buscar
# os resultados. Os resultados são retornados como uma tuplas de tuplas.
# Como mencionado no capítulo anterior, existem vários opções de busca
# incluiundo fetchone(), fetchmany(size) e fetchall(). No seguinte exemplo, usamos
# fetchall() pois sabemos que existem no máximo 6 linhas que podem ser retornadas.
# dados = cursor.fetchall()
# for linha in dados:
#   print('linha:', linha)
# Neste caso, fazemos um loop por cada tupla dentro da coleção de dados e
# exibimos aquela linha. Entretanto, poderíamos ter extraído a informação
# na tupla em elementos individuais. Esses elementos poderiam, então, ser
# usados para construir um objeto que poderis ser processado para uma aplicação, por exemplo:
# for linha in dados:
#   id, nome, sobrenome, materia, email = linha
#   estudante = Estudante(id, nome, sobrenome, materia, email)
#   print(estudante)
# ----------------------------------------
# Fechar a conexão
# Após terminar de usar a base de dados, ela deveria ser fechada
# connection.close()
# --------------------------------------


# Exemplo de consulta PyMySQL completo

#################################################
# import pymysql


# class Estudante:
#     def __init__(self, id, nome, sobrenome, materia, email):
#         self.id = id
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.materia = materia
#         self.email = email

#     def __str__(self):
#         return (
#             "Estudante["
#             + str(self.id)
#             + "] "
#             + self.nome
#             + " "
#             + self.sobrenome
#             + " - "
#             + self.materia
#             + " "
#             + self.email
#         )


# connection = pymysql.connect(
#     host="localhost", user="gui", password="gui", database="exemplos"
# )
# cursor = connection.cursor()

# cursor.execute("SELECT * FROM estudantes")
# print("cursor.rowcount: ", cursor.rowcount)
# print("cursor.description:", cursor.description)

# dados = cursor.fetchall()
# for linha in dados:
#     id_estudante, nome, sobrenome, materia, email = linha
#     estudante = Estudante(id_estudante, nome, sobrenome, materia, email)
#     print(estudante)
# connection.close()

#################################################

# Inserindo dados à base de dados
# Além de ler dados, também pode ser necessário acrescentar novos dados à
# base de dados. Isto é feito pelo DML(Data Manipulation Language) INSERT.
# O processo é bem similar a executar uma consulta à base de dados usando
# a declaração SELECT; isto é, você precisa fazer uma conexão, obter um
# objeto cursor e executar a declaração. A diferença é que não precisa buscar
# os resultados.

# import pymysql

# connection = pymysql.connect(
#     host="localhost", user="gui", password="gui", database="exemplos"
# )

# cursor = connection.cursor()

# try:
#     cursor.execute(
#         "INSERT INTO estudantes (id, nome, sobrenome, materia, email) VALUES (33, 'James', 'Andrews', 'Jogos', 'ja@my.com'), (36, 'Denise', 'Byrne', 'Historia', 'db@my.com')"
#     )
#     connection.commit()
# except:
#     connection.rollback()

# connection.close()

# Existem alguns pontos para se observar sobre este exemplo. O primeiro é
# que usamos aspas duplas em torno da string definindo o comando INSERT -
# isto pois a aspas duplas permite incluir aspas simples dentro da string.
# Isto é necessário pois precisamos colocar valores de string dentro de aspas
# que serão passados à base de dados.
# A segunda coisa é que, por padrão, a interface de base de dados de PyMySQL
# requer que o programador decida quando enviar ou cancelar uma transação.
# Uma transação foi introduzida no capítulo anterior como uma unidade atômica de
# trabalho que deve ou ser completada completamente ou cancelada de modo que
# nenhuma mudança seja feita. No entanto, a forma como indicamos que uma transação
# foi completa é chamando o método commit() na conexão com a base de dados. Por
# sua vez, podemos indicar que queremos cancelar a transação atual chamando
# rollback(). Em qualquer caso, após o método ter sido invocadoo, uma nova transação
# é iniciada para outras atividades na base de dados.

# ----------------------------------------
# Atualizando dados na base de dados
# Para isso, é usada a declaração UPDATE que precisa indicar qual linha existente
# está sendo atualizada assim como quais os novos dados.


# import pymysql

# connection = pymysql.connect(
#     host="localhost", user="gui", password="gui", database="exemplos"
# )
# cursor = connection.cursor()
# try:
#     cursor.execute("UPDATE estudantes SET email='denise@my.com' WHERE id = 36")
#     connection.commit()
# except:
#     connection.rollback()

# connection.close()

# -------------------------------------------

# Excluindo dados na base de dados
# Por fim, também é possível deletar dados, por exemplo, se um estudante
# desiste do curso. Também segue o mesmo formato dos exemplos anteriores:

# import pymysql

# connection = pymysql.connect(
#     host="localhost", user="gui", password="gui", database="exemplos"
# )

# cursor = connection.cursor()

# try:
#     cursor.execute("DELETE FROM estudantes WHERE id=36")
#     connection.commit()
# except:
#     connection.rollback()

# connection.close()

# -----------------------------------------------

# Criando tabelas
# Além de adicionar dados em uma base de dados, também é possível criar novas
# tabelas a serem usadas com uma aplicação. Este processo segue exatamente
# o mesmo padrão dos mostrados para as transações anteriores. A diferença é
# que o comando é CREATE TABLE com uma descrição da tabela a ser criada:
# import pymysql

# connection = pymysql.connect(
#     host="localhost", user="gui", password="gui", database="exemplos"
# )

# cursor = connection.cursor()

# try:
#     cursor.execute("CREATE TABLE log (message VARCHAR(100) NOT NULL)")
#     connection.commit()
# except:
#     connection.rollback()

# connection.close()

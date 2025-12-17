# Capítulo 23 - Introdução a base de dados(BD)
# Existem vários tipos diferentes de base de dados em uso comum hoje,
# incluindo Object, NoSQL e Relacionais. Este capítulo foca em Base de Dados
# Relacionais  tipificada por sistemas de base de dados como Oracle, Microsoft
# SQL Server e MySQL (que será a usada na sequência).
# --------------------------------------
# Uma base de dados é, essencialmente, um modo de armazenar e obter dados.
# Tipicamente, existe alguma forma de liguagem de consulta usada com a
# base de dados para ajudar a selecionar a informação a ser buscada como
# SQL(Structured Query Language). Na maioria dos casos, existe uma estrutura
# definida que é usada para armazenar os dados(apesar de não ser o caso para
# NoSQL ou bases de dados não estruturais não-relacionais como CouchDB ou Mongo DB).
# Em uma base de dados relacionais, os dados são armazenados em tabelas, onde
# as colunas definem os valores armazenados, como exemplificado na figura
# students.png. Neste diagrama, existe uma tabela chamada students; ela está sendo
# usada para armazenar informação sobre estudantes frequentanto uma reunião.
# A tabela tem 5 atributos (ou colunas), definidas para id, name, surname, subject e email.
# Neste caso, o id é, provavelmente, o que é conhecido como chave primária.
# A chave primária é uma propriedade usada para identificar unicamente uma linha
# (nesse caso, de estudantes); ela não pode ser omitida e deve ser única dentro
# da tabela. Obviamente, nomes e matérias podem aparecer duplicados pois
# há mais de um estudante em Animation e Games, e estudantes também podem
# ter o mesmo primeiro nome ou sobrenome. O e-mail pode ser único pois
# os estudantes provavelmente não compartilham endereços de e-mail, mas isso
# pode não ser necessariamente verdade.
# A razão de ser chamada de base de dados relacionais é devido ao tópico
# conhecido como álgebra relacional que sustena a teoria de BD Relacionais.
# Por sua vez, a Álgebra Relacional recebe esse nome devido ao conceito
# matemático conhecido como relação. Entretanto, para o propósito desse
# capítulo, não é necessário se preocupar sobre isso.
# -----------------------------------------------------
# Relações entre dados
# Quando os dados armazenados em uma tabela tem uma ligação ou relação
# com dados de outra tabela, um índice ou chave é usado para ligar os valores
# entre ambas tabelas. Em BD Relacionais, podem haver muitos tipos diferentes de
# relações como:
#   * 1:1 - onde apenas uma linha em uma tabela referencia uma linha em
#       outra tabela. Um exemplo de uma relação 1:1 poderia ser de uma pessoa
#       para um pedido de uma peça única de joalheria.
#   * 1:muitos - um valor em uma tabela pode referenciar múltiplos valores em outra
#   * muitos:muitros - quando muitas linhas em uma tabela podem referenciar muitas
#       linhas em outra.
# ---------------------------------------------------------
# Schema de base de dados
# A estrutura de uma Base de Dados Relacional é definida usando uma Linguagem
# de Definição/Descrição de Dados (DDL). Tipicamente, a sintaxe de uma linguagem
# como essa é limitada à semântica (significaod) necessária para definir a
# estrutura das tabelas. Esta estrutura é conhecida como schema da base de dados.
# Tipicamente, a DDL tem comandos como CREATE TABLE, DROP TABLE e ALTER TABLe.
# Muitas ferramentas fornecidas com uma base de dados permitem-lhe definir a
# estrutura da base de dados sem preocupar-se com a sintaxe da DDL; entretanto,
# é útil conhecer e entender que a base de dados pode ser criada desta maneira.
# O MySQL Workbench é uma ferramenta que permite trabalhar com bases de dados
# MySQL para gerenciar e consultar dados armazenados em uma instância de base de
# dados particular.
# -------------------------------------------------------
# SQL e Bases de Dados
# Após criação da tabela, pode-se usar linguagens de consulta para identificar
# e retornar dados armazenados nas bases de dados usando critérios específicos.
# Por exemplo, para retornar todas as pessoas cujo sobrenome é 'Jones, poderia-se
# formular uma consulta SQL:
# SELECT * FROM students WHERE surname='Jones';
# Note que é necessário especificar a tabela e quais dados quer retornar ('*'
# indica que queremos todos os dados).
# ---------------------------------------------------------
# Linguagem de Manipulação de Dados
# Dados também podem ser inseridos em uma tabela ou dados existentes em uma
# tabela serem atualizados. Isto é feito através da Linguagem de Manipulação
# de Dados (DML). Por exemplo, para inserir dados em uma tabela, simplesmente
# precisamos escrever uma declaração SQL INSERT fornecendo os valores a serem
# adicionados e como eles se posicionam nas colunas da tabela:
# INSERT INTO 'students' ('id', 'name', 'surname', 'subject', 'email')
#       VALUES ('6', 'James', 'Andrews', 'Games', 'ja@my.com');
# Atualizar uma linha existente é um pouco mais complicado pois, primeiro,
# é necessário identificar a linha a ser atualizada e então o dado a ser
# modificado. Assim, uma declaração UPDATE inclui uma cláusula WHERE para
# garantir a modificação da linha correta:
# UPDATE 'students' SET 'email'='grj@my.com' WHERE 'id'='2';
# ------------------------------------------------------
# Transações em Bases de Dados
# Outro conceito importante dentro de uma base de dados é o de Transação. Uma
# Transação representa uma unidade de trabalho realizado dentro de um sistema
# de gerenciamento de bases de dados (ou sistema similar) em uma instância
# de base de dados, e é independente de qualquer outra transação.
# Transações em um ambiente de base de dados tem dois propósitos principais:
#   * Fornecer uma unidade de trabalho que permite recuperação de falhas e
#       mantém uma base de dados consistente mesmo em casos de falha de sistema,
#       quando a execução é interrompida (completamente ou parcialmente).
#       Isto pois ou todas as operações dentro de uma transação são realizadas
#       ou nenhuma é. Assim, se uma operação causa um erro, então todas as
#       alterações sendo feitas pela transação até aquele ponto são desfeitas.
#   * Fornecer isolamento entre programas acessando uma base de dados simultaneamente.
#       Isto significa que o trabalho sendo feito por um programa não interagirá
#       com o trabalho de outro programa.
# Uma transação de base de dados, por definição, deve ser atômica, consistente,
# isolada e durável:
#   * Atomica: Indica que uma transação representa uma unidade atômica de
#       trabalho; isto é, ou todas as operações na transação são realizadas
#       ou nenhuma é.
#   * Consistente: Após finalizada, a transação deve deixar dados em estado
#       consistente com qualquer restrições de dados existentes(como uma linha
#       em uma tabela não deve referenciar um linha não-existente em outra tabelha etc)
#   * Isolada: Relaciona-se às alterações sendo feitas por transações simultaneas;
#       estas mudanças devem ser isoladas uma da outra.
#   * Durável: Significa que após uma transação ser completa, as mudanças
#       são armazenadas permanentemente na base de dados.
# Utilizadores de base de dados referem-se a essas propriedades de transações
# de bases de dados pelo acrônimo ACID(da primeira letra de cada propriedade).
#

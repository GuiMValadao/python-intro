import pymysql

connection = pymysql.connect()

cursor = connection.cursor()

try:
    cursor.execute(
        "CREATE TABLE info_contas (id_info_contas INT NOT NULL, nome VARCHAR(255) NOT NULL, PRIMARY KEY (id_info_contas))"
    )
    cursor.execute(
        "CREATE TABLE transacoes (id_transacoes INT NOT NULL, tipo VARCHAR(45) NOT NULL, valor VARCHAR(45), conta INT NOT NULL, PRIMARY KEY (id_transacoes))"
    )
    connection.commit()
except:
    connection.rollback()

connection.close()

import pymysql


class Conta:
    def __init__(self, numero, nome, saldo_inicial, tipo):
        self.numero = numero
        self.nome = nome
        self._saldo = saldo_inicial
        self.tipo = tipo
        self.historico = [Transacao.depositar(saldo_inicial)]

    def depositar(self, valor):
        self._saldo += valor
        self.historico.append(Transacao.depositar(valor))

    def sacar(self, valor):
        self._saldo -= valor
        self.historico.append(Transacao.sacar(valor))

    def obter_saldo(self):
        return self._saldo


class Transacao:

    def depositar(valor):
        return "deposito", valor

    def sacar(valor):
        return "saque", valor


def preencher_tabelas_contas(conta):
    dados = (conta.numero, conta.nome)
    declaracao = "INSERT INTO info_contas (id_info_contas, nome) VALUES (?, ?)"
    try:
        cursor.execute(declaracao, dados)
        connection.commit()
    except pymysql.err.IntegrityError:
        print("Conta já registrada.")
        connection.rollback()


def obter_indice():
    cursor.execute("SELECT * FROM transacoes")
    cursor.fetchall()
    return cursor.rowcount


def preencher_tabelas_transacoes(conta):

    for item in conta.historico:
        indice = obter_indice()
        dados = (str(indice + 1), item[0], str(item[1]), str(conta.numero))
        declaracao = "INSERT INTO transacoes (id_transacoes, tipo, valor, conta) VALUES (?, ?, ?, ?)"
        try:
            cursor.execute(declaracao, dados)
            connection.commit()
        except pymysql.err.IntegrityError:
            print("ID transação já registrado")
            connection.rollback()


connection = pymysql.connect(
    host="localhost", user="gui", password="gui", database="exemplos"
)

cursor = connection.cursor()


conta = Conta(1, "Joao", 200, "corrente")
conta.sacar(20)
conta.depositar(50)
# preencher_tabelas_contas(conta)
# preencher_tabelas(conta)
conta2 = Conta(2, "Gui", 100, "corrente")
conta2.sacar(50)
conta2.depositar(505)
print(conta2.historico)
# preencher_tabelas_contas(conta2)
preencher_tabelas_transacoes(conta2)

connection.close()

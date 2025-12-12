import csv


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


def salvar_transacoes_csv(conta):

    with open("transacoes.csv", "a", newline="") as arquivocsv:
        escritor = csv.writer(arquivocsv)
        escritor.writerow(("tipo_transacao", "valor"))
        for transacao in conta.historico:
            escritor.writerow(transacao)


conta = Conta(1, "Joao", 200, "corrente")
conta.sacar(20)
conta.depositar(50)
print(conta.historico)
salvar_transacoes_csv(conta)

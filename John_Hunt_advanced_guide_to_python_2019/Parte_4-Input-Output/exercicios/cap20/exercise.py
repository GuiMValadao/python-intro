import csv
from openpyxl import Workbook
import logging


class Conta:
    logging.basicConfig(
        format="%(asctime)s [%(levelname)s] %(funcName)s: %(message)s",
        level=logging.DEBUG,
    )
    logger = logging.getLogger(__name__)

    def __init__(self, numero, nome, saldo_inicial, tipo):

        self.numero = numero
        self.nome = nome
        self._saldo = saldo_inicial
        self.tipo = tipo
        self.historico = [Transacao.depositar(saldo_inicial)]
        global logger_classe
        logger_classe.debug(f"Nova instância de conta criada. Identificador:{numero}")

    def depositar(self, valor):
        Conta.logger.debug(f"valor de depósito: R$ {float(valor):.2f}")
        self._saldo += valor
        self.historico.append(Transacao.depositar(valor))

    def sacar(self, valor):
        Conta.logger.debug(f"valor de saque: R$ {float(valor):.2f}")
        self._saldo -= valor
        self.historico.append(Transacao.sacar(valor))

    def obter_saldo(self):
        Conta.logger.debug("Consulta ao saldo")
        return self._saldo


class Transacao:
    def depositar(valor):
        return "deposito", valor

    def sacar(valor):
        return "saque", valor


def salvar_transacoes_csv(conta):
    """Exercício cap 20 - arquivos .csv"""
    with open("transacoes.csv", "a", newline="") as arquivocsv:
        escritor = csv.writer(arquivocsv)
        escritor.writerow(("tipo_transacao", "valor"))
        for transacao in conta.historico:
            escritor.writerow(transacao)


def salvar_transacoes_excel(nome_arquivo, conta):
    """Exercicio cap 21 - arquivos excel"""
    workbook = Workbook()
    ws = workbook.active
    ws.title = "transacoes"
    ws.sheet_properties.tabColor = "1072BA"
    ws.append(["tipo de transacao", "valor"])
    for transacao in conta.historico:
        ws.append(transacao)
    workbook.save(f"{nome_arquivo}.xlsx")


logger_classe = logging.getLogger("Conta")

conta = Conta(1, "Joao", 200, "corrente")
conta.sacar(20)
conta.depositar(50)
print(conta.historico)
# salvar_transacoes_csv(conta)
# salvar_transacoes_excel(transacoes, conta)
conta.obter_saldo()

conta2 = Conta(2, "Joao", 200, "corrente")

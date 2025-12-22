import accounts
import logging

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(funcName)s: %(message)s",
    level=logging.DEBUG,
)
logger = logging.getLogger(__name__)


try:
    conta = accounts.ContaCorrente(1, "Joao", 200, 100)
    logger.info(f"Nova instância de conta criada.")
except:
    logger.error("Problema encontrado ao tentar criar a conta")

try:
    conta.saque(20)
    logger.info(f"Saque realizado com sucesso.")
except accounts.ErroQuantidade:
    logger.error("Valor de saque escolhido é inválido.")
except accounts.ErroSaldo:
    logger.error("Saldo insuficiente para realização do saque.")
except:
    logger.error("Erro desconhecido na tentativa de saque.")

try:
    conta.depositar(50)
    logger.info(f"Depósito realizado com sucesso.")
except accounts.ErroQuantidade:
    logger.error("Valor de depósito escolhido é inválido.")
except:
    logger.error("Erro desconhecido na tentativa de depósito.")

try:
    print(conta.historico)
    logger.info(f"Consulta ao historico de transacoes")
except:
    logger.error(f"Falha na tentativa de consulta ao histórico")
try:
    print(f"Seu saldo é de: {conta.saldo}")
    logger.info(f"Consulta ao saldo")
except:
    logger.error(f"Falha na tentativa de consulta ao saldo")


conta2 = accounts.ContaCorrente(2, "Joao", 200, "corrente")

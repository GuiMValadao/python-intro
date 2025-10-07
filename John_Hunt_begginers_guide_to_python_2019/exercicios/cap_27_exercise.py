##########################################
# Exercício cap. 27 - adicionar protocolo
# gerenciador de contexto na classe Contas
# e testar
##########################################

import fintech.accounts as accounts
with accounts.ContaPoupanca('891', 'Adam', 5.0, 50.0) as acc:
    acc.depositar(23.0)
    acc.saque(12.33)
    print(acc.saldo)

print('acc1.branch:', acc1.branch)
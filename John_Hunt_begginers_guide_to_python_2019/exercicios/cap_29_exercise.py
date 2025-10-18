import fintech.accounts as accounts

acc1 = accounts.ContaCorrente(123, 'Joao', 500, 100)
print(acc1)

acc1.saldo
print(acc1.saque.__name__)
acc1.depositar(150)
acc1.depositar(20)
acc1.depositar(50)
acc1.depositar(33)
acc1.saque(23)
acc1.saque(53)
print(acc1)
#print(acc1.historico)
#acc2 = accounts.Transacao(['Deposito: 12', 'Deposito: 152', 'Saque: 42'])
for transacao in acc1:
    print(transacao)
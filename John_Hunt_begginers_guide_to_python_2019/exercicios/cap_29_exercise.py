import fintech.accounts as accounts

acc1 = accounts.ContaPoupanca(123, 'Joao', 500000000, 100)
print(acc1)
acc1.saque(121233)
acc1.saldo
print(acc1.saque.__name__)
print(acc1.depositar.__name__)
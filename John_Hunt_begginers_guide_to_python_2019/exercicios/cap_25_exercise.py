#-------------------------------
# 25.11 Exercise
#The aim of this exercise is to create a module for the classes you have been
#developing.
#You should move your Account, CurrentAccount, DepositAccount
#and BalanceError classes into a separate module (file) called accounts. Save
#this file into a new Python package called fintech.
#Separate out the test application from this module so that you can import the
#classes from the package
#-------------------------------
import fintech.accounts as accounts

acc1 = accounts.ContaCorrente('123', 'John', 10.05, 100.0)
acc2 = accounts.ContaPoupanca('345', 'John', 23.55, 0.5)
acc3 = accounts.ContaInvestimento('567', 'Phoebe', 12.45, 'alto risco')
print(acc1)
print(acc2)
print(acc3)
acc1.saque(10.04)
print(f'{acc1.obter_saldo:.2f}')
print(accounts.Conta.quant_contas())
print(f'Seu saldo atual é de R$ {acc1.obter_saldo:.2f}')
print(f'Seu saldo atual é de R$ {acc2.obter_saldo:.2f}')

try:
    print(f'saldo: {acc1.saldo:.2f}')
    acc1.saque(-300.00)
    print(f'saldo: {acc1.saldo:.2f}')
except accounts.ErroQuantidade as q:
    print('Resolvendo exceção q')
    print(q)
except accounts.ErroSaldo as s:
    print('Resolvendo exceção s')
    print(s)

try:
    acc2.saque(1000)
    print(f'saldo: {acc2.saldo:.2f}')
except accounts.ErroQuantidade as q:
    print('Resolvendo exceção q')
    print(q)
except accounts.ErroSaldo as s:
    print('Resolvendo exceção s')
    print(s)

with accounts.ContaCorrente('891', 'Adam', 5.0, 00.0) as acc:
    acc.depositar(13.0)
    acc.saque(12.33)
    print(acc.saldo)

print('acc1.branch:', acc1.branch)
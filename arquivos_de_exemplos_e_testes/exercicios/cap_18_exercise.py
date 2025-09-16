#########################################################################
# The aim of this exercise is to create a new class called Account.
#1. Define a new class to represent a type of bank account.
#2. When the class is instantiated you should provide the account number, the name
#of the account holder, an opening balance and the type of account (which can be
#a string representing 'current', 'deposit' or 'investment' etc.). This means that
#there must be an __init__ method and you will need to store the data within
#the object.
#3. Provide three instance methods for the Account; deposit(amount),
#withdraw(amount) and get_balance(). The behaviour of these
#methods should be as expected, deposit will increase the balance, withdraw will
#decrease the balance and get_balance() returns the current balance.
#4. Define a simple test application to verify the behaviour of your Account class.
#It can be helpful to see how your class Account is expected to be used. For this
#reason a simple test application for the Account is given below:
#The following output illustrates what the result of running this test application
#might look like:
#acc1 = Account('123', 'John', 10.05, 'current')
#acc2 = Account('345', 'John', 23.55, 'savings')
#acc3 = Account('567', 'Phoebe', 12.45, 'investment')
#print(acc1)
#print(acc2)
#print(acc3)
#acc1.deposit(23.45)
#acc1.withdraw(12.33)
#print('balance:', acc1.get_balance())
#Account[123] - John, current account = 10.05
#Account[345] - John, savings account = 23.55
#Account[567] - Phoebe, investment account = 12.45
#balance: 21.17
##########################################################################

class Conta():
    """ Esta classe cria objetos que contém informações
    a respeito de uma conta bancária contendo as seguintes informações:
    número da conta; nome do titular da conta; um saldo de abertura
    e o tipo da conta.
    """
    quantidade_contas = 0

    @classmethod
    def criar_conta(cls):
        cls.quantidade_contas += 1

    def __init__(self, numero, nome, saldo, tipo):
        informacoes = Conta.criar_conta()
        self.numero = numero        
        self.nome = nome
        self.saldo = saldo
        self.tipo = tipo
        Conta.boas_vindas()

    def __str__(self):
        saldo_string = str(self.saldo)
        numero_string = str(self.numero)
        return ('Conta[' + numero_string + '] - ' + self.nome + 
                ', conta ' + self.tipo + ' = R$ ' + saldo_string)
    
    def depositar(self, valor):
        self.saldo = float(self.saldo) + float(valor)
        return self.saldo

    def saque(self, valor):
        self.saldo = float(self.saldo) - float(valor)
        return self.saldo
    
    def obter_saldo(self):
        print('Seu saldo atual é de R$', self.saldo)
        return

    @staticmethod
    def boas_vindas():
        print('Bem vindo! Sua conta foi criada com sucesso!')

    @classmethod
    def quant_contas(self):
        print(f'O número de instâncias de \
contas criadas é de {self.quantidade_contas}')
        
print(Conta.__doc__)
c1 = Conta(123, 'Gui', 200, 'corrente')
print(c1.saldo)
print(c1)
c2 = Conta('456', 'João', 20.23, 'depósito')
c2.depositar(245.23)
print('Saldo:', c2.saldo)
c2.depositar(245.23)
print('Saldo:', c2.saldo)
c3 = Conta('789', 'Carlo', 2340.54, 'investimento')
print('Titular:', c1.nome)
print('Número da conta:', c1.numero)
print('Saldo:', c1.saldo)
print('Tipo de conta:', c1.tipo)
c1.depositar(245.23)
print('Saldo:', c1.saldo)
c1.saque(105.04)
print('Saldo:', c1.saldo)
c1.obter_saldo()
print(c1)
print(c2)
print(c3)
Conta.quant_contas()

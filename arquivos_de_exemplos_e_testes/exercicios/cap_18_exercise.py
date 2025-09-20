#########################################################################
# Cap 18 - criar classe 'Conta'
# Cap 20 - criar subclasses 'ContaDeposito', 'ContaCorrente' e 
# 'ContaInvestimento'
##########################################################################

class Conta():
    """ Esta classe cria objetos que contém informações
    a respeito de uma conta bancária contendo as seguintes informações:
    número da conta; nome do titular da conta; um saldo de abertura
    e o tipo da conta."""
    quantidade_contas = 0

    @classmethod
    def criar_conta(cls):
        cls.quantidade_contas += 1

    def __init__(self, numero, nome, saldo):
        informacoes = Conta.criar_conta()
        self.numero = numero        
        self.nome = nome
        self.saldo = saldo
        Conta.boas_vindas()

    def __str__(self):
        return (f'Conta[{self.numero}] - {self.nome}\
, saldo = R$  {self.saldo:.2f}')
    
    def depositar(self, valor):
        self.saldo = float(self.saldo) + float(valor)
        return self.saldo

    def saque(self, valor):
        maximo = self.saldo
        if valor < maximo:
            self.saldo = float(maximo) - float(valor)
            return self.saldo
        else:
            print('Valor de saque solicitado acima do saldo disponível.')
    
    def obter_saldo(self):
        return f'Seu saldo atual é de R$ {self.saldo}'

    @staticmethod
    def boas_vindas():
        print('Bem vindo! Sua conta foi criada com sucesso!')

    @classmethod
    def quant_contas(self):
        print(f'O número de instâncias de \
contas criadas é de {self.quantidade_contas}')
        
class ContaCorrente(Conta):
    """ Esta subclasse fornece o atributo limite de crédito e 
        expande o método saque para permitir sacar do valor de crédito."""
    def __init__(self, numero, nome, saldo, limite ):
        super().__init__(numero, nome, saldo)
        self.limite = limite
    
    def __str__(self):
        return super().__str__() + f', seu limite de crédito\
 é R$ {self.limite:.2f}'

    def saque(self, valor):
        maximo = self.saldo + self.limite
        if valor < maximo:
            self.saldo = float(self.saldo) - float(valor)
            if self.saldo < 0:
                self.limite = self.limite + self.saldo
                self.saldo = 0.00
            return self.saldo, self.limite
        else:
            print('Transação interrompida, valor ' \
            'de saque excederia o limite de crédito.')

class ContaPoupanca(Conta):
    """ Esta subclasse possibilita a aplicação de juros
        sobre o saldo em conta. """
    def __init__(self, numero, nome, saldo, juros):
        super().__init__(numero, nome, saldo)
        self.juros = juros
    
    def __str__(self):
        return super().__str__() + f', juros de {self.juros:.2f}%'

class ContaInvestimento(Conta):
    """ Esta subclasse adiciona um atributo 'tipo de investimento'."""
    def __init__(self, numero, nome, saldo, tipo_investimento):
        super().__init__(numero, nome, saldo)
        self.tipo_investimento = tipo_investimento
    
    def __str__(self):
        return super().__str__() + f', investimento é de \
{self.tipo_investimento}'

acc1 = Conta('123', 'João', 210.12)
print(acc1)
acc1.saque(211)
print(acc1)
print(acc1.obter_saldo())
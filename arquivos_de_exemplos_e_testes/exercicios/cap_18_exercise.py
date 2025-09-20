#########################################################################
# Cap 18 - criar classe 'Conta'
# Cap 20 - criar subclasses 'ContaDeposito', 'ContaCorrente' e 
# 'ContaInvestimento'
# Cap 23 - tornar obter_saldo leitura-apenas.
##########################################################################

class Conta(object):
    """ Esta classe cria objetos que contém informações
    a respeito de uma conta bancária contendo as seguintes informações:
    número da conta; nome do titular da conta; um saldo de abertura."""

    quantidade_contas = 0

    @classmethod
    def criar_conta(cls):
        """ Mantém contagem do número total de contas """
        cls.quantidade_contas += 1

    def __init__(self, numero, nome, saldo):
        """ Inicializa a classe """
        Conta.criar_conta()
        self._numero = numero        
        self._nome = nome
        self.saldo = saldo
        Conta.boas_vindas()

    def depositar(self, valor):
        """ Altera o saldo de acordo com o valor de depósito """
        self.saldo = float(self.saldo) + float(valor)
        return self.saldo

    def saque(self, valor):
        """ Altera o saldo de acordo com o valor de saque """
        maximo = self.saldo
        if (valor < maximo):
            self.saldo = float(maximo) - float(valor)
            return self.saldo
        else:
            print('Valor de saque solicitado acima do saldo disponível.')
            return self.saldo
        
    @property
    def obter_saldo(self):
        """ Exibe o saldo atual """
        return self.saldo

    @staticmethod
    def boas_vindas():
        """ Exibe mensagem de boas vindas ao criar uma nova conta """
        print('Bem vindo! Sua conta foi criada com sucesso!')

    @classmethod
    def quant_contas(cls):
        """ Exibe o número total de contas criadas """
        return (f'O número de instâncias de \
contas criadas é de {cls.quantidade_contas}')
    
    def __str__(self):
        """ Exibe as informações da instância de classe chamada """
        return (f'Conta[{self._numero}] - {self._nome}\
, saldo = R$  {self.saldo:.2f}')
        
class ContaCorrente(Conta):
    """ Esta subclasse fornece o atributo limite de crédito e 
        expande o método saque para permitir sacar do valor de crédito."""
    
    def __init__(self, numero, nome, saldo, limite ):
        """ Inicializa a classe, inicializando primeiro a superclasse
            e, então, adicionando o atributo 'limite' da subclasse """
        super().__init__(numero, nome, saldo)
        self._limite = limite
    
    def __str__(self):
        """ Expande a funcionalidade de chamar uma instância de
            classe da superclasse, adicionando o valor do limite de crédito """
        return super().__str__() + f', seu limite de crédito\
 é R$ {self._limite:.2f}'

    def saque(self, valor):
        """ Altera a funcionalidade do método saque da função parente,
            permitindo saques acima do saldo, mas limitando o saque 
            pela soma do saldo e limite """
        maximo = self.saldo + self._limite
        if valor < maximo:
            self.saldo = float(self.saldo) - float(valor)
            if self.saldo < 0:
                self._limite = self._limite + self.saldo
                self.saldo = 0.00
            return self.saldo, self._limite
        else:
            print('Transação interrompida, valor ' \
            'de saque excederia o limite de crédito.')

class ContaPoupanca(Conta):
    """ Esta subclasse possibilita a aplicação de juros
        sobre o saldo em conta. """
    
    def __init__(self, numero, nome, saldo, juros):
        """ Chama a inicialização da classe parente e adiciona o
            atributo juros """
        super().__init__(numero, nome, saldo)
        self._juros = juros
    
    def __str__(self):
        """ Expande sobre a função parente, adicionando a exibição
            do valor de juros ao chamado de exibição de uma instância da subclasse """
        return super().__str__() + f', juros de {self._juros:.2f}%'

class ContaInvestimento(Conta):
    """ Esta subclasse adiciona um atributo 'tipo de investimento'."""

    def __init__(self, numero, nome, saldo, tipo_investimento):
        """ Chama a inicialização da superclasse e adiciona o atributo
            tipo_investimento """
        super().__init__(numero, nome, saldo)
        self._tipo_investimento = tipo_investimento
    
    def __str__(self):
        """ Expande a funcionalidade da superclasse, exibindo o
            tipo de investimento """
        return super().__str__() + f', investimento é de \
{self._tipo_investimento}'

acc1 = ContaCorrente('123', 'John', 10.05, 100.0)
acc2 = ContaPoupanca('345', 'John', 23.55, 0.5)
acc3 = ContaInvestimento('567', 'Phoebe', 12.45, 'alto risco')
print(acc1)
print(acc2)
print(acc3)
acc1.saque(10.04)
print(f'{acc1.obter_saldo:.2f}')
print(Conta.quant_contas())
print(f'Seu saldo atual é de R$ {acc1.obter_saldo:.2f}')
acc1.saque(300.00)
print(f'Seu saldo atual é de R$ {acc1.obter_saldo:.2f}')
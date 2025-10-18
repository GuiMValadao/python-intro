""" 
Este módulo cria contas bancárias de três tipos diferentes:
corrente, poupança e investimento, todas sendo subclasse da
classe base abstrata Conta
"""

from abc import ABCMeta, abstractmethod
#from fintech.timer import cronometro

class Conta(metaclass=ABCMeta):
    """ Esta classe abstrata cria objetos que contém informações
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
        self._saldo = saldo
        self.indice = 0
        self.historico = []
        self.historico = []
        Conta.boas_vindas()
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def nome(self):
        return self._nome
    
    def __enter__(self):
        print('__enter__')
        return self
    
    def __exit__(self, *args):
        print('__exit__:', args)
        return True

#    @cronometro
    def depositar(self, valor):
        """ Altera o saldo de acordo com o valor de depósito """
        if valor > 0:
            self.historico.append(f'Deposito: {valor}')
            self._saldo = (float(self._saldo) + float(valor))
            return self.saldo
        else:
            raise ErroQuantidade(valor, self)

#    @cronometro
    def saque(self, valor):
        """ Altera o saldo de acordo com o valor de saque """
        maximo = self.saldo
        if valor < 0:
            raise ErroQuantidade(valor, self)
        elif (valor < maximo):
            self.historico.append(f'Saque: {valor}')
            self.saldo = float(maximo) - float(valor)
            return self.saldo
        else:
            raise ErroSaldo(self)
          
    @property
    def saldo(self):
        """ Exibe o saldo atual """
        return self._saldo
    @saldo.setter
    def saldo(self, novo_saldo):
        self._saldo = novo_saldo  
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.limite = len(self.historico)
        if self.indice >= self.limite:
            raise StopIteration
        else:
            valor_retornado = self.historico[self.indice]
            self.indice += 1
            return valor_retornado

    @staticmethod
    def boas_vindas():
        """ Exibe mensagem de boas vindas ao criar uma nova conta """
        print('Bem vindo! Sua conta foi criada com sucesso!')

    @classmethod
    def quant_contas(cls):
        """ Exibe o número total de contas criadas """
        return (f'O número de instâncias de \
contas criadas é de {cls.quantidade_contas}')

    @abstractmethod
    def __str__(self):
        """ Exibe as informações da instância de classe chamada """
        return (f'Conta[{self.numero}] - {self.nome}\
, saldo = R$  {self.saldo:.2f}')
    
    def __getattr__(self, attribute):
        print('__getattr__: atributo desconhecido acessado - ', attribute)
        return f'self.{attribute}: -1'  

class ContaCorrente(Conta):
    """ Esta subclasse fornece o atributo limite de crédito e 
        expande o método saque para permitir sacar do valor de crédito."""
    
    def __init__(self, numero, nome, saldo, limite ):
        """ Inicializa a classe, inicializando primeiro a superclasse
            e, então, adicionando o atributo 'limite' da subclasse """
        super().__init__(numero, nome, saldo)
        self._limite = limite
    
    @property
    def limite(self):
        return self._limite
    @limite.setter
    def limite(self, limite_restante):
        self._limite = limite_restante
    
    def __str__(self):
        """ Expande a funcionalidade de chamar uma instância de
            classe da superclasse, adicionando o valor do limite de crédito """
        return super().__str__() + f', seu limite de crédito\
 é R$ {self._limite:.2f}'

#    @cronometro
    def saque(self, valor):
        """ Altera a funcionalidade do método saque da função parente,
            permitindo saques acima do saldo, mas limitando o saque 
            pela soma do saldo e limite """
        maximo = self.saldo + self.limite
        if valor < 0:
            raise ErroQuantidade(valor, self)
        elif valor < maximo:
            self.historico.append(f'Saque: {valor}')
            self.saldo =(float(self.saldo) - float(valor))
            if self.saldo < 0:
                self.limite(self.limite + self.saldo)
                Conta.saldo(0.00)
            return self.saldo, self.limite
        else:
            raise ErroSaldo(self)

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
      
class ErroQuantidade(Exception):
    """ Gera erro caso o valor de saque/depósito
        seja negativo. """
    def __init__(self, valor, conta):
        self.valor = valor
        self.conta = conta
    
    def __str__(self):
        return 'ErroQuantidade (valor de transações não devem ser' \
        ' negativos) na ' + f'{self.conta}'

class ErroSaldo(Exception):
    """ Gera erro caso o valor de saque ultrapasse o limite de
        saldo + crédito """
    def __init__(self, conta):
        self.conta = conta
    
    def __str__(self):
        return 'ErroSaldo (valor de saque superior ao máximo' \
        ' crédito disponível) na ' + f'{self.conta}'
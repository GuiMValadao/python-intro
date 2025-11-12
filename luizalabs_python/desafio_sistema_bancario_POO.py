from abc import ABC, abstractmethod
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):

    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        if self._cpf == "":
            return "Usuário não cadastrado"
        else:
            return self._cpf

    @property
    def nome(self):
        if self._nome == "":
            return "O nome não pode ser vazio"
        else:
            return self._nome

    @property
    def data_nascimento(self):
        if self._data_nascimento == "":
            return "Data de nascimento não informada"
        else:
            return self._data_nascimento

    @cpf.setter
    def cpf(self, valor):
        cpf_invalid = True
        while valor is None:
            self._cpf = input("CPF não pode ser nulo, digite novamente:")

        while cpf_invalid:
            try:
                int(valor)
                PessoaFisica.contar_pessoas()
                cpf_invalid = False
            except ValueError:
                print("Digite apenas os numeros do seu cpf.")
                valor = input("Por favor, digite seu cpf: ")
        self._cpf = valor

    @nome.setter
    def nome(self, valor):
        self._nome = valor
        while self._nome == "":
            valor = input("Nome vazio. Digite novamente: ")
            self._nome = valor

    @data_nascimento.setter
    def data_nascimento(self, valor):
        self._data_nascimento = valor
        while self._data_nascimento == "":
            valor = input("Por favor, informe sua data de nascimento: ")
            self._data_nascimento = valor

    # def __iter__(self):
    #     return self

    # def __next__(self):
    #     if self.__contador == self.valor_maximo:
    #         raise StopIteration
    #     else:
    #         retornar = self.cpf
    #         self.__contador += 1
    #         return retornar

    # método __str__?

    # @classmethod
    # def contar_pessoas(cls):
    #     cls.contagem_usuarios += 1


class Historico:

    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y, %H:%M:%S"),
            }
        )

    def __str__(self):
        return f"""\
---------------------------
----------EXTRATO----------
---------------------------\n
    
    {self._transacoes}
    
    
    """


class Conta:
    def __init__(self, numero, cliente, agencia="0001"):
        self._saldo = 0
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > 0:
            self._saldo -= valor
            print("\n Saldo realizado com sucesso.")
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n Depósito realizado com sucesso.")

        else:
            print("Operação falhou! O valor informado é inválido.")
            return False
        return True


class ContaCorrente(Conta):

    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n Operação falhou, o valor informado excede o limite.")

        elif excedeu_saques:
            print("\n Operação falhou, o número de saques foi excedido.")
        else:
            return super().sacar(valor)
        return False

    def __str__(self):
        return f"""\
        
        Agência:\t{self.agencia}
        C/C:\t\t{self.numero}
        Titular:\t{self.cliente.nome}
        """


class Transacao(ABC):

    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def menu_inicial():
    """
    Exibe o menu para criação de conta para o usuário.
    Recebe a escolha em uma string e a retorna.
    """
    menu = """
--------------
-MENU INICIAL-
--------------
Bem vindo ao Banco! O que deseja fazer?

[c] Criar conta
[e] Entrar com conta existente
[q] Sair

=> """
    escolha = input(menu).lower()
    return escolha


def menu_escolha_transacao():
    """
    Exibe o menu de escolha de transação para o usuário.
    Recebe a escolha em uma string e a retorna.
    """
    menu = """
--------------------
-MENU DE TRANSAÇÕES-
--------------------
Qual operação deseja realizar?

[d] Depositar
[s] Sacar
[e] Extrato
[i] Exibir dados da conta
[q] Retornar ao menu inicial


=> """
    escolha = input(menu).lower()
    return escolha


def filtrar_cliente(cpf, clientes):
    cliente_filtrado = [cliente for cliente in clientes if cliente.cpf == cpf]
    return cliente_filtrado[0] if cliente_filtrado else None


def filtrar_contas(cpf, contas):
    conta_filtrada = [conta for conta in contas if conta.cliente.cpf == cpf]
    return conta_filtrada if conta_filtrada else None


def criar_contas(contas, cliente):

    if not contas:
        conta = ContaCorrente(1, cliente)
        contas.append(conta)
        return conta
    else:
        ultima_conta = contas[-1].numero + 1
        conta = ContaCorrente(ultima_conta, cliente)
        contas.append(conta)
        return conta


def exibir_extrato(conta):
    print("\n=================EXTRATO=================")
    transacoes = conta.historico.transacoes
    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações nesta conta."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}\n\t{transacao['data']}"
    print(extrato)
    print(f"\nSaldo: \n\tR$ {conta.saldo:.2f}")
    print("\n=========================================")


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu_inicial()

        if opcao == "c":
            # Seção para criação de novos usuários e/ou novas contas
            print(
                """
------------------
-MENU DE CADASTRO-
------------------
    """
            )

            cpf = input("Digite seu cpf: ")
            cliente_atual = filtrar_cliente(cpf, clientes)
            if cliente_atual:
                criar_conta_usuario_existente = input(
                    """
    Deseja criar uma nova conta?

    1 - Sim
    2 - Não

    => """
                )
                if criar_conta_usuario_existente == "1":

                    criar_contas(contas, cliente_atual)

                    print("Conta corrente criada com sucesso.")
                elif criar_conta_usuario_existente == "2":
                    print("Criação de contada negada pelo usuário")
                else:
                    print("Escolha inválida, retornando ao menu inicial.")

            else:
                nome = input("Digite seu nome: ")
                data_nascimento = input("Digite sua data de nascimento: ")
                endereco = input("Digute seu endereço completo: ")
                novo_cliente = PessoaFisica(nome, cpf, data_nascimento, endereco)

                clientes.append(novo_cliente)

                opcao_criar_conta = input(
                    """Usuário criado com sucesso. Deseja criar uma conta?

    1 - Sim
    2 - Não

    => """
                )
                if opcao_criar_conta == "1":
                    criar_contas(contas, novo_cliente)
                    print("Conta corrente criada com sucesso.")
                elif opcao_criar_conta == "2":
                    print("Criação de contada negada pelo usuário")
                else:
                    print("Escolha inválida, retornando ao menu inicial.")

        elif opcao == "e":
            cpf = input(" Informe seu CPF: ")
            conta_filtrada = filtrar_contas(cpf, contas)
            if conta_filtrada == None:
                print("Conta não cadastrada.")
                conta_acessada = False

            elif len(conta_filtrada) > 1:
                print("Múltiplas contas existentes:\n")
                lista_contas = [num_conta.numero for num_conta in conta_filtrada]
                print([f"Conta: {num_conta.numero}" for num_conta in conta_filtrada])
                numero_conta_escolhida = int(input("\nQual conta quer utilizar?\n"))
                if numero_conta_escolhida in lista_contas:
                    for instancia_conta in conta_filtrada:
                        if instancia_conta.numero == numero_conta_escolhida:
                            conta_escolhida = instancia_conta
                    conta_acessada = True
                    nome = conta_filtrada[0].cliente.nome
                    del conta_filtrada
                else:
                    print("Conta informada não existente. Retornando ao menu inicial.")
                    conta_acessada = False
            else:
                numero_conta_escolhida = conta_filtrada[0].numero
                conta_escolhida = conta_filtrada[0]
                conta_acessada = True
                nome = conta_filtrada[0].cliente.nome
                del conta_filtrada

            if conta_acessada:
                print(f"Bem vindo {nome}, você está na conta {numero_conta_escolhida}.")

                while True:
                    opcao2 = menu_escolha_transacao()
                    if opcao2 == "d":
                        valor = float(input("Qual o valor deseja depositar?\n"))
                        realizar_deposito = Deposito(valor)
                        realizar_deposito.registrar(conta_escolhida)

                    elif opcao2 == "s":
                        valor = float(input("Qual o valor deseja sacar?\n"))
                        realizar_saque = Saque(valor)
                        realizar_saque.registrar(conta_escolhida)
                    elif opcao2 == "e":
                        exibir_extrato(conta_escolhida)
                    elif opcao2 == "i":
                        print(conta_escolhida)
                    elif opcao2 == "q":
                        print("Obrigado por ser nosso cliente!")
                        break
                    else:
                        print("Escolha inválida, escolha a transação apropriada.")

            if conta_acessada == False:
                print("Conta não cadastrada.")

        elif opcao == "q":
            print(" Tenha um bom dia.")
            break

        else:
            print("Opção inválida. Escolha entre os valores disponíveis.")


main()

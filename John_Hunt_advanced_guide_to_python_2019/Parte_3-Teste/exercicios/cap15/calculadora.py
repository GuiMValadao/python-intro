class Calculadora:

    def __init__(
        self,
    ):
        self._valor1 = 0
        self._valor2 = 0
        self.total = 0
        self._operador = ""

    @property
    def operador(self):
        return self._operador

    @operador.setter
    def operador(self, escolha_usuario):

        operadores = ["+", "-", "*", "/"]
        if escolha_usuario in operadores:
            self._operador = escolha_usuario
        else:
            print("Operação escolhida inválida!")
            self._operador = None

    @property
    def valor1(self):
        return self._valor1

    @property
    def valor2(self):
        return self._valor2

    @valor1.setter
    def valor1(self, valor):
        escolha_usuario = valor
        try:
            usuario_float = float(escolha_usuario)
            self._valor1 = usuario_float

        except ValueError:
            print("Valor escolhido não é um número.")
            self._valor1 = None

    @valor2.setter
    def valor2(self, valor):
        escolha_usuario = valor
        try:
            usuario_float = float(escolha_usuario)
            self._valor2 = usuario_float
        except ValueError:
            print("Valor escolhido não é um número.")
            self._valor2 = None

    def realizar_operacao(self):
        if self.operador == "+":
            return self._soma()
        elif self.operador == "-":
            return self._sub()
        elif self.operador == "*":
            return self._mult()
        elif self.operador == "/":
            return self._div()
        else:
            return None

    def _soma(self):
        resultado = self._valor1 + self._valor2
        # self.total += resultado
        return resultado

    def _sub(self):
        resultado = self.valor1 - self.valor2
        # self.total += resultado
        return resultado

    def _mult(self):
        resultado = self.valor1 * self.valor2
        # self.total += resultado
        return resultado

    def _div(self):
        try:
            resultado = self.valor1 / self.valor2
            # self.total += resultado
            return resultado
        except ZeroDivisionError:
            print("Divisão por zero, cálculo interrompido.")
            return None

    def mudar_total(self, valor):
        self.total += valor

    def total_atual(self):
        return self.total

    def limpar_total(self):
        self.total = 0

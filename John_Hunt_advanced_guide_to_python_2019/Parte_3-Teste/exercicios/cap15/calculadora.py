class Calculadora:

    def __init__(self, valor1, valor2, operador="+"):
        self.valor1 = valor1
        self.valor2 = valor2
        self.total = 0
        self.escolher_operador(operador, valor1, valor2)

    def escolher_operador(self, operador):
        operadores = ["+", "-", "*", "/"]
        operacoes = [self.soma, self.sub, self.mult, self.div]
        if operador in operadores:
            i = operadores.index(operador)
            operacoes[i](self)

        else:
            print("Operação escolhida não registrada.")

    def soma(self):
        resultado = self.valor1 + self.valor2
        self.total += resultado
        return resultado

    def sub(self):
        resultado = self.valor1 - self.valor2
        self.total += resultado
        return resultado

    def mult(self):
        resultado = self.valor1 * self.valor2
        self.total += resultado
        return resultado

    def div(self):
        try:
            resultado = self.valor1 / self.valor2
            self.total += resultado
            return resultado
        except ZeroDivisionError:
            print("Divisão por zero, cálculo interrompido.")

    def total_atual(self):
        return self.total

    def limpar_total(self):
        self.total = 0

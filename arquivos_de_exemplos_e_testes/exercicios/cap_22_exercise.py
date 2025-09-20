#########################################
# Exercício cap 22
#########################################
#   def checar_unidade(self, unidade, other)
#        possibilidades = ('m', 'milha')
#        if self.unidade in possibilidades:
#            return True
#        else:
#            print('A distância deve estar em metros ou milhas')
#            self.__init__(self, input(), input)

class Distancia:
    """ Cria uma classe distância que permite realizar operações 
        de adição e subtração entre distâncias e divisão e
        multiplicação por um inteiro """
    
    def __init__(self, valor = 0):
        self.valor = valor
 
    def __add__(self, other):
        nova_dist = self.valor + other.valor
        return Distancia(nova_dist)
    
    def __sub__(self, other):
        nova_dist = self.valor - other.valor
        return Distancia(nova_dist)
    
    def __truediv__(self, other):
        if isinstance(other, int):
            print('div')
            nova_dist = self.valor / other
        else:
            print('Este valor é a razão entre as distâncias:')
            nova_dist = self.valor / other.valor
        return Distancia(nova_dist)
    
    def __floordiv__(self, other):
        if isinstance(other, int):
            nova_dist = self.valor // other
        else:
            print('Este valor é a razão entre as distâncias:')
            nova_dist = self.valor // other.valor
        return Distancia(nova_dist)
    
    def __mul__(self, other):
        if isinstance(other, int):
            nova_dist = self.valor * other
        else:
            nova_dist = self.valor * other.valor
        return Distancia(nova_dist)

    def __str__(self):
        return (f'Quantity[{self.valor:}]')
    

d1 = Distancia(6)
d2 = Distancia(3)
print( d1 + d2)
print (d1 - d2)
print (d1 / d2)
print(d2 // 2)
print(d2 * 2)
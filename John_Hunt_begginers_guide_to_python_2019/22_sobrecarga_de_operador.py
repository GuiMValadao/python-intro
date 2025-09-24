# Capítulo 22 - Sobrecarga de Operador (Operator Overloading)
# 
# Por que TER sobrecarga de operador?
# Sobrecarga de operador permite a classes definidas pelo usuário
# parecerem ter um jeito natural de usar operadores como +, -, <,
# > ou ==, assim como operadores lógicos como &(and) e |(or).
# Isto leva a códigos mais sucintos e legíveis como torna possível
# escrever coisas como:
# q1 = Quantity(5)
# q2 = Quantity(10)
# q3 = q1 + q2
# A alternativa seria criar métodos como 'add' para escrever
# q1 = Quantity(5)
# q2 = Quantity(10)
# q3 = q1.add(q2)
# Que poderia, semanticamente, significar a mesma coisa, mas parece 
# menos natural para a maioria das pessoas.
# Por que NÃO TER sobrecarga de operador?
# Uma resposta é porque isso pode ser abusado. Por exemplo:
# p1 = Pessoa('John')
# p2 = Pessoa('Denise')
# p3 = p1 + p2
# Não é claro o que '+' significa neste contexto; como Denise está sendo
# somada a John; isto implica que eles estão se casando? Se sim, qual
# o resultado armazenado em p3?
# Como princípio geral, desenvolvedores deveriam seguir a semântica
# de tipos pré-construídos e deveriam apenas implementar aqueles operadores
# que são apropriados para o tipo sendo desenvolvido.
#----------------------------------------
# Implementando Sobrecarga de operador
# Para implementar operadores como '+' em uma classe definida pelo 
# usuário é necessário implementar métodos específicos que são, então,
# mapeados aos operadores aritméticos ou lógicos usados pelos 
# usuários da classe.
# Estes métodos são considerados especiais pois começam e terminam com uma
# barra dupla('__'). Tais métodos são considerados privados e geralmente
# restritor para implementações orientadas por Python (já vimos métodos
# assim com __init__() e __str__()).
# Como exemplo, suponha que queremos implementar os operadores '+' e '-' 
# para o tipo Quantidade. Também queremos nosso tipo Quantidade ter valores
# de fato e ser capaz de ser convertido em uma string para exibição.
# Para implementar esses operadores precisamos fornecer dois métodos
# especiais; um fornecerá a implementação de '+' e o outro  de '-'.
#   *   '+' é implementado por um método def __add__(self, outro):
#   *   '-' é implementado por um método def __sub__(self, outro):
# Onde 'outro' representa outra Quantidade ou outro tipo apropriado que
# será adicionado ou subtraido do obejto Quantidade atual.
# Os métodos serão mapeados por Python aos operadores '+' e '-'; 
# de forma que se alguém tentar adicionar quantidades o método 
# __add__() será chamado.
# A definição da classe Quantidade é dada abaixo; note que a classe 
# apenas cobre um número guardade no atributo 'valor':
class Quantidade:
    def __init__(self, valor=0):
        self.valor = valor
    def __add__(self, outro):
        novo_valor = self.valor + outro.valor
        return Quantidade(novo_valor)
    def __sub__(self, outro):
        novo_valor - self.valor - outro.valor
        return Quantidade(novo_valor)
    def __str__(self):
        return f'Quantidade [{str(self.valor)}]'
q1 = Quantidade(5)
q2 = Quantidade(10)
print('q1=', q1, ', q1 =', q2 )
q3 = q1 + q2
print('q3 +', q3)
# Ao executar esse código obtemos:
# q1= Quantidade [5] , q1 = Quantidade [10]
# q3 + Quantidade [15]
# Note que fizemos a classe Quantidade imutável; uma vez que uma
# instância foi criada, seu valor não pode ser alterado.
# Isto quer dizer que quando duas quantidades são somadas, uma nova
# instância da classe Quantidade é criada. Isto é análogo a como
# inteiros funcionam; somar 2 e 3 resulta em 5, sem modificar o 2
# inicial nem o 3.
#---------------------------------------
# Operadores numéricos
# Há nove diferentes tipos de operadores numéricos que podem ser
# implementados por métodos especiais. São eles:

# Operador                      | Expressão     | Método
#-------------------------------+---------------+-------------------
# Adição                        | q1 + q2       | __add__(self, q2)
# Subtração                     | q1 - q2       | __sub__(self, q2)
# Multiplicação                 | q1 * q2       | __mul__(self, q2)
# Potenciação                   | q1 ** q2      | __pow__(self, q2)
# Divisão                       | q1 / q2       | __truediv__(self, q2)
# Divisão inteira               | q1 // q2      | __floordiv__(self, q2)
# Módulo (Resto)                | q1 % q2       | __mod__(self, q2)
# Deslocamento de bits à esq    | q1 << q2      | __lshift__(self, q2)
# Deslocamento de bits à dir    | q1 >> q2      | __rshift__(self, q2)

# Já vimos exemplos e + e -; esta tabela mostra os demais operadores.
# A tabela também mostra os operadores de deslocamento de bits. Eles
# operam o nível de bit usado para representar números debaixo da
# tampa e pode ser um jeito muito eficiente de manipular valores
# numéricos; entretanto, não queremos suportar essas operações para
# nossa classe Quantidade, de modo que vamos apenas implementar operadores
# numéricos centrais de multiplicação, divisão e potência.
# A classe Quantidade atualizada é:
class Quantity:
    
    def __init__(self, value=0):
        self.value = value
    
    def __add__(self, other):
        new_value = self.value + other.value
        return Quantity(new_value)
    
    def __sub__(self, other):
        new_value = self.value - other.value
        return Quantity(new_value)
    
    def __mul__(self, other):
        if isinstance(other, int):
            new_value = self.value * other
        else:
            new_value = self.value * other.value
        return Quantity(new_value)
    
    def __pow__(self, other):
        new_value = self.value ** other.value
        return Quantity(new_value)
    
    def __truediv__(self, other):
        if isinstance(other, int):
            new_value = self.value / other
        else:    
            new_value = self.value / other.value
        return Quantity(new_value)
    
    def __floordiv__(self, other):
        new_value = self.value // other.value
        return Quantity(new_value)
    
    def __mod__(self, other):
        new_value = self.value % other.value
        return Quantity(new_value)
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __ne__(self, other):
        return self.value != other.value
    
    def __ge__(self, other):
        return self.value >= other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __le__(self, other):
        return self.value <= other.value
    
    def __str__(self):
        return 'Quantity[' + str(self.value) + ']'

# Isto significa que agora podemos estender nossa aplicação simples
# que usa a classe Quantidade para incluir alguns desse operadores
# numéricos adicionais:
q1 = Quantity(5)
q2 = Quantity(10)
print('q1 =', q1, ', q2 =', q2)
q3 = q1 + q2
print('q3 =', q3)
print('q2 - q1 =', q2 - q1)
print('q1 * q2 =', q1 * q2)
print('q1 / q2 =', q1 / q2)
# Um ponto de nota interessante é que nos estilos de método multiplicar
# e dividir, poderíamos querer multiplicar uma Quantidade por um inteiro
# ou dividir uma Quantidade por um inteiro. Seria um comportamento
# útil de se ter, permitindo uma Quantidade ser multiplicada por 2 
# ou dividida por 2:
#print('q1 * 2', q1 * 2)
#print('q2 / 2', q2 / 2)
# No entanto, isso resulta em um erro de atributo: "AttributeError: 
# 'int' object has no attribute 'value'". Podemos testar para
# ver se o argumento passado para __mult__() e __truediv__() é um
# int ou não usando a função 'isinstance'. Esta função pega uma
# variável e o nome de uma classe e retorna True se os conteúdos
# da variável são uma instância da classe nomeada, por exemplo:
#class Quantity:
# Code ommitted for brevity
#   def __mul__(self, other):
#       if isinstance(other, int):
#           new_value = self.value * other
#       else:
#           new_value = self.value * other.value
#       return Quantity(new_value)
#   def __truediv__(self, other):
#       if isinstance(other, int):
#           new_value = self.value / other
#       else:
#           new_value = self.value / other.value
#       return Quantity(new_value)
# Com essa alteração em mult e truediv podemos realizar as operações
# com inteiros.
#--------------------------------------
# Operadores de comparação
# Tipos numéricos também suportam operadores de comparação como
# igual, não-igual, maior, menor, maior ou igual e menor ou igual.
# Estes operadores também podem ser definidos para classes/tipos
# definidas pelo usuário.
# Operador                      | Expressão     | Método
#-------------------------------+---------------+-------------------
# Menor que                     | q1 < q2       | __lt__(q1, q2)
# Menor que ou igual a          | q1 <= q2      | __le__(q1, q2)
# Igual a                       | q1 == q2      | __eq__(q1, q2)
# Não-igual a                   | q1 != q2      | __ne__(q1, q2)
# Maior que                     | q1 > q2       | __gt__(q1, q2)
# Maior que ou igual a          | q1 >= q2      | __ge__(q1, q2)

# Podemos adicionar estas definições a nossa classe Quantidade para
# fornecer um tipo mais completo que pode ser usado em testes de comparação
# de estilo (como declarações if).
# A classe Quantidade é atualizada acima. Isto agora significa que podemos
# atualizar nossa aplicação de amostra para isar operações de comparação.
#-------------------------------------------
# Operadores Lógicos
# # Operador                      | Expressão     | Método
#-------------------------------+---------------+-------------------
# AND                           | q1 & q2       | __and__(q1, q2)
# OR                            | q1 | q2       | __or__(q1, q2)
# XOR                           | q1 ^  q2      | __xor__(q1, q2)
# NOT                           | ~q1           | __invert__()
# Como esses operadores não fazem sentido para o tipo Quantidade, 
# não os definiremos
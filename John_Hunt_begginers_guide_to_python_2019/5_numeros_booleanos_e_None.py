#Tres tipos de numeros: inteiros (integers), reais (float) e complexos (complex)
#numeros imaginario sao representados por um j, como 3 + 5j
#x = 1.2 + 3.8j
#print(x)
#print(type(x))
#x = 10000000000000000
#print(x)
#print(type(x))
#----------------------------------------------
#NUMEROS INTEIROS
#Convertendo para numeros inteiros:
#idade = input('Insira sua idade:')
#print(type(idade))
#print(idade)
#idade_int = int(idade)
#print(type(idade_int))
#print(idade_int)
#----------------------------------------------
#NUMEROS COMPLEXOS
#c1 = 3 + 5j
#c2 = 3.5j
#print('c1:', c1, 'c2:', c2)
#print(type(c1))
#print(c1.real)
#print(c1.imag)
#print(c2.real)
#print(c2.imag)
#----------------------------------------------
#BOOLEANOS
#all_ok = True
#print(all_ok)
#not_ok = False
#print(not_ok)
#print(type(all_ok))
#print(all_ok != not_ok)
#print(int(True))
#print(int(False))
#print(bool(1))
#print(bool(0))
#status = bool(input('Tudo certo pra continuar: '))          #?Deveria retornar T ou F para as respostas T ou F, mas retorna T para qualquer coisa digitada e F para o input vazio.
#print(status)
#print(type(status))
#----------------------------------------------
#OPERADORES ARITMETICOS
#+, -, *, /, //(Divisao integral, ignorando restos), %(Modulo, ou restante, retorna apenas o resto), **(Expoente, com o valor na potencia do numero a direita
#print(7+3)      #int
#print(15-4)     #int
#print(2*23)     #int
#print(200/20)   #float
#print(type(200/20)) #float
#print(200//20)      #int
#print(type(200//20))    #int
#print(200%20)       #% pode ser usado para checar se um numero e divisivel por outro.
#print(200%19)       #Se % retorna zero, e divisivel, caso contrario nao e
#print(28%3)
#print(27%3)
#Divisao numeros inteiros negativos
#print(3/2)
#print(-3/2)
#print(3//2)
#print(-3//2)        #Python sempre arredonda o resultado da divisao de integrais para menos infinito, ou seja, para o menor numero. 1 < 1,5; mas -2 < -1,5
#Calculos de numeros racionais (float)
#print(1.2+2.3)
#print(2.3-1.2)
#print(1.2-2.3)
#print(1.2*2.3)
#print(1.2/2.3)
#print(3+0.1)
#print(3*0.1)        #devido a questoes de arredondamento a aproximaçao computacional, floats sao um aproximaçao computacional. Pode-se resolver esse problema com uma biblioteca(ou modulo) de Python, como 'decimal'
#Calculo com numeros complexos
#c1 = 1j
#c2 = 5j
#c3 = c1 + c2
#print(c3)
#print(c1*c2)
#c4 = c1*c2
#int1 = '45'
#print(complex(int1))        #complex(string_or_number) transforma o argumento em um numero complexo. O modulo 'math' provide funçoes matematicas para numeros complexos.
#---------------------------------------------
#Operadores de atribuiçao - funcionam com aaaas mesmas operaçoes anteriores
#mas simplificam a escrita, substituindo x = x + 2 por x += 2
#x = 0
#x += 2
#print(x)
#x -= 5
#print(x)
#x *= -10
#print(x)
#x /= 2
#print(x)
#x //= 2
#print(x)
#x %= 4
#print(x)
#x **= 4
#print(x)
#------------------------------------------
#Variavel None
#O tipo None e um tipo especial, que representa um valor nao existente, ou vazio, sendo diferente de 'False' (booleano), '0' (integer) ou ''(string vazia)
#winner = None
#print(type(winner))
#print(winner is None)
#print(winner is not None)
#winner = True
#print(type(winner))
#print(winner is None)
#print(winner is not None)

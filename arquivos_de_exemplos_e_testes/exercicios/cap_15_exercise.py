#----------------------------------------------
#The aim of this exercise is to explore higher order functions.
#You should write a higher order function function called
#my_higher_order_function(i, func). This function takes a parameter
#and a second function to apply to the parameter.
#Now you should write a sample program that uses the higher order function you
#just created to perform. An example of the sort of thing you might implement is
#given below:
#print(my_higher_order_function(2, double))
#print(my_higher_order_function(2, triple))
#print(my_higher_order_function(16, square_root))
#print(my_higher_order_function(2, is_prime))
#print(my_higher_order_function(4, is_prime))
#print(my_higher_order_function('2', is_integer))
#print(my_higher_order_function('A', is_integer))
#print(my_higher_order_function('A', is_letter))
#print(my_higher_order_function('1', is_letter))
#If you are using the above code as your test application then you should write
#each of the supporting functions; each should take a single parameter.
#Sample output from this code snippet is:
#4
#8
#4.0
#True
#False
#True
#False
#True
#False
#Note a simple way to ﬁnd the square root of a number is to use the exponent (or
#power of) operator and multiply by 0.5
def minha_funcao_de_alta_ordem(i, func):
    return func(i)

def dobro(i):
    return 2 * i

def triplo(i):
    return 3 * i

def raiz_quadrada(i):
    return i ** 0.5

def e_primo(i):
    j = 0
    for n in range(2, (i + 2) // 2):
        if i % n == 0:
            return False
        else:
            j += 1
    if j == (i - 2) // 2:
        return True

def e_inteiro(i):
    if i.isnumeric():
        return True
    else:
        return False

def e_letra(i):
    if i.isalpha():
        return True
    else:
        return False

print(minha_funcao_de_alta_ordem(2, dobro))
print(minha_funcao_de_alta_ordem(2, triplo))
print(minha_funcao_de_alta_ordem(16, raiz_quadrada))
print(minha_funcao_de_alta_ordem(2, e_primo))
print(minha_funcao_de_alta_ordem(4, e_primo))
print(minha_funcao_de_alta_ordem('2', e_inteiro))
print(minha_funcao_de_alta_ordem('A', e_inteiro))
print(minha_funcao_de_alta_ordem('A', e_letra))
print(minha_funcao_de_alta_ordem('1', e_letra))
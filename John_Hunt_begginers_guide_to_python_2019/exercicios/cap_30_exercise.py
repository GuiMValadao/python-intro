#
# Capitulo 30

# Write a prime number generator; you can use the prime number program you
# wrote earlier in the book but convert it into a generator. The generator should take a
# limit to give the maximum size of the loop you use to generate the prime numbers.
# You could call this prime_number_generator().

def gerador_numeros_primos(numero:int):
    """
    Gera números primos até o limite definido por numero.
    """
    i = 2
    print('funcao')
    while i <= numero:
        
        for j in range(2, i+1):     # Limite i+1 pois é exclusivo, com i+1 retorna também 2 como primo
        
            if i % j == 0 and i != 2:
                break
            else:
                j += 1
                if j == i or i == 2:
                    yield i
        i += 1

def gerador_numeros_primos_infinito():
    """
    Gera números primos infinitamente enquanto
    a função for chamada.
    """
    i = 2
    print('funcao')
    while True:
        
        for j in range(2, i+1):     # Limite i+1 pois é exclusivo, com i+1 retorna também 2 como primo
        
            if i % j == 0 and i != 2:
                break
            else:
                j += 1
                if j == i or i == 2:
                    yield i
        i += 1


# Parte para chamada de gerador_numeros_primos
#alcance = input('Digite o número máximo a verificar: ')
#if alcance.isnumeric():         
#    alcance = int(alcance)      # Definir alcance como número fixo
    #Loop para calcular os números primos
    #if alcance > 2:
    #    for primo in gerador_numeros_primos(alcance):
    #        print(primo, end=', ')
    #else:
    #    print('Erro, o alcance deve ser maior que dois')
#else:
    #print('Erro, insira um número inteiro positivo.')


# Parte para chamada de gerador_numeros_primos_infinito
#ger = gerador_numeros_primos_infinito()

#for i in range(5000):
#    print(next(ger), end=', ')


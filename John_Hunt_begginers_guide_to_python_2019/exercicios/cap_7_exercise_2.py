#A Prime Number is a positive whole number, greater than 1, that has no other
#divisors except the number 1 and the number itself.
#That is, it can only be divided by itself and the number 1, for example the
#numbers 2, 3, 5 and 7 are prime numbers as they cannot be divided by any other
#whole number. However, the numbers 4 and 6 are not because they can both be
#divided by the number 2 in addition the number 6 can also be divided by the
#number 3.
#You should write a program to calculate prime number starting from 1 up to the
#value input by the user.
#If the user inputs a number below 2, print an error message.
#For any number greater than 2 loop for each integer from 2 to that number and
#determine if it can be divided by another number (you will probably need two for
#loops for this; one nested inside the other).
#For each number that cannot be divided by any other number (that is its a prime
#number) print it out.

# Pedir o alcance desejado ao usuario
alcance = input('Digite o número máximo a verificar: ')
# Loop para garantir que e número positivo e inteiro
if alcance.isnumeric():
    alcance = int(alcance)      # Definir alcance como número fixo
    #Loop para calcular os números primos
    if 2 < alcance:
        for i in range(2,alcance+1):
            for j in range (2,i+1):
                if i%j == 0 and i != 2:
                    break
                else:
                    j += 1
                    if j == i or i == 2:
                        print(i, end=' ')

            i += 1
    else:
        print('Erro, o alcance deve ser maior que dois')
else:
    print('Erro, insira um número inteiro.')

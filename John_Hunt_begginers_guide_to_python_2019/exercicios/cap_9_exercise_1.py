#1. Write a program to determine if a given number is a Prime Number or not. Use
#recursion to implement the solution. The following code snippet illustrates how
#this might work:
#print('is_prime(3):', is_prime(3)) # True
#print('is_prime(7):', is_prime(7)) # True
#print('is_prime(9):', is_prime(9)) # False
#print('is_prime(31):', is_prime(31)) # True

def primo_calc(n, num = 2):
    if n%num != 0:
        if num + 1 < n:
            return primo_calc(n,num + 1)
        else:
            return 'Sim'
    else:
        return 'Nao'

x = int(input('Insira o numero para saber se e primo: '))
print('O numero', x, 'e primo?', primo_calc(x))



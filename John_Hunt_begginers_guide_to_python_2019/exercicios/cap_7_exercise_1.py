#Write a program that can ﬁnd the factorial of any given number. For example, ﬁnd
#the factorial of the number 5 (often written as 5!) which is 1 * 2 * 3 * 4 * 5 and
#equals 120.
#The factorial is not deﬁned for negative numbers and the factorial of Zero is 1;
#that is 0! = 1
#Your program should take as input an integer from the user (you can reuse your
#logic from the last chapter to verify that they have entered a positive integer value
#using isnumeric()).
#You should
#1. If the number is less than Zero return with an error message.
#2. Check to see if the number is Zero—if it is then the answer is 1—print this out.
#3. Otherwise use a loop to generate the result and print it out.

# Pede o inteiro ao usuario
num = input('Insira o valor a ser obtido o fatorial: ')

# Loop para checar se e inteiro:
if num.isnumeric():
    num_int =  int(num)
    fat = int(num)
    # Checa se o numero e zero. Se for, entao o fatorial é 1.
    if num_int == 0:
        fat = 1
    else:
        # Se o numero nao e zero, procede para calcular o fatorial
        while num_int > 2:                      # Como o fatorial vai estar multiplicando o numero atual
            fat = fat*(num_int-1)               # pelo atual menos 1 so precisamos calcular ate num_int == 3,
            num_int -= 1                        # ou num_int > 2
    print ('O fatorial de ', int(num), 'é ', fat)
else:
    print('Erro!! Insira um numero inteiro.')
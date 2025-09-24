#The aim of this exercise is to write a small program to test if an integer is positive or
#negative.
#Your program should:
#1. Prompt the user to input a number (use the input() function). You can assume
#that the input will be some sort of number.
#2. Convert the string into an integer using the int() function.
#3. Now check whether the integer is a positive number or a negative number.
#4. You could also add a test to see if the number is Zero

x = input('Digite um numero: ')
x = int(x)
if x > 0:
    print('Positivo')
elif x < 0:
    print('Negativo')
else:
    print('Zero')

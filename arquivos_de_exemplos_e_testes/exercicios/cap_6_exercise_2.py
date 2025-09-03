#The exercises recquires you to write a program to take input from the user and
#determine if the number is odd or even. Again you can assume that the user will
#enter a valid integer number.
#Print out a message to the user to let them know the result.
#To test if a number is even you can use
#(num % 2) == 0
#Which will return True if the number is even (note the brackets are optional but
#make it easier to read).
number = int(input('Digite um numero: '))
if number%2 == 0:
    print(number, 'é Par')
else:
    print(number, 'é Impar')
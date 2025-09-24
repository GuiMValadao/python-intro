#Explore replacing a string
#Create a string with words separated by ',' and replace the commas with spaces;
#for example replace all the commas in 'Denyse,Marie,Smith,21,London,UK'
#with spaces. Now print out the resulting string.

lista = 'Denyse,Marie,Smith,21,London,UK'
print(lista.replace(',',' '))

#Handle user input
#The aim of this exercise is to write a program to ask the user for two strings and
#concatenate them together, with a space between them and store them into a new
#variable called new_string.
#Next:
#-Print out the value of new_string.
#-Print out how long the contents of new_string is.
#-Now convert the contents of new_string to all upper case.
#-Now check to see if new_string contains the string 'Albus' as a substring.

frase1 = input('Insira a primeira frase:')      #input do usuario
frase2 = input('Insira a segunda frase:')       #input do usuario
new_string = frase1 + ' ' + frase2              #aglutina os dois inputs, com um espaço entre eles
print (new_string)                              #exibe a frase composta
print(len(new_string))                          #calcula o comprimento da frase composta e exibe o valor
print(new_string.upper())                       #transforma todos os caracteres em letra maiuscula
print(new_string.find('Albus'))                 #Procura a palavra 'Albus' na frase composta.
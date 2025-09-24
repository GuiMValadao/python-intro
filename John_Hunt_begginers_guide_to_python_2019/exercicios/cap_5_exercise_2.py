#The aim of this exercise is to write a program to convert a distance in Kilometres
#into a distance in miles.
#1. Take input from the user for a given distance in Kilometres. This can be done
#using the input() function.
#2. Convert the value returned by the input() function from a string into an
#integer using the int() function.
#3. Now convert this value into miles—this can be done by dividing the kilometres
#by 0.6214
#4. Print out a message telling the user what the kilometres are in miles.

distancia = int(input('Digite a distância em Km: '))
distanciamilhas = distancia/0.6214
print(distancia, ' Km equivalem a ', distanciamilhas,' milhas')

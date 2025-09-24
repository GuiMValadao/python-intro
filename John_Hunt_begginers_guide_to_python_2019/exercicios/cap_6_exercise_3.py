#In this exercise you should return to the kilometres to miles converter you wrote in
#the last chapter.
#We will add several new tests to your program:
#1. Modify your program such that it verify that the user has entered a positive
#distance (i.e. they cannot enter a negative number).
#2. Now modify your program to verify that the input is a number; if it is not a
#number then do nothing; otherwise convert the distance to miles.
#To check to see if a string contains only digits use the method isnumeric()
#for example '42'.isnumeric(); which returns True if the string only con-
#tains numbers. Note this method only works for positive integers; but this is suf-
#ﬁcient for this example.

#Input do usuario
distancia = input('Digite a distância em Km: ')
#Verificar que a distancia e positiva
if distancia.isnumeric():
    distanciamilhas = int(distancia)/0.6214
    print(distancia, ' Km equivalem a ', distanciamilhas,' milhas')



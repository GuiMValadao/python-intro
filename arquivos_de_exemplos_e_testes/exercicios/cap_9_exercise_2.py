#Write a function which implements Pascal’s triangle for a speciﬁed number of
#rows. Pascals triangle is a triangle of the binomial coefﬁcients. The values held
#in the triangle are generated as follows: In row 0 (the topmost row), there is a
#unique nonzero entry 1. Each entry of each subsequent row is constructed by
#adding the number above and to the left with the number above and to the right,
#treating blank entries as 0. For example, the initial number in the ﬁrst (or any
#other) row is 1 (the sum of 0 and 1), whereas the numbers 1 and 3 in the third
#row are added together to generate the number 4 in the fourth row. An example
#of Pascals triangle for 4 rows is given below:106
#9 Recursion
#For example, your function might be called pascals_traingle() in which
#case the following application illustrates how you might use it:
#triangle = pascals_triangle(5)
#for row in triangle:
#print(row)
#The output from this might be:
#[1]
#[1, 1]
#[1, 2, 1]
#[1, 3, 3, 1]
#[1, 4, 6, 4, 1]

#-------------------------------------------------------
# Pseudocodigo
# definir a funcao triangulo pascal que vai imprimir uma linha ate i =n
#   na linha 0, t[0,0] = 1
#   na linha seguinte, t[1,0] = t[{1-1}, {(0-1)+(0-1)}]

# O programa aqui e adaptado da resposta.
#----------------------------------------
def triangulo_pascal(n):
   # Condiçao de terminaçao
    if n == 1:
        return [[1]]                        # Primeiro termo
    else:
       res = triangulo_pascal(n-1)          # Linha que chama recursivamente a funcao
       linha_atual = [1]                    # Primeira coluna e sempre 1
       linha_anterior = res[-1]             # seleciona ultimo termo da linha anterior

       for i in range(len(linha_anterior)-1):
           linha_atual.append(linha_anterior[i]+linha_anterior[i+1])    # Adiciona dois termos da linha anterior
       linha_atual += [1]                   # Adiciona 1 ao ultimo termo da linha atual
       res.append(linha_atual)

       return res

x = int(input('Digite o tamanho da piramide: '))
triangulo = triangulo_pascal(x)

for linha in triangulo:
    print(linha)



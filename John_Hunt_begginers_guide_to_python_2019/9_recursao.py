# Á á Â â Ã ã Ê ê É é Í í Ó ó Ú ú
#-------------------------------------------
# RECURSÃO
#-------------------------------------------
# Recursão é quando uma funçao chama a si mesma uma ou mais vezes,
# para resolver um problema. Precisa ter uma condiçao de termino.
# Essas condiçao pode ser apos a soluçao ser econtrada, o problema
# se tornou simples e nao precisa mais de recursao ou um nivel maximo
# de recursoes foi atingido, possivelmente sem uma soluçao.

#def funcao_recursiva():
#    print('Chamando a função recursiva')
#    funcao_recursiva()
#funcao_recursiva()

#--------------------------------------------
# Fatorial

#def fatorial(n, depth = 1):     # depth apenas fornece uma indentaçao aos prints
#    if n == 1:      # Condiçao de terminaçao
#        print('\t'*depth, 'Retornando 1')
#        return 1    # O caso base
#    else:
#        print('\t'*depth, 'Chamando fatorial recursivamente(', n-1, ')')
#        result = n * fatorial(n-1, depth +1)     # Chamada recursiva
#        print('\t'*depth, 'Retornando: ', result)
#        return result
#x = int(input('Insira o numero a ser calculado o fatorial: '))
#print('Chamando fatorial de (', x, ')')
#print (fatorial(x))
# A recursao costuma ser mais exigente que iteraçao em termos de memoria por necessitar
# que o computador guarde valores antes de executar a funçao novamente.
# Isso pode ser contornado fazendo com que o calculo seja feito antes da  nova
# chamada recursiva, tornando a recursao a algo similar de processar que a iteraçao
# mas mantendo a concisao da funçao, o que e chamado de recursao de cauda (tail recursion)
# Escrevendo um programa para calcular fatorial usando recursao de cauda:
def fatorial_cauda(n, acc=1):
    if n == 0:
        return acc
    else:
        return fatorial_cauda(n-1, acc*n)   # O parametro acc passa o resultado do calculo para cada execuçao recursiva seguinte.
x = int(input('Insira o numero para calcular o fatorial: '))
print(fatorial_cauda(x))
#--------------------------------------------


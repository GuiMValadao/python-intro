# Funçoes Curry
# Currying e uma tecnica que permite novas funçoes serem criadas de funçoes existentes
# 'prendendo' um ou mais parametros a um valor especifico. E uma grande fonte de
# reutilizaçao de funçoes em Python, que significa que funcionalidade pode ser escrita
# uma vez, em um lugar, e entao reutilizada em multiplas outras situaçoes.
# A tecnica e nomeada em homenagem a Haskell Curry.
#----------------------------------------------------
# Conceitos de Currying
# Em um nivel abstrato, considere ter uma funçao que recebe dois parametros.
# Estes dois parametros, x e y, sao usados quando o corpo da funçao com o
# operador multiplicador na forma x * y. Por exemplo, podemos ter:
# operation(x, y): return x * y
# Esta funçao operation() poderia entao ser usada como:
# total = operation(2, 5)
# Que resultaria em 5 sendo multiplcado por 2 para retornar 10. Se precisassemos
# duplicar um numero, poderiamos assim reutilizar a funçao operation() muitas vezes:
# operation(2, 5)
# operation(2, 10)
# operation(2, 6)
# operation(2, 151)
# Todas as utilizaçoes acima duplicam o segundo numero. No entanto, tivemos que lembrar
# de fornecer o 2 para que o numero fosse dobrado. Alem disso, o numero 2 nao
# foi alterado entre qualquer uma das invocaçoes da funçao operation().
# E se fixassemos o primeiro parametro para sempre ser 2, isto significaria que poderiamos
# criar uma nova funçao que aparentemente apenas recebe um parametro(o numero para duplicar).
# Por exemplo, poderiamos escrever algo como:
# double = operation(2, *)
# de modo que podemos agora escrever
# double(5)
# double(151)
# Em essencia, double() e uma alcunha para operation(), mas uma alcunha que fornece
# o valor 2 para o primeiro parametro e deixa o segundo parametro aberto para ser preenchido
# em futuras invocaçoes da funçao double.
#------------------------------------------------------
# Python e funcoes Curry
# Uma funçao Curry em Python e uma funçao onde um ou mais de seus parametros
# foram 'aplicados' ou 'presos' a um valor, resultando na criaçao de uma nova
# funçao com menos parametros que a original. Por exemplo, vamos criar uma funçao
# que multiplica dois numeros:
#def multiply(a, b):
#    return a * b
# Esta pe uma funçao geral que faz exatamente o que diz; multiplica quaisquer
# dois numeros. Estes numeros podem ser quaisquer numeros inteiros ou reais etc.
# Podemos entao invoca-la do modo comum:
#print(multiply(2, 5))
# Poderiamos agora definir um novo metodo que pega uma funçao e um numero
# e retorna uma nova funçao (anonima) que pega um parametro novo
# e chama a funçao passada com o numero fornecido e o novo parametro.
#def multby(func, num):
#    return lambda y:func(num, y)
# Olhe cuidadosamente a esta funçao; ela foi usada para prender o numero passado
# para a funçao multby a invocaçao da funçao passada a ela, mas tambem definiu
# uma nova variavel 'y' que devera ser fornecida quando essa nova funçao anonima
# for invocada. Entao ela retorna uma referencia a funçao anonima como resultado
# de multby.
# A funçao multby pode agora ser usada para prender o primeiro parametro da funçao
# multiply a qualquer coisa que quisermos. Por exemplo, poderiamos prende-la como
# 2 de modo que sempre ira dobrar o segundo parametro e guardar a referencia da
# funçao resultante em uma propriedade double:
#double = multby(multiply, 2)
# Poderiamos tambem prender o valor 3 para o primeiro parametro de multiply
# para fazer uma funçao que vai triplicar qualquer valor:
#triple = multby(multiply, 3)
#print(double(5))
#print(triple(5))
# Nao ha limitaçao em prender apenas um parametro, pode-se prender
# qualquer numero de parametros desta forma.
# Funçoes Curry sao, portanto, muito uteis para criar novas funçoes
# de funçoes existentes.
#--------------------------------------------
# Fechamentos
# Uma questao que pode surgir agora e o que acontece quando uma funçao referencia
# algum dado que esta em seu alcance quando e definida mas nao esta mais quando e
# avaliada? Esta questao e respondida pela implementaçao de um conceito conhecido
# como fechamento.
# Dentro da ciencia computacional (e linguagens de programaçao em particular)
# um fechamento(ou fechamento lexical ou funçao de fechamento) e uma funçao
# (ou mais estritamente, uma referencia a uma funçao) junto com um ambiente de
# referenciamento. Este ambiente de referenciamento grava o contexto dentro do qual
# a funçao foi originalmente definida e, se necessario, uma referencia a cada
# uma das variaveis nao-locais usada por aquela funçao. Estas variaveis naoo locais,
# ou livres, permitem o corpo da funçao referenciar variaveis que sao externas a
# funçao, mas que sao usadas pela funçao.
# O conceito geral de fechamento lexico foi desenvolvido primerio nos anos 60
# mas implementado completamente na linguagem Scheme nos anos 70.
# Em nivel conceitual, um fechamento permite uma funçao a referenciar uma
# variavel avaliavel no alcance onde a funçao foi originalmente definida, mas
# nao avaliavel por padrao no alcance onde e executada.
# Por exemplo, no seguinte programa simples, a variavel 'more' e definida
# fora do corpo da funçao chamada 'increase'. Isto e permissivel como a
# variavel e uma variavel global. Assim, a variavel 'more' esta dentro do alcance
# no ponto de definiçao.
#more = 100

#def increase(num):
#    return num + more

#print(increase(10))
#more = 50
#print(increase(10))

# Note que e o atual valor de 'more' que esta sendo usado quando a funçao executa
# e nao o valor de 'more' presente no ponto em que a funçao foi definida.
# Isto pode parecer obvio como a variavel 'more' ainda esta no alcance
# dentro da mesma funçao que as invocaçoes da funçao referenciada 'increase'.
# Entretanto, considere o seguinte exemplo:
#def increment(num):
#    return num + 1

#def reset_function():
#    global increment
#    addition = 50
#    increment = lambda num: num + addition
#print(increment(5))
#reset_function()
#print(increment(5))

# Nas linhas acima a funçao 'increment' inicialmete adiciona 1 a qualquer
# valor que foi passado a ela. Entao, no programa, esta funçao e chamada com o
# valor 5 e o resultado retornado pela funçao e exibido. Este valor e 6.
# Entretanto, depois disso uma segunda funçao, 'reset_function()', e invocada.
# ESta funçao tem uma variavel que e local a funçao. Isto e, normalmente,
# estaria apenas avaliavel dentro da funçao 'reset_function()'. Esta variavel
# e chamada adiçao e tem o valor de 50.
# A variavel 'addition' e, entretanto, usada dentro do corpo da funçao da
# definiçao de uma nova funçao anonima. Esta funçao pega um numero e adiciona
# o valor de 'addition' aquele numero e retorna isto como resultado da funçao.
# Esta nova funçao e, entao, atribuida o nome 'increment'. Note que para assegurar
# que referenciamos o nome global 'increment', devemos usar a palavra chave global,
# caso contratio seria criada uma funçao local increment cujo nome apenas coincide
# com a outra funçao.
# Agora, quando a segunda invocaçao de 'increment' ocorre, o metodo 'reset_function()
# terminou e normalmente a variavel adiçao nao existiria mais. Entretanto, quando
# este programa executa o valor 55 e exibido da segunda invocaçao de 'increment'.
# Isto e, a funçao sendo referenciada pelo nome increment, ao ser chamada pela
# segunda vez, e a definida dentro de 'reset_function()' e que usa a variavel addition.
# Este e um exemplo concreto do uso de um ambiente de referenciamento com o conceito
# de fechamento. Python garante que a variavel addition esta avaliavel para a funçao,
# mesmo se a invocaçao ocorra fora do alcance da funçao, prendendo quaisquer variaveis
# livres e guardando-as de modo que possam ser acessadas pelo contexto da funçao,
# efetivamente tornando a variavel como se fosse global apenas para aquela funçao especifica.

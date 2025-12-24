# Crie uma função chamada printer() que pega uma mensagem e um valor máximo
# para usar para um período para dormir. Dentro da função, crie um loop que itera
# 10 vezes. Dentro do loop:
#   * gere um número aleatório de 0 até o período máximo especificado e então
#       durma por aquele período. Pode usar a função random.randint() para isso.
#   * Após o período de inatividade, exiba a mensagem passada à função.
#   * Realize o loop novamente até isto ser repetido 10 vezes.
# Agora cria 5 threads para executar 5 invocações da função que você criou acima
# e inicie todas elas. Cada thread deveria ter um valor diferente de tempo de inatividade
# máximo.

from threading import Thread
from time import sleep
from random import randint


def printer(msg, max_sleep):
    for i in range(0, 10):
        num_sleep = randint(0, max_sleep)
        sleep(num_sleep)
        print(msg + "-" + str(i))


t1 = Thread(target=printer, args=("A", 1))
t2 = Thread(target=printer, args=("B", 8))
t3 = Thread(target=printer, args=("C", 3))
t4 = Thread(target=printer, args=("D", 10))
t5 = Thread(target=printer, args=("E", 13))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

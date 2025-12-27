from time import sleep
from threading import Thread, Condition, enumerate


class Pilha:
    def __init__(self):
        self._lista = []
        self.condition = Condition()

    def colocar(self, element):
        with self.condition:
            self._lista.append(element)
            self.condition.notify()

    def retirar(self):
        with self.condition:
            self.condition.wait()
            return self._lista.pop()

    def __len__(self):
        return len(self._lista)

    def esta_vazia(self):
        return self.__len__() == 0

    def top(self):
        if self.esta_vazia():
            return self.esta_vazia()
        else:
            return self._lista[-1]

    def __str__(self):
        return "Pilha:" + str(self._lista)

    def __iter__(self):
        return iter(self._lista)


def producer(pilha):
    for i in range(0, 6):
        data = "Task" + str(i)
        print("Producer colocando:", data)
        pilha.colocar(data)
        sleep(2)


def consumer(label, pilha):
    while True:
        print(label, "stack.retirar():", pilha.retirar())


if __name__ == "__main__":

    print("Criar pilha compartilhada")
    pilha = Pilha()
    print("Pilha:", pilha)

    print("Criando e iniciando threads consumidoras")
    c1 = Thread(target=consumer, args=("Consumer1", pilha))
    c2 = Thread(target=consumer, args=("Consumer2", pilha))
    c3 = Thread(target=consumer, args=("Consumer3", pilha))
    c1.start()
    c2.start()
    c3.start()

    print("Criando e iniciando thread produtora")
    p = Thread(target=producer, args=[pilha])
    p.start()

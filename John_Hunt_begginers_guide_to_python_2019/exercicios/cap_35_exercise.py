class Pilha:
    def __init__(self):
        self._lista = []

    def push(self, element):
        self._lista.append(element)

    def pop(self):
        return self._lista.pop()

    def __len__(self):
        return len(self._lista)

    def is_empty(self):
        return self.__len__() == 0

    def top(self):
        if self.is_empty():
            return self.is_empty()
        else:
            return self._lista[-1]

    def __str__(self):
        return "Pilha:" + str(self._lista)

    def __iter__(self):
        return iter(self._lista)


def is_job(frase: str):
    return frase.startswith("Job")


def add_item(element: str):
    return "item:" + element


stack = Pilha()
stack.push("Task1")
stack.push("Task2")
stack.push("Job1")
stack.push("Task3")
stack.push("Job2")
stack.push("Job3")
print("stack:", stack)
print("stack.is_empty():", stack.is_empty())
print("len(stack):", len(stack))
print("stack contents:", stack)
nova_lista = list(map(add_item, stack))
print("nova_lista:", nova_lista)

lista_filtrada = list(filter(is_job, stack))
print("lista_filtrada:", lista_filtrada)

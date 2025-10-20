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


stack = Pilha()
stack.push("T1")
stack.push("T2")
stack.push("T3")
print("stack:", stack)
print("stack.is_empty():", stack.is_empty())
print("len(stack):", len(stack))
print("stack.top():", stack.top())
print("stack.pop():", stack.pop())
print("stack:", stack)

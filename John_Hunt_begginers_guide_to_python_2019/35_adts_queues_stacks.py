# Capítulo 35 - ADT's, Queues e Stacks
# Há diversas estruturas de dados comuns que são usadas dentro de programas
# de computador que você poderia esperar ver dentro da lista de Python
# de coleções ou classes de armazenamento; elas incluem Queues e Stacks.
# Entretanto, nas classes de collection básicas eles estão ausentes.
# Podemos ou criar nossas próprias implementações ou usar uma das
# bibliotecas de extensão que fornecem tais coleções. Neste capítulo
# vamos explorar implementar nossas próprias versões.
# ------------------------------------------
# Tipos de dado abstrato (ADT, Abstract Data Types)
# Queue e Stack são exemplos concretos do que são conhecidos como
# tipos de dados abstratos.
# Um ADT é um modelo para um tipo de dado particular, onde um tipo de
# dado é definido por seu comportamento (ou semantica) do ponto de vista
# do usuário daquele tipo de dado. Este comportamento é tipicamente
# definido em termos de possíveis valores, possíveis operações nos dados
# desse tipo e comportamento das operações fornecidas pelo tipo de dado.
# Um ADT é usado para definir um conceito comum que pode ser implementado
# por uma ou mais estruturas de dados. Estas implementações podem usar
# representações internas diferentes do dado ou diferentes algoritmos para
# habilitar o comportamento; pela semântica eles cumprem as descrições
# fornecidas pelo ADT.
# Por exemplo, uma Lista ADT pode ser definida que define as operações
# e comportamento que uma estrutura similar a estrutura de dados similar
# a listas poderia fornecer. Implementações concretas podem cumprir
# a semantica de uma Lista usando um conjunto de elementos por trás, ou por
# juntar elementos com apontadores (pointers) ou usando algum tipo de
# tabela hash.
# -------------------------------------------
# Estruturas de dados
# Vamos olhar como os tipos coleção em Python podem ser usados como
# tanto Queue quanto Stack, mas primeiro precisamos definir estas
# duas ADT's:
#   *   Queue é uma ADT que define como uma coleção de entidades são
#           gerenciadas e mantidas. Queues tem o comportamento que é
#           conhecido como primeiro a entrar, primeiro a sair
#           (First-In-First-Out, FIFO) que é a primeira entidade
#           adicionada ao queue é a primeira coisa removida do queue.
#           Dentro do queue a ordem em que as entidades foram adicionadas
#           é mantida.
#   *   Stack é outra ADT mas desta vez tem um comportamento do tipo
#           último a entrar, primeiro a sair (Last-In-First_Out, LIFO).
#           Isto é, a última entidade adicionada à Stack será a próxima
#           a ser removida. Dentro da stack a ordem em que as entidades
#           foram adicionadas é mantida.
# --------------------------------------------
# Queues
# São amplamente usados em ciência computacional e engenharia de software.
# Permitem que dados sejam armazenados para processamento onde é garantido
# que os elementos adicionados mais cedo serão processados antes que os
# elementos adicionados mais tarde. Há diversas variações nas operações de
# queue básicas, mas, em essência, todos os queues fornecem os seguintes
# recursos:
#   * Criação de filas de espera(queue)
#   * Adicionar um elemento ao fim da lista de espera (conhecido como enqueuing)
#   * Remover um elemento da frente da lista de espera (conhecido como dequeuing)
#   * Encontrar o tamanho do Queue.
#   * Checar se a fila de espera está vazia.
#   * Queues podem ser de tamanho fixo ou variável.
# Muitos queues também permitem recursos como:
# * Olhar o elemento na frente da fila (isto é, ver qual é o elemento
#   mas não removê-lo)
# * Fornecer prioridades de forma que elementos com maiores prioridades não
#   são adicionados para o fim da fila mas a um ponto no meio da fila
#   relacionado com sua prioridade.
# ------------------------------------------
# Lista Python como Queue
# O container List de Python pode ser usado como uma fila usando as
# operações existentes como append() e pop(), por exemplo:
# queue = []  # Create an empty queue
# queue.append("task1")
# print("initial queue:", queue)
# queue.append("task2")
# queue.append("task3")
# print("queue after additions:", queue)
# element1 = queue.pop(0)
# print("element retrieved from queue:", element1)
# print("queue after removal", queue)
# Que retorna:
# initial queue: ['task1']
# queue after additions: ['task1', 'task2', 'task3']
# element retrieved from queue: task1
# queue after removal ['task2', 'task3']
# -----------------------------------------
# Definindo uma classe Fila(Queue)
# Apesar de usar uma lista como fila funcionar, não é óbvio que ela
# está sendo usada como tal(com exceção do nome da variável). Por exemplo,
# usamos pop(0) para remover o primeiro elemento, mas seria fácil de um
# desenvolvedor esquecer de colocar o argumento 0 e escrever pop(), removendo
# o último elemento adicionado.
# Podemos definir nossa própria classe Queue em Python:
class Queue:
    def __init__(self):
        self._list = []  # initial internal data

    def enqueue(self, element):
        self._list.append(element)

    def dequeue(self):
        return self._list.pop(0)

    def __len__(self):
        """Supports the len protocol"""
        return len(self._list)

    def is_empty(self):
        return self.__len__() == 0

    def peek(self):
        return self._list[0]

    def __str__(self):
        return "Queue: " + str(self._list)


# # O seguinte código ilustra a utilização da classe Queue:
# queue = Queue()
# print("queue.is_empty():", queue.is_empty())
# queue.enqueue("task1")
# print("len(queue):", len(queue))
# queue.enqueue("task2")
# queue.enqueue("task3")
# print("queue:", queue)
# print("queue.peek():", queue.peek())
# print("queue.dequeue():", queue.dequeue())
# print("queue:", queue)
# # Saída:
# queue.is_empty(): True
# len(queue): 1
# queue: Queue: ['task1', 'task2', 'task3']
# queue.peek(): task1
# queue.dequeue(): task1
# queue: Queue: ['task2', 'task3']
# Python possui uma classe container de fila no módulo collections
# chamada deque. A implementação é otimizada para ser mais eficiente
# que uma lista básica.
# ----------------------------------------
# Stacks(Pilhas)
# São outra ADT amplamente usada em ciência computacional e aplicações
# de software. São frequentemente usadas para avaliar expressões matemáticas,
# parse sintaxe, gerenciar resultados intermediários etc.
# A estrutura básica fornecida por uma pilha inclui:
#   * Criação de pilhas
#   * Adicionar um elemento ao topo da pilha (conhecido como empurrar em uma pilha)
#   * Remover um elemento do topo de uma pilha (conhecido como 'popping' da pilha)
#   * Descobrir o tamanho da pilha
#   * Checar se a pilha está vazia
#   * Pilhas podem geralmente ser de tamanho fixo ou variável.
# # Assim como filas, listas podem ser usadas como pilhas
# stack = []  # create an empty stack
# stack.append("task1")
# stack.append("task2")
# stack.append("task3")
# print("stack:", stack)
# top_element = stack.pop()
# print("top_element:", top_element)
# print("stack:", stack)
# # Com a saída:
# stack: ['task1', 'task2', 'task3']
# top_element: task3
# stack: ['task1', 'task2']

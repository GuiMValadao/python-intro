# Capítulo 32 - Sincronização Inter-Thread/Processo
# Neste capítulo vamos estudar diversos recursos das bibliotecas threading e
# multiprocessing que permitem sincronização e cooperação entre Threads ou Processos.
# A maioria das bibliotecas são espelhadas entre threading e multiprocessamento,
# mas não se deve misturar ambas abordagens. Se usar Threads, deve-se usar apenas
# recursos da biblioteca threading, e se usar Processes, apenas da multiprocessing.
# -----------------------------------------------
# Usando uma barreira
# Usar uma threading.Barrier (ou multiprocessing.Barrier) é uma das maneiras mais
# simples na qual a execução de um conjunto de Threads(ou Processes) pode ser
# sincronizada. As threads ou processos envolvidos na barreira são conhecidos como
# as partes (parties) que estão envolvidas na barreira. Cada uma das partes na
# barreira pode trabalhar independentemente até atingir o ponto da barreira no
# código. A barreira representa um ponto final que todas as partes devem atingir antes
# de qualquer comportamento subsequente se disparado. No ponto em que todas as
# partes atingem a barreira, é possível disparar opcionalmente uma ação pós-fase
# (também conhecida como barrier callback). Esta ação pós-fase representa algum
# comportamento que deveria ser executado quando todas as partes chegam à barreira
# mas antes de permitir que continuem. A ação pós-fase(callbak) executa em uma única
# thread(ou processo). Após completa, então todas as partes são desbloqueadas e
# podem continuar.
# Isto é ilustrado na figura barrier-callback.png. As threads t1, t2 e t3 estão envolvidas
# na barreira. Quando a thread t1 atinge a barreira, deve esperar até ser liberada
# por ela. De maneira similar, quando t2 atinge a barreira, também deve esperar.
# Após t3 chegar à barreira, a callbak é invocada. Após completa, a barreira libera
# todas as três threads que podem, então, continuar.
# Um exemplo de utilização do objeto Barrier é dado abaixo. Perceba que a função
# sendo invocada em cada Thread também deve cooperar na utilização da barreira como
# o código será executado até o método barrier.wait() e então esperará até que
# todas as outras threads tenham atingido este ponto antes de serem permitidas
# continuar.
# Barrier é uma classe que pode ser usada para criar um objeto barreira. Quando a
# classe Barrier é instanciada, pode receber três parâmetros onde:
#   * parties: número das partes individuais que participarão da barreira
#   * action: objeto chamável que, quando fornecido, será chamado após todas
#       as partes terem entrado na barreira e antes de liberá-las para continuar.
#   * timeout: Se fornecido, é usado como o padrão para todas as chamadas
#       subsequentes do método wait() na barreira.
# Por exemplo, a seguinte linha indica que haverão 3 partes envolvidas na barreira
# e que a função callback será invocada após as três chegarem nela:
# b = Barrier(3, action=callback)
# O objeto barreira é criado fora das Threads (ou Processes) mas deve estar
# disponível para a função sendo executada pela Thread (ou Process). O modo mais
# fácil de lidar com isso é passar a barreira à função como um dos parâmetros;
# isso significa que a função será usada com diferentes objetos barreira dependendo
# do contexto.
# Um exemplo da classe Barrier com um grupo de Threads é:
# from threading import Barrier, Thread
# from time import sleep
# from random import randint


# def print_it(msg, barrier):
#     print("print_it para:", msg)
#     for _ in range(0, 10):
#         print(msg, end="", flush=True)
#         sleep(1)
#     sleep(randint(1, 6))
#     print("\nEspera pela barreira com:", msg)
#     barrier.wait()
#     print("Retornando de print_it:", msg)


# def callback():
#     print("Callback executando")


# def main():
#     print("\nMain - Iniciando")
#     b = Barrier(3, callback)
#     t1 = Thread(target=print_it, args=("A", b))
#     t2 = Thread(target=print_it, args=("B", b))
#     t3 = Thread(target=print_it, args=("C", b))
#     t1.start()
#     t2.start()
#     t3.start()
#     print("\nMain - Terminado")


# if __name__ == "__main__":
#     main()

# A saída desse programa é:
# Main - Iniciando
# print_it para: A
# Aprint_it para: B
# Bprint_it para: C
# C
# Main - Terminado
# ABCABCABCABCABCABCABCBACBAC
# Espera pela barreira com: C

# Espera pela barreira com: A

# Espera pela barreira com: B
# Callback executando
# Retornando de print_it: B
# Retornando de print_it: A
# Retornando de print_it: C

# Disto, pode-se ver que print_it() é executa três vezes concorrentemente; todas
# as três invocações alcançam barrier.wait() mas em ordens diferentes da que
# iniciaram. Após atingirem a barreira, executa a função callback antes de
# permitir que print_it prossiga.
# A classe Barrier tem vários métodos usados para gerenciar ou descobrir informações
# sobre a barreira:

#   Método          |   Descrição
# wait(timeout=None)| Espera até todas as threads chegarem à barreira-retorna o número de threads que passaram a barreira
# reset()           | Retorna a barreira para seu estado padrão
# abort()           | Coloca a barreira em um estado quebrado
# parties           | Retorna o número de threads necessárias para passar a barreira
# n_waiting         | Número de threads concorrentes esperando

# Um objeto Barreira pode ser reutilizado qualquer número de vezes para o mesmo
# número de threads. O exemplo acima poderia facilmente ser alterado para executar
# usando Process alterando a declaração import e criando um conjunto de processos
# em vez de threads:
# from multiprocessing import Barrier, Process
# ...
# print('Main-Iniciando')
# b = Barrier(3, callback)
# t1 = Process(target=print_it, args=('A', b))
# -------------------------------------------------------------
# Sinalização de eventos
# Apesar do ponto de utilização de múltiplas Threads ou Processes ser executar
# operações separadas concorrentemente, às vezes pode ser importante ser capaz
# de permitir duas ou mais Threads ou Processes cooperem na temporização(timing)
# de seu comportamento. O objeto Barrier mostrado acima é um modo de nível relativamente
# alto para fazer isso; entretanto, em alguns casos precisa-se de um controle mais refinado.
# As classes threading.Event ou multiprocessing.Event podem ser usadas para isso.
# Um Event gerencia uma flag interna que chama ou set() ou clear(). Outras threads
# podem esperar (método wait()) para a flag ser definida (set()), efetivamente
# bloquando seu próprio progresso até permitida continuar pelo Event. A flag interna
# é inicialmente definida como False, que garante que se uma tarefa receber o
# Event antes dele ser definido(set), então deve esperar(wait).
# De fato, você pode invocar com um timeout opcional. Se não incluir o timeout,
# então wait() esperará para sempre enquanto wait(timeout) esperará até o timeout
# indicado em segundos. Se o timeout for atingido, então wait retorna False; se não,
# retorna True.
# Como exemplo, o diagrama da figura event.png ilustra dois processos compartilhando
# um objeto evento. O primeiro processo executa uma função que espera pelo evento ser
# definido(set). O segundo processo executa uma função que definirá o evento e assim
# liberará o processo em espera.
# O seguinte programa implementa esse cenário:
# from multiprocessing import Process, Event
# from time import sleep


# def wait_for_event(event):
#     print("wait_for_event - Entrou e esperando")
#     event_is_set = event.wait()
#     print("wait_for_event - Evento foi definido:", event_is_set)


# def set_event(event):
#     print("set_event - Entrou e está prestes a dormir")
#     sleep(5)
#     print("set_event - Acordando e definindo o evento")
#     event.set()
#     print("set_event - Evento definido")


# def main():
#     print("Iniciando")
#     event = Event()
#     p1 = Process(target=wait_for_event, args=[event])
#     p1.start()
#     p2 = Process(target=set_event, args=[event])
#     p2.start()
#     p1.join()
#     print("Terminado")


# if __name__ == "__main__":
#     main()

# Com a saída:
# Iniciando
# wait_for_event - Entrou e esperando
# set_event - Entrou e está prestes a dormir
# set_event - Acordando e definindo o evento
# set_event - Evento definido
# wait_for_event - Evento foi definido: True
# Terminado

# Para alterar isto para usar Threads, basta trocar o import e criar Threads em
# vez de Processes.

# ---------------------------------------------------
# Sincronizando código concorrente
# Não é incomum precisar garantir que regiões críticas do código estejam protegidas
# da execução concorrente por múltiplas Threads ou Processes. Estes blocos de código
# normalmente envolvem a modificação de, ou acesso a, dados compartilhados. Portanto,
# é necessário garantir que apenas uma Thread ou Process esteja atualizando um objeto
# compartilhado por vez e que threads ou processos consumidores sejam bloqueados
# enquanto esta atualização esteja ocorrendo.
# Esta situação é bastante comum onde uma ou mais Threads ou Processes são produtores
# de dados e uma ou mais Threads ou Processes são consumidores desses dados.
# Isto é ilustrado no diagrama da figura bloqueio-multiprocesso.png. Neste diagrama,
# o Producer está executando sua própria Thread e coloca dados em algum container
# de dados compartilhados. Subsequentemente, alguns consumidores independentes podem
# consumir aqueles dados quando estiver disponível e quando estiverem livres para
# processar os dados. Entretanto, não há razão para os consumidores checarem
# repetidamente o container por dados pois isso seria desperdício de recursos.
# Assim, precisamos de alguma forma de notificação ou sincronização entre
# o Produtor e Consumidor para cuidar dessa situação.
# Python tem várias classes nas bibliotecas threading e multiprocessing que podem
# ser usadas para gerenciar blocos de código críticos. Estas classes incluem
# Lock, Condition e Semaphore
# --------------------------------------------------
# Python Locks
# A classe Lock definida nas duas bibliotecas(threading e multiprocessing) fornece
# um mecanismo para sincronizar o acesso a um bloco de código. O objeto Lock pode
# estar em um dos dois estados: locked e unlocked(com o estado inicial sendo
# unlocked). Lock permite acesso a uma única thread por vez; outras threads devem
# esperar para que a Lock seja liberada antes de processarem.
# A classe Lock tem dois métodos básicos para obter a tranca(acquire()) e liberá-la
# (release()):
#   * Quando o estado do objeto Lock é destravado(unlocked), então acquire()
#       altera o estado para trancado (locked) e retorna imediatamente.
#   * Quando o estado é locked, acquire() bloqueia até uma chamada para release()
#       em outra thread altere seu estado para unlocked, então acquire muda para
#       locked e retorna.
#   * O método release() só deve ser chamado no estado locked; altera o estado para
#       unlocked e retorna imediatamente. Se é feita uma tentativa de destravar
#       uma trava já destravada, é levantado um RuntimeError.
# Um exemplo de utilização de um objeto Lock é mostrado abaixo:
# from threading import Thread, Lock


# class SharedData(object):
#     def __init__(self):
#         self.value = 0
#         self.lock = Lock()

#     def read_value(self):
#         try:
#             print("read_value acquiring Lock")
#             self.lock.acquire()
#             return self.value
#         finally:
#             print("read_value releasing Lock")
#             self.lock.release()

#     def change_value(self):
#         print("change_value acquiring lock")
#         with self.lock:
#             self.value = self.value + 1
#         print("change_value lock released")


# A classe SharedData usa travas para controlar o acesso a blocos de código críticos,
# em particular read_value() e change_value(). O objeto Lock é armazenado internamente
# ao objeto SharedData e ambos métodos tentam obter a trava antes de executar seu
# comportamento, mas devem, então, liberar a trava após o uso.
# O método read_value() faz isso explicitamente usando try:finally enquanto change_value()
# usa a declaração with (pois o tipo Lock suporta o Protocolo de Gerenciamento de Contexto).
# Ambas abordagens obtém o mesmo resultado, mas o estilo with é mais conciso.
# A classe SharedData é usada abaixo com duas funções simples. Neste caso, o objeto
# SharedData foi definido como uma variável global, mas também poderia ter sido
# passada às funções reader() e updater() como um argumento. Ambas as funções fazem
# um loop, tentando chamar read_value() e change_value() no objeto shared_data.

# from time import sleep

# shared_data = SharedData()


# def reader():
#     while True:
#         print(shared_data.read_value())


# def updater():
#     while True:
#         shared_data.change_value()


# def stopper():
#     while True:
#         if shared_data.value == 5:
#             break


# print("Iniciando")

# t1 = Thread(target=reader)
# t2 = Thread(target=updater)
# t1.start()
# t2.start()


# print("Terminado")


# Os objetos Lock podem ser obtidos apenas uma vez; se uma thread tentar
# obter uma trava no mesmo objeto Lock mais de uma vez, então um RuntimeError
# é lançado. Se for necessário readquirir um objeto Lock, então a classe
# threading.RLock deveria ser usada. Esta é uma trava re-entrant que permit
# que a mesma Thread aqduira uma trava múltiplas vezes. O código deve, entretanto,
# liberar as travas o mesmo número de vezes que as aquiriu
# ------------------------------------------------
# Python Conditions
# Conditions podem ser usadas para sincronizar a interação entre duas ou
# mais Threads ou Processes. Os objetos Condition suportam o conceito de um
# modelo de notificação; ideal para um recurso de dados compartilhados sendo
# acessados por múltiplos consumidores e produtores.
# Uma Condition pode ser usada para notificar uma ou todas as Threads em espera
# que elas podem procedes (por exemplo, para ler dados de um recurso compartilhado).
# Os métodos disponíveis que suportam isso são:
#   * notify(): notifica uma thread em espera que então pode continuar
#   * notify_all(): notifica todas as threads em espera que podem continuar.
#   * wait(): faz com que um thread espere até ser notificada que pode continuar.
# Uma Condition é sempre associada com uma trava interna que deve ser adquirida
# e liberada antes dos métodos wait() e notify() sejam chamados. A Condition
# suporta o Protocolo Gerenciador de Contexto e pode ser usada com uma
# declaração with para obter esta trava. Por exemplo, para obter a trava
# de condição e chamar o método wait poderia-se escrever:
# with condition:
#   condition.wait()
#   print('Agora pode continuar')
#
# O objeto condição é usado no seguinte exemplo para ilustrar como uma
# thread produtora e duas consumidoras podem cooperar. Uma classe DataResource
# foi definida que guardará um item de dado que será compartilhado entre um
# consumidor e um conjunto de produtores. Também define um atributo Condition.
# Note que isto significa que a Condition está completamente internalizada
# à classe DataResource; código externo não precisa saber ou se preocupar
# com a Condition e seu uso. Em vez disso, o código externo pode simplesmente
# chamar as funções consumer() e producer() em Threads separadas se preciso.
# O método consumer() usa uma declaração with para obter a trava (interna)
# no objeto Condition antes de esperar ser notificado que o dado está disponível.
# Por sua vez, o método producer() também usa uma declaração with para obter
# uma trava no objeto Condition antes de gerar o valor do atributo dado
# e então notificar tudo que esteja esperando que podem proceder. Perceba
# que, apesar do método consumidor obter a trava no objeto condição, se tem
# que esperar, liberará a trava e a reobterá quando for notificado que pode
# continuar. Isto é uma sutileza que costuma passar despercebida.

# from threading import Thread, Condition, current_thread
# from time import sleep
# from random import randint


# class DataResource:
#     def __init__(self):
#         print("DataResource - Inicializando o dado vazio")
#         self.data = None
#         print("DataResource - Preparando o objeto Condition")
#         self.condition = Condition()

#     def consumer(self):
#         print("DataResource - Iniciando método consumidor em:", current_thread().name)
#         with self.condition:
#             self.condition.wait()
#             print("DataResource - Recurso está disponível para", current_thread().name)
#             print("DataResource - Dado lido em", current_thread().name, ":", self.data)

#     def producer(self):
#         print("DataResource - Iniciando método produtor")
#         with self.condition:
#             print("DataResource - Produtor preparando o dado")
#             self.data = randint(1, 100)
#             print("DataResource - Produtor notificando todas as threads em espera")
#             self.condition.notify_all()


# print("Main - Iniciando")
# print("Main - Criando o objeto DataResource")
# resource = DataResource()
# print("Main - Criando Threads cosumidoras")
# c1 = Thread(target=resource.consumer)
# c1.name = "Consumer1"
# c2 = Thread(target=resource.consumer)
# c2.name = "Consumer2"
# print("Main - Criando Thread produtora")
# p = Thread(target=resource.producer)

# print("Main - Iniciando threads consumidoras")
# c1.start()
# c2.start()
# sleep(1)
# print("Main - Iniciando thread produtora")
# p.start()
# print("Main - Terminada")

# -----------------------------------------------------
# Python Semaphores
# A classe Semaphore em Python implementa o modelo de contagem de semáforo
# de Dijkstra. Em geral, um semáforo é como uma variável inteira, com
# seu valor representando um número de recursos disponíveis de algum tipo.
# Existem normalmente duas operações em um semáforo: acquire() e release()
# (apesar de algumas bibliotecas os nomes originais de Dijkstra p() e v()
# são usados).
#   * A operação acquire() subtrai um do valor do semáforo, a menos que o
#       valor seja 0, quando bloqueia a thread chamando até o valor aumentar
#       acima de 0 novamente.
#   * A operação signal() acrescenta um ao valor, indicando que uma nova
#       instância do recurso foi acrescentada à pool.
# Ambas as classes threading.Semaphore e multiprocessing.Semaphore suportam
# o Protocolo de Gerenciamento de Contexto. Um parâmetro opcional usado
# com o construtor do Semaphore dá o valor inicial para o contador interno;
# o padrão é 1. Se o valor dado é menor que 1, ValueError é levantado.
# O seguinte exemplo ilustra 5 Threads diferentes executando a mesma
# função worker(). Essa função tenta adquirir um semáforo; se consegue,
# continua dentro do bloco with; se não, espera até poder adquirí-lo. Como
# o semáforo é inicializado com 2, podem haver apenas duas threads que podem
# adquirir o Semaphore por vez.
# from threading import Thread, Semaphore, current_thread
# from time import sleep


# def worker(semaphore):
#     with semaphore:
#         print(current_thread().name + " - entrou")
#         sleep(0.5)
#         print(current_thread().name + " - saindo")


# print("MainThread - Iniciando")

# semaphore = Semaphore(2)
# for i in range(0, 5):
#     thread = Thread(name="T" + str(i), target=worker, args=[semaphore])
#     thread.start()
# print("MainThread - Terminado")

# Que exibe:
# MainThread - Iniciando
# T0 - entrou
# T1 - entrou
# MainThread - Terminado
# T0 - saindo
# T2 - entrou
# T1 - saindo
# T3 - entrou
# T2 - saindo
# T4 - entrou
# T3 - saindo
# T4 - saindo

# -----------------------------------------------
# A classe concorrente Queue
# Como poderia-se esperar o modelo onde uma Thread ou Process produtor
# gera dados para serem processados por um ou mais Threads ou Processes
# consumidores é tão comum que um nivel de abstração maior é dado em Python
# que o uso de Locks, Conditions e Semaphores; este é o modelo de fila
# bloquadora implementado pelas classes threading.Queue ou multiprocessing.Queue.
# Ambas as classes Queue são seguras para Thread e Process. Isto é, elas
# trabalham apropriadamente (usando travas internas) para gerencias o acesso
# a dados de Threads e Processos concorrentes.
# Um exemplo da utilização de um Queue para trocar dados entre um processo
# worker e o processo principal é mostrado abaixo.
# O processo worker executa a função worker() dormindo, por 2 s, antes de
# exibir a string 'Hello World' na fila. A aplicação principal prepara a
# fila e cria o processo. A fila é passada para o processo como um de seus
# argumentos. O processo é, então, iniciado. O processo principal espera
# até que dados estejam disponíveis na fila pelos métodos bloqueadores get().
# Quando disponíveis, os dados são pegos e exibidos antes do final do processo
# principal.
# from multiprocessing import Process, Queue
# from time import sleep


# def worker(queue):
#     print("Worker - indo dormir")
#     sleep(2)
#     print("Worker - acordou e colocando dados na fila")
#     queue.put("Hello World")


# def main():
#     print("Main - iniciando")
#     queue = Queue()
#     p = Process(target=worker, args=[queue])
#     print("Main - Iniciando o processo")
#     p.start()
#     print("Main - esperando por dados")
#     print(queue.get())
#     print("Main - Terminado")


# if __name__ == "__main__":
#     main()

# A saída é:
# Main - iniciando
# Main - Iniciando o processo
# Main - esperando por dados
# Worker - indo dormir
# Worker - acordou e colocando dados na fila
# Hello World
# Main - Terminado
#
# Entretanto, isto não deixa claro como a execução dos dois processos
# se interliga. O diagrama queue.png ilustra isso graficamente. Nesse
# diagrama, o processo principal espera que um resultado seja retornado
# do queue após a chamada para o método get(); como está esperando, não
# está usando qualquer recurso do sistema. Por sua vez, o processo worker
# dorme por dois segundos antes de colocar algum dado na fila. Depois
# deste valor ser enviado para o Queue, o valor é retornado para o processo
# principal que é acordado (retirado do estado de espera) e pode continuar
# a processar o resto da função main().

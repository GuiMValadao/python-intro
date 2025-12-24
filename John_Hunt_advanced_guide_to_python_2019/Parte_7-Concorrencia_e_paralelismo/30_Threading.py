# Capítulo 30 - Threading


# Threading é uma das maneiras com que Pyhton permite a escrita de programas
# que execultam multitarefas; isto é, parecem fazer mais de uma coisa por vez.
# Threads
# Em Python, a classe Thread do módulo threading representa uma atividade que
# é executada em uma thread de execução separada dentro de um único processo.
# Estas threads de execução são leves e preventivas. Como comentado no capítulo
# anterior, uma thread é leve por não ocupar um endereço de espaço, não sendo
# tratada como uma entidade separada pelo sistema operacional; não é um processo.
# Em vez disso, existe dentro de um único processo da máquina usando o mesmo
# endereço de espaço que outras threads.
# ------------------------------------------------------------------
# Estados de Thread
# Quando um objeto Thread é criado pela primeira vez, ele existe mas ainda não
# é executável; precisa ser iniciado. Após iniciado, então torna-se executável,
# ou seja, disponível para ser agendado(escalonado) para execução. Pode, então, trocar entre
# estar executando e ficar executável sob controle do escalonador (scheduler).
# O escalonador é responsável por gerenciar múltiplas threads onde todas querem
# pegar algum tempo de execução.
# Um objeto thread permanece executável ou executando até seu método run() terminar;
# neste ponto, finalizaou sua execução e então está morta. Todos os estados
# entre não-iniciada e morta são considerados para indicar que a Thread está viva
# (e, portanto, pode executar em algum momento). Isto é mostrado na imagem thread.png.
# Uma Thread também pode estar no estado de espera; por exemplo, quando está
# esperando por outra thread terminar seu trabalho antes de continuar (possivelmente
# por precisar de resultados produzidos pela outra thread para continuar).
# Isto pode ser alcançado usando o método join() e também ilustrado na imagem
# threads.png. Após a segunda thread completar, a thread em espera tornará-se
# executável novamente.
# A thread sendo executada é chamada thread ativa. Há alguns pontos de nota sobre
# os estados das threads:
#   * É considerada viva a menos que o método run() termine, quando torna-se morta.
#   * Uma thread viva pode estar executando, executável, esperando etc.
#   * O estado executável indica que a thread pode ser executada pelo processador
#       mas não está em execução. Isto pode ocorrer caso um processo de prioridade
#       equivalente ou maior já estiver em execução, e a thread deve esperar até
#       o processador tornar-se livre. Assim, o diagrama mostra que o escalonador
#       pode mover uma thread entre os estados executando e executável. De fato,
#       isto pode acontecer muitas vezes com a thread executando por um período,
#       é então removida do processador pelo escalonador e adicionada à fila de
#       espera, antes de retornar ao processador novamente em um período posterior.
# ---------------------------------------------------------
# Criando uma Thread
# Há duas formas de iniciar uma nova thread de execução:
#   * Passar uma referência a um objeto chamável (como uma função ou método)
#       para o construtor da classe Thread. Esta referência age como o alvo para
#       a Thread executar.
#   * Criar subclasses da classe Thread e redefinir o método run() para realizar
#       o conjunto de ações que a thread tem como objetivo.
# Como uma thread é um objeto, pode ser tratada como qualquer outro objeto:
# pode ser enviada mensagens, pode ter variáveis de instância e pode fornecer
# métodos. Assim, todos os aspectos de multi-threads de Python concordam com
# o modelo orientado a objetos. Isto simplifica bastante a criação de sistemas
# multi-threads assim como a manutenção e clareza do software resultante.
# Assim que uma nova instância da thread é criada, deve ser iniciada. Antes
# de ser iniciada, não pode executar, apesar de existir.
# ---------------------------------------------
# Instanciando a classe Thread
# A classe Thread é encontrada no módulo threading e, portanto, deve ser
# importada antes do uso. Essa classe define um único construtor que pega até
# seis argumentos opcionais:

#   class threading.Thread(group=None,target=None,name=None,args=(),kwargs={},daemon=None)

# O construtor da Thread deve sempre ser chamado usando argumentos de palavra
# chave; o significado desses argumentos é:
#   * group: deveria ser None; reservado para extensão futura quando uma classe
#       ThreadGroup é implementada.
#   * target: é o objeto chamável a ser invocado pelo método run(). É None pode padrão,
#       dizendo que nada é chamado.
#   * name: nome da Thread. Por padrão, um nome único é construído da forma
#       "Thread-N" onde N é um número inteiro.
#   * args: é a tupla de argumentos para a invocação do alvo. Por padrão é ().
#       Se um único argumento é fornecido, a tupla não é obrigatória. Se
#       múltiplos argumentos, então cada argumento é um elemento dentro da tupla.
#   * kwargs: é um dicionário de argumentos de palavra chave para a invocação do
#       alvo. Por padrão, é {}.
#   * daemon: indica se a thread executa como uma thread daemon ou não. Se não
#       for None, daemon define explicitamente se a thread é daemonic. Se None
#       (o padrão), a propriedade daemonic é herdada da thread atual,
# Após criada, a Thread deve ser iniciada para tornar-se disponível para execução
# usando o método Thread.start(). O seguinte ilustra um programa simples que cria uma
# Thread que executará a função simple_worker():


# from threading import Thread


# def simple_worker():
#     print("hello")

# t1 = Thread(target=simple_worker)
# t1.start()


# Neste exemplo, a thread t1 executará a função simple-worker. O código principal
# será executado pela thread principal que está presente quando o programa inicia;
# portanto, existem duas threads usadas no programa acima: a principal(main) e t1.
#
# ------------------------------------------------------
# A classe Thread
# A classe Thread define todos os recursos necessários para criar um objeto que
# pode executar dentro de seu processo leve. Os métodos principais são:
#   * start(): inicia a atividade da thread. Deve ser chamado no máximo uma vez
#       por objeto thread. Ele arranja que o método run() do objeto seja invocado
#       em um controle de thread separado. Este método gerará um RuntimeError se
#       chamado mais de uma vez por objeto thread.
#   * run(): método representando a atividade da thread. Você pode sobrescrever
#       este método em uam subclasse. O método padrão run() invoca o objeto
#       chamável passado ao construtor como argumento target, se houver, com
#       argumentos posicionais e de palavra chave pegos dos argumentos args e
#       kwargs, respectivamente. Você não deve chamar este método diretamente.
#   * join(timeout=None): espera até a thread que recebeu essa mensagem termine.
#       Isto bloqueia a thread chamando até que a thread cujo método join() foi
#       chamado termina. Quando o argumento timeout está presenta e não é None,
#       deveria ser um número real(floating-point) especificando um timeout para
#       a operação em segundos (ou frações de segundos). Uma thread pode ser
#       join()ed muitas vezes.
#   * name: uma string usada apenas para propósito de identificação. Não possui
#       semântica. Múltiplas threads podem receber o mesmo nome. O nome inicial
#       é definido pelo construtor. Dar um nome a uma thread pode ser útil para
#       o propósito de debug.
#   * ident: O 'identificador da thread' desta thread ou None se a thread não
#       foi iniciada. É um número inteiro e não-zero.
#   * is_alive(): Retorna se a thread está viva. Este método retorna True logo antes
#       do método run() iniciar até logo após o método run() terminar. A função
#       do módulo threading.enumerate() retorna uma lista de todas as threads vivas.
#   * daemon: Um valor booleano indicando se esta thread é uma thread daemon(True)
#       ou não(False). Isto deve ser definido antes de start() ser chamado, caso
#       contrário será levantado um RuntimeError. Seu valor padrão é herdado da
#       thread criadora. O programa Python inteiro sai quando nenhuma thread viva
#       sem daemon está restando.
# Um exemplo ilustrando alguns desses métodos é dado abaixo:

# from threading import Thread


# def simple_worker():
#     print("hello")


# t1 = Thread(target=simple_worker)
# print("Antes do inicio: thread is_alive?:", t1.is_alive())
# t1.start()
# print("Logo após o inicio: thread is_alive?:", t1.is_alive())
# print(t1.name)  # No livro é usado getName(), que não é mais usado desde Python 3.10
# print(t1.ident)
# print("Antes do final do programa: thread is_alive?:", t1.is_alive())


# Isto retorna:
# Antes inicio: thread is_alive?: False
# hello
# Logo após inicio: thread is_alive?: True
# Thread-1 (simple_worker)
# 23744
# Antes do final do programa: thread is_alive?: False

# O método join() pode causar que uma thread espere que outra complete.
# Por exemplo, se queremos que a thread principal espere até uma thread complete
# antes de exibir a mensagem 'pronto', podemos usar join() com aquela thread:

# from threading import Thread
# from time import sleep


# def worker():
#     for i in range(0, 10):
#         print(".", end="", flush=True)
#         sleep(1)


# print("Iniciando")
# t = Thread(target=worker)
# t.start()
# t.join()
# print("\nPronto.")

# Esse código retorna:
# Iniciando
# ..........
# Pronto.

# ----------------------------------
# Funções do módulo threading
# Existem um conjunto de funções do módulo threading que ajudam no trabalho com
# threads; são elas:
#   * threading.active_count(): Retorna o número de objetos Thread atualmente
#       vivos. A contagem retornada é igual ao tamanho da lista retornada por enumerate().
#   * threading.current_thread(): Retorna o objeto Thread atual, correspondendo
#       à thread de controle do que chamou. Se a thread de controle do chamador
#       não foi criada através d módulo threading, um objeto simulado com funcionalidades
#       limitadas é retornado.
#   * threading.get_ident(): Retorna o identificador da thread atual. É um inteiro não-zero.
#       Identificadores de threads podem ser reciclados quando uma thread sai e outra é criada.
#   * threading.enumerate(): retorna uma lista de todos os objetos Thread atualmente
#       vivos. A lista inclui threads daemon, objetos thread simulados criados
#       pelo current_thread() e a thread principal(main). Exclui threads terminadas
#       e threads que ainda não foram inicidas.
#   * threading.main_thread(): retorna o objeto Thread principal.
# -----------------------------------------------
# Passando argumentos a uma Thread
# Muitas funções esperam receber um conjunto de valores para parâmetros quando
# são executadas; estes argumentos ainda precisam ser passados à função quando
# são executadas por uma thread separada. Estes parâmetros podem ser passados
# à função pelo parâmetro args, por exemplo:


# from threading import Thread
# from time import sleep


# def worker(msg):
#     for i in range(0, 10):
#         print(msg, end="", flush=True)
#         sleep(1)


# print("Iniciando")
# t1 = Thread(target=worker, args="A")
# t2 = Thread(target=worker, args="B")
# t3 = Thread(target=worker, args="C")
# t1.start()
# t2.start()
# t3.start()

# print("Terminado.")

# A saída é:
# Iniciando
# ABCTerminado.
# ABCABCABCACBABCACBABCBCAACB

# Neste exemplo, a função worker pega uma mensagem a ser exibida 10 vezes dentro
# de um loop. Dentro do loop, a thread exibirá a mensagem e então dormirá por 1
# segundo. Isto permite que outras threads sejam executadas como a Thread deve
# esperar pelo final da função sleep antes de tornar-se executável novamente.
# Três threads t1, t2 e t3 são criadas, cada uma com uma mensagem diferente.
# Note que a função worker() pode ser reutilizada com cada Thread pois cada
# invocação da função terá seus próprios valores para os parâmetros passados.
# As três threads são, então, iniciadas. Isto significa que neste ponto, existe
# a thread principal, e três threads de worker que são executáveis (Sendo que
# apenas uma é executável da cada vez). As três threads executam a função worker()
# exibindo a letra A, B ou C dez vezes. Isto significa que, após iniciada, cada thread
# exibirá uma string, dormirá por 1 segundo e esperará até ser selecionada para
# execução novamente, isto é ilustrado no diagrama thread_params.png.
# Note que a thread principal termina após as threads de worker terem sido exibidas
# apenas uma única vez cada; entretanto, enquanto existe pelo menos uma thread
# não-daemon executando, o programa não terminará; como nenhuma dessas threads
# são marcadas como daemon, o programa continua até o final de execução da última
# thread(após a exibição das 10 letras de todas as 3 threads).
# Também pode-se observar como as threads tem a chance de executar no processador
# antes de dormirem novamente; assim, pode-se ver que a ordem de ABC pode ser alterada.
# -------------------------------------------------------
# Estendendo a classe Thread
# A segunda abordagem mencionada anteriormente é usar uma subclasse de Thread.
# Pra fazer isso é necessário:
#   1. Definir uma nova subclasse de Thread
#   2. Sobrescrever o método run()
#   3. Definir um novo método __init__() que chama o método construtor da classe
#       pai para passar os parâmetros necessários para o construtor de classe de Thread.
# Isto é ilustrado abaixo onde a classe WorkerThread passa name, target e daemon
# para o construtor da superclasse Thread.
# from threading import Thread
# from time import sleep


# class WorkerThread(Thread):
#     def __init__(self, daemon=None, target=None, name=None):
#         super().__init__(daemon=daemon, target=target, name=name)

#     def run(self):
#         for _ in range(0, 10):
#             print(".", end="", flush=True)
#             sleep(1)


# print("Iniciando")
# t = WorkerThread()
# t.start()
# # t.join()  # Descomentando essa linha, todos os pontos são mostrados antes de executar a linha seguinte.
# print("\nTerminado")

# Esse código retorna:
# Iniciando
# .
# Terminado
# .........

# ---------------------------------------------
# Daemon Threads
# Uma thread pode ser marcada como uma thread daemon definindo a propriedade
# daemon para True ou no construtor ou posteriormente pela propriedade acessório.
# Por exemplo:
# from threading import Thread
# from time import sleep


# def worker(msg):
#     for _ in range(0, 10):
#         print(msg, end="", flush=True)
#         sleep(1)


# print("Iniciando")
# d = Thread(daemon=True, target=worker, args="C")
# d.start()
# sleep(5)
# print("Terminado")

# Isto exibe:
# Iniciando
# CCCCCTerminado
# Isto cria uma thread daemon de fundo que executará a função worker(). Tais
# threads são frequentemente usadas para tarefa de organização (housekeeping)
# (como backups de dados de fundo etc).
# Como mencionado acima, uma thread daemon não é suficiente, por si só, para
# evitar o término do programa atual. Isto significa que a thread daemon continuará
# o loop até a thread principal terminar. Como a thread principal dorme por 5s,
# isto permite que a thread daemon exiba 5 strings antes do término da thread
# principal e, consequentemente, do programa.
# ----------------------------------------------
# Nomeando threads
# Threads podem ser nomeadas, o que pode ser bem útil para fazer debug de uma
# aplicação com múltiplas threads. No exemplo seguinte, três threads foram
# criadas; duas foram dadas um nome explicitamente relacionado com o que elas
# estão fazendo enquando a do meio foi deixada com o nome padrão. Então começamos
# todas as três threads e usamos a função threading.enumerate() para fazer um loop
# por todas as threads atualmente vivas, exibindo seus nomes:
# import threading
# from threading import Thread
# from time import sleep


# def worker(msg):
#     for _ in range(0, 10):
#         print(msg, end="", flush=True)
#         sleep(1)


# t1 = Thread(name="worker", target=worker, args="A")
# t2 = Thread(target=worker, args="B")  # usa o nome padrão, Thread-1
# d = Thread(daemon=True, name="daemon", target=worker, args="C")
# t1.start()
# t2.start()
# d.start()

# print()
# for t in threading.enumerate():
#     print(t.name)

# A saída desse programa é:
# ABC
# MainThread
# worker
# Thread-1 (worker)
# daemon
# ABCABCABCCABACBACBACBACBCAB

# --------------------------------------
# Dados locais de thread
# Em algumas situações, cada Thread requer sua própria cópia dos dados com que
# está trabalhando; isto significa que a memória compartilhada(heap) é difícil
# de usar pois é, inerentemente, compartilhada entre todas as threads.
# Para superar isso, Python tem um conceito conhecido como dados locais da Thread(Thread-Local data).
# Thread-local data são dados cujos valores estão associados com uma thread em
# vez da memória principal. Esta ideia é ilustrada na imagem thread_local.png.
# Para criar dados locais da thread é apenas necessário criar uma instância de
# threading.local(ou uma subclasse disso) e armazenar atributos nela. As instâncias
# serão específicas da thread; ou seja, outras threads não verão valores
# armazenados por uma thread. Por exemplo:

# from threading import Thread, local, current_thread
# from random import randint


# def show_value(data):
#     try:
#         val = data.value
#     except AttributeError:
#         print(current_thread().name, " - Nenhum valor ainda")
#     else:
#         print(current_thread().name, " - valor =", val)


# def worker(data):
#     show_value(data)
#     data.value = randint(1, 100)
#     show_value(data)


# print(current_thread().name, " - Iniciando")
# local_data = local()
# show_value(local_data)
# for i in range(2):
#     t = Thread(name="W" + str(i), target=worker, args=[local_data])
#     t.start()


# show_value(local_data)
# print(current_thread().name, " - Terminado")

# Isso exibe:

# MainThread  - Iniciando
# MainThread  - Nenhum valor ainda
# W0  - Nenhum valor ainda
# W0  - valor = 50
# W1  - Nenhum valor ainda
# MainThread  - Nenhum valor ainda
# W1  - valor = 17
# MainThread  - Terminado

# Esse exemplo define duas funções:
#   * A primeira função tenta acessar um valor no objeto de dado local da thread.
#       Se o valor não está presente, uma exceção é levantada (AttributeError).
#       A função show_value() pega a exceção ou processa com sucesso o dado.
#   * A função worker chama show_value() duas vezes, uma vez antes de definir um
#       valor no objeto de dado local e a outra depois. Como essa função será
#       executada por threads separadas, o nome da thread atual é exibido pela
#       função show_value().
# A função principal cria um objeto de dado local usando a função local() da
# biblioteca threading. Então chama show_value(). Em seguinda, cria duas threads
# para executar a função worker passando o objeto local_data para elas; cada
# thread então é iniciada. Por fim, chama show_value novamente.
# Como pode ser ver da saída, uma thread não vê o dado definido para a outra thread
# no objeto local_data(mesmo quando o nome do atributo é o mesmo).
# -----------------------------------------
# Cronômetros/Temporizadores (Timers)
# A classe Timer representa uma ação (ou tarefa) a ser executada após alguma
# quantidade de tempo passar. Ela é subclasse de Thread e assim também funciona
# como um exemplo da criação de threads customizadas.
# Cronômetros podem ser iniciados, assim como threads, chamando o método start().
# O cronômetro pode ser parado (antes de sua ação iniciar) chamando o método
# cancel(). O intervalo que o cronômetro esperará antes de executar sua ação
# pode são ser exatamente o mesmo que o especificado pelo usuário pois outra
# thread pode estar executando quando o cronômetro quiser iniciar.
# A assinatura do construtor da classe Timer é:
# Timer(interval, function, args=None, kwargs=None)
# Um exemplo de utilização da classe Timer é dado abaixo:
from threading import Timer


def hello():
    print("hello")


print("iniciando")
t = Timer(5, hello)
t.start()
print("Terminado")

# Assim, o Timer executará a função hello() após um atraso de 5 s.
# iniciando
# Terminado
# hello
# --------------------------------------
# A trava do interpretador global
# A Trava do Interpretador Global(GIL-Global Interpreter Lock) é uma trava global
# dentro do interpretador CPython que foi criada para evitar potenciais impasses
# entre múltiplas tarefas. É projetada para proteger acesso a objetos Python prevenindo
# que múltiplas threads executem ao mesmo tempo.
# Para a maior parte, não é necessário preocupar-se com a GIL pois é de menor nível
# que os programas que você estará escrevendo. Entretanto, é digno de nota que
# a GIL é controversa pois previne que programas de Python com múltiplas Threads
# tirem vantagem completa do sistema de multiprocessadores em certas situações.
# Isto ocorre pois para poder executar uma thread, é necessário obter o GIL e
# apenas uma thread por vez pode ter o GIL. Isto significa que Python age como
# uma máquina de uma única CPI; apenas uma coisa pode executar por vez. Uma Thread
# apenas dará o GIL se dormir, tiver de esperar por alguma coisa(como I/O) ou
# segurou o GIL por uma certa quantidade de tempo. Se o tempo máximo que uma thread
# pode segurar o GIL foi atingido, o escalonador liberará o GIL daquela thread
# (resultando na interrupção da execução e agora tendo que esperar até ter o
# GIL retornado a ela) e selecionará outra thread para obter o GIL e iniciar
# execução. Portanto, é impossível para threads padrão em Python aproveitar
# múltiplas CPUs tipicamente disponíveis no hardware moderno de computadores.
# Uma solução é usar a biblioteca de Python multiprocessing descrita no próximo capítulo.

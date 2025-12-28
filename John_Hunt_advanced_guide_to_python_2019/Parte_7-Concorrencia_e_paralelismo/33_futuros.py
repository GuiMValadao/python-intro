# Capítulo 33 - Futuros
# Um futuro é uma thread (ou processo) que promete retornar um valor no futuro,
# após o comportamento associado ser completo. Assim, tem um valor futuro.
# Fornece um modo muito simples de disparar comportamento que ou será demorado
# de executar ou pode ser atrasado devido a operações caras como I/O e que
# poderiam atrasar a execução de outros elementos de um programa.
# ---------------------------------------------
# A necessidade de um futuro
# Na invocação normal de um método ou função, ele é executado na linha com
# o código invocador (caller), tendo que esperar até que a função ou método
# (calee) retorne. Apenas após isto, o invocador pode continuar a próxima
# linha de código e executá-la. Em muitas(maioria) situações, isto é exatamente
# o que você quer pois a próxima linha de código pode depender de um resultado
# retornado da linha anterior.
# Entretanto, em algumas situações, a próxima linha de código é independente
# da linha anterior. Por exemplo,suponha que estamos preenchendo uma UI. A
# primeira linha de código pode ler o nome do usuário de alguma fonte de
# dados externa (como uma base de dados) e então exibí-lo dentro de um
# campo na UI. A próxima linha pode, então, acrescentar a data de hoje a
# outro campo da UI. Essas duas linhas são independentes entre si e poderiam
# ser executadas concorrentemente/em paralelo. Nesta situação, poderíamos
# usar uma Thread ou um Process para executar as duas independentemente,
# conseguindo assim um nível de concorrência e permitindo ao chamador
# que siga para a terceira linha do código etc.
# Entretanto, nem Thread nem Process, por padrão, possuem um mecanismo
# simples para obter um resultado de tais operações independentes. Isto
# pode não ser um problema pois operações podem ser auto-contidas; por
# exemplo, podem obter dados da base de dados ou da data de hoje e então
# atualizar a UI. Entretanto, em várias situações, o cálculo retornará um
# resultado que precisa ser manipulado pelo código invocador original. Isto
# poderia envolver a realização de um cálculo de longa execução e então
# usar o resultado retornado para gerar outro valor ou atualizar outro objeto
# etc.
# Um futuro é uma abstração que simplifica a execução de tais tarefas
# concorrentes. Eles estão disponíveis em várias linguagens diferentes
# incluindo Python, Java, Scala, C++ etc. Quando usar um Future, um objeto
# chamável (como uma função) é passado ao Future que executa o comportamento
# ou como uma Thread separada ou Processo separado e então retorna o resultado
# quando gerado. O resultado pode ser manipulado por uma função de callback
# (invocada quando o resultado estiver disponível) ou usando uma operação
# que esperará pelo resultado.
# -------------------------------------------------
# Futuros em Python
# A biblioteca concurrent.futures foi introduzida ao Python na versão 3.2.
# Ela fornece a classe Future e uma API de alto nível para trabalhar com
# futuros.
# A classe concurrent.futures.Future encapsula a execução assíncrona de um
# objeto chamável(uma função ou método). Essa classe tem vários métodos
# que podem ser usados para obter informação sobre o estado do futuro, receber
# resultados ou cancelar o futuro:
#   * cancel(): Tenta cancelar o Future. Se Future estiver sendo executado
#       e não puder ser cancelado, então retornará False, se não retornará True.
#   * cancelled(): Retorna True se o Future foi cancelado com sucesso.
#   * running(): Retorna True se o Future estiver em execução e não puder ser cancelado.
#   * done(): Retorna True se o Future  foi cancelado com sucesso ou terminou de executar.
#   * result(timeout=None): Retorna o valor retornado pelo Future. Se ainda
#       não completou, este método esperará até 'timeout' segundos. Se a chamada
#       não foi completa dentro do timeout, então levantará TimeoutError.
#       O timeout pode ser um inteiro ou um float. Se não for especificado
#       ou for None, não terá limite no tempo de espera. Se o Future foi
#       cancelado antes de completar, então levantará CancelledError.
#       Se a chamada levantar um erro, este método levantará a mesma exceção.
# Deve-se notar que instâncias de Future não deveriam ser criadas diretamente,
# mas pelo método submit de um executor apropriado.
# -------------------------------------------------
# Criação de futuro
# Futures podem ser criados e executados por Executores. Um Executor fornece
# dois métodos que podem ser usados para executar um Future e um para
# desligar o executor. Na raiz da hierarquia de classe dos executores está
# a classe abstrata concurrent.futures.Executor. Ela tem duas subclasses:
#   ThreadPoolExecutor;
#   ProcessPoolExecutor.
# De acordo com seus nomes, a primeira usa threads para executar os futuros
# enquanto a outra usa processos separados.
# -----------------------------------------------------
# Exemplo simples de Future
# Para ilustrar essas ideias, olharemos um exemplo prático. Para isso, vamos
# usar uma função simples worker, parecida com a usada em capítulos anteriores.
from time import sleep


def worker(msg):
    for i in range(0, 10):
        print(msg, end="", flush=True)
        sleep(1)
    return i


# A única diferença dessa versão é que ela retorna um resultado que é o número
# de vezes que a função exibiu a mensagem.
# Podemos tornar a invocação dessa função em um Future. Para isso, usamos
# uma ThreadPoolExecutor importada do módulo concurrent.futures. Então
# submetemos a função worker à pool para execução. Isto retorna uma referência
# ao Future que podemos usar para pegar o resultado:

# from concurrent.futures import ThreadPoolExecutor

# print("Preparando a ThreadPoolExecutor")

# pool = ThreadPoolExecutor(1)

# print("Submetendo a função worker para a pool")
# future = pool.submit(worker, "A")

# print("Obtida uma referência ao objeto futuro", future)
# print("future.result():", future.result())

# print("Pronto")

# O resultado desse programa é:
# Preparando a ThreadPoolExecutor
# Submetendo a função worker para a pool
# AObtida uma referência ao objeto futuro <Future at 0x210ddeaf0e0 state=running>
# AAAAAAAAAfuture.result(): 9
# Pronto

# Perceba que a saída do programa principal está envolvida com a exibição de
# 1 'A' antes da mensagem 'Obtida uma referência...'. Neste caso, um novo
# ThreadPoolExecutor está sendo criado com uma thread na pool (normalmente
# haveriam múltiplas threads, mas foi usada uma para ilustração).
# O método submit() é usado para submeter a função worker com o parâmetro
# 'A' para a ThreadPoolExecutor para agendar a execução da função. Este
# método retorna um objeto Future. O programa principal, então, espera pelo
# retorno do objeto futuro para (chamando result()). Este método poderia
# receber um parâmetro de expiração(timeout). Para alterar esse exemplo de
# Threads para processos, basta alterar o executor para ProcessPoolExecutor.
# ---------------------------------------------------
# Executando múltiplos futuros
# Ambas ThreadPoolExecutor e ProcessPoolExecutor podem ser configuradas
# para suportar múltiplas Threads/Processes pela pool. Cada tarefa
# submetida à pool será executada dentro de uma Thread/Processo separado.
# Se mais tarefas são submetidas do que o número de threads/processos
# disponíveis, então a tarefa submetida esperará pela liberação da primeira
# thread/processo antes de ser executada. Isto pode agir como um modo
# de gerenciar a quantidade de trabalho concorrente sendo feito.
# Por exemplo, a função worker() é submetida á pool 4 vezes no programa a seguir,
# mas a pool está configurada para usar 3 threads. Assim, a quarta execução
# de worker deverá esperar até uma das três primeiras seja completa antes
# de poder executar:
# from concurrent.futures import ThreadPoolExecutor

# print("Iniciando...")
# pool = ThreadPoolExecutor(3)
# f1 = pool.submit(worker, "A")
# f2 = pool.submit(worker, "B")
# f3 = pool.submit(worker, "C")
# f4 = pool.submit(worker, "D")
# print("\nfuture4.result():", f4.result())
# print("Todas finalizadas")

# O resultado é:
# Iniciando...
# ABCABCABCABCABCABCABCABCABCABCDDDDDDDDDD
# future4.result(): 9
# Todas finalizadas

# Perceba que a execução de f1, f2 e f3 ocorre concorrentemente, e assim
# que uma termina, inicia a execução da f4.

# --------------------------------------------------
# Esperando que todos os futuros completem
# Pode-se esperar para a finalização de todos os futuros antes de prosegguir.
# Na seção anterior, foi assumido que f4 seria o último a completar; mas
# em muitos casos, pode não ser possível saber qual será o último. Nesse
# caso, é útil ser capaz de esperar que todos os futuros sejam completos antes
# de continuar. Isto pode ser feito usando a função concurrent.futures.wait.
# Ela pega uma coleção de futuros e um timeout e return_when opcionais:
# wait(fs, timeout=None, return_when=ALL_COMPLETED)
# onde:
#   * timeout pode ser usado para controlar o número máximo de segundos a esperar
#       antes de retornar.
#   * return_when indica quando a função deve retornar. Deve ser uma das
#       seguintes constantes:
#       - FIRST_COMPLETED: quando qualquer futuro terminar ou for cancelado.
#       - FIRST_EXCEPTION: quando qualquer futuro terminar levantando uma exceção.
#           Se nenhum levantar uma exceção, é equivalente a ALL_COMPLETED.
#       - ALL_COMPLETED: retorna quando todos os futuros terminem ou forem cancelados.
# A função wait() retorna dois conjuntos done e not_done. O primeiro contém
# os futuros que completaram (finalizados ou cancelados) antes da esperar
# completar. O segundo contém futuros não completados. Pode-se usar a função
# wait() para modificar exemplos anteriores para não precisar mais depender
# que f4 termine por último:
# from concurrent.futures import ProcessPoolExecutor
# from concurrent.futures import wait
# from time import sleep


# if __name__ == "__main__":
#     print("Iniciando... preparando a pool")
#     pool = ProcessPoolExecutor(3)
#     futures = []

#     print("Submetendo os futuros")
#     future1 = pool.submit(worker, "A")
#     futures.append(future1)
#     future2 = pool.submit(worker, "B")
#     futures.append(future2)
#     future3 = pool.submit(worker, "C")
#     futures.append(future3)
#     future4 = pool.submit(worker, "D")
#     futures.append(future4)

#     print("Esperando a finalização de todos os futuros")
#     wait(futures)
#     print("\nTodos terminados")

# A saída é:
# Iniciando... preparando a pool
# Submetendo os futuros
# Esperando a finalização de todos os futuros
# ABCABCABCABCABCABCABCABCABCABCDDDDDDDDDD
# Todos terminados
# -----------------------------------------------
# Processando resultados conforme completam
# E se quisermos processar cada um dos resultados retornados pela coleção
# de futuros? Poderíamos usar um loop pela lista futures na seção anterior
# após todos os resultados terem sido gerados. Entretanto, isso significa
# que teríamos de esperar por todos completarem antes de processar a lista.
# Em muitos casos, poderíamos querer processar os resultados assim que estivessem
# disponíveis; com todos os futuros eventualmente sendo retornados mas sem
# garantia da ordem. Por exemplo, no seguinte exemplo, a função is_even()
# dorme por um número de segundos aleatório e então calcula um resultado.
# from concurrent.futures import ThreadPoolExecutor, as_completed
# from time import sleep
# from random import randint


# def is_even(n):
#     print(f"Checando se {n} é par")
#     sleep(randint(1, 5))
#     return str(n) + " " + str(n % 2 == 0)


# print("Iniciado")
# data = [1, 2, 3, 4, 5, 6]
# pool = ThreadPoolExecutor(5)
# futures = []

# for v in data:
#     futures.append(pool.submit(is_even, v))

# for f in as_completed(futures):
#     print(f.result())

# print("Terminado")

# Com a saída:
# Iniciado
# Checando se 1 é par
# Checando se 2 é par
# Checando se 3 é par
# Checando se 4 é par
# Checando se 5 é par
# Checando se 6 é par
# 1 False
# 3 False
# 4 True
# 5 False
# 6 True
# 2 True
# Terminado

# -------------------------------
# Processando resultados futuros usando um callback
# Uma alternativa para a abordagem as_complete é fornecer uma função que será
# chamada após um resultado ser gerado. Isto tem a vantagem de que o programa
# principal nunca é pausado; pode continuar fazendo o que é requerido.
# A função chamada quando o resultado é gerado é conhecida como função
# callback, isto é, o futuro chama retroativamente esta função quando o
# resultado estiver disponível.
# Cada futuro pode ter uma callback separada como a função a ser invocada
# usando o método add_done_callback(). Este método pega o nome da função
# a ser invocada.
# Por exemplo, nesta versão modificada do exemplo anterior, especificamos uma
# função de callback que será usada para exibir os resultados futuros.
# Esta função de callback é chamada prinf_future_result(). Ela pega o
# futuro que completou como argumento:
# from concurrent.futures import ThreadPoolExecutor
# from time import sleep
# from random import randint


# def is_even(n):
#     print(f"Checando se {n} é par")
#     sleep(randint(1, 5))
#     return str(n) + " " + str(n % 2 == 0)


# def print_future_result(future):
#     print("In callback Future result:", future.result())


# print("Iniciado")
# data = [1, 2, 3, 4, 5, 6]
# pool = ThreadPoolExecutor(5)

# for v in data:
#     future = pool.submit(is_even, v)
#     future.add_done_callback(print_future_result)

# print("Terminado")

# Que retorna:
# Iniciado
# Checando se 1 é par
# Checando se 2 é par
# Checando se 3 é par
# Checando se 4 é par
# Checando se 5 é par
# Terminado
# In callback Future result: 3 False
# Checando se 6 é par
# In callback Future result: 4 True
# In callback Future result: 5 False
# In callback Future result: 1 False
# In callback Future result: 2 True
# In callback Future result: 6 True

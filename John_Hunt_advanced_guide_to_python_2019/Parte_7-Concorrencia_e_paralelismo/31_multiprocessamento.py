# Capítulo 31 - Multiprocessamento
# A biblioteca multiprocessing suporta a geração de processos separados(no nível
# do sistema operacional) que executam comportamentos (como funções ou métodos)
# usando uma API que é similar à de Threading mostrada no capítulo anterior.
# Pode ser usada para evitar a limitação introduzida pelo GIL, usando processos
# do sistema operacional separados em vez de threads leves (executadas em um único
# processo). Isto significa que essa biblioteca permite que desenvolvedores
# aproveitem completamente o ambiente multiprocessador do hardware de computadores
# modernos que tipicamente tem múltiplos cores de processamento que permitem
# a execução de múltiplas operações/comportamentos em paralelo; isto pode ser
# muito significativo para análise de dados, processamento de imagens, animação
# e jogos.
# A biblioteca de multiprocessamento também introduz alguns novos recursos,
# notavelmente o objeto Pool para paralelizar a execução de um objeto chamável que
# não tem um equivalente na API de Threading.
# -----------------------------------------------------
# A classe Process
# Na biblioteca multiprocessing, esta classe é o equivalente à classe Thread
# da biblioteca threading. Pode ser usada para executar um objeto chamável como
# uma função em um processo separado. Para fazer isso, é necessário criar uma
# nova instância da classe Process e então chamar o método start() nela. Métodos
# como join() também estão presentes, de modo que um processo pode esperar pelo
# término de outro antes de continuar etc.
# A principal diferença é que quando um processo é criado, é executado dentro
# de um processo separado no sistema operacional(Windows, Linux etc). Em contraste,
# uma Thread executa dentro do mesmo processo que o programa original. Isto significa
# que o processo é gerenciado e executado diretamente pelo sistema operacional em
# um dos processadores que são parte do hardware do computador.
# O lado positivo disso é que permite explorar o paralelismo inerente do hardware
# do computador. O lado negativo é que Process é mais trabalhoso de configurar que
# as Threads.
# O construtor da classe Process fornece o mesmo conjunto de argumentos que a
# Thread:
# class multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, daemon=None)

#   * group: deveria sempre ser None; existe apenas por compatibilidade com a API threading.
#   * target: objeto a ser chamado pelo método run(). Por padrão é None.
#   * name: nome do processo.
#   * args: tupla de argumentos para a chamada do alvo(target)
#   * kwargs: dicionário de argumentos de palavras-chave para chamada do alvo.
#   * daemon: define a flag de daemon para True ou False. Se None, será herdada
#       do processo criador.
# Assim como a classe Thread, o construtor Process deveria sempre ser chamado
# usando argumentos de palavras-chave. A classe Process também fornece um conjunto
# similar de métodos à classe Thread:
#   * start(): Inicia a atividade do processo.
#   * join([timeout]): se o argumento opcional é None(o padrão), o método bloqueia
#       até o processo submetido ao join termina. Se o timeout é positivo, bloqueia
#       no máximo 'timeout' segundos.
#   * is_alive(): retorna se o processo está vivo.
# Também tem vários atributos:
#   * name: Nome do processo. É uma string usada para identificação. Múltiplos processos podem receber o mesmo nome.
#   * daemon: flag de daemon do processo, valor booleano. Deve ser definida antes
#       de chamar start. Quando um processo termina, tenta terminar todos os
#       processos filhos que são daemonic.
#   * pid: retorna o ID do processo. Antes do processo surgir(spawned), é None.
#   * exitcode: código de saída do processo. Será None se o processo ainda não
#       terminou. Um valor negativo -N indica que o processo filho foi terminado pelo sinal N.
# Além desses métodos e atributos, a classe Process também define métodos
# relacionados aos processos incluindo:
#   * terminate(): termina o processo
#   * kill(): mesmo que terminate(), exceto que no Unix, o sinal SIGKILL é usado
#       em vez do sinal SIGTERM.
#   * close(): Fecha o objeto processo, liberando todos os recursos associados com
#       ele. ValueError é levantado se o processo ainda está executando. Após
#       close() é retornado com sucesso, a maioria dos outros métodos e atributos
#       do objeto Process levantarão ValueError.
# -------------------------------------------------------------------------
# Trabalhando com a classe Process
# O seguinte programa simples cria três objetos Process; cada um executa a função
# worker(), com os argumentos de string A, B e C. Esses três objetos processo são
# iniciados usando start().
# from multiprocessing import Process
# from time import sleep


# def worker(msg):
#     for _ in range(0, 10):
#         print(msg, end="", flush=True)
#         sleep(1)


# if __name__ == "__main__":
#     print("Iniciando")
#     t2 = Process(target=worker, args="A")
#     t3 = Process(target=worker, args="B")
#     t4 = Process(target=worker, args="C")
#     t2.start()
#     t3.start()
#     t4.start()
#     print("Terminado")

# A saída desse programa é:
# Iniciando
# Terminado
# ABCABCABCABCABCABCABCABCABCABC
# A principal diferença entre as versões Thread e Process é que Process executa
# a função worker em processos separados enquanto na Thread todas as threads
# executam no mesmo processo.
# ------------------------------------------------
# Modos alternativos de iniciar um processo
# Quando o método start() é chamado em um Process, três abordagens diferentes
# para iniciar os processos são possíveis. Elas podem ser configuradas usando
# multiprocessing.set_start_method() que pega uma string indicando a abordagem
# a ser usada. A disponibilidade dos mecanismos efetivos de inicialização dos
# processos depende do sistema operacional:
#   * 'spawn': O processo pai inicia um novo processo do interpretador Python.
#       O processo filho herdará somente os recursos necessários para executar
#       o método run() dos objetos processo. Em particular, descritores de
#       arquivos e handles desnecessários do processo pai não serão herdados.
#       Iniciar um processo usando este método é mais demorado em comparação com
#       a utilização de fork ou forkserver. Disponível no Windows e Linux, sendo o padrão no Windows.
#   * 'fork': O processo pai usa os.fork() para bifurcar o interpretador Python.
#       O processo filho, ao iniciar, é efetivamente idêntico ao pai. Todos os
#       recursos do pai são herdados pelo filho. Disponível apenas em sistemas
#       operacionais do tipo Unix. É o padrão no Unix, Linux e MacOS.
#   * 'forkserver': Neste caso, um processo servidor é iniciado. Dali em diante,
#       sempre necessita-se de um novo processo, o processo pai conecta-se ao
#       servidor e pede para bifurcar um novo processo. O servidor bifurcador
#       tem thread única de modo que é seguro para ele usar os.fork(). Nenhum
#       recurso desnecessário é herdado. Disponível em plataformas do estilo
#       Unix que suportam a passagem de descritores de arquivo por pipes Unix.
# O set_start_method() deveria ser usado para definir o método de inicialização(e
# deveria ser usado apenas uma vez dentro de um programa). Isto é ilustrado abaixo,
# onde o método de inicialização spawn é especificado:
# from multiprocessing import Process, set_start_method
# from time import sleep
# import os


# def worker(msg):
#     print("nome módulo:", __name__)
#     print("processo pai:", os.getppid())
#     print("id do processo:", os.getpid())
#     for i in range(0, 10):
#         print(msg, end="", flush=True)
#         sleep(1)


# def main():
#     print("Iniciando")
#     print("ID do processo da aplicação raiz:", os.getpid())
#     set_start_method("spawn")
#     t = Process(target=worker, args="A")
#     t.start()
#     print("Pronto")


# if __name__ == "__main__":
#     main()

# Esse código tem a saída:
# Iniciando
# ID do processo da aplicação raiz: 21680
# Pronto
# nome módulo: __mp_main__
# processo pai: 21680
# id do processo: 13812
# AAAAAAAAAA

# Os IDs do processo pai e processo atual são exibidos para a função worker(),
# enquanto o método main() exibe apenas seu próprio id. Isto mostra que o id
# de aplicação main é o mesmo que o id do pai do processo worker.
# Alternativamente, é possível usar o método get_context() para obter um objeto
# contexto. Objetos contexto tem o mesmo API que o módulo multiprocessing e
# permitem-lhe usar múltiplos métodos start() no mesmo programa, por exemplo:
# ctx = multiprocessing.get_context('spawn')
# q = ctx.Queue()
# p = ctx.Process(target = foo, args = (q,))
# -------------------------------------------------------------
# Usando um Pool
# A criação de um processo é cara em termos de recursos computacionais. Portanto,
# seria útil ser capaz de reutilizar processos dentro de uma aplicação. A classe
# Pool permite esse tipo de reutilização.
# A classe Pool representa um conjunto(pool) de processos trabalhadores que podem
# ser usados para realizar um conjunto de operações concorrentes, paralelas.
# Pool fornece métodos que permitem que tarefas entregues para tais processos.
# O construtor dessa classe pega um número de argumentos:
# class multiprocessing.pool.Pool(processes, initializer, initargs, maxtaskperchild, context)

# Esses argumentos representam:
#   * processes: número de processos trabalhadores a serem usados. Se é None,
#       então o número retornado por os.cpu_count() é usado.
#   * initializer: Se initializer não é None, então cada processo trabalhador
#       chamará initializer(*initargs) quando iniciar.
#   * maxtaskperchild: é o número de tarefas que um processo trabalhador pode
#       completar antes de sair e ser substituído com um novo processo trabalhador,
#       para liberar recursos não utilizados. O padrão é None, que significa que o
#       processo trabalhador viverá o mesmo tanto que o pool.
#   * context:pode ser usado para especificar o contexto usado para iniciar os
#       processos trabalhadores. Geralmente, uma pool é criada usando a função
#       multiprocessing.Pool(). Alternativamente, a pool pode ser criada usando
#       o método Pool de um objeto contexto.
# A classe Pool tem vários métodos que podem ser usados para submeter trabalho aos
# processos trabalhadores gerenciados pela pool. Note que os métodos do objeto
# Pool devem ser chamados apenas pelo processo que a criou.
# O diagrama da figura pool.png ilustra o efeito de submeter algum trabalho ou
# tarefa à pool. Da lista de processos disponíveis, um processo é selecionado
# e a tarefa é passada ao processo. O processo, então, executará a tarefa. Após
# completa, qualquer resultado é retornado e o processo é retornado à lista disponível.
# Se, quando uma tarefa é submetida à pool, não há processos disponíveis, então
# a tarefa será acrescentada à fila de espera até que um processo torne-se
# disponível para realizá-la.
# O método mais simples da classe Pool para a submissão de trabalho é map:
# pool.map(func, iterable, chunksize=None)
# Este método retorna uma lista dos resultados obtidos pela execução da função
# em paralelo a cada item do parâmetro iterable.
#   * o parâmetro func é o objeto chamável para ser executado(como função ou método)
#   * iterable é usado para passar quaisquer parâmetros à função.
#   * este método divide o iterável em um número de pedaços(chunks) que submete
#       à pool do processo como tarefas separadas. O tamanho(aproximado) desses
#       pedaços pode ser especificado definindo chunksize como um número inteiro.
#       O método bloqueia até o resultado estar pronto.
# O seguinte programa de exemplo ilustra o uso básico de Pool e map().
# from multiprocessing import Pool


# def worker(x):
#     print("No método worker com: ", x)
#     return x * x


# def main():
#     with Pool(processes=4) as pool:
#         print(pool.map(worker, [0, 1, 2, 3, 4, 5]))


# if __name__ == "__main__":
#     main()

# Note que o objeto Pool deve ser fechado após terminar de usá-lo; portanto,
# foi usada a declaração 'with...as' para lidar com Pool de forma limpa.
# A saída desse programa é:
# No método worker com:  0
# No método worker com:  1
# No método worker com:  2
# No método worker com:  3
# No método worker com:  4
# No método worker com:  5
# [0, 1, 4, 9, 16, 25]

# Como pode ser visto da saída, a função map() é usada para executar seis instâncias
# diferentes da função worker() com os valores fornecidos pela lista de inteiros.
# Cada instância é executada por um processo worker gerenciado pela Pool.
# Entretanto, note que Pool possui apenas 4 processos trabalhadoresm o que significa
# que as últimas duas instâncias da função worker devem esperar que dois dos
# processos trabalhadores terminaram sua execução e podem ser reutilizados. Isto
# pode agir como um modo de 'throttling', ou controlar, quanto trabalho é feito
# em paralelo.
# Uma variação do método map() é imap_unordered(). Este método também aplica uma dada
# função a um iterável mas não tenta manter a ordem dos resultados. Os resultados
# são acessíveis pelo iterável retornado pela função. Isto pode melhorar o desempenho
# do programa resultante.
# O seguinte programa modificou a função worker() para retornar seu resultado
# em vez de exibi-lo. Este resultados são, então, acessíveis pela iteração sobre
# eles conforme são produzidos por um loop for:
# from multiprocessing import Pool


# def worker(x):
#     print("No método worker com: ", x)
#     return x * x


# def main():
#     with Pool(processes=4) as pool:
#         for result in pool.imap_unordered(worker, [0, 1, 2, 3, 4, 5]):
#             print(result)


# if __name__ == "__main__":
#     main()

# A saída desse programa é:

# No método worker com:  1
# 0
# No método worker com:  2
# 1
# No método worker com:  3
# 4
# 9
# No método worker com:  5
# No método worker com:  4
# 25
# 16

# --> A sequência de resultados retornados foi na ordem correta, mas diferentes
#       execuções do programa alteram a ordem em que cada resultado é retornado;
#       isto é, a sequência 'No método worker com:  x' e o resultado não aparecem
#       de maneira consistente.
#
# Outro método disponível na classe Pool é Pool.apply_async(). Ele permite que
# operações/funções sejam executadas de maneira assíncrona, permitindo que as
# chamadas do método retornem imediatamente. Isto é, assim que o método foi
# chamado, o controle é retornado ao código que chamou que pode continuar imediatamente.
# Quaisquer resultados a serem coletados das operações assíncronas podem ser obtidos
# ou fornecendo uma função de chamada retroativa(callback) ou usando o método
# bloqueador get() para obter um resultado.
# Dois exemplos são mostrados abaixo, com o primeiro usando o método bloqueador
# get(). Este método esperará até um resultado estar disponível antes de continuar.
# A segunda abordagem usa uma função retroativa. Esta função é chamada quando um
# resultado estiver disponível; o resultado é passado para a função.
# from multiprocessing import Pool


# def collect_results(result):
#     print("Em colect_results: ", result)


# def worker(x):
#     print("Em worker com: ", x)
#     return x * x


# def main():
#     with Pool(processes=2) as pool:
#         res = pool.apply_async(worker, [6])
#         print("Resultado de async: ", res.get(timeout=1))

#     with Pool(processes=2) as pool:
#         pool.apply_async(worker, args=[4], callback=collect_results)
#         pool.close()  # Fecha a Pool
#         pool.join()  # Espera todas as tarefas completarem


# if __name__ == "__main__":
#     main()


# O retorno desse exemplo é:
# Em worker com:  6
# Resultado de async:  36
# Em worker com:  4
# Em colect_results:  16

# --> No livro não tem as declarações pool.close() e pool.join(). Sem elas, o resultado
#       da segunda declaração 'with as' não é exibido no console, mas através da
#       ferramenta de debug o resultado aparece. usando close e join faz com que
#       o resultado completo apareça.
# -------------------------------------------------
# Trocando dados entre processos
# Em algumassituações, é necessário que dois processos troquem informações.
# No entanto, dois processos não cmopartilham memória pois estão executando
# processos separados no nível do sistema operacinal. Para contornar isso,
# a biblioteca de multiprocessamento tem a função Pipe(). Essa função retorna
# um par de objetos connection.Connection conectados a um pipe que, por padrão,
# é duplex(ida e volta).
# Os dois objetos conexão retornados por Pipe() representam os dois finais do
# pipe. Cada objeto conexão tem os métodos send() e recv()(entre outros). Isto
# permite que um processo envie dados pelo método send() de um final do objeto conexão.
# Por sua vez, um segundo processo pode receber aqueles dados pelo método receive()
# do outro objeto conexão. Isto é ilustrado na figura pipe.png.
# Assim que um programa finalizou com uma conexão, deveria ser fechado usando close().
# from multiprocessing import Process, Pipe
# from time import sleep


# def worker(conn):
#     print("Trabalhador - iniciado agora, dormindo por 1 segundo")
#     sleep(1)
#     print("Trabalhador - enviando dados pelo pipe")
#     conn.send("hello")
#     print("Trabalhador - fechando trabalhador, fim da conexão")
#     conn.close()


# def main():
#     print("Main - Iniciando, criando o Pipe")
#     main_connection, worker_connection = Pipe()
#     print("Main - Preparando o processo")
#     p = Process(target=worker, args=[worker_connection])
#     print("Main - Iniciando o processo")
#     p.start()
#     print("Main - Esperando por uma resposta do processo filho")
#     print(main_connection.recv())
#     print("Main - fechando processo pai, fim da conexão")
#     main_connection.close()
#     print("Main-terminado")


# if __name__ == "__main__":
#     main()

# Perceba que os dados em um pipe podem tornar-se corrompidos se dois processos
# tentarem ler de ou escrever para o mesmo final do pipe ao mesmo tempo. Entretanto,
# não há risco de corrupção de processos usando diferentes finais do pipe ao
# mesmo tempo.
# --------------------------------------------------------
# Compartilhando estado entre processos
# Em geral, se pode-se evitar, então você não deve compartilhar estados entre
# processos separados. Entretanto, se é inevitável, então a biblioteca multiprocessing
# fornece duas maneiras com as quais o estado(dados) podem ser compartilhados,
# sendo Shared Memory(suportado por mulltiprocessing.Value e multiprocessing.Array)
# e Server Process.
# --------------------------------------------
# Memória compartilhada entre processos
# Dados podem ser armazenados em um mapa compartilhado de memória usando
# multiprocessing.Value ou multiprocessing.Array. Estes dados podem ser acessados
# por vários processos.
# O construtor de multiprocessing.Value é:
# multiprocessing.Value(typecode_or_type, *args, lock=True)
# Onde:
#   * typecode_or_type determina o tipo do objeto retornado:ou é um ctype ou um
#       typecode de um caractere. Por exemplo, 'd' indica um float com precisão
#       dupla e 'i' indica um inteiro assinado(signed).
#   * *args é passado para o construtor para o tipo.
#   * lock se for True, o padrão, então um novo objeto recursivo é criado para
#       sincronizar o acesso ao valor. Se lock é False, então o acesso ao objeto
#       retornado não será protegido automaticamente por uma tranca, de modo que
#       não será necessáriamente process-safe.
# O construtor para multiprocessing.Array é:
# multiprocessing.Array(typecode_or_type, size_or_initializer, lock=True)
# Onde:
#   * typecode_or_type determina o tipo dos elementos da matriz retornada
#   * size_or_initializer, se for um inteiro, então determina o comprimento
#       da matriz, e a matriz será inicialmente zeros(zeroed). De outro modo,
#       é uma sequência que é usada para inicializar a matriz e cujo comprimento
#       determina o comprimento da matriz.
#   * Se lock é True (o padrão), então um novo objeto lock é criado para sincronizar
#       o acesso ao valor. Se é False, então o acesso ao objeto retornado não
#       será protegido por uma tranca automaticamente, não sendo necessariamente
#       process-safe.
# from multiprocessing import Process, Value, Array


# def worker(n, a):
#     n.value = 3.1415927
#     for i in range(len(a)):
#         a[i] = -a[i]


# def main():
#     print("Iniciando")
#     num = Value("d", 0.0)
#     arr = Array("i", range(10))
#     p = Process(target=worker, args=(num, arr))
#     p.start()
#     p.join()
#     print(num.value)
#     print(*arr)
#     print("Terminado")


# if __name__ == "__main__":
#     main()

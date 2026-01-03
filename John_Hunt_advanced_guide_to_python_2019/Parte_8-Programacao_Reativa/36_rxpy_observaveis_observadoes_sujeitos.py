# Capítulo 36 - Observáveis, Observadores e Sujeitos em RxPy
#
# Observáveis em RxPy
# Um Observable é uma classe Python que publica dados para que possam ser
# processados por um ou mais observadores. Pode ser craido para publicar
# dados de ou para fontes dinâmicas. Também podem ser conectados para
# controlar como e quando dados são publicados, transformar dados antes
# de serem publicados e restringir quais dados são publicados.
# Por exemplo, para criar um Observable de uma lista de valores, podemos
# usar a função rx.from_list(). Esta função (também conhecida como operador
# RxPy) é usada para criar o novo objeto observável:
# import rx

# observable = rx.from_list([2, 3, 5, 7])

# Observadores em RxPy
# Podemos adicionar um Observador a um Observável usando o método subscribe().
# Este método pode ser fornecido com uma função lambda, uma função nomeada ou um
# objeto cuja classe implementa o protocolo observador.
# Por exemplo, o modo mais simples de criar um observador é usar a função lambda:

# observable.subscribe(lambda value: print("Lambda recebida", value))

# Quando o observável publica os dados, a função lambda é invocada. Cada
# item de dado publicado será fornecido independentemente à função. A saída
# dessa inscrição do observador ao observavel é:
# Lambda recebida 2
# Lambda recebida 3
# Lambda recebida 5
# Lambda recebida 7


# Poderíamos também ter usado uma função padrão ou nomeada como observador:
# def prime_number_reporter(value):
#     print("Função recebida", value)


# observable.subscribe(prime_number_reporter)

# Dessa forma, apenas o nome da função é passado para subscribe().
# Função recebida 2
# Função recebida 3
# Função recebida 5
# Função recebida 7

# Na realidade, o método subscribe pega 4 parâmetros opcionais, sendo eles:
#   * on_next: ação para invocar cada item de dado gerado pelo Observável
#   * on_error: ação para invocar sob término com exceção da sequência observável.
#   * on_completed: Ação a invocar sob término correto da sequência observável.
#   * Observer: O objeto que vai receber notificações. Pode subscrever usando
#       um Observador ou callbacks, mas não os dois juntos.
# Cada um dos items acima pode ser usado como parâmetros posicionais ou argumentos
# de palavras chave:
# observable.subscribe(
#     on_next=lambda value: print("Recebido on_next", value),
#     on_error=lambda exp: print("Erro ocorreu", exp),
#     on_completed=lambda: print("Recebido notificação de compleção"),d
# )


# O código acima define três funções lambda que serão chamadas dependendo em se
# dados são fornecidos ao Observável, se um erro ocorreu ou quando o fluxo de
# dados é terminado.
# Recebido on_next 2
# Recebido on_next 3
# Recebido on_next 5
# Recebido on_next 7
# Recebido notificação de compleção


# Perceba que a função on_error não foi executada pois não surgiram erros neste exemplo.
# O parâmetro final opcional é um objeto Observador. Um objeto Observador pode
# implementar o protocolo observador que tem os métodos on_next(), on_completed()
# e on_error():
# class PrimeNumberObserver:
#     def on_next(self, value):
#         print("Objeto recebido", value)

#     def on_completed(self):
#         print("Fluxo de dados completo")

#     def on_error(self, error):
#         print("Erro ocorreu", error)


# Instâncias desta classe podem agora ser usadas como um Observador pelo método
# subscribe():
# observable.subscribe(PrimeNumberObserver())

# Objeto recebido 2
# Objeto recebido 3
# Objeto recebido 5
# Objeto recebido 7
# Fluxo de dados completo

# Perceba que o método on_completed() também é chamado, mas on_error() não
# pois não surgiram exceções. A classe Observador deve garantir que os métodos
# implementados aderem ao protocolo Observador.
# --------------------------------------------------------
# Múltiplos inscritos/Observadores
# Um observador pode  ter vários observadores inscritos. Neste caso, cada
# um dos observadores recebe todos os dados publicados pelo Observável.
# Múltiplos Observadores podem ser registrados com um Observável chamando o
# método subscribe múltiplas vezes. Por exemplo, o seguinte programa tem 4
# inscritos assim como on_error e on_completed registrados:
# import rx

# observable = rx.from_list([2, 3, 5, 7])


# class PrimeNumberObserver:
#     def on_next(self, value):
#         print("Objeto recebido", value)

#     def on_completed(self):
#         print("Fluxo de dados completo")

#     def on_error(self, error):
#         print("Erro ocorreu", error)


# def prime_number_reporter(value):
#     print("Função recebida", value)


# print("Preparando observadores/inscritos")
# observable.subscribe(lambda value: print("Lambda recebido", value))
# observable.subscribe(prime_number_reporter)
# observable.subscribe(PrimeNumberObserver())
# observable.subscribe(
#     on_next=lambda value: print("Recebido on_next", value),
#     on_error=lambda exp: print("Erro ocorreu", exp),
#     on_completed=lambda: print("Recebida notificação de compleção"),
# )

# A saída é:
# Lambda recebido 2
# Lambda recebido 3
# Lambda recebido 5
# Lambda recebido 7
# Função recebida 2
# Função recebida 3
# Função recebida 5
# Função recebida 7
# Objeto recebido 2
# Objeto recebido 3
# Objeto recebido 5
# Objeto recebido 7
# Fluxo de dados completo
# Recebido on_next 2
# Recebido on_next 3
# Recebido on_next 5
# Recebido on_next 7
# Recebida notificação de compleção

# Perceba que cada um dos observadores recebe todos os dados antes do próximo
# receber os dados(comportamento padrão do RxPy com uma única thread)
# ----------------------------------------------
# Sujeitos em RxPy
# Um sujeito é ambos Observador e Observável. Isto permite que um sujeito
# receba um item de dados e então republique aqueles dados ou dados derivados
# deles. Por exemplo, imagine que um sujeito recebe dados do preço do mercado de ações
# publicados por uma fonte externa(à organização recebendo os dados). Este
# sujeito poderia acrescentar um rótulo temporal e local da fonte ao dado
# antes de republicá-lo para outros observadores internos.
# Entretanto, existe uma diferença sutil que precisa ser notada entre um sujeito
# e um Observável simples. Uma subscrição a um Observável causará uma execução
# independente do observável quando dados forem publicados. Note como a seção
# anterior todas as mensagens foram enviadas a um Observador específico antes
# do próximo Observador recebar qualquer dado. Entretanto, um Sujeito compartilha
# a ação da publicação com todos os inscritos e portanto, todos receberão os mesmos
# items de dados em cadeia antes do próximo item.
# Na hierarquia de classes, a classe Subject é subclasse direta de Observer.
# O seguinte exemplo cria um sujeito que enriquece os dados recebidos acrescentando
# um rótulo temporal a cada item de dado. Então republica aquele item a quaisquer
# observadores que estejam inscritos a ele.
# import rx
# from rx.subject import Subject
# from datetime import datetime

# source = rx.from_list([2, 3, 5, 7])


# class TimeStampSubject(Subject):
#     def on_next(self, value):
#         print("Sujeito recebeu", value)
#         super().on_next((value, datetime.now()))

#     def on_completed(self):
#         print("Fluxo de dados completo")
#         super().on_completed()

#     def on_error(self, error):
#         print("Em Sujeito - Ocorreu um erro", error)
#         super().on_error(error)


# def prime_number_reporter(value):
#     print("Função recebida", value)


# print("Preparando")
# subject = TimeStampSubject()
# subject.subscribe(prime_number_reporter)
# subject.subscribe(lambda value: print("Recebido Lambda", value))
# subject.subscribe(
#     on_next=lambda value: print("Recebido on_next", value),
#     on_error=lambda exp: print("Ocorreu um erro", exp),
#     on_completed=lambda: print("Recebida notificação de compleção"),
# )
# source.subscribe(subject)
# print("Terminado")


# Observe que no programa acima, os observadores são adicionados ao sujeito
# antes do sujeito ser adicionado ao observavel source. Isto garante que
# os observadore estão inscritos antes que subject comece a receber dados
# publicados pelo observável.
# A saída é:
# Preparando
# Sujeito recebeu 2
# Função recebida (2, datetime.datetime(2025, 12, 30, 14, 44, 41, 281826))
# Recebido Lambda (2, datetime.datetime(2025, 12, 30, 14, 44, 41, 281826))
# Recebido on_next (2, datetime.datetime(2025, 12, 30, 14, 44, 41, 281826))
# Sujeito recebeu 3
# Função recebida (3, datetime.datetime(2025, 12, 30, 14, 44, 41, 282565))
# Recebido Lambda (3, datetime.datetime(2025, 12, 30, 14, 44, 41, 282565))
# Recebido on_next (3, datetime.datetime(2025, 12, 30, 14, 44, 41, 282565))
# Sujeito recebeu 5
# Função recebida (5, datetime.datetime(2025, 12, 30, 14, 44, 41, 283294))
# Recebido Lambda (5, datetime.datetime(2025, 12, 30, 14, 44, 41, 283294))
# Recebido on_next (5, datetime.datetime(2025, 12, 30, 14, 44, 41, 283294))
# Sujeito recebeu 7
# Função recebida (7, datetime.datetime(2025, 12, 30, 14, 44, 41, 284561))
# Recebido Lambda (7, datetime.datetime(2025, 12, 30, 14, 44, 41, 284561))
# Recebido on_next (7, datetime.datetime(2025, 12, 30, 14, 44, 41, 284561))
# Fluxo de dados completo
# Recebida notificação de compleção
# Terminado
# -------------------------------------------
# Concorrência de observadores
# Por padrão, RxPy usa um modelo de thread única; isto é, Observáveis e
# Observadores executam na mesma thread de execução. No entanto, isto é apenas
# o padrão, sendo a abordagem mais simples.
# É possível indicar que quando um Observador se inscreva a um Observável, ele
# deveria executar em uma thread separada usando a palavra chave scheduler
# no método subscribe(). Esta palavra chave é dada um escalonador (scheduler)
# apropriado como o rx.concurrency.NewThreadScheduler. O escalonador garantirá
# que o Observador executa em uma thread separada.
# Para ver a diferença, observe os seguintes 2 programas. A principal diferença
# entre eles é o uso de escalonadores específicos:
# import rx

# Observable = rx.from_list([2, 3, 5])
# Observable.subscribe(lambda v: print("Lambda1 recebida", v))
# Observable.subscribe(lambda v: print("Lambda2 recebida", v))
# Observable.subscribe(lambda v: print("Lambda3 recebida", v))

# A saída é dada abaixo:
# Lambda1 recebida 2
# Lambda1 recebida 3
# Lambda1 recebida 5
# Lambda2 recebida 2
# Lambda2 recebida 3
# Lambda2 recebida 5
# Lambda3 recebida 2
# Lambda3 recebida 3
# Lambda3 recebida 5

# O método subscribe() pega um parâmetro de palavra chave opcional chamado
# scheduler que permite que um objeto escalonador seja fornecido. Agora,
# se especificamos alguns escalonadores diferentes, veremos que o efeito
# é a execução dos Observadores concorrentemente, com a saída resultante sendo
# embaralhada:
# import rx
# from rx.scheduler import NewThreadScheduler, ThreadPoolScheduler, ImmediateScheduler

# Observable = rx.from_list([2, 3, 5])

# Observable.subscribe(
#     lambda v: print("Lambda1 recebido", v), scheduler=ThreadPoolScheduler(3)
# )
# Observable.subscribe(
#     lambda v: print("Lambda2 recebido", v), scheduler=ImmediateScheduler()
# )
# Observable.subscribe(
#     lambda v: print("Lambda3 recebido", v), scheduler=NewThreadScheduler()
# )

# Como o Observável executa em uma Thread separada, é necessário garantir
# que a thread principal não seja terminada:
# input("Aperte enter para terminar\n")

# Com a saída:
# Lambda2 recebido 2
# Lambda1 recebido 2
# Lambda2 recebido 3
# Lambda1 recebido 3
# Lambda2 recebido 5
# Lambda1 recebido 5
# Lambda3 recebido 2
# Lambda3 recebido 3
# Aperte enter para terminar
# Lambda3 recebido 5

# Por padrão, a palavra chave scheduler no método subscribe() é None, indicando
# que a thread atual será usada para a inscrição ao Observável.
# ---------------------------------------------------
# Escalonadores Disponíveis
# Para suportar diferentes estratégias de agendamento, A biblioteca RxPy
# possui dois módulos que fornecem diferentes escalonadores: o rx.concurrency
# e o rx.concurrency.mainloopscheduler. Os módulos contém diversos escalonadores
# incluindo os listados abaixo:
# No módulo rx.concurrency(em 01/2026 é em rx.scheduler):
#   * ImmediateScheduler: agenda uma ação para execução imediata.
#   * CurrentThreadScheduler: agenda uma atividade para a thread atual.
#   * TimeoutScheduler: este agendador funciona por uma callback cronometrada.
#   * NewThreadScheduler: cria um escalonador para cada unidade de trabalho em uma thread separada.
#   * ThreadPoolScheduler: é um escalonador que utiliza um pool de threads para
#       executar trabalho. Este escalonador pode agir como um modo de limitar
#       (throttling) a quantidade de trabalho realizada concorrentemente.
# No módulo rx.concurrency.mainloopscheduler(em 01/2026: rx.scheduler.eventloop ou .mainloop):
#   * IOLoopScheduler: Um escalonador que agenda trabalho pelo Tornado I/O loop de evento principal.
#   * PyGameScheduler: Um escalonador que agenda trabalhos para PyGame.
#   * WxScheduler: Um escalonador para um loop de evento de wxPython.

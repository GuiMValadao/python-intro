# Concorrência com AsyncIO

# Os recursos de Async IO em Python são adições recentes a Python, originalmente
# introduzidas no Python 3.4. São compostas (no Python 3.7) por duas
# palavras chave, async e await e o pacote Async IO para Python.
# --------------------------------------
# IO Assíncrono
# Async IO é um modelo(paradigma) linguagem-agnóstico de programação
# concorrente que tem sido implementado em diversas linguagens de programação.
# Asynchronous IO é outro jeito de se construir aplicações concorrentes em
# Python. De várias maneiras, é uma alternativa aos recursos fornecidos pela
# biblioteca Threading. Entretanto, enquanto Threading é mais suscetível a
# problemas associados com o GIL que podem afetar o desempenho, os recursos
# AsyncIO são melhor isolados deste problema.
# O modo em que Async IO opera é também mais leve que os recursos da biblioteca
# multiprocessing pois as tarefas assíncronas executam dentro de um único
# processo em vez de precisar criar processos distintos no hardware.
# Portanto, o Async IO é outra maneira alternativa de se implementar
# soluções concorrentes para problemas. Deve-se perceber que ela não constroi
# nem sobre threading nem sobre multiprocessing; em vez disso, é baseada na
# ideira de multitarefas cooperativas. Estas tarefas operam assíncronamente;
# isso significa que as tarefas:
#   * são capazes de operar separadamente de outras tarefas;
#   * são capazes de esperar que outra tarefa retorne um resultado quando necessário;
#   * são assim capazes de permitir a execução de outras tarefas enquanto esperam.
# O aspecto IO(Input/Output) do nome Async IO é pois essa forma de programação
# concorrente é melhor aplicada para tarefas ligadas a I/O. Nesse tipo de tarefa,
# um programa passa a maioria de seu tempo enviando ou recebendo dados de
# alguma forma de dispositivo externo. Esta comunicação é demorada e significa
# que o programa passa a maior parte do tempo esperando uma resposta desse
# dispositivo externo. Um jeito no qual tais aplicações ligadas(bound) a
# I/O pode (parecer) acelerar é a sobreposição da execução de diferentes tarefas;
# assim, enquanto uma tarefa está esperando uma resposta, outra tarefa pode
# estar escrevendo dados em um arquivo de registro etc.
# ------------------------------------------------------
# Loop de Evento Async IO
#
# Quando estiver desenvolvendo código usando os recursos Async IO, não
# precisará se preocupar sobre como é o funcionamento interno da biblioteca;
# no entanto, é útil entender um conceito chave em nível conceitual: o
# Async IO Event Loop; este loop controla como e quando cada tarefa é executada.
# Para essa discussão, uma tarefa representa algum trabalho que pode ser
# executado independentemente de outras partes de trabalho.
# O Loop de Evento sabe sobre cada tarefa a ser executada e qual seu estado
# atual(por exemplo, se está esperando algo acontecer/completar). Ele
# seleciona uma tarefa que está pronta para ser executada da lista de tarefas
# disponíveis e a executa. Esta tarefa tem controle completo da CPU até
# ou completar a tarefa ou devolver o controle para o Loop de Evento. Nesse
# ponto, o Loop de Evento checa se alguma das tarefas em espera estão prontas
# para execução e toma nota de seus estados. Então seleciona outra tarefa
# pronta para execução e a inicia. Este loop continua até todas as tarefas
# serem completas. Um ponto importante sobre esse processo é que uma tarefa
# não libera o processador até decidir liberá-lo, por exemplo, se tiver
# que esperar por alguma coisa. Elas nunca são interrompidas no meio de uma
# operação; isto evita o problema que duas threas poderiam ter quando sendo
# divididas temporalmente por um escalonador separado como ambas poderiam
# estar compartilhando o mesmo recurso.
# ----------------------------------------------------------
# As palavras chave async e await
# A palavra chave async, introduzida no Python 3.7, é usada para marcar uma
# função como sendo algo que usa a palavra chave await. Uma função que usa
# a palavra chave await pode ser executada como uma tarefa separada e
# devolver o controle do processador quando chamar await contra outra
# função async e deve esperar por aquela função ser completada. A função
# async invocada pode, então, ser executada como uma tarefa separada etc.
# Para invocar uma função async, é necessário iniciar o Loop de Evento de
# Async IO e que aquela função seja tratada como uma tarefa pelo Loop de Evento.
# Isto é feito através do método asyncio.run() e passando a função raiz async.
# Essa função foi introduzida no Python 3.7. Deve-se notar que esta função foi
# marcada como provisória no Python 3.7, estando sujeita a alterações em
# versões futuras. Por isso, deve-se checar a documentação para a versão
# de Python para verificar sua disponibilidade e possíveis alterações no uso.
# -------------------------------------------------------
# Usando Async e Await

# import asyncio
# def main():
#     print('Main - Iniciando')
#     asyncio.run(do_something())
#     print('Main - Done')
# if __name__ == '__main__':
#     main()

# A função main() é o ponto de entrada para o programa e chama asyncio.run(...).
# Isto inicia o Evento de loop do AsyncIO e resulta na função do_something()
# sendo encapsulada em uma Task que é gerenciada pelo Loop. Note que não
# é necessário criar explicitamente uma Task; elas sempre são criadas por
# alguma função, mas é útil estar ciente de Tasks pois você pode interagir
# com elas para checar seus status ou recuperar um resultado.
# A função do_something() é marcada com a palavra chave async:
# async def do_something():
#     print('do_something - espera pelo worker')
#     result = await worker()
#     print('do_something - result:', result)
# Como mencionado anteriormente, isso indica que pode ser executada como
# uma tarefa separada e que pode usar a palavra chave await para esperar
# que alguma outra função ou comportamento completem.
# A palavra chave await faz mais que simplesmente indicar que a função
# do_something() deve esperar pela worker completar. Ela engatilha(triggers)
# a criação de outra Task que executará a função worker e liberará o processador,
# permitindo que o Loop de Evento selecione a próxima tarefa a ser executada.
# O status de do_something() agora é esperando enquanto o status de worker
# é pronta (para execução).
# async def worker():
#     print('worker - levará algum tempo')
#     time.sleep(3)
#     print('worker - finalizada')
#     return 42
# Novamente, a palavra chave async indica que esta função pode ser executada
# como uma tarefa separada. Entretanto, o corpo da função não usa await.
# Isto é um caso especial conhecido como uma função corrotina AsyncIO.
# Esta é uma função que retorna um valor de uma Task (relacionada à ideia
# da corrotina padrão do Python que é consumidora de dados).
# O programa completo é colocado abaixo:

# import asyncio
# import time


# async def do_something():
#     print("do_something - espera pelo worker")
#     result = await worker()
#     print("do_something - result:", result)


# async def worker():
#     print("worker - levará algum tempo")
#     time.sleep(3)
#     print("worker - finalizada")
#     return 42


# def main():
#     print("Main - Iniciando")
#     asyncio.run(do_something())
#     print("Main - Done")


# if __name__ == "__main__":
#     main()

# Que retorna:

# Main - Iniciando
# do_something - espera pelo worker
# worker - levará algum tempo
# worker - finalizada
# do_something - result: 42
# Main - Done

# Apesar de não ser completamente óbvio aqui, a função do_something() foi
# executada como uma tarefa, então esta tarefa esperou quando chegou à
# função worker(), que foi executada como outra tarefa. Após worker completar,
# a tarefa do_comething pode continuar e completar sua operação.

# ------------------------------------------------
# Tarefas Async IO
#
# As Tasks são usadas para executar concorrentemente funções marcadas com
# a palavra chave async. Elas nunca são criadas diretamente, sendo criadas
# implicitamente pela palavra chave await ou por funções como asyncio.run
# descrita acia ou asyncio.create_task(), asyncio.gather() e asyncio.as_completed().
# Estas funções adicionais são descritas abaixo:
#   * asyncio.create_task(): Pèga uma função marcada com async e a encapsula
#       dentro de uma Task, agendando para execução pelo Loop de Evento.
#   * asyncio.gather(*aws): Esta função executa todas as funções async
#       passadas a ela como Tasks separadas. Ela junta os resultados de cada
#       tarefa e os retorna como uma lista. A ordem dos resultados corresponde
#       à ordem das funções async passadas na lista aws.
#   * asyncio.as_completed(aws): executa cada uma das funções async passadas a ela.
# Um objeto Task suporta vários métodos úteis:
#   * cancel(): cancela a execução de uma tarefa. Chamar esse método fará com
#       que a Task lance a exceção CancelledError.
#   * cancelled(): retorna True se a Task foi cancelada.
#   * done(): retorna True se a tarefa foi completa, levantou uma exceção ou foi cancelada.
#   * result(): retorna o resultado da tarefa se tiver terminado. Se o resultado
#       ainda não estiver disponível, então o método levanta a exceção InvalidStateError.
#   * exception(): retorna uma exceção se a Task levantou uma exceção. Se a
#       Task foi cancelada, então levanta a exceção CancelledError. Se ainda
#       não terminou, levanta a exceção InvalidStateError.
# Também é possível acrescentar uma função de callback para invocar quando
# a tarefa tiver completado(ou remover uma callback se tiver sido adicionada):
#   * add_done_callback(callback): acrescenta a callback a ser executada ao término da Task.
#   * remove_done_callback(callback): remove a callback da lista de callbacks.
# O método é chamado 'add' em vez de 'set', o que implica a possibilidade
# de múltiplas funções poderem ser chamadas quando a tarefa completar(se preciso).

# import asyncio


# async def worker():
#     print("worker - levará algum tempo")
#     await asyncio.sleep(1)
#     print("worker - pronto")
#     return 42


# def print_it(task):
#     print("print_it resultado:", task.result())


# async def do_something():
#     print("do_something - cria tarefa para worker")
#     task = asyncio.create_task(worker())
#     print("do_something - acrescenta callback")
#     task.add_done_callback(print_it)
#     await task
#     print("do_something - task.cancelled():", task.cancelled())
#     print("do_something - task.done():", task.done())
#     print("do_something - task.result():", task.result())
#     print("do_something - task.exception():", task.exception())
#     print("do_something - terminada")


# def main():
#     print("Main - Iniciando")
#     asyncio.run(do_something())
#     print("Main - Terminada")


# if __name__ == "__main__":
#     main()

# Que exibe:
# Main - Iniciando
# do_something - cria tarefa para worker
# do_something - acrescenta callback
# worker - levará algum tempo
# worker - pronto
# print_it resultado: 42
# do_something - task.cancelled(): False
# do_something - task.done(): True
# do_something - task.result(): 42
# do_something - task.exception(): None
# do_something - terminada
# Main - Terminada

# Neste exemplo, a função worker() é encapsulada dentro de um objeto tarefa
# que é retornado da chamada asyncio.create_task(worker()).
# Neste exemplo, a função async do_something explicitamente espera a tarefa
# completar. Após isso acontecer, vários métodos diferentes são usados para
# obter informação sobre a tarefa. Outro ponto para observar-se é que na
# função worker() acrescentamos um await com a função async.sleep(1); isto
# permite que worker durma e espera a tarefa engatilhada completar. É uma
# alternativa da biblioteca async à função time.sleep(1).
# --------------------------------------------
# Executando mútliplas tarefas
# Em vários casos, é útil ser capaz de exectuar várias tarefas concorrentemente.
# Existem duas opções para fazer isso: asyncio.gather() e asyncio.as_completed().
#
# Reunindo(collating) resultados de múltiplas tarefas
# Muitas vezes é útil coletar todos os resultados de um conjunto de tarefas
# de uma vez para continuar apenas quando todos os resultados foram obtidos.
# Ao usar Threads ou Processos, isto pode ser conseguido iniciando mútltiplas
# Threads/Processos e então usando algum outro objeto como uma Barreira para
# esperar que todos os resultados estejam disponíveis antes de continuar.
# Dentro da bibliotec AsyncIO, tudo que é necessário é usar a função
# asyncio.gather() com uma lista das funções async para executar, por exemplo:
# import asyncio
# import random


# async def worker():
#     print("Worker - levará algum tempo")
#     await asyncio.sleep(1)
#     result = random.randint(1, 10)
#     print("Worker - Pronto")
#     return result


# async def do_something():
#     print("do_something - irá esperar por worker")
#     results = await asyncio.gather(worker(), worker(), worker())
#     print("resultado das chamadas:", results)


# def main():
#     print("Main - Iniciando-")
#     asyncio.run(do_something())
#     print("Main - Terminado")


# if __name__ == "__main__":
#     main()

# O resultado é:
# Main - Iniciando-
# do_something - irá esperar por worker
# Worker - levará algum tempo
# Worker - levará algum tempo
# Worker - levará algum tempo
# Worker - Pronto
# Worker - Pronto
# Worker - Pronto
# resultado das chamadas: [2, 2, 6]
# Main - Terminado

# A função do_something usa três chamadas à função worker em três Tasks
# separadas e espera os resultados de todas as três estarem disponíveis antes
# de retorná-los como uma lista de valores e armazenados na variável results.
# Isto torna bastante simples trabalhar com múltiplas tasks concorrentes e
# reunir(collate) seus resultados.
#
# ------------------------------------------
# Manipulando resultados de tarefas conforme tornam-se disponíveis
# Outra opção ao executar múltiplas Tasks é manipular os resultados conforme
# tornam-se disponíveis em vez de esperar por todos os resultados serem
# fornecidos antes de continuar. Esta opção é suportada pela função
# asyncio.as_completed(). Esta função retorna um iterador de funções async que
# serão entregues assim que completarem seu trabalho.
# O construto for-loop pode ser usado com o iterador retornado pela função;
# entretanto, dentro do loop for, o código deve chamar await nas funções
# async retornadas para que o resultado da tarefa possa ser obtido. Por exemplo:

# import asyncio
# import random


# async def do_something():
#     print("do_something - esperará por worker")
#     for async_func in asyncio.as_completed((worker("A"), worker("B"), worker("C"))):
#         result = await async_func
#         print("do_something - result:", result)


# # asyncio.as_completed pega um container como uma tupla de funções async.
# async def worker(label):
#     print("Worker - will take some time")
#     await asyncio.sleep(1)
#     result = random.randint(1, 10)
#     print("Worker - Done it")
#     return label + str(result)


# def main():
#     print("Main - Starting")
#     asyncio.run(do_something())
#     print("Main - Done")


# if __name__ == "__main__":
#     main()

# Main - Starting
# do_something - esperará por worker
# Worker - will take some time
# Worker - will take some time
# Worker - will take some time
# Worker - Done it
# Worker - Done it
# Worker - Done it
# do_something - result: C6
# do_something - result: A5
# do_something - result: B8
# Main - Done

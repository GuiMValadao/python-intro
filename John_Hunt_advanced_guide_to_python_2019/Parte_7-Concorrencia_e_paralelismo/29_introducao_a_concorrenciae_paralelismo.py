# Capítulo 29 - Introdução a concorrência e paralelismo
#
# Concorrência
# É definida pelo dicionário como:
#       'dois ou mais eventos ou circunstâncias acontecendo ou existindo ao mesmo tempo.'
# Na Ciência Computacional, concorrência refere-se à habilidade de partes
# diferentes de um programa, algoritmo ou problema serem executados ao mesmo
# tempo, potencialmente em múltiplos processadores ou múltiplos cores.
# Aqui, um processador se refere à unidade de processamento central(CPU, Central
# Processing Unit) ou um computador, enquanto 'core' se refere à ideia que um
# chip de CPU pode ter múltiplos cores ou processadores nele.
# Originalmente, um chip de CPU tinha um único core, isto é, o chip da CPU
# tinha uma única unidade de processamento nele. Entretanto, com o tempo, o
# aumento do desempenho de computadores, produtores de hardware acrescentaram
# cores, ou unidades de processamento, adicionais aos chips. Assim, um CPU
# dual-core tem duas unidades de processamento ou um quad-core tem 4 unidades.
# Isto significa que, no que refere-se ao sistema operacional do computador,
# existem múltiplas CPUs que podem executar programas.
# A execução de programas ao mesmo tempo em múltiplas CPUs pode melhorar
# substancialmente o desempenho de uma aplicação. Por exemplo, vamos assumir que
# temos um programa que chamará três funções independentes, sendo elas:
#   * fazer um backup dos dados atuais do programa,
#   * exibir(print) os dados armazenados atualmente no programa,
#   * executar uma animação usando os dados atuais.
# Vamos supor que essas funções são executadas em sequência, levando os seguintes tempos:
#   * o backup demora 13 s,
#   * a função print demora 15 s,
#   * a animação demora 10 s.
# Isto resulta num total de 38 s para a realização das três operações. Entretanto,
# as três funções são completamente independentes uma da outra. Isto é, os
# resultados e comportamento das outras não interferem em sua execução. Logo,
# podemos executar cada função concorrentemente.
# Se o sistema operacional e linguagem de programação em uso suportam múltiplos
# processos, então podemos, potencialmente, executar cada função em um processo
# separado ao mesmo tempo e obter uma melhora no tempo de execução total.
# Se as três funções iniciam no mesmo momento, o tempo máximo necessário para
# a continuação do processo principal é de 15 s, o tempo da função que demora mais.
# Entretanto, o programa principal pode ser capaz de continuar assim que as três
# funções iniciam pois não depende dos resultados de nenhuma delas; assim, o
# atraso pode ser negligível(apesar de normalmente haver algum delay quando cada
# processo inicia).
# -------------------------------------------------
# Paralelismo
# Uma distinção é, geralmente, feita na ciência computacional entre cocorrência
# e paralelismo:
#   * Na concorrência, tarefas separadas e independentes são realizadas, potencialmente, ao mesmo tempo.
#   * No paralelismo, uma tarefa grande e complexa é dividida em um conjunto de subtarefas.
#       As subtarefas representam uma parte do problema total. Cada subtarefa pode
#       ser executada ao mesmo tempo. Tipicamente, é necessário combinar os
#       resultados das subtarefas para gerar um resultado geral. Estas subtarefas
#       também são muito similares, se não funcionalmente idênticas.
# Assim, paralelismo é quando múltiplas cópias da mesma funcionalidade são executadas
# ao mesmo tempo, mas com diferentes dados.
# Alguns exemplos de onde o paralelismo pode ser aplicado incluem:
#   * Um motor de busca da web: sistemas deste tipo podem procurar por inúmeras
#       páginas da web. Cada vez que o faz, deve enviar um pedido ao site apropriado,
#       receber o resultado e processar os dados obtidos. Estes passos são os
#       mesmos independente do site procurado. Assim, os pedidos podem ser executados
#       sequencialmente ou em paralelo.
#   * Processamento de imagens: Uma imagem grande pode ser quebrada em fatias
#       de modo que cada fatia pode ser analisada em paralelo.
#
# ------------------------------------
# Distribuição
# Ao implementar uma solução concorrente ou paralela, onde os processos resultantes
# são executados é normalmente um detalhe da implementação. Conceitualmente,
# estes processos poderiam executar no mesmo processador, máquina física ou em uma
# máquina remota ou distribuída. Dessa forma, a distribuição, em que problemas
# são executados compartilhando o trabalho em diversas máquinas físicas, é
# frequentemente relacionada a concorrência e paralelismo.
# Entretanto, não existe requerimento para distribuir trabalho em várias
# máquinas físicas, e fazer isso de fato normalmente envolve trabalho extra.
# Para distribuir trabalho para uma máquina remota, dados e, em muitos casos,
# código, devem ser transferidos e disponibilizados à máquina remota. Isto pode
# resultar em atrasos significantes na execução do código remotamente e potencialmente
# perder quaisquer vantagens de performance por usar um compitador separado.
# Como resultado, muitas tecnologias concorrentes/paralelas padronizam executar
# código em um processo separado na mesma máquina.
# ---------------------------------------
# Computação de grade (Grid Computing)
# É baseada no uso de uma rede de computadores fracamente acoplados, na qual
# cada computador pode ter um trabalho submetido a ele, que executará até o
# final antes de retornar um resultado. Em muitos casos, a grade é composta de
# um conjunto heterogêneo de computadores (em vez de todos os computadores serem
# iguais) e podem estar dispersos geograficamente. Estes computadores pode ser
# compostos de máquinas físicas e virtuais.
# Uma máquina virtual é um pedaço de software que emula um computador inteiro
# e executa algum hardware que é compartilhado com outras máquinas virtuais. Cada
# VM(virtual machine/máquina virtual) pensa ser o único computador no hardware;
# entretanto, as VMs todas compartilham os mesmos recursos do computador físico.
# Múltiplas VMs podem, portanto, ser executadas em um mesmo computador físico.
# Cada VM fornece seu próprio hardware virtual, incluindo CPUs, memória,
# HDs, interfaces de rede e outros dispositivos. O hardware virtual é, então,
# mapeado para o hardware real na máquina física, o que diminui custos ao reduzir
# a necessidade de sistemas de hardware físico junto com os custos de manutenção
# associados, assim como reduz a demanda de energia e resfriamento de mútliplos
# computadores.
# Dentro de uma grade, software é usado para gerenciar nós da grade e submeter
# trabalhos para estes nós. Este software receberá os trabalhos a serem realizados
# (programas a serem executados e informação sobre o ambiente como quais bibliotecas
# usar) de clientes da grade. Estes trabalhos são, tipicamente, acrescidos à
# fila de trabalhos antes do organizador (scheduler) de trabalhos submetê-los
# a um nó da grade. Após resultados serem gerados pelo trabalho, são coletados
# do nó e retornados ao cliente.
# O uso de grades pode facilitar o uso de processos paralelo/concorrentes entre
# um grupo de máquinas físicas e virtuais.
# -------------------------------------------
# Concorrência e sincronização
# Concorrência relaciona-se à execução de múltiplas tarefas ao mesmo tempo.
# Em muitos casos, estas tarefas não tem relação entre si. Nestes casos, as tarefas
# separadas são completamente independentes e podem executar ao mesmo tempo sem
# qualquer interação.
# Em outras situações, múltiplas tarefas concorrentes podem precisar interagir;
# por exemplo, onde uma ou mais tarefas produzem dados e uma ou mais tarefas
# consomem aqueles dados. Isto é comumente referido como uma relação produtor-consumidor.
# Em outras situações, todos os processos paralelos devem ter chego ao mesmo ponto
# antes de outro comportamento ser executado.
# Outra situação que pode ocorrer é onde queremos garantir que apenas uma
# tarefa concorrente executa um pedaço de código sensível por vez; este código
# deve, portanto, ser protegido do acesso concorrente. Tanto bibliotecas
# de concorrência quanto de paralelismo tem recursos que permitem este tipo de sincronização.
# ---------------------------------------------
# Orientação a objetos e concorrência
# Os conceitos por trás da programação orientada a objetos são são facilmente
# transponíveis para os conceitos associados com concorrência. Por exemplo, um sistema
# pode ser descrito como um conjunto de objetos discretos se comunicando um com
# o outro quando necessário. Em Python, apenas um objeto pode executar em um
# dado momento no tempo dentro de um único interpretador. Entretanto, pelo menos
# conceitualmente, não há um motivo para que esta restrição seja reforçada.
# Os conceitos básicos por trás da orientação a objetos ainda se mantém, mesmo
# se cada objeto execute dentro de um processo independente separado.
# Tradicionalmente, uma mensagem enviada é tratada como uma chamada processual,
# em que a execução do objeto sendo chamado é bloqueada até que uma resposta
# seja retornada. Entretanto, podemos estender este modelo de modo simples para
# visualizar cada objeto como um programa executável concorrentemente, com
# atividade iniciando quando o objeto é criado e continuando mesmo após uma mensagem
# ser enviada para outro objeto (a menos que a resposta seja exigida para
# processamentos subsequentes). Neste modelo, podem existir muitos objetos(concorrentes)
# executando ao mesmo tempo. Claro, isto introduz problemas associados com a
# alocação de recursos etc, mas não mais que em qualquer sistema concorrente.
# Uma implicação do modelo de objetos concorrente é que objetos são maiores
# que na abordagem tradicional de thread única. Overheads como a necessidade de
# um scheduler para lidar com estas threads de execução e mecanismos de
# alocação de recursos significam que não é factível ter inteiros, caracteres,
# etc como processos separados.
# ----------------------------------------------
# Threads X Processos
# Como parte desta discussão, é útil entender o que quer-se dizer com um processo.
# Um processo é uma instância de um programa de computador que está sendo executada
# pelo sistema operacional. Qualquer processo tem três elementos chave: o programa
# sendo executado, os dados usados por aquele programa(como as variáveis) e o
# estado do programa (também conhecido como o contexto de execução do programa).
# Uma Thread(em Python) é um processo preventivamente leve.
# Uma Thread é considera preventiva pois toda thread tem uma chance de executar
# como a thread principal em algum ponto. Quando uma thread é executada, então
# será executada até:
#   * término;
#   * estar esperando alguma forma de entrada/saída(I/O);
#   * dormir por um período de tempo;
#   * executou por 15 ms (o ponto de corte atual em Python 3).
# Se a thread não completou quando uma das situações acima ocorreu, então
# desistirá de ser a thread em execução e outra thread será executada em seu
# lugar. Isto significa que uma thread pode ser interrompida no meio da realização
# de uma série de passos relacionados.
# Uma thread é considerada um processo leve pois não possui seu próprio
# endereço de espaço e não é tratada como uma entidade separada pelo sistema
# operacional host. Em vez disso, existe dentro de um único processo da máquina
# usando o mesmo endereço de espaço.
# É útil ter uma ideia clara da diferença entre uma thread e um sistema multiprocessos
# que usa processos separados no hardware.
# ---------------------------------
# Alguma terminologia:
#   * Invocações Assíncronas x Síncronas: a maioria dos métodos, funções ou
#       invocações de procedimentos que viu em programação representam invocações
#       síncronas. Uma chamada de método ou função síncrona é aquela que bloqueia
#       a execução do código que a chamou até retornar. Tais chamadas estão,
#       normalmente, dentro de uma única thread de execução. Chamadas assíncronas
#       são aquelas onde o fluxo de controle imediatamente retorna para o chamador,
#       que é capaz de executar sua própria thread de execução, permitindo tanto
#       o chamador como o chamado continuarem o processamento.
#   * Código não-bloqueador x bloqueador: código bloqueador é um termo usado para
#       descrever o código executando em uma thread de execução, esperando por
#       alguma atividade ser finalizada que cause uma ou mais threads de execução
#       separadas serem atrasadas. Por exemplo, se uma thread é o produtor de
#       algum dados e outras threads são consumidoras daqueles dados, então
#       as threads consumidoras não podem continuar até a produtora gerar os dador
#       para serem consumidos. Ao contrário, não-bloquador significa que nenhuma
#       thread estará sujeita a atrasos.
#   * Código concorrente x paralelo: Ambos tipos são similares, mas com um aspecto
#       crucial diferente: concorrência indica que duas ou mais atividades estão
#       tendo progrsso mesmo que não sejam executadas no mesmo momento. Isto
#       é normalmente conseguido pela troca contínua de processos competindo entre
#       execução e não-execução. Isto é repetido até que pelo menos uma das
#       threads de execução completou sua tarefa. Isto pode ocorrer pois duas
#       threads estão compartilhando o mesmo processador físico com cada uma
#       sendo dada um curto período de tempo para progredir antes da outra receber
#       um pequeno período de tempo para progredir. As duas threads são ditas
#       que compartilham o tempo de processamento usando uma técnica conhecida como
#       fatiamento temporal. Paralelismo, por outro lado, implica que existem
#       mútliplos processadores disponíveis permitindo cada thread executar em seu
#       próprio processador simultaneamente.

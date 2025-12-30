# Capítulo 35 - Introdução à programação reativa
#
# Programação Reativa é um jeito de escrever programas que permite o sistema
# reagir a dados sendo publicados nele. Vamos olhar a biblioteca RxPy que
# fornece uma implementação em Python da abordagem ReactiveX à Programação Reativa.
# -----------------------------------------------------------
# Uma aplicação reativa deve reagir a dados; normalmente, ou à presença de
# dados novos, ou a mudanças em dados existentes. O 'Reactive Manifesto' apresenta
# as características chave de sistemas reativos, como:
#   * responsivo: significa que sistemas respondem em tempo hábil. Aqui,
#       claro, 'hábil' diferirá dependendo da aplicação e domínio; em uma
#       situação, um segundo pode ser hábil, enquanto em outra pode ser
#       muito demorado.
#   * resiliente: tais sistemas permanecem responsivos mesmo diante de falhas.
#       Os sistemas devem, portanto, ser projetados para lidar com falhas de
#       maneira elegante e continuar o trabalho apropriadamente após a falha.
#   * elástico: conforme a carga de trabalho cresce, o sistema deveria continuar
#       a ser responsivo.
#   * guiado por mensagem: informação é trocada entre elementos de um sistema
#       reativo usando mensagens. Isto garante acoplamento fraco, isolamento e
#       transparência local entre esses componentes.
# Como um exemplo, considere uma aplicação que lista um conjunto de valores
# do Equity Stock Trade baseado nos valores dos dados mais recentes. Esta
# aplicação poderia apresentar o valor atual de cada negócio dentro de uma
# tabela. Quando novos dados de preços de ações forem publicados, então a
# aplicação deve atualizar o valor do negócio dentro da tabela. Tal
# aplicação pode ser descrita como sendo reativa.
# Programação Reativa é um estilo de programação (normalmente apoiado por
# bibliotecas) que permite que o código seja escrito seguindo as ideias de
# sistemas reativos.
# ------------------------------------------
# O projeto ReactiveX
#
# ReactiveX é a melhor implementação conhecida do paradigma de Programação
# Reativa. É baseado no padrão de projeto(design) Observer-Obervable.
# Entretanto, é uma extensão a esse projeto pois estende o padrão de modo que
# a abordagem apoia sequências de dados e/ou eventos e acrescenta operadores
# que permitem que desenvolvedores componham sequências declarativamente
# enquanto abstraindo preocupações associadas a threads de baixo-nível, sincronização,
# estruturas de dados concorrentes e I/O não-bloqueador.
# O projeto ReactiveX tem implementações para muitas linguagens incluindo
# RxJava, RxScala e RxPy; a última é a versão para Python. RxPy é descrito como:
#   Uma biblioteca para composição de programas assíncronos e baseados em eventos
#   usando coleções Observáveis e funções de operador de consulta em Python.
# ---------------------------------------------
# O Padrão Observador
# O Padrão Observador é um dos conjuntos de Padrões de Design da Gang of Four.
# Os padrões são chamados assim pois seu livro em padrões de design foi
# escrito por 4 autores famosos:Erich Gamma, Richard Helm, Ralph Johnson e John Vlissides.
# O Padrão Observador fornece um meio de garantir que um conjunto de objetos
# é notificado sempre que o estado de outro objeto seja alterado. Tem sido amplamente
# usado em várias linguagens (como Smalltalk e Java), incluindo Python.
# A intenção do Padrão Observador é gerenciar uma relação de 1 para muitos
# entre um objeto e aqueles objetos interessados no estado, e em particular
# alterações de estado, daquele objeto. Assim, quando o estado o objeto
# é alterado, os objetos interessados(dependentes) são notificados daquela
# mudança e podem tomar qualquer ação que for apropriada.
# Existem dois papeis chave dentro do Padrão Observador, sendo o Observável
# e o Observador.
#   * Observável: O objeto responsável por notificar outros objetos que uma
#       alteração em seu estado ocorreu.
#   * Observador: Um observador é um objeto que será notificado da alteração
#       de estado do observável e pode tomar a ação apropriada.
# Além disso, o estado normalmente é representado explicitamente:
#   * Estado: Este papel pode ser desempenhado por um objeto que é usado
#       para compartilhar informação sobre a alteração no estado que ocorreu
#       dentro do Observável. Isto poderia ser tão simples quanto uma String
#       indicando o novo estado do Observável ou poderia ser um objeto
#       orientado a dados que fornece informações mais detalhadas.
# É comum que um observável apenas publique dados quando há um Observador disponível
# para processar aqueles dados. O processo de registrar com um Observável é
# referido como assinatura(subscribing). Assim, um Observável terá zero ou
# mais assinantes (Observadores).
# Se o Observável publica dados em uma velocidade maior do que pode ser processado
# pelo Observador, então os dados são enfileirados pelo Fluxo de Dados(Data Stream).
# Isto permite que o Observador processe os dados recebidos um de cada vez
# em seu próprio tempo, sem se preocupar com perda de dados(desde que o fluxo
# tenha memória disponível suficiente).
# --------------------------------------------------
# Observáveis Quente e Frio
# Outro conceito útil é o de Observáveis quente e frio:
#   * Observáveis frios são preguiçosos. Isto é, apenas publicará dados se pelo
#       menos um Observador for assinante.
#   * Observáveis Quentes, por outro lado, publicarão dados independente da
#       presença de um Observador assinante ou não.
# ------------------------------------------
# Observáveis Frios
# Além de precisar de pelo menos um assinante para publicar dados, um Observável
# Frio apenas fornecerá dados a um Observador quando o Observador estiver pronto
# para processar os dados; isto pois a relação Observável-Observador é mais
# de puxar(pull). Por exemplo, dado um Observável que gerará um conjunto de
# valores baseados em um alcance, então aquele Observável gerará cada resultado
# preguiçosamente quando pedido por um Observador.
# Se o Observador levar algum tempo para processar os dados emitidos pelo Observável,
# então o Observador esperará até o Observador estar pronto para processar os
# dados antes de emitir outro valor.
# -----------------------------------------
# Observáveis Quentes
# Quando um Observador registra com o Observável Quente, começará a receber dados
# naquele ponto, conforme e quando o Observável publicar novos dados. Se o
# Observável já publicou items de dados anteriores, então estes terão sido
# perdidos e não serão recebidos pelo Observador.
# A situação mais comum na qual um Observador Quente é criado é quando a fonte
# produtora representa dados que podem ser irrelevantes se não forem processados
# imediatamente ou podem ser substituídos por dados subsequentes. Por exemplo,
# dados publicados por um feed de Preços de Mercado de Ações cairiam nessa
# categoria. Quando um Observável encapsula em torno deste feed de dados, pode
# publicar esses dados independentemente de haver um Observador inscrito.
# --------------------------------------
# Implicações de Observáveis Quentes e Frios
# É importante saber se você tem um Observável Quente ou Frio pois isso pode
# impactar no que pode ser assumido sobre os dados fornecidos aos Observadores
# e assim como você precisaria projetar sua aplicação. Se é importante que nenhum
# dado seja perdido, então deve-se tomar cuidado para garantir que os inscritos
# estão no lugar antes de um Observável Quente comece a publicar dados.
# -----------------------------------
# Diferenças entre Programação Guiada por Eventos e Programação Reativa
# Na programação guiada por eventos, um evento é gerado em resposta a
# algo acontecendo; o evento, então, representa isto com qualquerdado associado.
# Por exemplo, se o usuário clicar o mouse, então um MouseClickEvent poderia
# ser gerado. Este objeto normalmente armazenarpa informação sobre as coordenadas
# x e y do mouse junto com qual botão foi clicado etc. Então, é possível
# associar algum comportamento com este evento de modo que se o evento ocorrer,
# a operação associada é invocada com o objeto evento como parâmetro. Esta é
# a abordagem usada na biblioteca wxPython apresenta nos capítulos iniciais.
# Na programação reativa, um Observador é associado com um observável. Qualquer
# dado gerado pelo Observável será recebido e manipulado pelo Observador.
# Isto é verdade independente de qual dado seja, como o Observador é um
# manipulador de dados gerados pelo Observável em vez de um manipulador de um
# tipo de dado específico(como na abordagem de Eventos).
# Ambas abordagens poderiam ser usadas em muitas situações. Por exemplo,
# poderíamos ter um cenário em que algum dado deve ser processado sempre
# que o preço de uma ação sofra alteração.
# Isto poderia ser implementado usando um StockPriceChangeEvent associado
# a um StockPriceEventHandler. Poderia também ser implementado por um
# StockPriceChangeObservable e um StockPriceChangeObserver. Em ambos os casos,
# um elemento lida com os dados gerados pelo outro elemento. Entretanto, a
# biblioteca RxPy simplifica este processo e permite que o Observador execute
# na mesma Thread ou em uma Thread separada que o Observável com apenas uma
# pequena alteração no código.
# ----------------------------------------------
# Vantagens da programação reativa
#   * Evita múltiplos métodos de callback: os problemas associados ao uso de
#       callbacks são, às vezes, referidos como 'inferno callback'. Isto pode
#       ocorrer quando há várias callbacks, todas definidas para executar em
#       resposta a algum dado sendo ferado ou alguma operação completando.
#       Pode ser difícil entender, manter e depurar tais sistemas.
#   * Execução mais simples assíncrona e multithreaded: A abordagem adotada
#       por RxPy torna fácil executar operações/comportamento dentro de um
#       ambiente de várias threads com funções assíncronas independentes.
#   * Operadores disponíveis: A biblioteca RxPy tem vários operadores embutidos
#       que tornam o processamento dos dados criados pelo Observável muito mais fácil.
#   * Composição de dados: É simples compor novos fluxos de dados a partir
#       de dados fornecidos por dois ou mais Observáveis para processamento
#       assíncrono.
# ---------------------------------------------
# Desvantagens da programação reativa
# É fácil complicar as coisas quando se começa a conectar operadores.
# Se usar muitos operadores, ou um conjunto de funções muito complexas com
# os operadores, pode ficar difícil de entender o que está ocorrendo.
# Muitos desenvolvedores acham que programação reativa é inerentemente
# multithreaded; isto não é necessáriamente verdade; de fato, a RxPy é
# de 1 thread por padrão. Se um aplicativo precisar de comportamento que
# deve ser executado assíncronamente, isso precisa ser explicitamente indicado.
# Outro problema de frameworks de programação reativa é que pode se tornar
# intensivo em termos de memória para guardar fluxos de dados.

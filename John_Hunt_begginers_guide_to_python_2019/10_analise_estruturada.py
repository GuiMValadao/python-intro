# Analise/design estruturada/o
# Ha varios metodos especificos e bem documentados, alguns deles sendo
# SSADM (Structured SystemsAnalysis and Design Method e o metodo estruturado Yourden
# Foco nos dois elementos principais da maioria dos metodos de analise estruturada
# Decomposiçao funcional e Analise de fluxo de dados
#--------------------------------------------------------
# O metodo de analise estruturada geralmente utiliza uma abordagem
# orientada a processos (com um conjunto de passos ou estagios prescritos)
# que, de um jeito ou outro considera quais sao as entradas e saidas de
# um sistema e como as entradas se tranformam nas saidas.
# Para isso usa-se a aplicaçao de uma ou mais funçoes.
# Essas funçoes sao identificadas e divididas em funçoes menores ate
# atingir um nivel adequado de detalhe. Este processo e conhecido como
# Decomposiçao Funcional.
#---------------------------------------------------------
# Decomposiçao Funcional
# E um modo como um sistema pode ser dividido em suas partes
# constituentes. Por exemplo, para um sistema de pagamento computacional
# decidir quanto cada empregado pago deve receber pode ser necessario:
#   1 - Carregar os detalhes dos empregados de um arquivo permanente (como um arquivo ou base de dados).
#   2 - Carregar quantas horas o empregado trabalhou na semana (possivelmente de outro sistema que grava o numero de horas trabalhada).
#   3 - Multiplicar as horas pelo preço por hora do empregado.
#   4 - Gravar quanto o empregado deve ser pago em uma base de dados ou arquivo de pagamentos.
#   5 - Imprimir o contracheque do empregado.
#   6 - Transferir o valor apropriado da conta do empregador para a conta do empregado.
#   7 - Gravar na base de dados de pagamentos que todos os passos foram completos.
# Cada um dos passos acima poderia representar uma funçao realizada pelo sistema.
# Cada uma dessas funçoes, por sua vez, poderiam ser divididas em funçoes de niveis menores.
# Isto e conhecido tambem como abordagem de refinamento de cima a baixo (top-bottom).
# O termo 'refinamento de cima a baixo' destaca a ideia de dividir um sistema em suas
# componentes menores.
# E comum representar as funçoes identificadas como uma arvore ilustrando
# as relaçoes entre as funçoes de maior nivel com as de menor nivel.
#                                   |-- Emitir cartao de credito    |- Revisar por conformidade-----|- Revisar comparando com as regras internas
#   Aplicaçao de cartao de credito -|-- Revisar aplicaçao ----------|                               |- Checar o credito
#                                   |-- Submeter aplicaçao          |- Checar dados fornecidos
#------------------------------------------------------------
# Terminologia da Decomposiçao Funcional
# - FUNÇAO: Tarefa realizada por um dispositivo, sistema ou processo
# - DECOMPOSIÇAO: Processo pelo qual funçoes de alto nivel sao divididas em funçoes de nivel menor
# - FUNÇAO DE NIVEL MAIOR: Esta e uma funçao que tem uma ou mais subfunçoes.
# - SUBFUNÇAO: Esta e uma funçao que fornece algum elemento do comportamento de uma funçao de nivel maior; tambem pode ser dividida em suas proprias subfunçoes
# - FUNÇAO BASICA: Funçao que nao tem subfunçoes.
#------------------------------------------------------------
# Processo de Decomposiçao Funcional
# Em um nivel muito alto, consiste em uma serie de passos como os descritos abaixo:
# 1 - Encontrar/Identificar as entradas e saidas do sistema.
# 2 - Definir como as entradas sao convertidas nas saidas.
# 3 - Olhar na funçao atual e tentar dividi-la em uma lista de subfunçoes. Identificar o que cada subfunçao deve fazer e quais suas entradas e saidas sao.
# 4 - Repetir o passo 2 para cada funçao identificada ate as funçoes identificadas nao puderem ou deverem mais ser divididas.
# 5 - Desenhar um diagrama da hierarquia de funçoes criadas. Visualizar as funçoes e suas relaçoes e algo bastante util pois permite que desenvolvedores visualizem o sistema funcionalmente.
# 6 - Examinar o diagrama por quaisquer funçoes repetidas. Isto e, que faze a mesma coisa mas aparecem em diferentes lugares no diagrama.
# 7 - Refinar/Estilizar(Design) as interfaces entre uma funçao e outra. Isto e, qual dado/informaçao e passada para e de uma funçao para uma subfunçao assim como entre funçoes.
#-----------------------------------------------------------
# Exemplo de calculadora de Decomposiçao Funcional
# Queremos que uma calculadora execute um conjunto de operaçoes matematicas em dois numeros, como +, -, /, *.
# Podemos desenhar um Diagrama de Decomposiçao Funcional (FDD) como:
#                   |-- Adiçao
# Calculadora ------|-- Subtraçao
#                   |-- Multiplicaçao
#                   |-- Divisao
# Podemos, entao, identificar a necessidade de uma operaçao para entrar dois numeros ser adicionada.
#                   |-- Entrar dois numeros-----|-- Entrar o primeiro numero
#                   |-- Adiçao                  |-- Entrar o segundo numero
# Calculadora ------|-- Subtraçao
#                   |-- Multiplicaçao
#                   |-- Divisao
# Tambem e necessario determinar qual operaçao numerica deve ser escolhida baseada na entrada do usuario.
# Esta funçao pode ser colocada acima das funçoes numericas ou ao seu lado. Isto e um exemplo de decisao de estilo que o
# estilista/desenvolvedor deve fazer baseado no seu entendimento do problema e como o software sera desenvolvido/testado/usado etc.
#                   |-- Selecionar operaçao
#                   |-- Entrar dois numeros-----|-- Entrar o primeiro numero
#                   |-- Adiçao                  |-- Entrar o segundo numero
# Calculadora ------|-- Subtraçao
#                   |-- Multiplicaçao
#                   |-- Divisao
#---------------------------------------------------
# Fluxo funcional
# O FDD mostra a hierarquia entre as funçoes, mas nao como os dados fluem entre elas nem a ordem em que sao chamadas.
# Ha varias abordagens para descrever as interaçoes entre as funçoes identificadas pela decomposiçao funcional, incluindo
# o uso de pseudocodigo, diagramas de fluxo de dados e diagramas sequenciais.
# - Pseudo codigo: E uma forma de ingles estruturado que nao esta presa a nenhuma
#                  linguagem de programaçao particular, mas que pode ser usado para expressar ideias simples incluindo
#                  escolhas condicionais e iteraçoes. Como  esta em uma pseudolinguagem, o desenvolvedor nao esta preso
#                  a uma sintaxe especifica e pode incluir funçoes sem definilas detalhadamente.
# - Diagramas de fluxo de dados: Sao usados para mapear as entradas, processos e saidas  das funçoes em uma forma grafica estruturada.
#                                Um diagrama de fluxo de dados tipicamente nao tem um fluxo de controle, regras de decisao ou loops.
#                                Para cada fluxo de dados, deve haver pelo menos uma entrada e um ponto final.
# - Diagramas sequenciais: Estes sao usados para representar iteraçoes entre entidades diferentes (ou objetos) em sequencia.
#                          AS funçoes chamadas sao representadas como sendo chamadas de uma entidade para outra. Tipicamente usados com sistemas orientados por objeto.
#-----------------------------------------------------
# Diagramas de fluxo de dados (DFD)
# Consiste em um conjunto de entradas e saidas, processos(funçoes), fluxos, armazenamentos/armazens de dados (data stores/warehouses) e terminadores.
# - Processos: Este e o processo(ou funçao ou transformaçao) que converte entradas em saidas. O nome do processos deve ser descritivo indicando o que faz.
# - Fluxo de dados: O fluxo indica a transferencia de dados/informaçao de um elemento a outro (isto e, o fluxo tem direçao). O fluxo deveria ter um nome
#                  que indica qual informaçao/dado esta sendo trocado. Fluxo conecta processos, armazens de dados e terminadores.
# - Armazenamento/armazens de dados: O armazenamento de dados (que pode ser algo como um arquivo, pasta, base de dados ou outro repositorio de dados) e usado para guardar
#                                   dados para uso posterior. O nome do armazenamento de dados e um substantivo plural. O fluxo do armazenamento de dados geralmente representa
#                                   a leitura dos dados guardados na armazenamento de dados, e o fluxo para o 'waredata storehouse' feralmente expressa a entrada de dados ou atualizaçao.
# - Terminador: O terminador representa uma entidade exterior (ao sistema) que comunica-se com o sistema. Exemplos de entidades podem ser usuarios humanos ou outros sistemas etc.
# Um exemplo de diagrama de fluxo de dados e dado abaixo usando as funçoes identificadas para a calculadora:
#               Usuario -------------> Calculadora-----------------> Usuario                                Nivel 0
#                                          \/
#                    /------------------------------------------------------------\
#                       /-----------------------\
#               Usuario -->Seleçao de operaçoes-->Entrar numeros --> Adicionar --> Usuario                  Nivel 1
#                                                    \/
#                           /-------------------------------------------\
#                       Usuario --> Entrar o primeiro numero --> Entrar o segundo numero                    Nivel 2
#------------------------------------------------------------
# Mapas de fluxo (Flowcharts)
# Um mapa de fluxo e uma representaçao grafica de um algoritmo, fluxo de trabalho ou processo para um dado problema.
# Mapas de fluxo sao usados na analise, projeto(design) e documentaçao de sistemas de software.
# Assim como outras formas de notaçao (como DFD) mapas de fluxo ajudam projetistas e desenvolvedores a visualizar os passos
# envolvidos em uma soluçao e assim auxiliar no entendimento dos processos e algoritmos envolvidos.
# Os passos no algoritmo sao representados como varios tipos de caixas. O ordenamento dos passos e indicado por flechas
# entre as caixas. O fluxo de controle e representado por caixas de decisao.
#   /-----\
#   |     |     Terminal            ------->    Fluxo
#   \-----/
#   ---------                        --------
#   |       |   Processo            ||      ||  Processo predeterminado
#   ---------                        --------
#       /\                          /-------/
#      /  \     Decisao            |       |    Dado armazenado
#      \  /                         \-------\
#       \/
#       /-------/                     |-----|
#      /       / Entrada/Saida        |     |   Conector fora da pagina
#     /-------/                          \/
# O significado destes simbolos e dado abaixo:
# - Terminal:   Indica o inicio ou fim de um programa ou subprocesso. Geralmente contem as palavras
#               'Inicio', 'Fim', 'Parar' ou uma frase indicando o inicio ou fim de alguns processos como 'Iniciar execuçao de 'print'
# - Processo:   Este simbolo representa uma ou mais operaçoes (ou declaraçoes/expressoes de programaçao) que, de um jeito ou outro
#               aplicam um comportamento ou mudam o estado do sistema. Por exemplo, eles podem adicionar dois numeros, executar algum calculo ou mudar o tipo de um booleano.
# - Decisao:    Representa um ponto de decisao no algoritmo; isto e, representa um ponto de decisao que vai alterar o fluxo do programa
#               (tipicamente entre dois caminhos diferentes). O ponto de decisao e frequentemente representado como uma questao com uma resposta sim/nao e
#               isto e indicado no mapa de fluxo pelo uso de etiquetas sim(ou 'yes', 'y') e nao (ou 'no', 'n') no mapa de fluxo; Em Python, este ponto de decisao pode
#               ser implementado usando uma declaraçao 'if'.
# - Entrada/Saida:  Esta caixa indica a entrada ou saida de dados do algoritmo. Isto pode representar a obtençao de entrada do usuario ou a exibiçao de resultados.
# - Fluxo:      Estas flechas sao usadas para representar a ordem de execuçao das caixas.
# - Processo predeterminado:    Representa um processo que foi definido em outro lugar.
# - Dado armazenado:    Representa que dados foram armazenados em alguma forma de sista de armazenamento persistente.
# - Conector fora da pagina:    Um conector etiquetado para uso quando o alvo esta em outra pagina(outro mapa de fluxo).


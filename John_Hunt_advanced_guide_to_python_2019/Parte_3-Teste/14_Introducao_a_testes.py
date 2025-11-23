# Capítulo 14 - Introdução a testes

# Este capítulo conosidera diferentes tipos de testes que você poderia querer realizar
# com os sistemas que desenvolver em Python. Também introduz Desenvolvimento Baseado
# em Testes.
# ------------------------------------------
# Tipos de testes
# Existem pelo menos duas formas de pensar sobre testes:
#   1 - É o processo de executar um programa com a intenção de encontrar erros/bugs
#   2 - É um processo usado para estabelecer quais componentes de software cumprem
#       os requerimentos identificados para eles, isto é, que fazem o que deveriam.
# Estes dois aspectos de testes tendem a ser enfatizados em diferentes pontos do ciclo
# de vida do software. Teste de Erros é uma parte intrínseca do processo de desenvolvimento.
# e uma ênfase crescente está sendo depositada em fazer testes uma parte central do
# desenvolvimento de software.
# Deve ser notado que é extremamente difícil, e, em muitos casos, impossível, provar que
# um software funciona e é completamente livre de erros. O fato que um conjunto de testes
# não encontra defeitos não prova que o software seja livre de erros.
# Testar para estabelecer que os componentes de software cumprem seu contrato envolve
# checar operações contra suas exigências. Apesar disto acontecer no momento do desenvolvimento,
# forma uma parte principal da cartificação de qualidade (QA, Quality Assurance) e
# teste de aceitação dos usuários. Deveria ser notado que, com o advento do Desenvolvimento
# Baseado em Testes, a ênfase em teste comparado aos requerimentos durante desenvolvimento
# tem se tornado significantemente maior.
# Existem, claro, muitos outros aspectos de testagem, por exemplo, Testagem de Desempenho,
# que identifica como um sistema desempenhará conforme vários fatores que afetam aquele
# sistema mudam. Por exemplo, conforme o número de requisições aumentam, conforme o
# número de processadores usados pelo hardware subjacente muda, conforme o tamanho da
# base de dados cresce etc.
# Independente de como visualizar a testagem, quanto mais testes são aplicados a um
# sistema, maior o nível de confiança que o sistema funcionará como requisitado.
# ---------------------------------------
# O que deve ser testado?
# Em geral, tudo que é repitível deveria ser sujeito a testagem formal (e idealmente
# automatizada). Isso inclui, mas não é limitado a:
#   * O processo de construção para todas as tecnologias envolvidas
#   * O processo de entrega para todas as plataformas sob consideração
#   * O processo de instalação para todos os ambientes de execução
#   * O processo de atualização para todas as versões suportadas
#   * A performance do sistema/servidores conforme as cargas aumentam
#   * A estabilidade para sistemas que devem executar para algum período de tempo (como sistemas 24x7)
#   * Os processos de backup
#   * A segurança do sistema
#   * A habilidade de recuperação do sistema após ocorrência de falhas
#   * A funcionalidade do sistema
#   * A integridade do sistema
# Note que os últimos dois items acima poderiam ser o que é comumente considerado como
# áreas que seriam submetidas a testes. Entretanto, para garantir a qualidade do
# sistema sob consideração, todos os item são relevantes. De fato, testes deveriam cobrir
# todos os aspectos do ciclo de vida de desenvolvimento de software e não apena a fase QA.
# Durante levantamento de requisitos, teste é o processo de procurar por requisitos
# ausentes ou ambíguos. Durante esta fase, considerações também deveriam ser feitas
# com relação a como os requisitos gerais serão testados, no sistema final.
# Planejamento de testes também deveria olhar para todos os aspectos do software sob
# teste para funcionalidade, usabilidade, concordância lega, conformância com restrições
# regulamentadores, segurança, desempenho, disponibilidade, resiliência etc. Testes
# deveriam ser guiados pela necessidade de identificar e reduzir riscos.
# -------------------------------------------------
# Testar sistemas de software
# Existem diversos tipos de testes que são comumente usados dentro da indústria. São eles:
#   * Teste unitário - usado para verificar o comportamento de componentes individuais
#   * Teste de integração - testa quando componentes individuais são combinadas para
#       fornecer unidades funcionais de niveis maiores e que essa combinação funciona.
#   * Teste de regressão - quando novos componentes são acrescentados ao sistema, ou
#       componentes existentes são alteradas, se é necessário verificar que novas
#       funcionalidades não quebram outras existentes.
#   * Teste de desempenho - usado para garantir que o desempenho do sistema é como
#       requisitado e, dentro dos parâmetros de desenvolvimento, é capaz de ser escalado
#       coforme seu uso aumenta.
#   * Teste de estabilidade - representa um estilo de teste que tenta simular a operação
#       do sistema sobre um período de tempo prolongado. Por exemplo, para um aplicativo
#       de compras online que seja esperado funcionar 24x7, um teste de estabilidade
#       poderia garantir que, com uma carga média, o sistema pode, de fato, executar
#       24 horas por dia, 7 dias por semana.
#   * Teste de segurança - garante que acesso ao sistema é controlado de maneira apropriada
#       dados os requisitos. Por exemplo, um sistema de compras online pode ter requisitos
#       de segurança diferentes dependendo se você está olhando a loja, comprando alguns
#       produtos ou mantendo o catálogo de produtos.
#   * Teste de usabilidade - pode ser realizado por um grupo especializado em utilização
#       e pode envolver filmagem de usuário enquando utilizam o sistema.
#   * Teste de sistema - valida que o sistema como um todo de fato cumpre os requisitos
#       dos usuários e está em conformidade com a integridade exigida da aplicação.
#   * Teste de Instalação, deployment e atualização - Estes três tipos de teste validam
#       que um sistema pode ser instalado e deployed apropriadamente incluindo quaisquer
#       processos de atualização que possam ser necessários.
#   * Testes fumaça - usados para checar que os elementos centrais de um grande sistema
#       operam corretamente. Eles podem, tipicamente, ser executados rapidamente e em
#       uma fração do tempo necessário para executar testes de sistema completos.
# ---------------------------------------------
# Teste unitário/de unidade
# Uma unidade pode ser tão pequena quanto uma única função ou tão grande quanto um
# subsistema, mas tipicamente é uma classe, objeto, biblioteca auto-contida(API) ou
# página da internet.
# Olhando em um componente pequento auto-contido, um grande conjunto de testes pode ser
# desenvolvido para exercitar os requisitos e funcionalidades definidos da unidade.
# Teste unitário tipicamente segue uma abordagem 'caixa branca'(também chamada Caixa
# de Vidro ou testagem estrutural), onde o teste utiliza conhecimento e entendimento do
# código e sua estrutura em vez de apenas sua interface (que é conhecida como abordagem
# 'caixa preta').
# Na testagem 'caixa branca', a cobertura de teste é medida pelo número de caminhos de
# código que foram testados. O objetivo do teste unitário é fornecer 100 % cobertura:
# exercitar todas as instruções, todos os lados de ramos lógicos, todos os objetos
# chamados, resolução de todas as estruturas de dados, término normal e anormal de todos
# os loops etc. Claro, isto pode nem sempre ser possível, mas é um objetivo que sempre
# deveria ser almejado. Muitas ferramentas de teste automatizadas incluirão uma medida da
# cobertura de código de modo que você esteja ciente de quanto código foi exercitado por
# qualquer conjunto de testes.
# Testagens unitárias é quase sempre automatizada - existem muitas ferramentas para ajudar
# com isto, talvez a mais conhecida sendo a família de estrutura de testes xUnit como
# JUnit para Java e PyUnit para Python. A estrutura permite que desenvolvedores:
#   * foquem no teste da unidade
#   * simulam dados ou resultados chamando outra unidade
#   * criam testes guiados por dados para máxima flexibilidade e repetibilidade
#   * dependem de objetos teste(mock) que representam elementos fora da unidade com que devem interagir
# Tendo os testes automatizados significa que podem ser executados frequentemente,
# no mínimo após o desenvolvimento inicial e após cada mudança que afeta a unidade.
# Após se estabelecer confiança no funcionamento correto de uma unidade, desenvolvedores
# podem, então, usá-la para ajudar a testar outras unidades com as quais ela tem
# interfaces, formando unidades maiores que também podem ser testadas unitariamente ou,
# conforme a escala aumenta, serem postas para Testes de Integração.
# ---------------------------------------------------
# Testes de integração
# É onde várias unidades(ou módulos), são agrupados para teste como uma entidade por
# si próprios. Tipicamente, teste de integridade objetiva garantir que módulos interajam
# corretamente e os desenvolvedores das unidades individuais interpretaram os requisitos
# de forma consistente. Um conjunto de módulos integrados pode ser tratado como uma
# unidade e testado unitariamente da mesma forma que os módulos constituintes, mas geralmente
# funcionando em um nivel mais 'alto' de funcionalidade. Teste de integração é o estágio
# intermediário entre teste unitário e teste do sistema completo.
# Portanto, os testes de integração focam na interação entre dusa ou mais unidades para
# garantir que aquelas unidades funcionam junto com sucesso e apropriadamente. Tais testes
# são tipicamente conduzidos do baixo para cima, mas também podem ser conduzidos de
# cima para baixo usando 'mocks' ou 'stubs' para representar funções já chamadas ou que serão
# chamadas. Um ponto importante é que não se deveria querer testar tudo junto de uma vez
# (chamado testagem 'Big Bang') como é mais difícil isolar bugs de uma forma que eles
# possam ser corrigidos. Por isso é mais comum descobrir que teste de integração
# foi realizado em um estilo de baixo para cima.
# ----------------------------------------------------
# Teste de sistema
# Testes de sistema objetivam validar que a combinação de todos os módulos, unidades,
# dados, instalação, configuração etc. operam apropriadamente e cumpre os requisitos
# especificados para o sistema inteiro. Testar o sistema como um todo tipicamente
# envolve testar a funcionalidade ou comportamento mais altas do sistema. Tais testes
# Baseados em Comportamento frequentemente envolvem usuários finais e outros interessados
# que são menos técnicos. Para suportar tais testes várias tecnologias evoluiram para pemitir
# um estilo de teste mais descritivo em inglês. Este estilo de teste pode ser usado como
# parte do processo de levantamento de requisitos e pode levar a um processo de
# Desenvolvimento Baseado em Comportamento (BDD). O módulo pytest-bdd fornece uma extensão
# no estilo BDD para o centro do framework pytest.
# ---------------------------------------------
# Teste de Instalação/Atualização
# Teste de instalação é o teste do processo de instalação completo, parcial ou de upgrade.
# Também valida o software de instalação e transição necessários para mover para a nova versão
# do produto estão funcionando. Tipicamente:
#   * verifica que o software pode ser completamente desinstalado pelo processo de desistencia(back-out)
#   * determina quais arquivos são adicionados, mudados ou deletados no hardware no qual
#       o programa foi instalado.
#   * determina se algum outro programa no hardware é afetado pelo novo software
#       que foi instalado.
#   * determina se o software instala e opera corretamente em todas as plataformas
#       de hardware e sistemas operacionais nos quais deverá funcionar.
# ---------------------------------------------
# Testes fumaça
# Um teste fumaça é um teste ou grupo de testes projetados para verificar que os
# fundamentos do sistema funcionam. Testes de fumaça podem ser executados contra um
# novo lançamento(deployment) ou um lançamento modificado para poder verificar que a
# instalação se desempenha bem o suficiente para justificar testes subsequentes.
# Falha em passar um teste fumaça parariam qualquer teste seguinte até o teste fumaça
# passar. O nome é derivado dos dias iniciais da eletrônica: se um dispositivo começasse
# a fumacear após ter sido ligado, os testadores sabiam que não fazia sentido continuar
# testando. Para tecnologias de software, as vantagens de realizar testes de fumaça
# incluem:
#   * Testes fumaça são normalmente automatizados e padronizados de uma versão para outra.
#   * Como testes fumaça validam coisas que se espera que funcionem, quando falham, é
#       geralmente uma indicação que alguma coisa fundamental deu errado(a versão errada
#       de uma biblioteca foi usada) ou que uma nova versão introduziu um bug nos
#       aspectos centrais do sistema.
#   * Se um sistema é construído diariamente, deveria passar por testes de fumaça diariamente.
#   * Será necessário, periodicamente, acrescentar testes fumaça conforme novas
#       funcionalidades são adicionadas ao sistema.
# ---------------------------------------------
# Teste automatizado
# A forma real em que testes são escritos e executados precisa de consideração cuidadosa.
# Em geral, queremos automatizar tudo que for possível do processo de teste pois isso
# facilita a execução dos testes e também garante que não apenas todos os testes são
# executados, mas são executados da mesma forma cada vez. Além disso, uma vez que um
# teste automatizado é configurado, será, tipicamente, mais rápido de re-executar
# aquele teste automatizado que repetir manualmente uma série de testes. Entretanto,
# nem todos os recursos de um sistema podem ser facilmente testados via teste uma
# ferramenta de teste automatizada e, em alguns casos, o ambiente físico pode tornar
# difícil automatizar os testes.
# Tipicamente, a maioria dos testes unitários são automatizados e a maior parte do
# teste de aceitação é manual. Você também precisará decidir quais formas de teste
# devem ser feitas. A maioria dos projetos de software deveria ter testes unitários,
# testes de integração, teste de sistema e teste de teste de aceitação são necessários.
# Nem todos os projetos implementarão testes de desempenho ou estabilidade, mas
# você deveria ser cuidadoso ao omitir qualquer estapa de teste e ter certeza se
# não é aplicável.
# -------------------------------------------------
# Desenvolvimento Baseado em Teste
# Do inglês Test Driven Development(TDD), é uma técnica de desenvolvimento onde
# desenvolvedores escrevem casos de teste antes de escrever qualquer implementação
# de código. Os testes, portanto, guiam ou ditam o código que é desenvolvido. A
# implementação apenas fornece tantas funcionalidades quanto forem exigidas para
# passar dos testes e, assim, os testes agem como uma especificação do que o código faz.
# TDD tem o benefício que, como os testes devem ser escritos primeiro, sempre estarão
# disponíveis um conjunto de testes para realizar testes unitários, integração, regressão etc.
# Isto é bom pois desenvolvedores podem descobrir que escrever testes e manter
# testes é entediante e de menor interesse que o código em si, e assim colocar menos
# ênfase no regime de testes do que seria desejável. TDD encoraja, e defato requer,
# que desenvolvedores mantenham um conjunto extenso de testes repetíveis e que
# os testes sejam desenvolvidos com a mesma qualidade e padrões do corpo principal
# do código.
# Essas são as três regras do TDD, definidas por Rovert Martin:
#   1 - Você não tem permissão de escrever qualquer código de produção a menos
#       que seja pra faze um teste unitário passar.
#   2 - Você não tem permissão de escrever mais de um teste unitário que o suficiente
#       para falhar; e falhas de compilação são falhas.
#   3 - Você não tem permissão de escrever mais código de produção que o suficiente
#       para passar aquele teste unitário.
# Isto leva ao ciclo TDD descrito na próxima seção.
# ------------------------------------
# O ciclo TDD
# Existe um ciclo para o desenvolvimento quando trabalhando de maneira TDD. A menor
# forma do ciclo é o mantra TDD:
# Red/Green/Refactor.
# Que se relaciona ao conjunto de ferramentas do teste unitário onde é possível escrever
# um teste unitário. Dentro de ferramentas como PyCharm, quando se executa um teste
# pyunit ou pytest uma visualização de teste(Test View) é exibida com vermelho indicando
# que um teste falhou ou verde indicando que o teste passou. Por isso Red/Green, em
# outras palavras, escreve-se o teste unitário e deixa-o falhar, então implementa-se
# o código para garantir que passe. A última parte deste mantra é o Refactor, que
# indica que uma vez que esteja funcionando, deixe o código mais limpo, melhor,
# e mais ajustado refatorando-o. Refatoração é o processo no qual o comportamento
# do sistema não é alterado mas a implementação é alterada para melhorá-la. O ciclo
# TDD é mostrado no diagrama da imagem tdd.pnd.
# O mantra TDD pode ser visto no ciclo TDD da imagem e descrito em mais detalhes abaixo:
#   1-Escrever um único teste
#   2-Executar o teste e vê-lo falhar
#   3-Implementar apenas código suficiente para que o teste passe
#   4-Executar o teste e vê-lo passar
#   5-Refatorar por clareza e lidar com qualquer problema de reutilização etc.
#   6-Repetir para o próximo teste.
# --------------------------------------------
# Complexidade dos testes
# O objetivo é almejar simplicidade em tudo que escreve dentro de TDD. Assim, você
# escreve um teste que falha, então faz apenas o suficiente para fazer aquele teste passar
# (mas não mais que isso). Então refatora o código de implementação (isto é, mudar o
# código interno da unidade sub teste) para melhorar o código base. Continua a fazer isso
# até todas as funcionalidades para uma unidade serem completas. Em termos de cada teste,
# você deveria, novamente, almejar por simplicidade com cada teste apenas testando uma coisa
# com apenas uma única asserção por teste (apesar desta questão ser sujeita a muito debate
# detro do mundo TDD).
# --------------------------------------------
# Refatoração
# A ênfase na refatoração na TDD torna-a mais que apenas teste ou Desenvolvimento
# com Teste Primeiro. Este foco na refatoração é, na verdade, um foco no (re)design
# e melhora incremental. Os testes fornecem a especificação do que é necessário assim
# como verificação que o comportamento existente é mantido, mas refatoração leva a
# melhor design do software. Assim, sem refatoração, TDD não é TDD.
# ------------------------------------------
# Design para testabilidade
# A testabilidade tem várias facetas:
#   * Configurabilidade: Configurar o objeto sob teste para configuração apropriada.
#   * Controlabilidade: Controlar a entrada (e estado interno)
#   * Observabilidade: Observar a saída
#   * Varificabilidade: Que podemos verificar que aquela saída de forma apropriada.
# ---------------------------------------
# Dicas(Rules of Thumb) de testabilidade
# Se não pode testar código, então altere-o para poder
# Se seu código é difícil de validar então altere-o para que não seja
# Apenas uma classe concreta deveria ser testada por teste Unitário e então simule o resto
# Se seu código é difícidl de reconfigurar para trabalhar com simulacros, então faça com que possa usá-los
# Projete seu código para testabilidade.

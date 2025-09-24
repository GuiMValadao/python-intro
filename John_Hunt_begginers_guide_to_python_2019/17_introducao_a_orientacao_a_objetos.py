# Orientaçao a objetos
# Classes
# Uma classe e um dos blocos basicos de construçao em Python.
# Tambem e um conceito central no estilo de programaçao conhecido como
# Programaçao orientada a objetos (ou OOP). OOP providencia uma abordagem
# para estruturar programas/aplicaçoes de modo que os dados armazenados,
# e as operaçoes realizadas naqueles dados, sao agrupados junto em classes
# e acessados via objetos.
# Como exemplo, em um programa no estilo OOP, empregados poderiam ser
# representados por uma classe 'Empregado' onde cada empregado tem uma
# identificaçao, nome, departamento e um numero_de_mesa, etc. Eles poderiam
# tambem ter operaçoes associadas a eles, como tirar_ferias() ou ser_pago().
# Em muitos casos, classes sao usadas para representar entidades do mundo real
# (como empregados), mas nao e obrigatorio, elas tambem podem representar
# conceitos mais abstratos como uma transaçao entre uma pessoa e outra (como um
# acordo para comprar uma refeiçao).
# Classes agem como 'templates', que sao usadas para construit instancias ou
# exemplos de uma classe de coisas. Cada exemplo da classe 'Pessoa' poderia
# ter um nome, uma idade, um endereço, etc, mas eles tem seus proprios valores
# para seu nome idade e endereço. Por exemplo, para representar as pessoas
# em uma familia poderiamos criar um exemplo da classe 'Pessoa' com o nome Paul,
# 52 anos de idade e endereço em Londres. Poderiamos tambem criar outro objeto (instancia)
# 'Pessoa' com o nome Fiona, de 48 anos de idade e com endereço tambem em Londres e assim por diante.
# Uma instancia ou objeto e, portanto, um exemplo de uma classe. Todas as instancias/
# objetos de uma classe possuem as mesmas variaveis de dados mas contem seus
# proprios valores. Cada instancia de uma classe responde ao mesmo conjunto de
# solicitaçoes e tem o mesmo comportamento.
# Classes permitem programadores especificar a estrutura de um objeto,
# isto e, seus atributos ou campos etc. e seu comportamento separadamente
# dos objetos em si. Isto e importante, pois seria extremamente
# demorado (assim como ineficiente), para programadores definir cada objeto
# individualmente. Em vez disso, eles definem classes e criam instancias ou objetos dessas classes.
# Eles podem entao armazenar dados relacionados juntos em um conceito nomeado que
# torna muito mais facil estruturar e manter o codigo.
#----------------------------------------------------
# Para que servem as classes?
# Ja vimos varios tipos de dados em Python, como inteiros, strings, booleanos, etc.
# Cada um desses nos permitiu guardar um unico item de dado.
# Entretanto, como poderiamos representar uma Pessoa, um Estudante ou um Empregado
# de uma empresa? Um modo de fazer isso e usando uma classe para representa-los.
# Como indicado acima, poderiamos representar qualquer tipo de (mais complexos)
# itens de dados usando uma combinaçao de atributos (ou campos) e comportamentos.
# EStes atributos usarao tipos de dado existentes, que poderiam ser inteiros, strings,
# Booleanos, numeros reais ou outras classes.
# Por exempo, ao definir a classe Pessoa poderiamos dar-lhe:
# - um campo ou atributo para o nome da pessoa,
# - um campo ou atributo para sua idade,
# - um campo ou atributo para seu e-mail,
# - algum comportamento para lhes dar um aniversario (que aumentara sua idade),
# - algum comporatmento para nos permitir enviar-lhes uma mensagem por e-mail,
# - etc.
# Em Python, classes sao usadas:
# - como modelos para criar instancias (ou objetos) daquela classe,
# - definir metodos de instancia ou comportamento comum para uma classe de objetos,
# - definir atributos ou campos para armazenar dados dentro dos objetos,
# - receber mensagens.
# Objetos (ou instancias), por outro lado, podem:
# - ser criados de uma classe,
# - armazenar seus proprios valores para variaveis de instancia,,
# - receber mensagens,
# - executar metodos de instancia,
# - ter muitas copias no sistema (todas com seus proprios dados).
#-------------------------------------------------------
# O que uma classe deveria fazer?
# Uma classe deveria realizar um proposito especifico; deveria capturar
# apenas uma unica ideiia. Se mais de uma ideia esta encapsulada em uma
# classe, vocE pode reduzis as chances de reutilizaçao, assim como infringir
# as leis de encapsulaçao em sistemar orientados a objetos. Por exemplo,
# voce pode ter unido dois conceitos junto de forma que um pode diretamente
# acessar os dados de outro. Isto raramente e desejavel.
# As seguintes diretrizes podem ajuda-lo a decidir se deve-se divir a classe
# com a qual se esta trabalhando. Olha ao comentario descrevendo a classe.
# Considere os seguintes pontos:
#   *   A descriçao da classe e curta e clara? Se nao, seria isto uma reflexao
#       da classe? Considere como o comentario pode ser dividido em uma serie
#       de curtos comentarios claros. Baseie novas classes em torno desses
#       comentarios.
#   *   Se o comentario e curto e claro, as variaveis de classe e instancia fazem
#       sentido dentro do contexto do comentario? Se nao, entao a classe precisa
#       ser reavaliada. Pode ser que o comentario e inapropriado, ou que as
#       variaveis de classe e instancia sao inapropriadas.
#   *   Olhe como e onde os atributos da classe sao utilizados. O seu uso esta
#       de acordo com o comentario da classe? Se nao, voce deveria agir de acordo.
#------------------------------------------------------------
# Terminologia de classe
# Os seguintes termos sao usados em Python (e outras linguagens que suportam OOP):
#   * Classe:   Uma classe define uma combinaçao de dados e comportamento que operam
#               naqueles dados. Uma classe age como um modelo ao criar novas instancias.
#   * Instancia ou objeto:  Uma instancia, tambem chamada objeto, e um exemplo de uma
#                           classe. Todas as instancias de uma classe possuem os mesmos
#                           campos/atributos de dados mas contem seus proprios valores.
#                           Cada instancia de uma classe responde ao mesmo conjunto
#                           de pedidos.
#   * Atributo/campo/:      O dado armazenado por um objeto e representado por seus
#   variavel de instancia   atributos(tambem conhecidos como campo ou variavel de instancia)
#                           O 'estado' de um objeto em qualquer momento em particular
#                           se relaciona aos valores atuais guardados por seus atributos.
#   * Metodo:   Um metodo e um procedimento definido dentro de um objeto.
#   * Mensagem: Uma mensagem e enviada a um objeto solicitando que alguma operaçao
#               seja realizada ou algum atributo acessado. E uma solicitaçao que o objeto
#               faça alguma coisa ou retorne alguma coisa. Entretanto, e papel do objeto
#               determinar como fazer algo ou retornar algo. Uma mensagem podde ser
#               considerada similar a uma chamada de procedimento em outras linguagens.
#----------------------------------------------------------
# Como e um sistema orientado a objetos construido?
# Vamos usar um sistema do mundo real (fisico) para explorar o que uma aplicaçao
# OOP poderia se parecer.
#                                                   |-- Wiper Motor--|
#     --------  Wash wipe system----|               |                |
#   - (minus)                       |--Relay ========---- |          |-- + (plus)
#     --------  Fuse----------------|                    Pump--------|
#                                                         |
#                                                      Water Bottle
# Este sistema pretende fornecer um tutor de diagnostico para o equipamento
# ilustrado acima. Em vez de usar o sistema wash-wipe de um carro real,
# estudantes em um curso de diagnostico mecanico de carro usam esta simulaçao
# de software. O sistema de software simula o sistema real, de modo que o
# comportamento da bomba depende da informaçao fornecida pelo 'relay' e a garrafa d'agua.
# A operaçao do sistema wash-wipe e controlada por um botao que pode estar em uma de
# cinco posiçoes: desligado, intermitente, devagar, rapido e lavagem. Cada uma
# dessas configuraçoes colocar o sistema em um estado diferente:
# Configuraçao do botao | Estado do sistema
#-----------------------|--------------------------------------------------------------
# Desligado             | O sistema esta inativo
# Intermitente          | As laminas limpam o parabrisa a cada alguns segundos
# Devagar               | As laminas limpam o parabrisa continuamente
# Rapido                | As laminas limpam o parabrisa continuamente e rapidamente
# Lavagem               | A bommba puxa agua da garrafa d'agua e espalha no parabrisa
#--------------------------------------------------------------------------------------
# Para a bomba e o motor limpador funcionarem corretamente, o rele (relay) deve
# funcionar corretamente. Por sua vez, o rele deve ser fornecido com um
# circuito eletrico. Este circuito e negativamente ligado e assim o fusivel deve estar
# intacto para o circuito ser feito. Carros sao acionados negativamente pois isso
# reduz as chances de curto-circuitos levando a ligaçao nao intencional de circuitos.
#----------------------------------------------------------------------------------
# Onde começamos?
# Um sistema orientado a objetos e fundamentalmente preocupados com itens de dados.
# Na visao de mundo orientada a objetos, a enfase maior e colocada nos
# itens de dados envolvidos e consideramos as operaçoes associadas a eles (efetivamente,
# o reverso da visao da decomposiçao funcional). Isto significa que começamos
# tentando identificar os itens de dados primarios no sistema; em seguida,
# procuramos olhar quais operaçoes sao aplicadas em, ou realizadas sobre, os
# itens de dados; finalmente, agrupamos os itens de dados e operaçoes
# juntos para formar objetos. Ao identificar as operaçoes, podemos ter de
# considerar itens de dados adicionais, que podem ser objetos separados ou
# atributos do objeto atual. Identifica-los e principalmente uma questao
# de habilidade e experiencia.
# A abordagem de projetos orientados a sistemas considera as operaçoes muito menos
# importantes que dados e suas relaçoes. Na proxima seçao nos examinamos os
# objetos que poderiam existir em nosso sistema de simulaçao.
#-------------------------------------------------------
# Identificando os objetos
# Olhamos para o sistema como um t odo e perguntamos o que indica o estado do sistema
# Poderiamos dizer que a posiçao do interruptor ou o status da bomba e importante.
# Isto resulta nos itens de dados abaixo:
# Item de dado          | Estados
#-----------------------|-------------------------------------------
# config. interruptor   | O interruptor esta em desligado, intermitente, limpar, limpar rapido ou lavar?
# motor do limpador     | O motor esta funcionando ou nao?
# estado da bomba       | A bomba esta funcionando ou nao?
# condiçao fusivel      | O fusivel queimou ou nao?
# nivel garrfa d'agua   | O nivel de agua atual
# status do rele        | A corrente esta correndo ou nao?

# A identificaçao dos itens de dados e considerada em maior detalhe
# posteriormente. Neste ponto, simplesmente note que nao mencionamos
# ainda a funcionalidade do sistema ou como eles se encaixam juntos,
# apenas mencionamos os itens importantes. Como este e um sistem a simples,
# podemos assumir que cada um desses elementos e um objeto
# e ilustrar isto em um diagrama de objetos simples:
#    /------------\                         /------------\
#   ( Int. lavador )                       (Motor limpador)
#    \------------/     /------------\      \------------/
#                      (     rele     )     /------------\
#    /------------\     \------------/     (    bomba     )
#   (    fusivel   )                        \------------/
#    \------------/                         /------------\
#                                          ( garrafa agua )
#                                           \------------/
# Note que nomeamos caa objeto pelo elemento associado com o item de dado
# (p. ex o elemento associado com a condiçao do fusivel e o proprio fusivel)
# e que o dado atual ( a condiçao do fusivel) e uma variavel de instancia do objeto.
# Isto e um modo muito comum de nomear objetos e suas variaveis de instanca.
# Agora temos os objetos basicos necessarios para nossa aplicaçao.
#------------------------------------------------
# Identificando os serviços ou metodos
# No momento, temos um conjunto de objetos, em que cada um pode
# guardar algum dado. Por exemplo, a garrafa de agua pode guardar um inteiro
# indicando o nivel de agua atual. Apesar de sistemas orientados a objetos
# serem estruturados em torno de dados, ainda precisamos de algum conteudo
# processual para mudar o estado de um objeto ou fazer o sistema alcançar algum
# objetivo. Portanto, tambem precisamos considerar as operaçoes que um usuario
# de cada objeto pode requerer. Note que a enfase aqui esta no usuario do objeto
# e o que eles podem solicitar do objeto em vez de quais operaçoes sao realizadas sobre os dados.
# Vamos começar com o objeto 'interruptor'. O estado do interruptorpode assumir
# diversas variaveis. Como nao queremos outros objetos tendo acesso direto
# a esta variavel, devemos identificar os serviçoes que o interruptor deveria
# oferecer. Como um usuario de um interruptor, queremos ser capazes de move-lo entre
# suas varias configuraçoes. Como estas configuraçoes sao essencialmente
# um tipo enumerado, podemos ter o conceito de aumentar ou diminuir a posiçao
# do interruptor. Um interruptor deve, portanto, providenciar uma interface
# 'move_up' e 'move_down'. Exatamente como isso e feito depende da linguagem de
# programaçao; por hora, nos concentramos em especificar as instalaçoes necessarias.
# Se examinamos cada objeto em nosso sistema e identificamos os serviçoes necessarios,
# podemos terminar com a seguinte tabela:
# Objeto           | Serviço            | Descriçao
# -----------------|--------------------|-------------------
# interruptor      | mover_para_cima    | Aumentar valor do interruptor
#                  | mover_para_baixo   | Diminuir valor do interruptor
#                  | estado?            | Retornar um valor indicando o estado atual
#---------------------------------------|--------------------
# fusivel          | funcionando?       | Indica se o fusivel esta queimado ou nao
# motor do limpador| funcionando?       | Indica se os limpadores estao funcionando ou nao
# rele             | funcionando?       | Indica se o rele esta ativo ou nao
# bomba            | funcionando?       | Indica se a bomba esta ativa ou nao
# garrafa d'agua   | echer              | Enche a garrafa com agua
#                  | extrair            | Retira um pouco de agua da garrafa
#                  | esvaziar           | Esvazia a garrafaa de agua

# Geramos esta tabela examinando cada um dos objetos isoladamente
# para identificar os serviços que poderiam ser requeridos razoavelmente.
# Podemos identificar outros serviços quando tentamos juntar tudo.
# Cada um destes serviços deveria se relacionar a um metodo dentro do objeto
# Por exemplo, os serviços moverParaCima e moverParaBaixo deveriam se relacionar
# a metodos que mudam o estado da variavel de instancia dentro do objeto. Usando um
# pseudocodigo gennerico, poderia conter o seguinte codigo:
# def move_up(self):
#   if self.state == "off" then
#       self.state = "wash"
#   else if self.state == "wash" then
#       self.state = "wipe"
# Este metodo muda o valor da variavel de estano no interruptor. O novo
# valor da variavel de instancia depende no estado anterior. Voce pode definir
# moveDown de um modo similar. Note que a referencia a variavel de instancia
# ilustra que e global para o objeto. O metodo moveUp nao requer parametros.
# Em sistemas orientados a objetos, e comum para novos parametros serem passados
# entre metodos (particularmente do mesmo objeto), como e o objeto que guarda os dados.
#----------------------------------------------------
# Refinando os objetos
# Se olharmos para a tabela acima, podemos ver que fusivel, motor do limpador,
# rele e bomba todos tem um serviço chamado 'funcionando?'. Esta e uma dica
# que estes objetos podem ter algo em comum. Cada um deles tem a mesma interface
# para o mundo exterior. Se, entao, considerarmos seus atributos, eles todos  possuem
# uma variavel de instancia comum. Neste ponto, e muito cedo dizer se o fusivel,
# motor do limpador, rele e bomba sao todos instancias da mesma classe de objetos
# (isto e, uma classe 'Componente') ou se eles todos sao instancias de classes que
# herdam de alguma superclasse em comum. No entanto, isto e algo que devemos ter em mente posteriormente.
#--------------------------------------------------------
# Juntando tudo
# Ate aqui, identificamos os objetos primarios em nosso sistema e o conjunto basico
# de serviçoes eles deveriam apresentar. Estes serviçoes foram baseados apenas nos dados
# que os objetos guardam. Devemos agora considerar como fazer o sistema funcionar
# Para fazer isso, precisamos considerar como isto poderia ser usado. O sistema e parte
# de umm tutor de diagnose muito simples; um aluno usa o sistema para aprender sobre os
# efeitos de varios problemas na operaçao real de um sistema de um limpador, sem a
# necessidade de sispositivos eletronicos caros. Portanto queremos permitir
# um usuario do sistema realizar as seguintes operaçoes:
#   *   mudar o estado de um dispositivo componente;
#   *   perguntar ao motor qual seu novo estado e
# As operaçoes 'move_up' e 'move_down' no interruptor mudam o estado dele.
# Operaçoes similares podem ser fornecidas para o fusivel, a garrafa d'agua
# e o rele. Para o fusivel e o rele, poderiamos fornecer uma interface 'change_state'
# usando o seguinte algoritmo:
# define change_state(self)
#   if self.state == "working" then
#       self.state = "notWorking"
#   else
#       self.state = "working"
# Descobrir o estado do motor e mais complicado. Encontramos uma situaçao
# onde o estado de um objeto (o valor de sua variavel de instancia) e dependente
# da informaçao provida por outros objetos. Se escrevemos processualmente como o
# valor de outros objetos afetam o status da bomba, poderiamos ter o seguinte pseudo-code:
# if fuse is working then
#   if switch is not off then
#       if relay is working then
#           pump statur = "working"
# Este algoritmo diz que o status da bomba depende do status do rele, a configuraçao
# do interruptor e o status do fusivel. Este e o tipo de algoritmo que poderia se
# esperar encontrar na aplicaçao. Ela liga subfunçoes e processos aos dados.
# Em um sistema orientado a objetos, objetos bem-comportados passam mensagens um
# para o outro. Como, entao, conseguimos o mesmo efeito do algoritmo acima?
# A resposta e que devemos fazer os objetos passarem mensagens pedindo a informaçao
# apropriada. Um jeito de fazer isso e definir um metodo no objeto 'bomba' que obtem
# aquela informaçao de outros objetos e determina o estado do motor. Entretanto,
# isto requer que a bomba tenha ligaçoes a todos os outros objetos de modo que pode
# envia-los mensagens. Isto e um pouco artificial e perde a estrutura do sistema
# subjacente. Tambem perde qualquer modularidade do sistema. Isto e, se queremos
# acrescentar novos componentes, entao temos que mudar o objeto da bomba, mesmo se
# os novos componentes apenas afetem o interruptor. Esta abordagem tambem indica que
# o desenvolvedor esta pensando muito processualmente e nao em termo de objetos.
# Em uma visao orientada a objetos, o objeto 'bomba' apenas precisa saber o estado do rele.
# Deveria, porttanto, requerir esta informaçao do rele. Por sua vez, o rele deve pedir
# informaçao do interruptor e fusivel.
#    /------------\   2. estado?                              /------------\
#   ( Int. lavador ) <-------|                               (Motor limpador)
#    \------------/     /------------\  1. funcionando?       \------------/
#                      (     rele     ) <----------|          /------------\  fncionando?
#    /------------\     \------------/              |------  (    bomba     )<---
#   (    fusivel   ) <--------|                               \------------/-----|
#    \------------/    3. funcionando?                       /------------\      |4. extrair(status da bomba)
#                                                            ( garrafa agua )<---|
#                                                             \------------/
#
# 1. a bomba envia a mensagem funcionando? para o rele
# 2. o rele envia uma mensagem estado? para o interruptor, o interruptor responde para o rele
# 3. o rele envia uma segunda mensagem funcionando? para o fusivel:
#       * O fusivel responde para o rele
#       * O rele responde ao motor
#       * Se a bomba esta funcionando, entao o objeto bomba manda a mensagem final para a garrafa d'agua
# No passo 4, um parametro e enviado com a mensagem pois, diferente das mensagens anteriores
# que apenas pediam a informaçao do estado, esta mensagem pede uma mudança no estado.
# O parametro indica a taxa a qual a bomba puxa agua da garrafa.
# A garrafa nao deveria gravar o valor do status da bomba pois nao e dono deste valor
# Se precisa do status do motor no futuro, deveria pedi-lo a bomba em vez de usar
# o (potencialmente obsoleto) valor passado a ele anteriormente.
# Na figura acima assumimos que a bomba entrega o serviço 'funcionando?' que permite ao
# processo começar. Por completeza, o pseudocodigo do metodo 'funcionando?' para o
# objeto bomba e:
# def working(self)
#       self.status = relay..working()
#       if self.status == "working" then
#           water_bottle.extract(self.status)
# este metodo e bem mais simples que o programa processual apresentado anteriormente.
# Em nenhum ponto mudamos o valor de quaisquer variaveis que nao sao parte da bomba,
# apesar deles puderem ter sido alterados como resultados das mensagens sendo enviadas.
# Tambem, apenas nos mostraa parte da historia que e diretamente relevante a bomba.
# Isto quer dizer que pode ser muito mais dificil deduzir a operaçao de um sistema
# orientado a objetos so olhando para o codigo fonte. Alguns ambientes Python
# (como o IDE PyCharm) aliviam este problema, em algum nivel, pelo uso de browsers sofisticados.
#---------------------------------------------------------------------------
# Onde esta a estrutura em um programa OO
# Pessoas novas a orientaçao a objetos podem se confundir pois perderam um dos
# elementos chave que usam para ajuda-los entender a eestrutura de um sistema de software:
# o corpo principal do programa. Isto e porque os objetos e as interaçoes entre
# eles sao a pedra angular do sistema.
# A estrutura e ditada pelas mensagens enviadas entre os objetos. Isto e, um objeto
# deve possuir uma referencia a outro objeto para envia-lo uma mensagem.
# Em Python, esta estrutura e obtida fazendo variaveis de instancia referenciarem os
# objetos apropriados. Esta e a estrutura que existe entre as instancias no sistema
# e nao se relaciona as classes, que agem como modelos para as instancias.
# Consideramos agora as classes que criam as instancias. Poderiamos assumir que cada
# objeto e uma instancia de uma classe equivalente. Entretanto, com ja foi notado,
# algumas das classes sao muito similares. Em particular, o fusivel, rele, motor e
# a bomba compartilham varias caracteristicas em comum. Esses objetos diferem apenas
# no nome. Isto sugere que sao todos instancias de uma mesma classe em comum
# como 'Componente'. Esta classe poderia possuir uma variavel de instancia
# adicional, para simplificar a identificaçao de objetos.
# Se eles todos sao instancias de uma classe em comum, deveriam se comportar
# exatamente da mesma maneira. Entretanto, queremos que a bomba inicie o processo
# de analise quando receber a mensagem 'funcionando?', entao ela deveria
# possuir uma definiçao diferente de 'funcionando?' do que o fusivel e rele.
# De outros modos e muito similar ao fusivel e rele, entao eles podem ser
# instancias de uma classe (como 'Componente') e bomba e motor podem ser
# instancias de classes que herdam de 'Componente' (mas redefinem 'funcionando?').
#


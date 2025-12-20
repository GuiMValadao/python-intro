# Capítulo 26 - Introdução a Registros (Logging)
# Muitas linguagens de programação tem bibliotecas de registro comuns,
# incluindo Java, C# e Python. O módulo de logging faz barte do python
# padrão desde Python 2.3.
# Este capítulo discute porque você deve acrescentar logging aos seus
# programas, o que deve (e não deve) ser registrado e porque usar print()
# não é suficiente.
# ------------------------------------------------------------
# Porque Log?
# Logging é, normalmente, um aspecto típico de qualquer aplicação em produção;
# isto pois é importante fornecer informações apropriadas para permitir
# investigações futuras após algum evento ou problema nas aplicações.
# Essas investigações incluem:
#   * Diagnosticar falhas: isto é, porque um aplicativo falhou/qubrou(crash).
#   * Identificar comportamentos incomuns ou inesperados: que poderiam não
#       levar a aplicação a falhar mas que poderiam deixá-la em um estado
#       inesperado ou onde dados poderiam ser corrompidos etc.
#   * Identificar problemas de desempenho ou capacidade: nestas situações,
#       a aplicação está executando como esperado mas não está cumprindo
#       algumas exigências não-exigidas associadas à velocidade no qual está
#       operando ou sua habilidade de escalar com o crescimento da quantidade
#       de dados ou número de usuários.
#   * Lidar com tentativas de comportamento malicioso: no qual algum agente
#       externo tenta afetar o comportamento do sistema ou adquirir informações
#       que não deveriam ter acesso etc. Isto poderia acontecer, por exemplo,
#       se você criar um aplicativo web com Python e um usuário tenta hackear
#       seu servidor.
#   * Compliance regulatória ou legal: Em alguns casos, registros de execução
#       de programas podem ser necessários por razões regulatórias ou legais.
#       Isto é particularmente verdade para o setor financeiro onde registros
#       devem ser mantidos por muitos anos caso haja necessidade de investigar
#       o comportamento de organizações ou indivíduos.
# ----------------------------------------------------------
# Qual o propósito de registros?
# Em geral, há duas razões gerais para registrar o que um aplicativo está
# fazendo durante sua operação:
#   * Para diagnósticos de modo que eventos/passos registrados possam ser
#       usados para analisar o comportamento do sistema quando algo dá errado.
#   * Para auditação que permitem análise posterior do comportamento do sistema
#       para propósitos de negócios, legais ou regulatórios. Por exemplo, neste
#       caso, determinar quem fez o que com o que e quando.
# Sem tais informações registradas, é impossível saber o que aconteceu após
# o event. Por exemplo, se tudo que souber é que um aplicativo qubrou (parou
# de executar inesperadamente), como pode determinar qual era o estado da
# aplicação, quais funções, métodos, etc estavam sendo executados e quais
# declarações foram executadas?
# Lembre-se que, apesar de um desenvolvedor possa estar usando uma IDE para
# executar seus aplicativos durante desenvolvimento e, possivelmente, usar
# os recursos de debuggins disponíveis que permitiriam ver quais funções ou
# métodos, declarações e mesmo valores de variáveis estão definidas; isto não
# é como a maioria dos sistemas de produção são executados. Em geral, um sistema
# de produção em Python será executado ou de linha de comando ou, possivelmente,
# através de um atalho para simplificar a execução do programa. Tudo que o
# usuário saberá é que alguma coisa deu errado ou que o comportamento que
# esperavam não ocorreu - se, de fato, tiverem ciência do problema.
# Registros são, portanto, chave para análises de falhas após o evento,
# comportamento inesperado ou para análise da operação do sistema por questões
# de negócios.
# --------------------------------------------------------
# O que deveria ser registrado?
# Um aplicativo deveria ter informações registradas o suficiente para que
# investigadores possam entender o que estava acontecendo, quando e onde.
# Em geral, isto significa que você irá registrar a hora da mensagem de
# registro, o módulo/nome do arquivo, nome da função ou método sendo executada,
# potencialmente o nível de registro sendo usado(explicado mais à frente) e
# em alguns casos, o valor/estado de parâmetros do ambiente, programa ou classe envolvida.
# Em muitos casos, desenvolvedores registram a entrada (e, em nível menor),
# a saída de uma função ou método. Entretanto, também pode ser útil registrar
# o que ocorre em pontos extremos (branch) dentro de uma função ou método
# para que a lógica da aplicação possa ser seguida.
# Todas as aplicações deveriam registrar todos os erros/exceções.Cuidado
# é necessário para garantir que isso seja feito corretamente. Por exemplo,
# se uma exceção for pega e então relançada muitas vezes, não é necessário
# registrar todas as vezes que ela é pega. De fato, fazer isso pode fazer
# com que os arquivos de registro tornem-se muito maiores, causem confusão
# quando o problema for investigado e resulte em cabeçalhos(overheads) desnecessários.
# Uma abordagem comum é registrar uma exceção onde é levantada e pega
# pela primeira vez, e não registrar após isso.
# -------------------------------------------------
# O que não registrar
# Uma ideia geral é não registrar quaisquer informações pessoais ou sensíveis
# incluindo informações que possam ser usadas para identificar um indivíduo.
# Este tipo de informação é conhecida como PII(Personally Identification Information).
# Essas informações incluem:
#   * id's e senhas de usuários
#   * endereços de e-mail
#   * data e local de nascimento
#   * Informações financeiras identificáveis como detalhes de contas de banco, de cartão de crédito etc
#   * informação biométrica
#   * informação médica/de saúde
#   * informação pessoal fornecida pelo governo como detalhes de passaporte,
#       número de licença de motorista, números de securidade social, etc
#   * informação organizacional oficial como registros profissionais e números de cadastro de membros
#   * endereços físicos, números de telefone
#   * informação de verificação como nome de solteira da mãe, de animais de
#       estimação, de escola do ensino médio etc
#   * também inclui informações online relacionadas a mídias sociais como contas de Facebook ou LinkedIn.
# Nenhuma dessas informações deve ser registrada diretamente. Isto não quer
# dizer que não possa e não deva registrá-las; pode ser necessário fazer isso.
# Entretanto, a informação deveria, pelo menos, ser obscurecida e não deve
# incluir qualquer informação não necessária. Por exemplo, pode registrar
# que um usuário representado por algum id tentou logar em um determinado
# momento e se ele teve sucesso ou não. Entretanto, não deve-se registrar
# sua senha e pode-se não registrar o userid de fato, mas um id que possa
# ser usado para mapear o userid real.
# Também deve-se ter cuidado com registrar dados de entrada diretamente de
# uma aplicação em um arquivo de registro. Um modo que um agente malicioso
# pode atacar uma aplicação (particularmente uma aplicação web) é tentando
# enviar grandes quantidades de dados a ela (como parte de um campo ou
# parâmetro para uma operação). Se o aplicativo registra todos os dados
# que recebe sem cuidado, então os arquivos de registro serão preenchidos
# muito rapidamente. Isto pode resultar no armazenador de arquivos da aplicação
# sendo preenchida e causar potenciais problemas para todos os softwares
# usando o mesmo armazenador de arquivos. Esta forma de ataque é conhecida
# como um ataque de injeção de registro (log injection attack) e é bem documentada.
# Outro ponto importante é que não é suficiente apenas registrar o erro, isto
# não é resolver o erro; registrar um erro significa apenas que observou o
# erro. O aplicativo deveria ainda decidir como gerenciar o erro ou exceção.
# Em geral, você deveria procurar esvaziar registros em um sistema de produção;
# isto é, apenas informação que requer o registro deveria ficar registrada
# (geralmente informações sobre erros, exceções ou comportamento inesperado).
# Finalmente, também é importante registrar informações no local correto.
# Muitas aplicações (e organizações) registram informações em um arquivo de
# registro, erros e exceções em outro e informação de segurança em um terceiro.
# Portanto, deve-se saber para onde sua informação será enviada e não enviá-la
# ao registro errado.
# ------------------------------------------------------
# Por que não usar apenas print?
# Na realidade, usar print() para registrar informações em um sistema de
# produção é, quase nunca, a resposta correta por várias razões:
#   * A função print(), por padrão, escreve strings na saída padrão (stdout)
#       ou saída de erro padrão (stderr), que, por padrão, direciona a saída
#       ao console/terminal. Isto é razoável durante o desenvolvimento,
#       mas se o programa não for executado por linha de comando, sendo lançado
#       durante inicialização do sistema operacional por exemplo, não haverá
#       um terminal para receber o dado, que acaba perdido.
#   * Outro problema em usar a função print() é que todas as chamadas a ela
#       serão exibidas. Quando usamos a maioria dos registradores, é possível
#       especifiar o nível de registro requerido. Estes diferentes níveis
#       permitem que diferentes quantidades de informação sejam geradas
#       dependendo do cenário. Por exemplo, em um sistema de produção confiável
#       bem testado, podemos querer apenas que informações relacionadas a erros
#       ou informações críticas sejam registradas. Isto reduz a quantidade
#       de informação coletada e reduz o impacto no desempenho introduzido
#       pelo registro na aplicação. Por outro lado, em fase de testes, podemos
#       precisar de níveis mais detalhados.
#   # Em outras situações, podemos querer alterar o nível de registro sendo
#       usado para um sistema de produção em funcionamento sem precisar
#       alterar o código em si (pois isso possui o risco de introduzir potenciais
#       erros ao código). Em vez disso, poderíamos ter o recurso de alterar
#       externamente o modo com que o sistema de registro se comporta, por
#       exemplo, por um arquivo de configuração. Isto permite que administradores
#       modifiquem a quantidade de detalhe da informação sendo registrada.
#       Normalmente, também permite que a designação da informação registrada seja alterada.
#   * Por fim, ao usar a função print(), um desenvolvedor pode usar qualquer
#       formato queiram, podem incluir o tempo (timestamp) na mensagem ou
#       não, podem incluir o nome do módulo ou função/método ou não, incluir
#       ou não parâmetros. Usar um sistema de registro normalmente padroniza
#       a informação gerada junto com a mensagem de registro. Assim, todas
#       as mensagens registradas terão(ou não) a hora, informação da função/método/módulo,
#       em que foram geradas etc.
#

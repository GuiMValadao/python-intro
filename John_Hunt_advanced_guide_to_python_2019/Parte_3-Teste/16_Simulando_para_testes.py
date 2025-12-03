# Capítulo 16 - Simulando(Mocking) para testes
# O teste de sistemas de software não é algo fácil de se fazer; as funções, objetos,
# métodos etc que estão envolvidos em um programa podem ser coisas complexas por si só.
# Em muitos casos, eles dependem de e interagem com outras funções, métodos e objetos;
# poucas funções e métodos operam isoladamente. Assim, o sucesso ou falha de uma função
# ou método ou o estado geral de um objeto é dependente de outros elementos do programa.
# Entretanto, em geral é muito mais fácil testar uma única unidade isolada em vez de
# testá-la como parte de um sistema maior, mais complexo. Por exemplo, se pegarmos uma
# única classe Python como uma única unidade a ser testada. Se pudermos testá-la por si
# só, teremos apenas de levar em conta o estado do objeto da classe e o comportamento
# definido pela classe ao escrever o teste e determinar saídas apropriadas.
# Entretando, se aquela classe interage com sistemas externos como serviços externos,
# bases de dados, softwares terceirizados, fontes de dados etc, então o processo de teste
# se torna mais complexo. Pode ser necessário verificar atualizações de dados
# feitas na base de dados, ou informação enviada para um serviço remoto etc para
# confirmar que a operação de um objeto da classe está correta. Isto faz com
# que não apenas o software sendo testado seja mais complexo mas também torna
# os testes em si mais complexos. Isto significa que há maior chance que o
# teste falhará, que os testes conterão bugs ou problemas neles próprios e
# que o testes serão mais difíceis de se entender e manter. Assim, um objetivo
# comum ao escrever testes ou testes de subsistemas é ser capaz de testar
# elementos/unidades isoladamente. A pergunta é como fazer isso quando uma função
# ou método depende de outros elementos?
# A chave para desacoplar funções, métodos e objetos de outro programa ou elementos
# de um sistema é usar simulados (mocks). Esses simulados podem ser usados para
# desacoplar um objeto de outro, uma função de outra e um sistema de outro;
# dessa forma simplificando o ambiente de teste. Esses simulados tem objetivo
# apenas de serem usados nos testes. Simulações não é um conceito específico de
# Python e existem vária bibliotecas disponíveis para diferentes linguagens.
# Entretanto, neste capítulo focaremos na biblioteca unites.mock que é parte
# da distribuição padrão do Python desde Python 3.3.
# -------------------------------------------------
# Porque simular?
# Há várias razões para utilizar simulados em vez dos sistemas reais, algumas
# delas sendo:
#   * Teste em isolamento é mais fácil
#   * O objeto real não está disponível: em muitos casos, é necessário simular
#       parte de um sistema ou interface de outro sistema pois o real ainda
#       não está disponível. Isto pode ser por diversos motivos, incluindo que
#       ainda não foi desenvolvido ou que uma parte estará disponível apenas
#       no contexto de produção.
#   * Elementos reais podem ser demorados: queremos que os testes sejam executados
#       o mais rapidamente possível e, certamente dentro de um ambiente de
#       Integração Contínua (CI-Continuous Integration), queremos executá-los
#       rápido o suficiente que podemos testar um sistema repetidamente
#       ao longo do dia. Em algumas situações, o objeto real pode levar uma
#       quantidade significativa de tempo para se processar no cenário de teste.
#       Como queremos teste nosso próprio código, podemos não nos preocupar
#       sobre se um sistema além de nosso controle opera corretamente ou não
#       (pelo menos nesse nível do teste, podendo ser uma preocupação para
#       o teste de integração e sistema). Podemos, então, melhorar os tempos
#       de resposta de nossos testes se simularmos o sistema real e substituirmos
#       com um simulado que possibilita tempos de resposta muito mais rápidos.
#   * O objeto real leva tempo para configurar: Em um ambiente CI, novas
#       versões de um sistema são regularmente e repetidamente testadas
#       (por exemplo, sempre que uma alteração é feita à base de código).
#       Em tais situações, pode ser necessário configurar e lançar(deploy)
#       o sistema final em um ambiente apropriado para realizar os testes
#       apropriados. Se a configuração, lançamento e inicialização de um
#       sistema externo é demorada, pode ser mais efetivo simular aquele sistema.
#   * Dificuldade de emular certas situações: Estas situações são frequentemente
#       relacionadas a circunstâncias de erros ou excepcionais que não
#       deveriam ocorrer nunca em um ambiente corretamente funcional.
#       Entretanto, pode ser necessário validar que se tal situação vir
#       a ocorrer, o software pode lidar com aquele cenário. Se estes scanners
#       são relacionados a como o sistema externo (a unidade sob teste)
#       falha ou opera incorretamente, então pode ser necessário simular
#       esses sistemas para ser capaz de gerar os cenários.
#   * Queremos testes repetíveis: Por sua própria natureza, quando você
#       executa um teste você irá querer ou que passe ou falhe todas as vezes
#       que for executado com as mesmas entradas. Se passar algumas vezes e
#       falhar outras significa que não há confiança nos testes e as pessoas
#       geralmente começam a ignorar testes falhos. Isto pode acontecer se
#       os dados fornecidos pelos sistemas nos quais um teste depende não
#       fornecem dados repetíveis. Isto pode acontecer por diversas razões
#       diferentes, mas uma causa comum é pois eles retornam dados reais. Tais
#       dados podem estar submetidos a mudança, por exemplo, considere um sistema
#       que usa um feed de dados para a taxa de câmbio atual entre fundos e
#       dólares. Se o teste associado confirma que uma transação, quando
#       precificada em dólares é corretamente convertida a fundos usando a
#       taxa de câmbio atual, então aquele teste provavelmente gerará um
#       resultado diferente cada vez que for executado. Nesta situação, seria melhor
#       simular a taxa de câmbio atual de modo que um taxa fixa/conhecida é usada.
#   * O sistema real não tem confiança suficiente: em alguns casos, o sistema
#       real não é confiável o suficiente para permitir testes repetíveis.
#   * O sistema real pode não permitir que testes sejam repetidos: Por
#       exemplo, um teste que envolve
#

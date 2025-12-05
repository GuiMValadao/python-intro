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
#       exemplo, um teste que envolve o registro(lodging) de negociações
#       para um certo número de ações com um sistema gerenciador de Trade Order
#       pode não permitirque  aquele negócio, com aquelas ações, para aquele
#       cliente seja executado várias vezes (como pareceria, então, múltiplas
#       transações). Entretanto, para o propósito de teste, podemos querer
#       testar a submissão de testes similares em múltiplos cenários
#       diferentes, múltiplas vezes. Portanto, pode ser necessário simular
#       o Sistema Gerenciador de Ordem real para que os testes sejam escritos.
# -------------------------------------------------------
# O que é simulação?
# Conhecendo as diversas razões para se usar simulações, podemos perguntar o que elas são.
# As simulações (Mocks), incluindo funções e métodos simuladas e objetos
# simulados são coisas que:
#   * Possuem a mesma interface que a coisa real, sejam funções, métodos
#       ou objetos inteiro simulados. Assim, eles pegam a mesma faixa e
#       tipos de parâmetros e retornam informação similar usando tipos similares.
#   * Definem comportamentos que, de alguma forma, representa/imita o real,
#       mas tipicamente de modos muito controlados. Este comportamento pode
#       ser programado diretamente (hard coded), pode depender de um conjunto
#       de regras ou comportamento simplificado; pode ser muito simplista
#       ou bastante sofisticado.
# Assim, eles emulam o sistema real e, fora da simulação, podem parecer o sistema real.
# Em vários casos, o termo 'mock' é usado para cobrir uma faixa de diferentes
# modos em que a coisa real pode ser emulada; cada tipo de mock tem suas
# próprias características. Logo, é útil distinguir os tipos diferentes de
# simulados pois isto pode ajudar a determinar o estilo do simulado a ser adotado
# em uma situação de teste particular.
# Os diferentes tipos de simulados incluem:
#   * Test Stubs: é tipicamente uma função, método ou objeto programado à mão,
#       para o propósito do teste. O comportamento implementado por um teste stub
#       pode representar um subconjunto limitado da funcionalidade da coisa real.
#   * Fakes: Tipicamente fornecem funcionalidades adicionais comparados com
#       um Test Stub. Fakes podem ser considerados como uma versão específica
#       do teste da coisa real, como uma base de dados de memória usada para
#       testar em vez da base de dados real. Estes Fakes normalmente ainda
#       tem algumas limitações em sua funcionalidade, por exemplo, quando
#       os testes são terminados, todos os dados são removidos(purged) da
#       base de dados da memória em vez de salvos permanentemente em disco.
#   * Autogenerated Test Mocks: esses são normalmente gerados automaticamente
#       usando um framework de suporte.
#   * Test Mock Spy: Se estamos testando uma unidade particular e ela retorna
#       o resultado correto, poderíamos decidir que não precisamos considerar
#       o comportamento interno da unidade. Entretanto, é comum querer confirmar
#       que o simulado de teste foi invocado como esperado. Isto ajuda a verificar
#       o comportamento interno da unidade sob teste. Isto pode ser feito usando
#       um Test Mock Spy, que grava quantas vezes foi chamado e quais foram os
#       parâmetros usados (assim como outras informações). O teste pode, então,
#       interrogar o simulado de teste para validar que foi invocado como esperado/
#       quantas vezes esperado/com parâmetros corretos etc.
# ----------------------------------------------------------
# Conceitos comuns do framework de simulação
# Existem vários frameworks para simulação não apenas para Python, mas também para
# outras linguagens como Java, C#, Scala etc. Todos os frameworks tem um comportamento
# central em comum. Este comportamento permite uma função, método ou objeto simulado
# ser criado baseado na interface apresentada pela coisa real. Claro, linguagens
# diferentes como C# e Java ou Python não tem um conceito de interface formal;
# entretanto, isto não para o framework de simulação de usar a mesma ideia.
# Em geral, uma vez que um simulado foi criado, é possível definir como aquele
# simulado deveria parecer se comportar; em geral, isto envolve especificar o
# resultado de retorno para usar para uma função ou método. Também é possível
# verificar que o simulado foi invocado como esperado com os parâmetros esperados.
# O simulado real pode ser adicionado a um teste ou um conjunto de testes ou
# programaticamente ou por alguma forma de decorador. Em ambos os casos, para a
# duração do teste, o simulado será usado em vez da coisa real.
# Asserções podem, então, serem usadas para verificar os resultados retornados pela
# unidade sob teste enquanto os métodos específicos do simulado são tipicamente
# usados para verificar (espiar) os métodos definidos no simulado.
# ----------------------------------------------------
# Frameworks para simulação em Python
# Devido à natureza dinâmica do Python, ela é bastante apropriada para a construção
# de funções, métodos e objetos simulados. De fato, existem vários frameworks de
# simulação largamente usados disponíveis para Python, incluindo:
#   * unittest.mock: Incluido na distribuição do Python desde 3.3, é a biblioteca
#       para simulação padrão fornecida com Python para criar objetos simulados em testes Python.
#   * pymox: É um framework amplamente utilizado. É de código aberto e tem um
#       conjunto mais completo de instalações para reforçar a interface de uma classe simulada.
#   * Mocktest: Outro framework popular. Tem sua própria DSL(Domain Specific Language)
#       para auxiliar nas simulações e um largo conjunto de combinação de comportamentos
#       esperados para objetos simulados.
# No restante do capítulo usaremos a biblioteca unittest.mock.
# -------------------------------------------------------
# A biblioteca unittest.mock
# A chave da biblioteca unittest.mock é a classe Mock e sua subclasse MagicMock.
# Ambos objetos podem ser usados para simular funções, métodos e mesmo classes inteiras.
# Estes objetos simulados podem ter respostas 'enlatadas'(canned) definidas
# de modo que quando eles estão envolvidos pela unidade sob teste responderão
# apropriadamente. Objetos existentes também podem ter atributos ou métodos
# individuais simulados permitindo que um objeto seja testado com um estado
# conhecido e comportamento especificado. Para tornar fácil trabalhar com objetos
# simulados, a biblioteca fornece o decorador @unittest.mock.patch(). Este decorador
# pode ser usado para substituir funções reais e objetos com instâncias simuladas.
# A função por trás do decorador também pode ser usada como um gerenciador de
# contexto permitindo que seja usado em declarações with-as fornecendo controle
# refinado sobre o alcance da simulação se necessário.
# -----------------------------------------------
# Classes Mock e Magic Mock
# A classe Mock é a classe base para objetos simulados. A classe MagicMock é uma
# subclasse da classe Mock. É chamada MagicMock pois fornece implementações padrão
# para vários métodos mágicos como .__len__(), .__str__(), e .__iter__().
# Como um exemplo simples, considere as seguintes classes a serem testadas:
# class AlgumaClasse:
#     def _metodo_escondido(self):
#         return 0

#     def metodo_publico(self, x):
#         return self._metodo_escondido() + x


# Esta classe define dois métodos; um é pretendido como parte da interface pública
# da classe (o método_publico()) e uma que é pretendida apenas para uso interno ou
# privado (o _metodo_escondido()). Note que o método escondido usa a convenção de
# preceder seu nome por uma barra ('_').
# Vamos assumir que queremos testar o comportamento do metodo_publico() e queremos
# simular o _metodo_escondido().
# Podemos fazer isso escrevendo um teste que criará um objeto simulado e usa-o no
# lugar do _metodo_escondido() real. Poderíamos provavelmente usar ou a classe
# Mock ou MagicMock para isso; entretanto, devido às funcionalidades adicionais
# fornecidas pela classe MagicMock é uma prática comum para usar com aquela classe.
# Portantos, faremos o mesmo.
# O teste a ser criado será definido dentro de um método dentro de uma classe teste.
# Os nomes do método teste e da classe teste são, por convenção, descritivos e assim
# descreverão o que está sendo testado, por exemplo:
# from unittest.mock import *
# from unittest import TestCase
# from unittest import main


# class test_AlgumaClasse_interface_publica(TestCase):
#     def test_metodo_publico(self):
#         test_objeto = AlgumaClasse()
#         test_objeto._metodo_escondido = MagicMock(name="metodo_escondido")
#         test_objeto._metodo_escondido.return_value = 10
#         result = test_objeto.metodo_publico(5)
#         self.assertEqual(15, result, "valor retornado de metodo_publico incorreto")


# Neste caso note que a classe sendo testada é instanciada primeiro. MagicMock é,
# então, instanciada e atribuída ao nome do método a ser simulado. Então substitui
# aquele método para o test_objeto. O objeto MagicMock é dado um nome pois isso ajuda
# ao tratar quaisquer problemas no relatório gerado pelo framework unittest.
# Seguindo isto, a resposta enlatada da versão simulada do _metodo_escondido()
# é definida; sempre retornará o valor 10.
# Neste ponto, configuramos o simulado a ser usado para o teste e agora estamos
# prontos para executar o teste. Isto é feito na próxima linha onde o metodo_publico()
# chamado no test_objeto, com o parâmetro 5. O resultado é, então, guardado.
# O teste, então, valida o resultado para garantir que está correto; isto é, o
# valor retornado é 15. Apesar de ser um exemplo muito simples, ilustra como um
# método pode ser simulado com a classe MagicMock.
# ----------------------------------
# Patchers
# Os decoradores unittest.mock.patch(), unittest.mock.patch.object() e unittest.patch.dict()
# podem ser usados para simplificar a criação dos objetos simulados.
#   * O decorador patch pega um alvo para o patch e retorna um objeto MagicMock
#       em seu lugar. Pode ser usado como um método TestCase ou decorador de classe.
#       Como decorador de classe, decora cada método de teste na classe automaticamente.
#       Pode também ser usado como gerenciador de contexto pelas declarações with e with-as.
#   * O decorador patch.object pode ser fornecido com dois ou três argumentos. Quando
#       dado três argumentos substituirá o objeto a ser patched com um simulado para
#       o nome dado do atributo/método. Quando dado dois argumentos, o objeto a ser
#       patched é dado um objeto MagicMock padrão para o atributo/função especificado.
#   * O decorador patch.dict patches um dicionário ou objeto similar a dicionário.
# Por exemplo, podemos reescrever o exemplo apresentado acima usando o decorador
# @patch.object para fornecer o objeto simulado para o _metodo_escondido()

# class test_AlgumaClasse_interface_publica(TestCase):
#     @patch.object(AlgumaClasse, "_metodo_escondido")
#     def test_metodo_publico(self, mock_metodo):
#         mock_metodo.return_value = 10
#         test_objeto = AlgumaClasse()
#         result = test_objeto.metodo_publico(5)
#         self.assertEqual(15, result, "valor retornado de metodo_publico incorreto")

# No código acima o _metodo_escondido() é substituido com uma versão simulada para
# AlgumaClasse dentro do método test_metodo_publico(). Note que a versão simulada do
# método é passada como um parâmetro para o método teste para que a resposta enlatada
# possa ser especificada.
# Você também pode usar o decorador @patch() para simular uma função de um módulo.
# Por exemplo, dado algum módulo externo com uma função api_call, podemos simular
# aquela função usando o decorador @patch():
# @patch('external_module.api_call')
#   def test_some_func(self, mock_api_call):
# Isto usa patch() como decorador e passa o caminho do objeto alvo. O caminho alvo
# foi 'external_module.api_call' que consiste do nome do módulo e a função a ser simulada.
# ------------------------------------------
# Simulando objetos retornados
# Nos exemplos olhados até aqui, os resultados retornados das funções simuladas
# foram simples inteiros. Entretanto, em alguns casos os valores retornados também
# devem ser simulados como o sistema real retornaria um objeto complexo com múltiplos
# atributos e métodos.
# O seguinte exemplo usa um objeto MagicMock para representar um objeto retornado
# de uma função simulada. Este objeto tem dois atributos, um é um código de resposta
# e o outro é uma string JSON. JSON se refere à JavaScript Object Notation e é
# um formato comumente usado em serviços web.
# import external_module
# from unittest.mock import *
# from unittest import TestCase
# from unittest import main
# import json


# def some_func():
#     response = external_module.api_call()
#     return response


# class test_some_func_calling_api(TestCase):
#     @patch("external_module.api_call")
#     def test_some_func(self, mock_api_call):
#         mock_api_call.return_value = MagicMock(
#             status_code=200, response=json.dumps({"key": "value"})
#         )
#         result = some_func()
#         self.assertEqual(result.status_code, 200, "returned status code is not 200")
#         self.assertEqual(result.response, '{"key":"value"}', "response JSON incorrect")


# Neste exemplo, a função sendo testada é some_func(), mas ela chama a função
# simulada external_modula.api_call(). Esta função simulada retorna um objeto
# MagicMock com um status_code e response pré-especificados. As asserções, então,
# validam que o objeto retornado por some_func() contém o status e resposta corretos.
# ------------------------------------
# Validando que simulações foram chamadas
# Usando unittest.mock é possível validar que uma função simulada foi chamada
# apropriadamente usando assert_called(), assert_called_with() ou assert_called_once_with()
# dependendo em se a função pega parâmetros ou não.
# A seguinte versão de test_some_func_with_params() verifica que o api_call() simulado
# foi chamada com o parâmetro correto
# @patch('external_module.api_call_with_param')
# def test_some_func_with_param(self, mock_api_call):
#     mock_api_call.return_value = MagicMock(status_code=200, response=json.dumps({'age':'23'}))
#     result = some_func_with_param('Phoebe')
#     self.assertEqual(result.response, "{'age': '23'}", 'JSON result incorrect')
#     mock_api_call.api_call_with_param.assert_called_with('Phoebe')

# Se quisermos validar que foi chamado apenas uma vez, poderíamos usar o método
# assert_called_once_with().
# _-----------------------------------
# Uso de Mock e MagicMock
# Nomeando os simulados
# Pode ser útil dar nomes aos simulados. O nome é usado quando o simulado aparece
# nas mensagens de falha do teste. O nome também é propagado para atributos ou
# métodos do simulado:
# mock = MagicMock(name='foo')
# Classes Mock
# Assim como simular um método individual em uma classe, é possível simular uma
# classe inteira. Isto é feito fornecendo o decorador patch() com o nome da classe
# a ser alterada(patch)(sem atributos/métodos nomeados). Neste caso, a classe
# é substituída por um objeto MagicMock. Você deve, então, especificar como aquela classe
# deveria se comportar.
# import people
# from unittest.mock import *
# from unittest import TestCase
# from unittest import main

# class MyTest(TestCase):
#     @patch('people.Person')
#     def test_one(self, MockPerson):
#         self.assertIs(people.Person, MockPerson)
#         instance = MockPerson.return_value
#         instance.calculate_pay.return_value = 250.0
#         payroll = people.Payroll()
#         result = payroll.generate_payslip(instance)
#         self.assertEqual('You earned 250.0', result, 'payslip incorrect')

# Neste exemplo, a classe people.Person foi simulada. Esta classe tem um método
# calculate_pay() que espera receber um objeto Person. Então usa a informação
# fornecida pelo método calculate_pay() do objeto person para gerar a string
# retornada pelo método generate_payslip().
# ----------------------------------------
# Atributos em Classes Mock
# Os atributos de uma classe Mock são fáceis de se definir, por exemplo, se
# queremos definir um atributo em um objeto simulado então podemos apenas
# atribuir um valor para o atributo:
# import people
# from unittest.mock import *
# from unittest import TestCase
# class MyTest(TestCase):
#     @patch('people.Person')
#     def test_one(self, MockPerson):
#         self.asserIs(people.Person, MockPerson)
#         instance = MockPerson.return_value
#         instance.age = 24
#         instance.name = 'Adam'
#         self.assertEqual(24, instance.age, 'age incorrect')
#         self.assertEqual('Adam', instance.name, 'name incorrect')
#
# Neste caso, o atibuto age e name foram adicionados à instância simulada de people.Person.
# Se o atributo precisar ser um objeto simulado, então tudo que é exigido é que
# se atribua um objeto MagicMock (ou Mock) àquele atributo:
# instance.adress=MagicMock(name='Adress')
# ------------------------------------------
# Simulando constantes
# Isto é feito usando o decorador @patch() e dando o nome da constante e o novo
# valor a ser usado. Por exemplo:
# @patch('mymodule.MAX_COUNT', 10)
# def test_something(self):
# Teste pode, agora, usar mymodule.MAX_COUNT

# -----------------------------------------
# Simulando propriedades
# Também pode-se simular propriedades em Python. Novamente. isso é feito através
# do decorador @patch, mas usando unittest.mock.PropertyMock e o parâmetro
# new_callable:
# @patch('mymodule.Car.wheels', new_callable=mock.PropertyMock)
# def test_some_property(self, mock_wheels):
#     mock_wheels.return_value = 6

# ------------------------------------------
# Levantando exceções com Mocks
# Um atributo bastante útil que pode ser especificado quando um objeto mock é
# criado é o side_effect. Se ele for definido como uma classe ou instância de exceção
# então a exceção será levantada quando o simulado for chamado. Por exemplo:
# mock = Mock(side_effect=Exception('Boom!'))
# mock()

# ----------------------------------------------------
# Aplicando Patch para todos métodos de teste
# Se quiser simular algo para todos os teste em uma classe de teste, então
# pode decorar a classe inteira em vez de cada método individual. O efeito
# de decorar a classe é que o patch será automaticamente aplicado para todos
# os métodos de teste na classe (isto é, todos os métodos iniciando com a palavra
# 'teste'). Por exemplo:
# import people

# from unittest.mock import *
# from unittest import TestCase, main
# @patch('people.Person')
# class MyTest(TestCase):
#     def test_one(self, MockPerson):
#         self.assertIs(people.Person, MockPerson)
#     def test_two(self, MockSomeClass):
#         self.assertIs(people.Person, MockSomeClass)
#     def do_something(self):
#         return 'something'

# Na classe de teste acima, os testes test_one e test_two são fornecidos
# com a versão simulada da classe Person. Entretanto, o método do_something não é afetado.

# -----------------------------------------
# Usando Patch como gerenciador de contexto
# A função patch pode ser usada como um gerenciador de contexto. Ela fornece
# controle refinado sobre o alcance do objeto simulado. No seguinte exemplo,
# o método test_one() contém uma declaração with-as que usamos para patch(mock)
# a classe person como MockPerson. Esta classe simulada está disponível apenas
# dentro da declaração with-as.
# import people
# from unittest.mock import *
# from unittest import TestCase, main
# class MyTest(TestCase):
#     def test_one(self):
#         with patch('people.Person') as MockPerson:
#             self.assertIs(people.Person, MockPerson)
#             instance=MockPerson.return_value
#             instance.calculate_pay.return_value = 250.0
#             payroll = people.Payroll()
#             result = payroll.generate_payslip(instance)
#             self.assertEqual('You earned 250.0', result, 'payslip incorrect')

# --------------------------------------------
# Simule onde irá usar a simulação
# O erro mais comum feito por pessoas usando a biblioteca unittest.mock é
# simular no lugar errado. A regra é que você precisa simular onde irá
# usar a coisa; ou, em outras palavras, você sempre deve simular a coisa real
# onde ela será importada, não de onde ela foi importada.

# --------------------------------------------
# Problemas na ordenação de patches
# É possível ter vários decoradores patch em um método teste. Entretanto,
# a ordem na qual você define os decoradores patch é importante. A chave para
# entender qual deve ser a ordem é trabalhar de trás pra frente de modo que
# quando as simulações são passadas para o método de teste, são apresentados
# com os parâmetros corretos. Por exemplo:
# @patch('mymodule.sys')
# @patch('mymodule.os')
# @patch('mymodule.os.path')
# def test_something(self, mock_os_path, mock_os, mock_sys):
# resto do método de teste.
# Note que o últimado simulado do patch é passado para o segundo parâmetro
# do método test_something(). Por sua vez, o primeirp simulado do patch é passado
# como último parâmetro. Assim, os simulados são passados para o método teste
# na ordem reversa em que foram definidos.

# ------------------------------------------------
# Quantos simulados?
# O número de Mocks usados por teste é sujeito a debate na comunidade de
# teste de software. As regras gerais são dadas abaixo, mas deve-se ter
# em mente que são apenas guias e não regras rígidas.
#   * Evitar mais que 2 ou 3 Mocks por teste: Muitos consideram que se
#       você precisar de mais que 2-3 mocks por teste, então provavelmente
#       existem alguns problemas de design que precisam ser considerados.
#       Por exemplo, se você estiver testando uma classe Python, então aquela
#       classe pode ter dependências demais. Alternativamente, a classe pode
#       ter muitas responsabilidades e deveria ser dividida em diversas
#       classes independentes; cada qual com uma responsabilidade distinta.
#       Outra causa poderia ser que o comportamento da classe não está encapsulado
#       o suficiente e que você está permitindo que outros elementos interajam
#       com a classe de maneiras mais informais (isto é, a interface entre
#       a classe e outros elementos não é limpa/explorada o suficiente).
#   * Apenas simule seu vizinho mais próximo: Você deveria tentar evitar
#       simular dependências de dependências. Se você perceber que está
#       fazendo isso, então será mais difícil configurar, manter, entender
#       e desenvolver. Também será gradativamente mais provável que o que você
#       esteja testando sejam os simulados em vez da própria função/método/classe.

# ----------------------------------------------
# Considerações de simulação
# O seguinte fornece algumas regras gerais para considerar ao usar mocks:
#   * Não exagerar nos simulados
#   * Decidir o que simular: exemplos típicos incluem elementos que ainda
#       não estão disponíveis, que não são repetíveis por padrão ou que
#       são muito demorados ou complexos.
#   * Decidir onde simular: como interfaces para o teste unitário. Você pode
#       querer testar a unidade de modo que qualquer interface que ela tenha
#       com outro sistema, função, classe poderia ser candidata para simulação.
#   * Decidir quando simular
#   * Decidir como implementar as simulações
#

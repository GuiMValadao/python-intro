# Capítulo 15 - Framework de testes PyTest
# Existem vários frameworks disponíveis para Python, apesar de apenas um, unittest,
# faz parte da instalação típica do Python. Bibliotecas típicas incluem Unit test
# (que é embutida na instalação Python) e PyTest.
# ------------------------------------------
# PyTest é uma biblioteca para testes para Python; é, atualmente, uma das mais
# populars (outras incluem unittest e doctest). PyTest pode ser usada para vários níveis
# de teste, apesar da aplicação mais comum ser como um framework de testes unitários.
# Também é frequentemente usada como framework de teste dentro de projetos de desenvolvimento
# baseadas em TDD. De fato, é usada por Mozilla e Dropbox como seus frameworks de teste de Python.
# PyTest oferece um grande número de recursos e grande flexibilidade em como testes
# são escritos e em como o comportamento de configuração é definido. Ele automaticamente
# encontra testes baseado nas convenções de nome e pode ser facilmente integrada com
# uma grande quantidade de editores e IDEs.
# ----------------------------------------
# Um exemplo simples em PyTest
# Para explorar PyTest primeiro precisamos de algo para testar; portanto vamos
# definir uma classe Calculadora simples. Ela mantém um total recorrente das operações
# realizadas; permite que um novo valor seja definido e então este valor pode ser acrescido ou
# subtraído do total.
# class Caculadora:
#     def __init__(self):
#         self.current = 0
#         self.total = 0
#     def set(self, valor):
#         self.current = valor
#     def add(self):
#         self.total += self.current
#     def sub(self):
#         self.total -= self.current
#     def total(self):
#         return self.total

# Escrevendo um teste
# Agora criaremos um teste unitário muito simples com PyTest para a classe Calculadora.
# Este teste será definido em uma classe chamada teste_calculadora.py. Você terá
# de importar a classe calculadora que escrevemos no arquivo teste. Então definimos
# um teste, que deveria ser pre-fixado com test_ para PyTest encontrá-lo. De fato,
# PyTest usa várias convenções para encontrar teste, que são:
#   * Procura por arquivos test_*.py ou *_test.py
#   * Daqueles arquivos, coleta items de teste:
#       - funções de teste test_prefixed
#       - métodos de teste test_prefixed dentro de classes de teste Test prefixadas(sem um método __init__)
# Note que manteremos arquivos de teste e arquivos contendo o código a ser testado
# separados; de fato, em muitos casos eles são mantidos em diferentes estruturas de
# pastas. Isto significa que não terá chance de desenvolvedores acidentalmente usar
# testes em código de produção etc. Agora vamos adicionar ao arquivo uma função que
# define um teste. Vamos chamar a função test_add_one; ela precisa começar com test_ devido
# à convenção colocada acima. Entretanto, tentamos fazer o resto do nome da função
# descritivo, de forma que seja claro o que está sendo testado. A definição da função
# é dada abaixo:
# def test_add_one():
#     calc = Calculadora()
#     calc.set(1)
#     calc.add()
#     assert calc.total == 1


# A função teste cria uma nova instância da classe Calculadora e então chama vários
# métodos nela.
# A parte final do teste é a asserção. assert verifica que o comportamento da calculadora
# é o esperado. A declaração do PyTest assert encontra o que está sendo testado e o que
# deveria fazer com o resultado - incluindo acrescentar informação a ser colocada
# em um relatório de execução de testes. Ela evita a necessidade de precisar aprender
# uma grande quantidade de métodos do tipo 'assertSomething'. Note que um teste sem
# uma asserção NÃO é um teste; isto é, não está testando nada. Muitas IDEs fornecem suporte
# direto para frameworks de teste.
# ---------------------------------------
# Trabalhando com PyTest
# Testando funções:
# Podemos testar funções soltas (standalone) assim como classes usando PyTest. Por
# exemplo, fado a função increment abaixo :
# def increment(x):
#     return x + 1


# Podemos escrever um teste PyTest para isso como segue:
# def test_increment_integer_3():
#     assert increment(3) == 4

# Organizando testes
# Testes podem ser agrupados em um ou mais arquivos; PyTest buscará por todos os arquivos
# seguindo a convenção de nomeação (nomes de arquivo que começam ou terminam com 'test')
# nos locais especificados:
#   * Se nenhum argumento é especificao quando PyTest é executado, então a busca por
#       arquivos de testes nomeados de acordo começa da variável de ambiente testpaths
#       (se configurada) ou na pasta atual. Alternativamente, argumentos de linha
#       de comando podem ser usados em qualquer combinação de pastas ou nomes de arquivos etc.
#   * PyTest irá, recursivamente, procurar em subpastas, a menos que combinem com a
#       variável de ambiente norecursedirs.
#   * Nessas pastas, irá procurar por arquivos que combinem a convenção de nomes de teste
#       test_*.py ou *_test.py.
# Testes também podem ser arranjados dentro de arquivos de teste em classes de Teste.
# Usar classes de teste pode ser útil em agrupar testes e gerenciar o preparo e
# separar(tear down) comportamentos de grupos separados de testes. Entretanto, o mesmo
# efeito pode ser conseguido separando os testes relacionados a diferentes funções ou classes
# em arquivos diferentes.
# Acessórios de testes
# Não é incomum precisar executar algum comportamento antes ou depois de cada teste
# ou, de fato, antes ou depois de um grupo de teste. Tais comportamentos são definidos
# dentro do que é comumente conhecido como acessórios de testes.
# Podemos adicionar código especifico para executar:
#   * no início e fim de um módulo de teste de classe do código de teste(setup_module/teardown_module)
#   * no início e final de uma classe teste(setup_class/teardown_class) ou usando o estulo alternativo dos acessórios no nível de classe (setup/teardown)
#   * antes e após uma chamada de função teste (setup_function/teardown_function)
#   * antes e após uma chamada de método teste (setup_method/teardown_method)
# Para ilustra porque poderíamos usar um acessório, vamos expandir o teste da Calculadora:
# def test_initial_value():
#     calc = Calculadora()
#     assert calc.total == 0

# def test_add_one():
#     calc = Calculadora()
#     calc.set(1)
#     calc.add()
#     assert calc.total == 1
# def test_subtract_one():
#     calc = Calculadora()
#     calc.set(1)
#     calc.sub()
#     assert calc.total == -1
# def test_add_one_and_one():
#     calc = Calculadora()
#     calc.set(1)
#     calc.add()
#     calc.set(1)
#     calc.add()
#     assert calc.total == 2

# Agora temos 4 testes para executar (poderíamos ir além, mas isto é suficiente
# por hora). Um dos problemas com este conjunto de testes é que repetimos
# a criação do objeto Calculadora em cada início de cada teste. Enquanto
# isto não é um problema em si, ele resulta em código duplicado e na possibilidade
# de problemas futuros em termos de manutenção se quisermos alterar o modo
# com que uma calculadora é criada. Também pode não ser tão eficiente quanto
# reutilizar o objeto Calculadora para cada teste.
# Podemos, entretanto, definir um acessório que pode ser executado antes
# de cada teste de função individual ser executado. Para fazer isso, escrevemos
# uma nova função e usamos o decorador pytest.fixture naquela função. Isto
# marca a função como sendo especial e que pode ser usada como um acessório
# em uma função individual.
# Funções que requerem o acessório deveriam aceitar uma referência ao acessório
# como um argumento para a função teste individual. Por exemplo, para um teste
# aceitar um acessório chamado calculadora; deveria ter um argumento com o
# nomde do acessório, isto é, calculadora. Este nome pode, então, ser usado para
# acessar o objeto retornado. Isto é ilustrado abaixo:
# import pytest
# from calculadora import Calculadora

# @pytest.fixture
# def calculadora():
#     """ Retorna uma instância de Calculadora"""
#     return Calculadora()

# def test_initial_value(calculadora):
#     assert calculadora.total == 0

# def test_add_one(calculadora):
#     calculadora.set(1)
#     calculadora.add()
#     assert calculadora.total == 1

# def test_subtract_one(calculadora):
#     calculadora.set(1)
#     calculadora.sub()
#     assert calculadora.total == -1

# def test_add_one_and_one(calculadora):
#     calculadora.set(1)
#     calculadora.add()
#     calculadora.set(1)
#     calculadora.add()
#     assert calculadora.total == 2

# No código acima, cada uma das funções teste aceita o acessório caculadora
# que é usado para instancias o objeto Calculadora. Portanto, de-duplicamos
# nosso código; agora há apenas um pedaço de código que define como um objeto
# calculadora deveria ser criado para nossos testes. Note que cada teste é
# fornecido com uma instância completamente nova do objeto Calculadora; não há,
# portanto, nenhuma chance de um teste impactar outro teste.
# Também é considerado boa prática acrescentar uma docstring para seus
# acessórios como foi feito. Isto é pois PyTest pode criar uma lista de
# todos os acessórios disponíveis junto com suas docstrings. Da linha de comando,
# insto é feito usando:
# >pytest fixtures
# Os acessórios de PyTest podem ser aplicados a funções (como acima), classes,
# módulos, pacotes ou sessões. O alcance de um acessório pode ser indicado pelo
# parâmatro (opcional) scope ao decorador do acessório. O alcence determina
# em qual ponto um acessório deveria ser executado. Por exemplo, um acessório
# com escopo 'sessão' será executado uma vez para a sessão de teste, um acessório
# com escopo 'módulo' será executado uma vez para o módulo, um acessório com
# alcance de classe indica um acessório que é executado para cada nova instância
# de uma classe de teste criada etc.
# Outro parâmetro para o decorador acessório é autouse, que, se definido como
# True, ativará o acessório para todos os testes que pode ver. Se estiver definido
# como False (o padrão), então uma referência explícita em uma função teste
# (ou método) é exigida para ativar o acessório.
# Se adicionarmos alguns acessórios extras para os testes podemos ver quando
# são executados (alterado no arquivo test_calculadora.py). Para ver a saída dos
# testes, executar pelo terminal usando:
# > pytest -s path\test_calculadora.py.
# -----------------------------------------------------
# Testes parametrizados
# Um requisito comum de um teste é executar o mesmo teste múltiplas vezes
# com vários valores de entrada diferentes. Isto pode reduzir significativamente
# o número de testes que devem ser definidos. Tais testes são referidos como
# testes parametrizados; com os valores de parâmetro para o teste especificados
# usando o decorador @pytest.mark.parametrize.
# @pytest.mark.parametrize('input1, input2, expected', [(3,1,4), (3,2,5),])
# def test_calculadora_add_operacao(calculadora, input1, input2, expected):
#     calculadora.set(input1)
#     calculadora.add()
#     calculadora.set(input2)
#     calculadora.add()
#     assert calculadora.total == expected
# Isto ilustra a preparação de um teste parametrizado para a Calculadora no
# qual dois valores são somados e comparados com o resultado esperado. Note
# que os parâmetros são nomeados no decorador e então uma lista de tuplas é
# usada para definir os valores a serem usados para os parâmetros. Neste caso,
# o test_calculadora_add_operacao será executado duas vezes.
#
#  Testando para Exceções
#
# Pode-se escrever testes que verificam que uma exceção foi levantada. Isto
# é útil pois testar comportamento negativo é tão importante quanto testar
# comportamento positivo. Por exemplo, poderíamos querer verificar que uma
# exceção particular foi levantada quando tentamos sacar dinheiro de uma conta
# bancária que nos permitirá pegar valores acima do limite. Para verificar a
# presença de uma exceção em PyTest, usa-se a declaração 'with' e pytest.raises.
# Isto é um gerenciador de contexto que verificará na saída que a exceção
# especificada foi levantada. É usada como segue:
# with pytest.raises(accounts.BalanceError):
#     current_account.withdraw(200.0)
#
# Ignorando testes
#
# Em alguns casos, é útil escrever um teste para funcionalidades que ainda não
# foram implementadas; isto pode ser para garantir que um teste não é esquecido
# ou pois ajuda a documentar o que o item a ser testado deveria fazer. Entretanto,
# se o teste é executado então o conjunto de testes inteiro irá falhar pois
# o teste está sendo executado com comportamento que ainda será escrito.
# Uma maneira de lidar com esse problema é decorar um teste com o decorador
# @pytest.mark.skip:
# @pytest.mark.skip(reason='not implemented yet')
# def test_calculator_multiply(calculadora):
#     calculadora.multiply(2, 3)
#     assert calculadora.total == 6
# Isto indica que PyTest deveria guardar a presença do teste mas não deveria
# tentar executá-lo. PyTest notará então que o teste foi pulado.
# É geralmente considerado boa prática fornecer uma razão para a qual o teste
# foi pulado de modo que fica mais fácil manter controle. Esta informação também
# fica disponível quando PyTest pula o teste.

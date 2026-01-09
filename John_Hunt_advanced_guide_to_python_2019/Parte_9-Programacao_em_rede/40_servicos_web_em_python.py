# Capítulo 40 - Serviços web em Python
# Este capítulo trata da implementação de serviços web RESTful usando o framework Flask.

# Serviços RESTful
# REST significa Representation State Transfer(Tansferência de estado representacional)
# e foi um termo ideado por Roy Fielding em seu doutorado para descrever o estilo
# arquitetônico leve, orientado a recursos que sustenta a web. Fielding, um dos
# principais autores de HTTP, estava buscando um modo de generalizar a operação
# do HTTP e da web. Ele generalizou o fornecimento de páginas web como uma forma
# de dados fornecidos sob demanda a um cliente onde o cliente armazena o estado
# atual de uma troca. Baseado nesta informação de estado, o cliente pede o próximo
# item de dados relevantes a serem fornecidos com o pedido. Assim, os pedidos são
# independentes e não fazem parte de uma conversa síncrona(on-going) de estado (stateful).
# Deve-se notar que, apesar de Fielding ter pretendido criar uma maneira de descrever
# o padrão do comportamento dentro da web, ele também buscava produzir serviços
# baseados na web mais levers (que aqueles usados ou por frameworks proprietários
# da Enterprise Integration ou serviços SOAP). Esses serviços web mais leves,
# baseado em HTTP, tornaram-se muito populares e agora são amplamente usados em
# muitas áreas. Sistemas que seguem estes princípios são denominados serviços
# RESTful.
# Um aspecto chave de um serviço RESTful é que todas as interações entre um cliente
# são feitas usando operações simples baseadas em HTTP. HTTP suporta quatro operações,
# sendo elas GET, POST, PUT e DELETE. Elas podem ser usadas como verbos para indicar
# o tipo da ação sendo requisitada. Normalmente, são usados como segue:
#   * recuperar informação (HTTP Get)
#   * criar informação (HTTP Post)
#   * atualizar informação (HTTP Put)
#   * deletar informação (HTTP Delete)
# Deve-se notar que REST não é um padrão da mesma maneira que HTML é um padrão.
# Em vez disso, é um padrão de design que pode ser usado para criar aplicações
# web que podem ser invocadas por HTTP e dariam significado ao uso de operações
# HTTP Get, Post, Put e Delete com respeito a um recurso específico (ou tipo de dado).
# A vantagem da utilização de serviços RESTful como tecnologia, comparado com outras
# abordagens (como serviços baseado em SOAP que também podem ser invocados por
# HTTP) é que:
#   * as implementações tendem a ser mais simples
#   * a manutenção é facilitada
#   * executam sobre os protocolos padrão HTTP e HTTPS
#   * não requerem infraestruturas caras e licenças para utilização.
# Isto significa que os custos de servidor são menors. Há pouca dependência de
# vendedores ou tecnologia e os clientes não precisam saber nada sobre detalhes
# de implementação ou tecnologias em uso para a criação dos serviços.
# --------------------------------------------
# Uma API RESTful
# 1. Uma API RESTful é uma onde primeiro você deve determinar os conceitos chave
# ou recursos sendo representados ou gerenciados.
# 2. Eles poderiam ser livros, produtos em uma loja, reservas de quartos em hoteis
# etc. Por exemplo, um serviço relacionado a uma livraria poderia fornecer informações
# de recursos como livros, CDs, DVDs etc. Dentro desse serviço, livros são apenas
# um tipo de recurso. Vamos ignorar os outros recursos como DVDs e CDs etc.
# 3. Basaeado na ideia de um livro como um recurso, vamos identificar URLs
# apropriadas para esses serviços RESTful. Note que, apesar das URLs serem frequentemente
# usadas para descrever uma página web, aquele é apenas um tipo de recurso. Por exemplo,
# poderíamos desenvolver um recurso como:
# /bookservice/book
# Disto, poderíamos desenvolver uma URL baseada na API como:
# /bookservice/book/<isbn>
# Onde ISBN(Internation Standard Book Number) indica um número único para ser
# usado para identificar um livro específico cujos detalhes serão retornados usando
# esta URL.
# Também precisamos projetar a representação ou formatos que o serviço pode fornecer.
# Eles poderiam incluir texto bruto, JSON, XML etc. JSON é uma maneira concisa de
# descrever dados que serão transferidos de um serviço executando em um servidor
# para um cliente executando em um navegador. Este é o formato que usaremos na
# próxima seção. Como parte disso, poderíamos identificar uma série de operações
# a serem fornecidas pelos nossos serviços baseado no tipo do método HTTP usado
# para invocar nosso serviço e os conteúdos da URL fornecida. Por exemplo, para um
# simples BookServico, poderiam ser:
#   * GET /book/<isbn> - para recuperar um livro de um dado ISBN.
#   * GET /book/list - para recuperar todos os livros atuais em formato JSON.
#   * POST /book(JSON no corpo da mensagem) - que suporta a criação de um novo livro.
#   * PUT /book(JSON no corpo da mensagem) - para atualizar os dados de um livro existente.
#   * DELETE /book/<isbn> - para indicar que queremos deletar um livro específico da lista de livros armazenados.
# Perceba que o parâmetro isbn nas URLs acima forma parte do caminho URL.
# -------------------------------------------------
# Frameworks web em Python
# Existem muitos frameworks e bibliotecas disponíveis em Python que permitem a
# criação de um serviço web baseado em JSON; e o enorma número de opões disponíveis
# pode ser intimidador. Alguns exemplos são:
#   * Flask
#   * Django
#   * Web2py
#   * CherryPy
#   * FastAPI, para nomear alguns deles.
# Estes frameworks e bibliotecas oferecem diferentes grupos de recursos e níveis
# de sofisticação. Por exemplo, Django é um framework de web full-stack; isto é,
# permite desenvolvimento não só de serviços web mas de sites web inteiros.
# Entretanto, para nossos propósitos, isto é exagerado e a intergace Rest do
# Django é apenas uma parte pequena de uma infraestrutura muito maior. Obviamente,
# isso não significa que não poderíamos usar Django para criar nosso serviço de
# livraria; entretanto, existem opções mais simples disponíveis. O web2py é outro
# framework fullstack que desconsideraremos pela mesma razão.
# Em contraste, Flask e CherryPy são considerados frameworks não-fullstack
# (apesar de ser possível criar aplicações full-stack com eles). Isso significa
# que são mais leves e rápidos para começar a trabalhar. CherryPy foi, originalmente.
# mais focado em fornecer recursos de chamada remota que permitiam funções serem
# invocadas em vez de HTTP; mas foi estendido para fornecer recursos mais RESTful.
# Neste capítulo, focaremos em Flask, sendo um dos mais usados para serviços
# web leves em Python.
# ------------------------------------------------------
# Flask
# É um framework de desenvolvimento web para Python. Descreve si mesmo como um
# micro framework para Python, o que é meio confuso; ao ponto onde existe uma
# página dedicada a isso em seu site que explica o que significa e quais as implicações
# disso para o Flask. O micro em sua descrição tem a ver com seu objetivo primário
# de manter o cerne do Flask simples, mas extensível. Diferente do Django, ele
# não inclui recursos projetados para ajudar na integração da aplicação com uma
# base de dados, por exemplo. Em vez disso, Flask foca na funcionalidade central
# exigida de um framework de serviço web e permite que extensões sejam usadas como
# e quando necessário para funcionalidades adicionais.
# Flask também é um framework de convenções em vez de configurações; isto é, se
# seguir as convenções padrão, então não precisará lidar com muitras informações
# de configuração adicionais(apesar de que se você seguir um conjunto diferente de
# convenções, então pode fornecer informações de configuração para alterar os
# padrões). Como a maioria das pessoas vai (pelo menos inicialmente) seguir essas
# convenções, torna-se muito fácil conseguir alguma coisa executando rapidamente.
# --------------------------------------------------
# Olá mundo em Flask
# Usando JSON
# JSON é um formato leve de troca de dados que também é fácil de ler e escrever
# para humanos. Apesar de ser derivado de um subconjunto da linguagem de programação
# JavaScript, é, de fato, uma linguagem completamente independente e muitas
# linguagens e frameworks agora suporta automaticamente o processamento de seus
# próprios formatos de e para JSON, o que o torna ideal para serviços web RESTful.
# JSON é construído em algumas estruturas básicas:
#   * Uma coleção de pares nome/valor na qual o nome e valor são separados
#       por dois pontos ':' e cada par pode ser separado por vírgula ','.
#   * Uma lista ordenada de valores que são compreendidos em chaves '[]'.
# Isto torna bastante fácil construir estruturas que representam qualquer conjunto
# de dados, por exemplo, um livro com um ISBN, um título, qutor e preço poderiam
# ser representados por:
# {
#     "author": "Phoebe Cooke",
#     "isbn": 2,
#     "price": 12.99,
#     "title": "Java"
# }
# Por sua vez, uma lista de livros pode ser representada por um conjunto de livros
# separados por vírgula dentro de chaves:
# [{"author": "Gryff Smith", "isbn": 1, "price": 10.99, "title": "XML"},
# {"author": "Phoebe Cooke", "isbn": 2, "price": 12.99, "title": "Java"},
# {"author": "Jason Procter", "isbn": 3, "price": 11.55, "title":"C#"}]
# ----------------------------------------------------------------
# Implementando um serviço Web em Flask
# Existem vários passos envolvidos na criação de um serviço Web:
#   1. Importar Flask
#   2. Inicializar a aplicação Flask
#   3. Implementar uma ou mais funções (ou métodos) para suportar os serviços
#   4. Fornecer informação de roteamento para rotear da URL a uma função
#   5. Iniciar a execução do serviço web
# ----------------------------------------
# Um serviço simples
# Vamos criar um serviço web hello world. Para isso, devemos primeiro importar o
# módulo flask. Neste exemplo, vamos usar a classe Flask e jsonify() do módulo.
#
# from flask import Flask, jsonify

# app = Flask(__name__)


# O argumento passado para o construtor de Flask() é o nome do módulo ou pacote
# da aplicação. Como este é um exemplo simples vamos usar o atributo __name__
# do módulo que, nsete caso, será '__main__'. Em aplicações maiores, mais complexas,
# com vários pacotes e módulos, você deverá escolher um nome apropriado.
# A aplicação do objeto Flask implementa o WSGI (Web Server Gateway Interface)
# padrão para Python. ISto foi originalmente especificado na PEP-333 em 2003 e
# atualizado para Python 3 na PEP-3333 em 2010. Ele fornece uma convenção simples
# para como servidores web deveriam lidar requisições para aplicações. O objeto
# aplicação Flask é o elemento que pode rotear um pedido para uma URL apra uma
# função Python.
# -------------------------------------------------
# Fornecendo informação de roteamento
# Agora podemos definir a informação de roteamento para o objeto aplicação Flask.
# Esta informação mapeará uma URL para uma função. Quando aquela URL, pode exemplo,
# é entrada no campo URL de um navegador, então a aplicação Flask receberá aquela
# requisição e invocará a função apropriada. Para fornecer informação de mapeamento
# de rotas usamos o decorador @app.route em uma função ou método.
# Por exemplo, no seguinte código, o decorador @app.route mapeia a URL /hello à
# função welcome() para pedidos HTTP Get:
# @app.route("/hello", methods=["GET"])
# def welcome():
#     return jsonify({"msg": "Hello Flask World"})


# Existem duas coisas para se notar nesta definição de função:
#   * O decorador @app.route é usado para especificar declarativamente a informação
#       de roteamento para a função. Isto significa que a URL '/hello' será mapeada
#       à função welcome(). O decorador também especifica o método HTTP que é suportado;
#       neste caso, GET (que é, na verdade, o padrão, de modo que não precisaria ser
#       incluído aqui, mas é útil do ponto de vista de documentação).
#   * Vamos retornar nosso dado usando o formato JSON; portanto, usamos a função
#       jsonify() e passamos um dicionário Python a ela com um único par chave/valor.
#       Neste caso, a chave é 'msg' e o dado associado àquela chave é 'Hello Flask World'.
#       A função jsonify() converte esta estrutura Python em um JSON equivalente.
# --------------------------------------------------
# Executando o serviço
# Agora estamos prontos para executar nossa aplicação. Para isso, invocamos o método
# run() do objeto aplicação do Flask:
# app.run(debug=True)
# Opcionalmente, este método tem um parâmetro de palavra chave debug que pode ser
# definido como True; se isto é feito, então quando a aplicação for executada,
# alguma informação de debugging é gerada que permite que você veja o que está
# acontecendo. Isto pode ser útil no desenvolvimento mas normalmente não na produção.
#
# Ao executar este programa, a saída inicial gerada é mostrada abaixo:
#  * Serving Flask app '40_servicos_web_em_python'
#  * Debug mode: on
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000
# Press CTRL+C to quit
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 668-498-173
# 127.0.0.1 - - [09/Jan/2026 03:42:35] "GET / HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Jan/2026 03:42:35] "GET /favicon.ico HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Jan/2026 03:42:40] "GET /hello HTTP/1.1" 200 -

# Claro, não vemos nenhuma saída do programa ainda pois não invocamos a função
# welcome() pela URL /hello.
# -------------------------------------
# Invocando o serviço
# Usaremos um navegador web para acessar o serviço. Para isto, devemos entrar a
# URL completa que roteará a requisição para nossa aplicação em execução e fazer
# a função welcome().
# A URL é composta por dois elementos: o primeiro é a máquina onde a aplicação está
# em execução e o segundo é a porta que está usando para escutar por requisições.
# Isto é listado na saída acima: #  * Running on http://127.0.0.1:5000. Isto indica
# que a aplicação está executando na máquina 127.0.0.1 e escutando na porta 5000.
# Poderíamos usar localhost em vez de 127.0.0.1.
# O restante da URL deve ser fornecido, o que permitirá que Flask roteie do computador
# e porta para as funções que queremos executar. Assim, a URL completa é
# http://127.0.0.1:5000/hello, e a saída é o JSON da função welcome.
# Um recurso útil dessa abordagem é que se você alterar seu programa o framework
# Flask perceberá a alteração quando executar no modo desenvolvimento, e você
# pode reiniciar o serviço web com as alterações de códigos lançadas(deployed).
# Se fizer isso, verá que a saída notifica você da alteração. Isto também permite
# que mudanças sejam feitas na hora e seu efeito percebido imediatamente.
# ----------------------------------------
# A solução final
# Podemos organizar esse exemplo um pouco definindo uma função que pode ser usada
# para criar o objeto aplicação Flask e garantir que apenas executaremos a aplicação
# se o código for executado como o módulo main:
from flask import Flask, jsonify, url_for


def create_service():
    app = Flask(__name__)

    @app.route("/hello", methods=["GET"])
    def welcome():
        return jsonify({"msg": "Hello Flask World, alterando"})

    with app.test_request_context():
        print(url_for("welcome"))
    return app


if __name__ == "__main__":
    app = create_service()
    app.run(debug=True)

# Um recurso que acrescentamos a esse programa é o uso de test_request_context().
# O objeto retornado de test_request_context implementa o protocolo gerenciador
# de context e assim pode ser usado com uma declaração with; isto é útil para
# questões de debugging. Pode ser usado para verificar a URL usada para quaisquer
# funções com informação de rota especificada. Neste caso, a saída da declaração
# print é '/hello', pois é a URL definida no decorador @app.route.

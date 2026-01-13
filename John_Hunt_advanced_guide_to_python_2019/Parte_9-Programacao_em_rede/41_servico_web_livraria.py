# Capítulo 41 - Serviço Web Livraria


# Neste capítulo implementaremos o conjunto de serviços web
# descrito no capítulo 40 para uma livraria bastante simples.
# Isto significa que definiremos serviços para lisdar não só com pedidos
# GET mas também PUT, POST e DELETE para a API RESTful da livraria
from flask import Flask, abort, jsonify, request

from json import JSONEncoder


# -----------------------------------------------
# O Design
# Antes de analisarmos a implementação da API RESTful da livraria, vamos
# considerar quais elementos vamos usar para os serviços.
# A abordagem utilizada aqui é que a API de serviço Web fornece uma maneira
# de implementar uma interface para funções, objetos e métodos apropriados
# usados para implementar o modelo da aplicação/domínio.
# Isto significa que teremos um conjunto de classes que representarão
# a Livraria e os Livros armazenados nela. Por sua vez, as funções implmentando
# os serviços web acessarão a livraria para recuperar, modificar, atualizar
# e deletar os livros armazenados na livraria. O design geral é mostrado
# na Figura design.png. Ela mostra que um objeto Livro terá os atributos
# ISBN, título, autor e preço. Por sua vez, o objeto Livraria terá um
# atributo livros que armazenará zero ou mais Livros. O atributo livros
# armazenará uma List pois a lista de livros precisará mudar dinamicamente
# como e quando novos livros forem acrescentados ou livros velhos deletados.
# A Livraria também definirá três métodos que irão:
#   * permitir que um livro seja obtido por seu ISBN;
#   * permitir que um livro seja adicionado à livraria;
#   * permitir que um livro seja deletado da livraria por seu ISBN.
# A informação de roteamento será fornecida para um conjunto de funções que
# invocarão métodos apropriados no objeto Livraria. As funções a serem
# decoradas com @app.route, e os mapeamentos a serem usados, são:
#   * get_livros() que mapeia para a URL /livro/lista usando o método HTTP Get;
#   * get_livro(isbn) que mapeia para a URL /livro/<isbn> usando o método HTTP Get
#       onde <isbn> é um parâmetro URL que será passado à função;
#   * create_livro() que mapeia para a URL /livro usando o método HTTP Post;
#   * update_livro(isbn) que mapeia para a URL /livro/<isbn> usando o método HTTP Put;
#   * delete_livro(isbn) que mapeia para a URL /livro/<isbn> usando o método HTTP Delete.
# -----------------------------------------------
# O Modelo de Domínio
# O modelo de domínio consiste nas classes Livro e Livraria. Elas são:
class Livro:
    """Representa um livro na livraria"""

    def __init__(self, isbn, titulo, autor, preco):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

    def __str__(self):
        return (
            self.titulo
            + " por "
            + self.autor
            + " (ISBN: "
            + str(self.isbn)
            + ", Preço: R$"
            + str(self.preco)
            + ")"
        )


class Livraria:
    def __init__(self, livros):
        self.livros = livros

    def get(self, isbn):
        if isbn > len(self.livros):
            abort(404)
        return list(filter(lambda l: str(l.isbn) == str(isbn), self.livros))[0]

    def add_livro(self, livro):
        self.livros.append(livro)

    def delete_livro(self, isbn):
        self.books = list(filter(lambda l: l.isbn != isbn, self.livros))


# No código acima, o atributo livros armazena a lista dos livros disponíveis.
# O método get(isbn) retorna o livro com o ISBN fornecido.
# O método add_livro(livro) adiciona um novo objeto livro à livraria.
# O método delete_livro(isbn) remove um livro com o ISBN fornecido.
# A variável global livraria armazena o objeto Libraria inicializado com
# um conjunto padrão de livros:
livraria = Livraria(
    [
        Livro(1, "Effective Java", "Joshua Bloch", 45.0),
        Livro(2, "Design Patterns", "Gang of Four", 50.0),
        Livro(3, "Effective C++", "Scott Meyers", 42.0),
    ]
)


# -----------------------------------------------
# Codificando Livros em JSON
# Apesar da função jsonify() saber como converter tipos embutidos como
# strings, inteiros, listas, dicionários etc em um formato JSON apropriado,
# não sabe como converter objetos definidos pelo usuário como Livro.
# Portanto, precisamos definir uma função auxiliar que converta um objeto
# Livro em um dicionário que possa ser convertido em JSON.
# Uma maneira de fazermos isso é definir um método que pode ser chamado
# para converter uma instância de Livro para o formato JSON. Isto é
# feito através do método to_json():
# o método abaixo pode ser usado para obter um dicionário que pode ser transformado
# em um JSON.
# def to_json(self):
#     return {
#         'isbn': self.isbn,
#         'titulo': self.titulo,
#         'autor': self.autor,
#         'preco': self.preco
#     }
# Poderíamos, agora, usar este método com a função jsonify() para converter
# um livro para o formato JSON:
# jsonify({'livro': book.to_json()})
# Esta abordagem funciona e fornece uma maneira bem leve de converter um
# livro para um JSON. Entretanto, a abordagem acima significa que toda
# vez que quisermos jsonify um livro, precisamos lembrar de chamar o
# método to_json(). Em alguns casos, isso pode significar que também
# precisaremos escrever código um pouco convoluto. Por exemplo, se quisermos
# retornar uma lista de livros da Livraria como uma lista JSON, poderíamos
# escrever:
# jsonify({'livros': [livro.to_json() for livro in livraria.livros]})
# Aqui usamos uma list comprehension para criar uma lista contendo as versões
# JSON dos livros armazenados na livraria.
# Isto começa a parecer um pouco complicado e fácil de se esquecer e provavelmente
# levará a erros sutis. O próprio Flask usa codificadores para codificar tipos
# para o JSON. Ele também permite que definamos nossos próprios codificadores
# personalizados para tipos definidos pelo usuário, como a classe Livro,
# para um JSON. Estes codificadores podem ser usados automaticamente pela função
# jsonify().
# Para fazer isso, devemos implementar uma classe codificadora que estenderá
# a superclasse flask.json.JSONEncoder. A classe precisa definir um método
# default(self, obj). Este método pega um objeto e retorna a representação
# JSON daquele objeto. Podemos, assim, escrever um codificador para a classe
# Livro da seguinte maneira:
class LivroJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Livro):
            return {
                "isbn": obj.isbn,
                "titulo": obj.titulo,
                "autor": obj.autor,
                "preco": obj.preco,
            }
        return super(LivroJSONEncoder, self).default(obj)


# O método default() nesta classe checa que o objeto passado a ele é uma
# instância da classe Livro e, se for, então criará uma versão JSON do livro.
# A estrutura JSON é baseada nos atributos isbn, titulo, autor e preco.
# Se não for uma instância da classe Livro, então passa o objeto para a
# classe pai.
# Agora podemos registrar este codificador com o objeto aplicação Flask para
# que possa ser usado sempre que um livro precise ser convertido para JSON.
# Isto é feito atribuindo o codificador à propriedade app.json_encoder do Flask:
app = Flask(__name__)
# app.json_encoder = LivroJSONEncoder   # json_encoder foi depreciado em Flask 2.2.0
# app.json_provider_class. = LivroJSONEncoder


# Agora, se quisermos converter um único livro ou uma lista de livros,
# o conversor acima será usado automaticamente. Dessa forma, nosso exemplo
# anterior poderiam ser escritos simplesmente como:
# jsonify({'livro': livro})
# jsonify({'livros': livraria.livros})
# -----------------------------------------------
# Preparando os serviços GET
# Agora podemor preparar dois serviços que lidam com pedidos GET, sendo
# eles /livro/lista e /livro/<isbn>. As funções que essas URLs mapearão
# são dadas abaixo:
@app.route("/livro/lista", methods=["GET"])
def get_livros():
    livros = LivroJSONEncoder().encode(livraria.livros)
    return livros


@app.route("/livro/<int:isbn>", methods=["GET"])
def get_livro(isbn):
    livro = LivroJSONEncoder().encode(livraria.get(isbn))
    return livro
    # if livro:
    #     return jsonify({'livro': livro})
    # return jsonify({'error': 'Livro não encontrado'}), 404


# A primeira função simplesmente retorna a lista atual de livros com uma
# estrutura JSON usando a chave 'livros'. A segunda funçao pega um número
# isbn como parâmetro. Ele é um parâmetro de URL, ou seja, parte da URL
# usada para invocá-la. Isto significa que um usuário pode pedir detalhes de
# livros com diferentes ISBNs apenas alterando o elemento ISBN da URL, por
# exemplo:
#   * /book/1
#   * /book/2
# Para indicar em Flask que alguma coisa é um parâmetro de URL em vez de um
# elemento fixo(hard coded) da URL, usamos os sinais de menor e maior
# (< >) para envolver o nome do parâmetro. Eles circundam o nome do parâmetro
# de URL e permitem que seja passado para a função(usando o mesmo nome).
# No exemplo acima, também indicamos (opcionalmente) o tipo do parâmetro.
# Por padrão, o tipo é uma string; entretanto, sabemos que o ISBN é um número
# inteiro e, portanto, indicamos isso usando <int:isbn> em vez de apenas <isbn>.
# Existem outras opções disponíveis, como string(o padrão), int, float, uuid
# e path(uma string que pode conter barras).
# Podemos, novamente, usar um navegador para ver o resultado do chamado desses
# serviços. Desta vez, as URLs serão:
#   * http://localhost:5000/livro/lista (http://127.0.0.1:5000/livro/lista)
#   * http://localhost:5000/livro/1 (http://127.0.0.1:5000/livro/1)
# ---------------------------------------------------
# Deletando um livro
# Para deletar um livro o serviço web é bem similar ao serviço de obter um livro
# pois pega um parâmetro de caminho isbn. Entretanto, neste caso ele simplesmente
# retorna o reconhecimento que o livro foi deletado:
@app.route("/livro/<int:isbn>", methods=["DELETE"])
def delete_livro(isbn):
    livraria.delete_livro(isbn)
    return jsonify({"result": "Livro deletado com sucesso"})


# Entretanto, não podemos mais testar isso simplesmente usando um navegador.
# Isto pois o navegador usa o método HTTP GET para todas as URLs digitadas
# no campo URL. Entretanto, o serviço web de deleção está associado com o
# método HTTP DELETE. Para invocar delete_book() precisamos garantir que o
# pedido que é enviado usa o método DELETE. Isto pode ser feito de um cliente
# que pode indicar o tipo de pedido sendo usado. Exemplos poderiam incluir
# outro programa Python, um web site JavaScript, etc. No livro, é usado o
# programa curl, disponível para Linux e Mac. Ele é uma ferramenta de
# linha de comando e biblioteca que pode ser usada para enviar e receber
# dados pela internet. Ela suporta uma grande variedade de protocolos e padrões
# e, em particular, HTTP e HTTPS, e pode ser usada para enviar e receber
# dados usando diferentes métodos HTTP, incluindo GET, POST, PUT e DELETE.
# Por exemplo, para invocar a função delete_livro() usando a URL /livro/2
# e o método HTTP DELETE pode-se usar curl como segue:
# curl http://localhost:5000/livro/2 -X DELETE
# Isto indica que queremos invocar a URL mostrada e que queremos usar um método
# de pedido customizado (ou seja, não o padrão GET), que neste caso é DELETE
# (indicado pela opção -X). O resultado retornado pelo comando é {"result":true}.
# ---------------------------------------------------
# Acrescentando um novo livro
# Também queremos suportar a adição de novos livros à livraria. Os detalhes de
# um novo livro poderiam apenas ser acrescentados _a URL como parâmetros de
# caminho; entretanto, conforme a quantidade de dados a ser adicionados cresce,
# isto tornaria-se cada vez mais difícil de manter e verificar. De fato,
# apesar de historicamente ter existido um limite de 2083 caracteres no
# Microsoft Internet Explorer, que foi teoricamente removido desde IE8,
# na prática ainda existem limites para o tamanho das URLs. A maioria dos
# servidores web tem um limite de 8 KB (8192 bytes), apesar disso ser
# normalmente configurável. Também podem existir limites do lado do cliente.
# Se o limite é excedido seja no navegador ou no servidor, então a maioria
# dos sistemas apenas truncará os caracteres fora do limite (em alguns casos
# sem aviso prévio).
# Normalmente, estes dados são enviados ao corpo do pedido HTTP como parte de
# um pedido POST. O limite para o tamanho do corpo do pedido é muito maior,
# normalmente até 2 GB. Isto significa que é um modo muito mais confiável
# e seguro de transferir dados para um serviço web. No entanto, deve ser
# notado que isto não significa que o dado é mais seguro do que se for parte
# da URL; apenas que é enviado de uma maneira diferente. Do ponto de vista
# das funções Python invocadas como resultado do método POST, isto significa
# que os dados não estão disponíveis como um parâmetro para a URL e, assim,
# para a função. Em vez disso, dentro da função é preciso obter o objeto
# pedido e então usá-lo para obter a informação do corpo do pedido.
# Um atributo chave do objeto pedido, disponível quando um pedido HTTP
# contém dados JSON, é o atributo request.json. Este atributo contém uma
# estrutura do tipo dicionário armazenando os valores associados com chaves
# na estrutura JSON. Isto é mostrado abaixo, para a função create_livro():


@app.route("/livro", methods=["POST"])
def create_livro():
    if not request.json or not "isbn" in request.json:
        abort(400)
    livro = Livro(
        isbn=request.json["isbn"],
        titulo=request.json["titulo"],
        autor=request.json.get("autor", ""),
        preco=float(request.json["preco"]),
    )
    livraria.add_livro(livro)
    return LivroJSONEncoder().encode(livraria.livros), 201


# A função acima acessa o objeto flask.request que representa o pedido
# HTTP atual. Primeiro ela checa se o pedido contém dados JSON e se a chave
# 'isbn' está presente no JSON. Se não, a função flask.abort() é chamada
# passando o código de erro HTTP 400 (Bad Request). Neste caso, o erro
# indica que foi um Pedido Inválido(Bad Request).
# Entretanto, se dados JSON estiverem presentes e conter um número ISBN, então
# os valores para as chaves 'isbn', 'titulo', 'autor' e 'preco' são extraídos.
# Como JSON é uma estrutura tipo dicionário, podemos extrair os valores tanto
# através do uso de colchetes (por exemplo, request.json['isbn']) ou do uso
# de métodos de dicionário (por exemplo, request.json.get('autor', '')).
# Por fim, como queremos tratar o preço como um número de ponto flutuante,
# devemos usar a função float() para converter o formato string do JSON
# para um número. Usando os dados extraídos, podemos instanciar uma nova
# intância de Livro que pode ser acrescentada à livraria. Como é comum em
# serviços web, estamos retornando o objeto recém-criado como resultado de
# sua criação junto com a resposta HTTP 201 (Created).
# Podemos testar esse serviço usando curl como segue:
#   curl -i -H "Content-Type: application/json" -X POST -d
#   '{"isbn":4,"titulo":"The C Programming Language","autor":"Kernighan e Ritchie",
#   "preco":37.5}' http://localhost:5000/livro
# As opções usadas com este comando indicam o tipo de dado sendo enviado no
# corpo do pedido(-H) junto com dados para serem incluídos no corpo do pedido
# (-d). O resultado é:
{
    "book": {
        "author": "Kernighan e Ritchie",
        "isbn": 4,
        "price": 37.5,
        "title": "The C Programming Language",
    }
}


# ---------------------------------------------------
# Atualizando um livro
# Atualizar um livro já armazenado pela livraria é bastante similar a acrescentar
# um livro, exceto que o método PUT em vez de POST é usado.
# Novamente, a função implementando o comportamento pedido deve usar flask.request
# para acessar os dados submetidos no corpo do pedido. Entretanto, nesse
# caso o número ISBN especificado é usado para encontrar o livro a ser atualizado
# em vez de especificar um livro novo. A função é dada abaixo:
@app.route("/livro", methods=["PUT"])
def update_livro():
    if not request.json or not "isbn" in request.json:
        abort(400)
    isbn = request.json["isbn"]
    livro = livraria.get(isbn)
    livro.titulo = request.json["titulo"]
    livro.autor = request.json["autor"]
    livro.preco = request.json["preco"]
    return LivroJSONEncoder().encode(livro), 201


# ---------------------------------------------------
# O que ocorre se errarmos algo?
# O código acima da livraria não é particularmente defensivo, pois é possível
# tentar acrescentar um novo livro com o mesmo ISBN que o já existente. Entretanto,
# ele checa se um número ISBN foi fornecido ao tentar criar ou atualizar um livro.
# Mas o que ocorre se o número não é especificado? Em ambas funções, chamamos
# a função flask.abort(). Por padrão, se isso ocorrer um mensagem de erro
# é enviada ao cliente.
# Por padrão, Flask gera uma página HTML simples contendo a mensagem de erro.
# Podemos alterar isso definindo nossa própria função de manipulador de erros.
# Esta é uma função decorada com @app.errorhandler() que fornece o código
# de status da resposta que resolve. Por exemplo:
@app.errorhandler(400)
def not_foung(error):
    return jsonify({"livro": "Não encontrado"}), 400


# Agora, quando um erro 400 é gerado pela função abort(), a função acima
# é invocada para gerar a resposta de erro.
# ---------------------------------------------------


if __name__ == "__main__":
    app.run(debug=True)

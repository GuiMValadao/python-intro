# APIs RESTful é uma arquitetura de software utilizada para criar serviços
# web escaláveis. Criado por Roy Fielding em 2000, o REST é baseado em um
# conjunto de pricípios e restrições que promovem uma comunicação eficaz
# entre sistemas distribuídos. Utilizam o protocolo HTTP.
# As APIs RESTful são projetadas em torno de recursos, que  são qualquer
# tipo de objeto, dados ou serviço que podem ser acessados pelo cliente. Um
# recurso tem um identificador, que é um URL, que identifica exclusivamente
# o recurso.
# Consistência, escalabilidade e legibilidade.
# 7 boas práticas.
# ----------------------------------------
# 1 - Utilização de substantivos em Rotas
# Usar substantivos plurais para representar recursos. Por exemplo, get('/users')
# em vez de get('/getUsers')
# exemplo(Python):


# from flask import Flask, jsonify

# app = Flask(__name__)


# # Rota correta com substantivo plural
# @app.route("/products", methods=["GET"])
# def get_products():
#     return jsonify({"message": "Listando todos os produtos"})


# # Rota incorreta com verbo
# @app.route("/retrieveAllProducts", methods=["GET"])
# def retrieve_all_products():
#     return jsonify({"message": "Listando todos os produtos"})


# -----------------------------------------
# 2 - Utilização de Métodos HTTP
# Os métodos HTTP são fundamentais para a comunicação entre clientes (como
# navegadores) e servidores na web. Dfinem a ação que o cliente deseja realizar
# no servidor.
# Exemplos simples de uma API RESTful
# A Um exemplo clássico seria um serviço que gerencia um catálogo de produtos.
# A API poderia ter endpoints como:
#   * GET /products - recupera uma lista de todos os produtos
#   * GET /products/{id} - Recupera detalhes de um produto específico
#   * POST /products - Adiciona um novo produto ao catálogo
#   * PUT /products/{id} - Atualiza as informações de um produto existente
#   * DELETE /products/{id} - Remove um produto do catálogo

# GET: Recuperar recursos. É usado para solicitar dados de um servidor. Não
#   altera o estado dos dados no servidor.
# exemplo: Python(usando requests)


# from flask import Flask, request, jsonify

# app = Flask(__name__)

# users=[]
# @app.route('/users', methods=['GET'])
# def get_users():
#     return jsonify(users), 200

# @app.route('/users', methods=['POST'])
# def add_user():
#     new_user = request.get_json()
#     users.append(new_user)
#     return jsonify(new_user), 201
# if __name__ == '__main__':
#     app.run(debug=True)


# POST: é usado para enviar dados ao servidor para criar um novo recurso.
#   Altera o estado do servidor, geralmente criando um novo registro.

# exemplo(Python)

# import requests #acrescentar à importação do flask
# novo_usuario = {'nome': "João", "idade":30}
# response = requests.post('https://api.exemplo.com/usuarios', json=novo_usuario)
# print(response.json())

# PUT/PATCH: Atualizar recursos existentes. PUT substitui completamente um
#   recurso existente no servidor, enquanto PATCH realiza uma atualização
#   parcial, alterando apenas os campos especificados.

# exemplo(Python)
# import requests

# atualizacao_usuario = {"idade": 31}
# response = requests.patch("https://api.exemplo.com/usuarios/1", json=atualizacao_usuario)
# print(response.json())

# DELETE: Remove um recurso
# import requests
# response = requests.delete('https://api.exemplo.com/usuarios/1')
# print(response.json())
# --------------------------------------------
# 3 - Hierarquia e aninhamento em rotas
# Aninhamento de rotas significa criar uma URL que segue uma estrutura hierárquica
# para representar a relação entre diferentes recursos.
# Exemplo prático: pedidos de usuários
# Considere uma API que lida com usuários e os pedidos feitos por esses usuários.
# Se quisermos acessar todos os pedidos de um usuário específico, é comum
# usar uma rota que reflete essa relação:
# *URL: /users/{usersID}/orders
#
# Exemplos(Python)
# from flask import Flask, request

# app = Flask(__name__)


# @app.route("/users/<int:userId>/orders")
# def get_orders(userId):
#     return f"Pedidos do usuário {userId}"


# if __name__ == "__main__":
#     app.run(debug=True)

# ---------------------------------------------
# 4 - Nome de Ações
# Quando estamos desenvolvemtn APIs, é essencial seguir boar práticas para garantir
# que os endpoints(URLs) sejam intuitivos e fáceis de usar. Um dos princípios
# é evitar o uso de verbos ou ações nos URLs. Em vez disso, deve-se usar o método
# HTTP apropriado para indicar a ação que se quer realizar.
# Os métodos HTTP já foram criados para representar as operações que queremos
# realizar em um recurso.
# Exemplo(Python)
# from flask import Flask, request, jsonify

# app = Flask(__name__)


# @app.route("/users", methods=["POST"])
# def create_user():
#     new_user = request.json
#     return jsonify({"message:" "Usuário criado com sucesso!"}), 201


# if __name__ == "__main__":
#     app.run(port=5000)

# --------------------------------------------
# 5 - Versionamento de rotas
# Permite que sejam feitas mudanças na API sem afetar os clientes que
# dependem de versões anteriores.
# O versionamento de rotas permite que sejam mantidas mútliplas versões
# da API em paralelo. Cada versão é identificada por um número de versão
# que é incluído na URL das rotas.

# Exemplo em Python com Flask
# from flask import Flask, jsonify

# app = Flask(__name__)


# # Versão 1 da rota /users
# @app.route("/v1/users", methods=["GET"])
# def get_users_v1():
#     return jsonify([{"id": 1, "name": "John Doe v1"}])


# # Versão 2 da rota /users
# @app.route("/v2/users", methods=["GET"])
# def get_users_v2():
#     return jsonify([{"id": 1, "name": "John Doe v2", "email": "john@exemplo.com"}])


# if __name__ == "__main__":
#     app.run(port=5000)

# -------------------------------------------
# 6 - Parâmetros de consulta
# São parte de uma URL que permite que informações adicionais sejam enviadas para
# um servidor. Eles são usados para filtrar, paginar e ordenar dados, entre
# outras funções. São anexados à URL após um ponto de interrogação (?), e múltiplos
# parâmetros são separados por um e comercial (&).
# Exemplo Python
# Supondo que queremos buscar produtos de uma API com a categoria 'eletrônicos',
# limitar a 10 resultados por página, iniciar na primeira página e ordenar por preço.
# import requests
# url = 'https://example.com/products'
# params = {
#     'category': 'eletronics',
#     'limit': 10,
#     'page': 1,
#     'sort': 'price'
# }

# response = requests.get(url, params=params)
# print(response.json())
# ------------------------------------------------
# 7 - Tratamento de Erros
# Os códigos de status HTTP são mensagens enviadas pelo servidos para o
# cliente após o processamento de uma requisição. Eles indicam se a requisição
# foi bem-sucedida, se houve um erro ou se algo precisa ser corrigido.
# 1XX - Informational Codes: O servidor reconhece e está processando a solicitação.
# 2XX - Sucess Codes: O servidor recebeu, compreendeu e processou com sucesso a solicitação.
# 3XX - Redirection codes: O servidor recebeu a solicitação, mas há um redirecionamento para outro lugar.
# 4XX - Client Error Codes: O servidor não conseguiu encontrar(ou alcançar) a página ou o site. É um erro do lado do site
# 5XX - Server Error Codes: O cliente faz uma solicitação válida, mas o servidor falhou ao completar a solicitação.

# Exemplo
# from flask import Flask, jsonify, abort

# app = Flask(__name__)


# @app.route("/resource")
# def get_resource():
#     resource = None
#     if resource:
#         return jsonify(resource), 200
#     else:
#         abort(404, description="Recurso não encontrado")


# @app.errorhandler(400)
# def bad_request(error):
#     return str(error), 400


# if __name__ == "__main__":
#     app.run(port=3000)

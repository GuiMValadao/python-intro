# Capítulo 39 - Sockets em Python
# Um Socket é um endpoint em um link de comunicação entre processos separados.
# Em Python, sockets são objetos que fornecem uma maneira de trocar informação
# entre dois processos de maneira direta e independente de plataforma.
# ---------------------------------------
# Comunicação Socket com Socket
# Quando fois processos de nível de sistema operacional querem se comunicar,
# eles podem fazê-lo através de sockets. Cada processo tem um socket que é
# conectado ao socket do outro. Então, um processo pode escrever informação no
# socket, enquanto o segundo processo pode ler informação do socket.
# Associado com cada socket estão dois fluxos, um para entrada e um para saída.
# Assim, para passar informação de um processo para outro, deve-se escrever
# informação para o fluxo de saída de um objeto socket e lê-lo do fluxo de
# entrada de outro objeto socket (assumindo que ambos estão conectados).
# Vários tipos diferentes de sockets estão disponíveis, mas nesse capítulo vamos
# focar no TCP/IP. Um socket assim é orientado-a-conexão que fornecerá uma
# garantia de entrega dos dados (ou notificação em caso de falha na entrega).
# TCP/IP é uma suite de protocolos de comunicação usados para interconectar
# dispositivos de rede na internet ou em uma intranet privada. TCP/IP especifica
# como dados são trocados entre programas pela internet fornecendo comunicações
# end-to-end que identificam como os dados deveriam ser divididos em pacotes
# (packets), endereçados, transmitidos, roteados(routed) e recebidos no destino.
# ---------------------------------------------
# Preparando uma conexão
# Para preparar uma conexão, um processo deve estar executando um programa que
# esteja esperando por uma conexão enquando o outro deve tentar conectar com o
# primeiro programa. O primeiro é chamado como socket servidor e o segundo
# apenas socket. Para o segundo processo se conectar com o primeiro, deve saber
# qual máquina o primeiro está executando e qual porta está conectado.
# Por exemplo, na figura socketconection.png o socket servidor se conecta com
# a porta 8084. Por sua vez, o socket cliente se conecta à máquina na qual o
# servidor está executando e à porta 8084 daquela máquina.
# Nada acontece até que o socket servidor aceite a conexão. Naquele ponto, os
# sockets estão conectados, e os fluxos de sockets estão ligados um com o outro.
# Isto significa que o fluxo de saída do servidor está conectado ao fluxo de
# entrada do socket cliente e vice versa.
# -----------------------------------------------
# Uma aplicação de exemplo de cliente servidor
# O diagrama socketconection.png ilustra a estrutura básica do sistema que vamos
# tentar construir. Haverá um objeto servidor executando na máquina e um objeto
# cliente executando em outra. O cliente conectará ao servidor usando sockets
# para poder obter informação.
# A aplicação real sendo implementada neste exemplo é uma aplicação de busca de
# endereços. Os endereços dos empregados de uma empresa são armazenados em um
# dicionário. Este dicionário é configurado no programa do servidor mas poderia
# igualmente ser armazenado em uma base de dados etc. Quando um cliente se conecta
# com o servidor, pode obter o endereço do escritório de um empregado.
#
# ------------------------------------------------
# Implementando a aplicação servidor
# Primeiro descreveremos a aplicação servidor. Ela é o programa aplicativo Python
# que irá servir pedidos(requests) das aplicações cliente. Para isto, deve fornecer
# um socket de servidor com o qual os clientes se conectarão. Isto é feito prendendo
# um socket servidor a uma porta na máquina servidor. O programa servidor deve, então,
# escutar por conexões que chegarem.
# O programa abaixo apresenta o código fonte do programa servidor:
# import socket


# def main():
#     addresses = {"JOHN": "C45", "DENISE": "C44", "PHOEBE": "D52", "ADAM": "B23"}
#     print("Iniciando o servidor")
#     print("Criando um soket")
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print("Liga o socket à porta")
#     server_address = (socket.gethostname(), 8084)
#     print("Iniciando em", server_address)
#     sock.bind(server_address)

#     print("Esperando pela chegada de conexões")
#     sock.listen(1)
#     while True:
#         print("Esperando por uma conexão")
#         connection, client_address = sock.accept()
#         try:
#             print("Connection de", client_address)
#             while True:
#                 data = connection.recv(1024).decode()
#                 print("Recebido:", data)
#                 if data:
#                     key = str(data).upper()
#                     response = addresses[key]
#                     print("Enviando dados de volta para o cliente:", response)
#                     connection.sendall(response.encode())
#                 else:
#                     print("Sem mais dados de", client_address)
#                     break
#         finally:
#             connection.close()


# if __name__ == "__main__":
#     main()

# O servidor acima prepara os endereços que contém um Dicionário de nomes e endereços.
# Então espera pela conexão de um cliente. Isto é feito criando um socket e prendendo-o
# a uma porta específica (neste caso 8084), nas linhas 63 - 66.
# A construção do objeto socket é discutida em mais detalhes na próxima seção.
# Em seguida, o servidor escuta por uma conexão de um cliente. Note que sock.listen()
# pega o valor 1, indicando que lidará com 1 conexão por vez.
# Um loop infinito é, então, preparado. Quando uma conexão é feita de um cliente,
# ambos conexão e endereço do cliente tornam-se disponíveis. Enquanto existem dados
# disponíveis do cliente, são lidos usando a função recv. Note que dados recebidos
# do cliente são assumidos como sendo string. Isto é, então, usado como chave para
# procurar o endereço no Dicionário 'address'.
# Após obter o endereço, ele é retornado para o cliente. Em Python 3, pe necessário
# usar decode() e encode() para decodificar/codificar o formato da string para dados
# brutos transmitidos pelos fluxos do socket. Note que deve sempre fechar um socket
# quando terminar de usá-lo.
# --------------------------------------------------------
# Tipos de socket e domínios
# Quando criamos a classe socket acima, passamos dois argumentos para o construtor:
# socket(socket.AF_INET, socket.SOCK_STREAM)
# Para entender esses dois valores, é necessário entender que os sockets são
# caracterizados de acordo com duas propriedades: o domínio e seu tipo.
# O domínio de um socket refere-se, essecialmente, aos protocolos de comunicação
# que são usados para transferir dados de um processo para outro. Também encorpora
# como sockets são nomeados (para que possam ser referenciados ao estabelecer a
# comunicação).
# Dois domínios padrão são disponíveis nos sistemas Unix: eles são o AF_UNIX que
# representa comunicações intra-sistemas, onde dados são movidos de processo a
# processo pelos buffers de memória do kernel e AF_INET que representa a
# comunicação usando o protocolo TCP/IP, onde processos podem estar na mesma máquina
# ou em máquinas diferentes.
# O tipo de um socket indica como os dados são transferidos pelo socket. Existem
# basicamente duas opções:
#   * Datagram: que suporta um modelo baseado em mensagem, onde nenhuma conexão
#       está envolvida, e comunição não tem garantia de ser confiável.
#   * Stream: que suportam um modelo de circuito virtual, onde dados são trocados
#       como um fluxo de bytes e a conexão é confiável.
# Dependendo do domínio, outros tipos de sockets podem estar disponíveis, como
# aqueles que suportam a passagem de mensagem em um conexão confiável.
# ---------------------------------------------------
# Implementando a aplicação cliente
# A aplicação cliente é, essencialmente, um programa muito simples que cria um link
# à aplicação servidor. Para fazer isso, cria um objeto socket que conecta à
# máquina hóspede do servidor, e, em nosso caso, à porta 8084.
# Após a conexão ser feita, o cliente pode enviar a mensagem codificada para o
# servidor. O servidor, então, enviará de volta uma resposta que o cliente deve
# decodificar. Então fecha a conexão.
# A implementação é dada abaixo:
# import socket

# def main():
#     print('Iniciando cliente')
#     print('Cria um socket TCP/IP')
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print('Conecta o socket à porta do servidor')
#     server_address = (socket.gethostname(), 8084)
#     print('Conectando com:', server_address)
#     sock.connect(server_address)
#     print('Conectado com o servidor')
#     try:
#         print('Envia dados')
#         message = 'John'
#         print('Enviando:', message)
#         sock.send(message.encode())
#         data = sock.recv(1024).decode()
#         print('Recebido do servidor:', data)
#     finally:
#         print('Fechando o socket')
#         sock.close()

# if __name__ == '__main__';
#     main()

# O servidor espera por uma conexão do cliente. Quando o cliente conexta-se ao
# servidor, o servidor espera receber dados do cliente. Neste ponto, o cliente
# deve esperar que o servidor envie os dados. Então, o servidor prepara a
# resposta e a envia para o cliente. O cliente recebe isso, exibe e fecha a conexão.
# Então o servidor espera se há mais dados do cliente; quando o cliente fecha
# a conexão, o servidor volta a esperar pela próxima conexão.
# -------------------------------------------
# O módulo SocketServer
# No exemplo acima, o código do servidor é mais complexo que o do cliente; e isto
# é para um servidor de uma única thread. Se o servidor precisar usar múltiplas
# threads(isto é, o servidor precisa lidar com múltiplas requisições de clientes
# ao mesmo tempo), isso torna-se muito mais complexo.
# Entretanto, o módulo socketserver fornece uma abordagem mais conveniente, orientada
# a objetos, para a criação do servidor. Muito do código básico necessário para tal
# aplicação é denifido em classes, com o desenvolvedor tendo que se preocupar apenas
# em fornecer suas próprias classes ou sobrescrever métodos para definir funcionalidades
# específicas necessárias.
# Existem 5 classes de servidor diferentes no módulo socketserver:
#   * BaseServer: A raiz da hierarquia de classe do Servidor; não é ideada para
#       instanciação e usada diretamente. Em vez disso, é estendida por TCPServer
#       e outras classes.
#   * TCPServer: usa sockets TCP/IP para comunicar e é, provavelmente, o tipo mais
#       comumente usado de servidor socket.
#   * UDPServer: fornece acesso a sockets datagrama.
#   * UnixStreamServer e UnixDatagramServer: usam sockets de domínio Unix e estão
#       disponíveis apenas em plataformas Unix.
# A responsabilidade pelo processamento de uma requisição é dividida entre uma
# classe servidor e uma classe manipuladora de requisições. O servidor lida com
# questões de comunicação (escutar em um socket e porta, aceitar comunicações etc)
# enquando o manipulador de requisições lida com questões de requisições (interpretar
# dados que chegam, processá-los, enviar de volta ao cliente).
# Esta divisão de responsabilidade significa que, em muitos casos, você pode
# simplesmente usar uma das classes servidor existentes sem quaisquer modificações
# e fornecer um manipulador de requisições customizado para trabalhar com ela.
# O seguinte exemplo define um manipulador de requisições que está conextado ao TCPServer
# quando é construído. O manipulador de requisições define um método handle()
# que é esperado manipular o processamento da requisição.


# import socketserver


# class MyTCPHandler(socketserver.BaseRequestHandler):
#     """
#     Classe Manipuladora de Requisições para o servidor.
#     """

#     def __init__(self, request, client_address, server):
#         print("Prepara nomes e escritórios")
#         self.addresses = {
#             "JOHN": "C45",
#             "DENISE": "C44",
#             "PHOEBE": "D52",
#             "ADAM": "B23",
#         }
#         super().__init__(request, client_address, server)

#     def handle(self):
#         print("Em Handle")
#         data = self.request.recv(1024).decode()
#         print("dados recebidos:", data)
#         key = str(data).upper()
#         response = self.addresses[key]
#         print("response:", response)
#         self.request.sendall(response.encode())


# def main():
#     print("Iniciando o servidor")
#     server_address = ("localhost", 8084)
#     print("Criando o servidor")
#     server = socketserver.TCPServer(server_address, MyTCPHandler)
#     print("Ativando o servidor")
#     server.serve_forever()


# if __name__ == "__main__":
#     main()

# Perceba que o aplicativo cliente anterior não precisa alterar em nada; as alterações
# no servidor são escondidas do cliente.
# Entretanto, isto ainda é um servidor de Thread única. Podemos simplesmente torná-lo
# um servidor de múltiplas threads misturando socketserver.ThreadingMixIn no TCPServer.
# Isto pode ser feito definindo uma nova classe que nada mais é que uma classe
# que estende ambas ThreadingMixIn e TCPServer e cria uma instância desta nova classe
# em vez da TCPServer diretamente. Por exemplo:


# class ThreadedEchoServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
#     pass
# def main():
#     print('Iniciando')
#     address = ('localhost', 8084)
#     server = ThreadedEchoServer(address, MyTCPHandler)
#     print('Ativando o servidor')
#     server.serve_forever()


# De fato, não é necessário nem mesmo criar sua própria classe pois a classe
# socketserver.ThreadingTCPServer foi fornecida como mistura padrão entre
# TCPServer e ThreadingMixIn. Poderíamos apenas escrever:


# def main():
#     print('Iniciando')
#     address = ('localhost', 8084)
#     server = socketserver.ThreadingTCPServer(address, MyTCPHandler)
#     server.serve_forever()

# ------------------------------------------
# Servidor HTTP
# Além do servidor TCP, também existe um http.server.HTTPServer; ele pode ser
# usado de modo similar ao TCServer, mas é usado para criar servidores que
# respondem ao protocolo HTTP usado por muitos navegadores web. Em outras
# palavras, pode ser usado para criar um Servidor Web muito simples (mas deve-se
# notar que é apenas apropriado para criar servidores web de teste pois apenas
# implementa checagens de segurança muito básicas).
# O diagrama webserver.png ilustra as interações básicas entre um servidor web e
# um navegador web. Nele, o usuário está usando um navegador (como Chrome) para
# acessar um servidor web. O navegador está executando na máquina local dele. Para
# acessar o servidor web, eles entram um endereço URL(Universal Resource Locator)
# em seu navegador. No exemplo, é www.foo.com. Também indica que querem conectar com
# a porta 8080 (em vez da padrão 80 de conexões HTTP). A máquina remota (indicada
# pelo endereço www.foo.com) recebe esse pedido e determina o que fazer com ele.
# Se não há nenhum programa monitorando a porta 8080, rejeitará o pedido. Em nosso
# caso, temos um programa Python (que é o programa de servidor web) escutando
# naquela porta, que recebe o pedido. Então resolverá o pedido e gerará uma mensagem
# de resposta que será enviada de volta para o navegador da máquina local do usuário.
# A resposta indicará qual versão do protocolo HTTP suporta, se tudo ocorreu corretamente
# ou não (o código 200 do diagrama acima). O navegador na máquina local então
# renderiza os dados como uma página web ou manipula os dados como apropriado etc.
# Para criar um servidor web simples em Python o http.server.HTTPServer pode ser
# usado diretamente ou pode ser subclasseado junto com socketserver.ThreadingMixIn
# para criar um servidor de mútliplas threads, por exemplo:
# class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
#    """ Servidor HTTP simples de múltiplas threads"""
#    pass

# Desde Python 3.7, o módulo http.server agora fornece exatamente esta classe como
# um recurso embutido e assim não é mais necessário definí-la você mesmo.
# Para lidar com pedidos HTTP, você precisa implementar um dos métodos de requisição
# HTTP como do_GET(), ou do_POST(). Cada um deste mapeia a um tipo de requisição
# HTTP, por exeplo:
#   *do_GET() mapeia para uma requisição HTTP Get que é gerada se digitar um
#       endereço web na barra URL do navegador web
#   *do_POST() mapeia para uma requisição HTTP Post que é usada, por exemplo,
#       quando um formulário em uma página web é usado para submeter dados ao
#       servidor web.
# Os métodos do_GET(self) ou do_POST(self) devem, então, lidar com qualquer
# entrada fornecida com a requisição e gerar respostas apropriadas de volta para
# o navegador. Isto significa que deve sergui o protocolo HTTP.
# O seguinte programa simples cria um servidor web simples que gerará uma mensagem
# de boas vindas e a hora atual como resposta a um pedido GET. Faz isso usando
# o módulo datetime para criar uma estampa temporal da data e hora usando a
# função today(). Isto é convertido para uma matriz de bytes usando a codificação
# de caracteres UTF-8. Precisamos de uma matriz de bytes pois ela é que será
# executada pelo método write() posteriormente.
# Feito isso, existem vários items de metadados que precisam ser preparados
# para que o navegador saiba quais dados irá receber. Estes metadados são conhecidos
# como dados de cabeçalho(header) e podem incluir o tipo de conteúdo sendo enviado
# e a quantidade de dados(conteúdo) sendo transmitido. No nosso caso simples, precisamos
# dizer que estamos enviando texto limpo(plain text)(em vez de HTML usado para
# descrever uma página web típica) pela informação de cabeçalho 'Content-type'.
# Também precisamos deizer quandos dados estamos enviando usando o comprimento do
# conteúdo. Podemos, então, indicar que terminamos de definir o cabeçalho e começamos
# o envio dos dados. Os dados são enviados pelo atributo wfile herdado de
# BaseHTTPRequestHandler. Existem, na verdade, dois atributos relacionados rfile
# e wfile:
#   * rfile é um fluxo de entrada que permite a leitura dos dados de entrada.
#   * wfile armazena o fluxo de saída que pode ser usado para escrever(enviar)
#       dados para o navegador. Este objeto fornece um método write() que pega
#       um objeto do tipo byte que é escrito para (eventualmente) o navegador.
# O método main() é usado para preparar o servidor HTTP que segue o padrão usado
# para o TCPServer; entretanto, o cliente deste servidor será um navegador web.
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from datetime import datetime


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    """Manipulador de requisições muito simples. Permite apenas GET."""

    def do_GET(self):
        print("do_GET() iniciando a processar o pedido")
        welcome_msg = "Olá do servidor em " + str(datetime.today())
        byte_msg = bytes(welcome_msg, "utf-8")
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset-utf-8")
        self.send_header("Content-length", str(len(byte_msg)))
        self.end_headers()
        print("do_GET() respondendo com mensagem")
        self.wfile.write(byte_msg)


def main():
    print("Preparando o servidor")
    server_address = ("localhost", 8080)
    httpd = ThreadingHTTPServer(server_address, MyHTTPRequestHandler)
    print("Ativando servidor HTTP")
    httpd.serve_forever()


if __name__ == "__main__":
    main()

# Após o servidor estar executando, pode-se conectar a ele usando um navegador
# e entrando o endereço web apropriado no campo URL do navegador. Isto significa que
# no seu navegador (se estiver executando na mesma máquina do servidor) apenas
# precisa digitas http://localhost:8080 (isto indica que quer usar o protocolo http
# para conectar com a máquina local na porta 8080).

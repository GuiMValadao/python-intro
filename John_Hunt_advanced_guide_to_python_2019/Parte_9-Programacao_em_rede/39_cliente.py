import socket


def main():
    print("Iniciando cliente")
    print("Cria um socket TCP/IP")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Conecta o socket à porta do servidor")
    server_address = (socket.gethostname(), 8084)
    print("Conectando com:", server_address)
    sock.connect(server_address)
    print("Conectado com o servidor")
    try:
        print("Envia dados")
        message = "John"
        print("Enviando:", message)
        sock.send(message.encode())
        data = sock.recv(1024).decode()
        print("Recebido do servidor:", data)
    finally:
        print("Fechando o socket")
        sock.close()


if __name__ == "__main__":
    main()

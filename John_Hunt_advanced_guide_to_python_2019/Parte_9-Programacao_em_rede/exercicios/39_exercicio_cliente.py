import socket


def main():
    print("Iniciando cliente")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (socket.gethostname(), 8084)
    sock.connect(server_address)
    while True:
        message = input("Digite a informação que procura(data, hora ou dataehora): ")
        print("Conectado com o servidor")
        try:
            print("Enviando:", message)
            sock.send(message.encode())
            data = sock.recv(1024).decode()
            print("Recebido do servidor:", data)
        finally:
            if data == "-1":
                print("Fechando o socket")
                sock.close()
                break


if __name__ == "__main__":
    main()

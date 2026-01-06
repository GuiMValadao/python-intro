import socket


def main():
    addresses = {"JOHN": "C45", "DENISE": "C44", "PHOEBE": "D52", "ADAM": "B23"}
    print("Iniciando o servidor")
    print("Criando um soket")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Liga o socket à porta")
    server_address = (socket.gethostname(), 8084)
    print("Iniciando em", server_address)
    sock.bind(server_address)

    print("Esperando pela chegada de conexões")
    sock.listen(1)
    while True:
        print("Esperando por uma conexão")
        connection, client_address = sock.accept()
        try:
            print("Connection de", client_address)
            while True:
                data = connection.recv(1024).decode()
                print("Recebido:", data)
                if data:
                    key = str(data).upper()
                    response = addresses[key]
                    print("Enviando dados de volta para o cliente:", response)
                    connection.sendall(response.encode())
                else:
                    print("Sem mais dados de", client_address)
                    break
        finally:
            connection.close()


if __name__ == "__main__":
    main()

import socket
from datetime import datetime


def main():
    opcoes = {
        "DATA": datetime.now().strftime("%d/%m/%Y"),
        "HORA": datetime.now().strftime("%H:%M:%S"),
        "DATAEHORA": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    }
    print("Iniciando o servidor")
    print("Criando um soket")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Liga o socket à porta")
    server_address = (socket.gethostname(), 8084)
    print("Iniciando em", server_address)
    sock.bind(server_address)
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
                    try:
                        response = str(opcoes[key])
                        print("Enviando dados de volta para o cliente:", response)
                    except KeyError:
                        if key == "-1":
                            response = "-1"
                        else:
                            response = "UNKNOWN OPTION"

                    finally:
                        print("Enviando dados de volta para o cliente:", response)
                        connection.sendall(response.encode())
                        if key == "-1":
                            print("Encerrando a conexão e saindo do programa")
                            break
                else:
                    print("Sem mais dados de", client_address)
                    break
        finally:
            connection.close()
            exit()


if __name__ == "__main__":
    main()

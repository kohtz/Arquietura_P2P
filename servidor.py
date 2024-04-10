import socket
import threading

def handle_client(client_socket, friend_name):
    while True:
        try:
            # Recebe a mensagem do cliente
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"{friend_name}: {message}")
            else:
                # Conexão foi fechada
                break
        except:
            break

def main():
    host = '10.50.111.52'
    port = 3000
    my_name = "Esther"
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print(f"Escutando em {host}:{port}")

    client_sock, addr = server.accept()
    print(f"Aceito conexão de: {addr}")

    # Envia o nome para o cliente e recebe o nome do cliente
    client_sock.send(my_name.encode('utf-8'))
    friend_name = client_sock.recv(1024).decode('utf-8')
    print(f"Você está conectado com {friend_name}.")

    client_handler = threading.Thread(target=handle_client, args=(client_sock, friend_name,))
    client_handler.start()

    while True:
        message = input("")
        if message.lower() == 'sair':
            break
        client_sock.send(message.encode('utf-8'))

    client_sock.close()

if __name__ == "__main__":
    main()

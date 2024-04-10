import socket
import threading

def receive_message(sock, friend_name):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message:
                print(f"{friend_name}: {message}")
            else:
                # Conexão foi fechada
                break
        except:
            break

def main():
    host = input("Digite o endereço IP do servidor: ")
    port = 3000

    my_name = input("Digite seu nome: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    # Envia o nome para o servidor e recebe o nome do servidor
    client.send(my_name.encode('utf-8'))
    friend_name = client.recv(1024).decode('utf-8')
    print(f"Você está conectado com {friend_name}.")

    thread = threading.Thread(target=receive_message, args=(client, friend_name,))
    thread.start()

    while True:
        message = input("")
        if message.lower() == 'sair':
            break
        client.send(message.encode('utf-8'))

    client.close()

if __name__ == "__main__":
    main()

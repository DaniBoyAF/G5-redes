import socket

HOST = "127.0.0.1"
PORT = 5000

# Cria socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Envia handshake
modo = "Canal sem erros"
tamanho = 50
handshake = f"MODO:{modo};TAMANHO:{tamanho}"
client_socket.sendall(handshake.encode())
print("Handshake enviado:", handshake)

# Recebe confirmação
resposta = client_socket.recv(1024).decode()
print("Resposta do servidor:", resposta)

# Inicia troca de mensagens
while True:
    msg = input("Digite uma mensagem (ou 'sair' para encerrar): ")
    client_socket.sendall(msg.encode())
    if msg.lower() == "sair":
        break

    resposta = client_socket.recv(1024).decode()
    print("Servidor respondeu:", resposta)

client_socket.close()

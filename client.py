import socket

HOST = "127.0.0.1"
PORT = 5000

# cria socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# prepara handshake (modo + tamanho máximo)
modo_operacao = "Go-Back-N"
tamanho_maximo = 50
handshake = f"MODO:{modo_operacao};TAMANHO:{tamanho_maximo}"

# envia handshake
client_socket.sendall(handshake.encode())
print("Handshake enviado:", handshake)

# recebe resposta do servidor
resposta = client_socket.recv(1024).decode()
print("Resposta do servidor:", resposta)

client_socket.close()

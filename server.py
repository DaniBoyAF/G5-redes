import socket

HOST = "127.0.0.1"  # IP local
PORT = 5000         # Porta de conexão

# Cria o socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Servidor escutando em {HOST}:{PORT}...")

# Aceita a conexão do cliente
conn, addr = server_socket.accept()
print(f"Conexão estabelecida com {addr}")

# Recebe a primeira mensagem (handshake)
handshake = conn.recv(1024).decode()
print("Handshake recebido:", handshake)

# Responde ao handshake
conn.sendall("Handshake OK - Canal sem erros estabelecido".encode())

# Troca de mensagens confiável
while True:
    mensagem = conn.recv(1024).decode()
    if mensagem.lower() == "sair":
        print("Cliente encerrou a conexão.")
        break

    print(f"Mensagem recebida: {mensagem}")
    resposta = f"Servidor recebeu com sucesso: {mensagem}"
    conn.sendall(resposta.encode())

conn.close()
server_socket.close()

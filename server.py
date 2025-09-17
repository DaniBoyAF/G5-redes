import socket

HOST = "127.0.0.1"  # localhost
PORT = 5000         # porta do servidor

# cria socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Servidor escutando em {HOST}:{PORT}...")

conn, addr = server_socket.accept()
print(f"Conexão estabelecida com {addr}")

# recebe handshake
handshake = conn.recv(1024).decode()
print("Handshake recebido:", handshake)

# responde com confirmação
conn.sendall("Handshake OK - servidor pronto".encode())

conn.close()
server_socket.close()

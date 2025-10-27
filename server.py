import socket
from cryptography.fernet import Fernet

HOST = "127.0.0.1"
PORT = 5000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

conn, addr = server_socket.accept()
print("Conectado:", addr)

# Recebe a chave do cliente
chave = conn.recv(1024)
cipher = Fernet(chave)
print("Chave recebida.")

while True:
    data = conn.recv(1024)
    if not data:
        break

    msg = cipher.decrypt(data).decode()
    print(f"Mensagem descriptografada: {msg}")

    resposta = cipher.encrypt(f"Recebido: {msg}".encode())
    conn.sendall(resposta)

conn.close()
server_socket.close()

import socket
from cryptography.fernet import Fernet

# Gera ou usa uma chave fixa (as duas partes devem ter a mesma)
chave = Fernet.generate_key()
cipher = Fernet(chave)

HOST = "127.0.0.1"
PORT = 5000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Envia chave para o servidor
client_socket.sendall(chave)
print("Chave enviada para o servidor.")

while True:
    msg = input("Mensagem (ou sair): ")
    if msg.lower() == "sair":
        break

    criptografada = cipher.encrypt(msg.encode())
    client_socket.sendall(criptografada)

    resposta = client_socket.recv(1024)
    print("Servidor respondeu:", cipher.decrypt(resposta).decode())

client_socket.close()

import socket
from seguranca import criptografar, gerar_hash

# ========================
# CONFIGURAÇÃO DO CLIENTE
# ========================
HOST = 'localhost'
PORT = 5000

# Cria o socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("✅ Conectado ao servidor!")

# Recebe a chave do servidor
chave = client_socket.recv(4096)
print(f"🗝️ Chave recebida: {chave.decode()}")

# Envia mensagem
mensagem = input("Digite a mensagem para o servidor: ")

# Criptografa e gera hash
mensagem_criptografada = criptografar(mensagem, chave)
hash_msg = gerar_hash(mensagem)

# Envia ao servidor
client_socket.send(mensagem_criptografada)
client_socket.send(hash_msg.encode())

# Recebe resposta
resposta = client_socket.recv(4096).decode()
print(f"📨 Resposta do servidor: {resposta}")

client_socket.close()

import socket
from seguranca import gerar_chave, descriptografar, verificar_integridade

# ========================
# CONFIGURAÇÃO DO SERVIDOR
# ========================
HOST = 'localhost'
PORT = 5000

# Cria o socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"🔒 Servidor aguardando conexão em {HOST}:{PORT}...")

# Gera uma chave simétrica
chave = gerar_chave()
print(f"🗝️ Chave gerada (enviar ao cliente): {chave.decode()}")

# Aguarda conexão
conn, addr = server_socket.accept()
print(f"✅ Conectado com {addr}")

# Envia a chave para o cliente
conn.send(chave)

# Recebe mensagem criptografada
mensagem_criptografada = conn.recv(4096)
hash_recebido = conn.recv(4096).decode()

# Descriptografa
mensagem = descriptografar(mensagem_criptografada, chave)

# Verifica integridade
if verificar_integridade(mensagem, hash_recebido):
    print(f"📩 Mensagem recebida com sucesso: {mensagem}")
else:
    print("⚠️ ERRO: Mensagem corrompida ou alterada!")

# Envia confirmação
conn.send("Mensagem recebida com segurança!".encode())

conn.close()
server_socket.close()

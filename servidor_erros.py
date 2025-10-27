import socket
import random
import time

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Servidor escutando em {HOST}:{PORT}...")

conn, addr = server_socket.accept()
print(f"Conexão estabelecida com {addr}")

# Handshake
handshake = conn.recv(1024).decode()
print("Handshake recebido:", handshake)
conn.sendall("Handshake OK - Canal com erros simulados".encode())

# Loop de mensagens
while True:
    try:
        mensagem = conn.recv(1024).decode()
        if not mensagem:
            break

        if mensagem.lower() == "sair":
            print("Cliente encerrou a conexão.")
            break

        print(f"Mensagem recebida: {mensagem}")

        # Simula chance de erro (10%) e perda (10%)
        chance_erro = random.random()
        if chance_erro < 0.1:
            print("❌ Simulando erro: resposta corrompida")
            resposta = "ERRO_CORROMPIDO"
        elif chance_erro < 0.2:
            print("💨 Simulando perda: não responder")
            continue
        else:
            resposta = f"Servidor OK - Mensagem recebida: {mensagem}"

        # Aguarda um pequeno atraso (simula latência)
        time.sleep(random.uniform(0.2, 1.0))
        conn.sendall(resposta.encode())

    except ConnectionResetError:
        print("Conexão encerrada abruptamente.")
        break

conn.close()
server_socket.close()

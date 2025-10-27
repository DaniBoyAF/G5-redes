import socket
import time

HOST = "127.0.0.1"
PORT = 5000
TIMEOUT = 2  # tempo máximo de espera pela resposta (segundos)
MAX_TENTATIVAS = 3  # número máximo de retransmissões

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(TIMEOUT)
client_socket.connect((HOST, PORT))

# Handshake
modo = "Canal com erros"
tamanho = 50
handshake = f"MODO:{modo};TAMANHO:{tamanho}"
client_socket.sendall(handshake.encode())
print("Handshake enviado:", handshake)

try:
    resposta = client_socket.recv(1024).decode()
    print("Resposta do servidor:", resposta)
except socket.timeout:
    print("⏰ Timeout no handshake")

# Envio de mensagens com verificação
while True:
    msg = input("Digite uma mensagem (ou 'sair' para encerrar): ")
    if msg.lower() == "sair":
        client_socket.sendall(msg.encode())
        break

    tentativa = 1
    sucesso = False

    while tentativa <= MAX_TENTATIVAS and not sucesso:
        client_socket.sendall(msg.encode())
        print(f"Mensagem enviada (tentativa {tentativa})...")

        try:
            resposta = client_socket.recv(1024).decode()

            if resposta == "ERRO_CORROMPIDO":
                print("⚠️ Resposta corrompida! Reenviando mensagem...")
            else:
                print("Servidor respondeu:", resposta)
                sucesso = True

        except socket.timeout:
            print("⏰ Timeout - nenhuma resposta recebida. Reenviando...")

        tentativa += 1

    if not sucesso:
        print("❌ Falha após várias tentativas. Mensagem perdida.")

client_socket.close()

# Projeto Redes

Este projeto demonstra uma simples comunicação cliente-servidor usando **sockets TCP** em Python, implementando um **handshake inicial**.

## Arquivos

### server.py

* Cria um socket TCP e escuta na porta 5000.
* Aceita conexão de um cliente.
* Recebe handshake do cliente.
* Envia confirmação de recebimento.
* Fecha a conexão.

### client.py

* Cria um socket TCP e conecta ao servidor na porta 5000.
* Prepara handshake com modo de operação e tamanho máximo.
* Envia handshake ao servidor.
* Recebe confirmação do servidor.
* Fecha a conexão.

## Como usar

1. Execute o servidor:

```bash
python server.py
```

2. Execute o cliente em outro terminal:

```bash
python client.py
```

3. Observe a comunicação entre cliente e servidor.

## Observações

* Usa localhost (`127.0.0.1`) e porta 5000.
* Pode-se alterar `modo_operacao` e `tamanho_maximo` no cliente.
* Base para implementar protocolos mais complexos ou transferência confiável de dados.

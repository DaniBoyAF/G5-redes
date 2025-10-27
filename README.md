# Projeto Redes

Este projeto demonstra uma simples comunicação cliente-servidor usando **sockets TCP** em Python, implementando um **handshake inicial**.

## Arquivos

### server.py

* Cria um socket TCP e escuta na porta 5000.
* Aceita conexão de um cliente.
* Recebe handshake do cliente.
* Envia confirmação de recebimento.
* Implementa troca de mensagens confiável em loop contínuo.
* Processa mensagens do cliente e envia confirmações.
* Encerra conexão quando cliente envia "sair".
* Fecha a conexão e o socket do servidor.

### client.py

* Cria um socket TCP e conecta ao servidor na porta 5000.
* Prepara handshake com modo de operação e tamanho máximo.
* Envia handshake ao servidor.
* Recebe confirmação do servidor.
* Implementa interface interativa para envio de mensagens.
* Permite ao usuário digitar mensagens via input.
* Encerra conexão quando usuário digita "sair".
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

3. Após o handshake inicial, digite mensagens no cliente para enviar ao servidor.
4. O servidor responderá com confirmação de recebimento para cada mensagem.
5. Digite "sair" no cliente para encerrar a conexão.
6. Observe a comunicação entre cliente e servidor.

## Observações

* Usa localhost (`127.0.0.1`) e porta 5000.
* Pode-se alterar `modo_operacao` e `tamanho_maximo` no cliente.
* Implementa comunicação bidirecional com confirmação de recebimento.
* Interface interativa permite múltiplas mensagens até o encerramento.
* Sistema de encerramento controlado com comando "sair".
* Base para implementar protocolos mais complexos ou transferência confiável de dados.

## Integrantes

* João Pedro Patriota
* Mateus Dornelas
* Jarbas Esteves
* Daniel Andrade
* Thiago Brayner
* Luis Antônio Godoy

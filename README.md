# Projeto Redes

Este projeto demonstra uma comunicação cliente-servidor usando sockets TCP em Python, implementando um handshake inicial e troca de mensagens entre cliente e servidor, considerando um canal de comunicação onde erros e perdas não ocorrem. Contendo criptografia e checagem de integridade na comunicação.


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

### servidor_erros.py e cliente_erros.py

* Versões aprimoradas do cliente e servidor com criptografia e checagem de integridade.
* Utilizam a biblioteca cryptography para garantir segurança na comunicação.
* Implementam mecanismos de validação de dados recebidos para detectar e evitar corrupção de mensagens.
* Mantêm a lógica de handshake e troca de mensagens confiável entre as partes.

## Como usar

1. Instalar dependências, antes de executar as versões seguras, instale a biblioteca de criptografia:

```bash
pip install cryptography
```

---

2. Execute o servidor:

```bash
python server.py
```

* Para a versão com segurança e checagem de integridade:

```bash
python servidor_erros.py
```

---

3. Execute o cliente em outro terminal:

```bash
python client.py
```

* Para a versão com segurança e checagem de integridade:

```bash
python cliente_erros.py
```

---

4. Interagir com o sistema

* Após o handshake inicial, digite mensagens no cliente para enviar ao servidor.
* O servidor responderá com confirmação de recebimento para cada mensagem.
* Digite "sair" no cliente para encerrar a conexão.
* Observe a comunicação e a verificação de integridade na versão segura.

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

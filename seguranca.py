import hashlib
from cryptography.fernet import Fernet


# ========================
# GERAR CHAVE SIMÉTRICA
# ========================
def gerar_chave():
    """Gera uma nova chave simétrica Fernet."""
    return Fernet.generate_key()


# ========================
# CRIPTOGRAFAR MENSAGEM
# ========================
def criptografar(mensagem: str, chave: bytes) -> bytes:
    """Criptografa uma mensagem usando a chave."""
    f = Fernet(chave)
    return f.encrypt(mensagem.encode())


# ========================
# DESCRIPTOGRAFAR MENSAGEM
# ========================
def descriptografar(mensagem_criptografada: bytes, chave: bytes) -> str:
    """Descriptografa a mensagem."""
    f = Fernet(chave)
    return f.decrypt(mensagem_criptografada).decode()


# ========================
# CHECAR INTEGRIDADE
# ========================
def gerar_hash(mensagem: str) -> str:
    """Gera o hash SHA-256 da mensagem."""
    return hashlib.sha256(mensagem.encode()).hexdigest()


def verificar_integridade(mensagem: str, hash_recebido: str) -> bool:
    """Verifica se o hash da mensagem confere com o recebido."""
    return gerar_hash(mensagem) == hash_recebido

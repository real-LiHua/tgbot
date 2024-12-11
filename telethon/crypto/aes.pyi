from . import libssl as libssl
from _typeshed import Incomplete

__log__: Incomplete

class AES:
    @staticmethod
    def decrypt_ige(cipher_text, key, iv): ...
    @staticmethod
    def encrypt_ige(plain_text, key, iv): ...

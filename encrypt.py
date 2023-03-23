from abc import ABC, abstractmethod


class Cipher(ABC):
    ABC_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    ABC_ENG = 'abcdefghijklmnopqrstuvwxyz'
    OTHER_SYMBOL = '.,<>?!()'

    def __init__(self, text: str = None, key=None):
        self.text = text
        self.key = key

    @abstractmethod
    def encrypt(self, text: str=None, key=None) -> str:
        pass

    @abstractmethod
    def decrypt(self, text: str=None, key=None) -> str:
        pass


class Caesar(Cipher):
    def __init__(self, text: str = None, key=None):
        super().__init__()

    def encrypt(self, text: str=None, key=None) -> str:
        pass

    def decrypt(self, text: str=None, key=None) -> str:
        pass


class Replace(Cipher):
    def __init__(self, text: str = None, key=None):
        super().__init__()

    def encrypt(self, text: str=None, key=None) -> str:
        pass

    def decrypt(self, text: str=None, key=None) -> str:
        pass


class Vigenere(Cipher):
    def __init__(self, text: str = None, key=None):
        super().__init__()

    def encrypt(self, text: str=None, key=None) -> str:
        pass

    def decrypt(self, text: str=None, key=None) -> str:
        pass


class Becon(Cipher):
    def __init__(self, text: str = None, key=None):
        super().__init__()

    def encrypt(self, text: str=None, key=None) -> str:
        pass

    def decrypt(self, text: str=None, key=None) -> str:
        pass


class Atbash(Cipher):
    def __init__(self, text: str = None, key=None):
        super().__init__()

    def encrypt(self, text: str=None, key=None) -> str:
        pass

    def decrypt(self, text: str=None, key=None) -> str:
        pass
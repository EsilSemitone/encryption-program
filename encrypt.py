from abc import ABC, abstractmethod


class Cipher(ABC):
    ABC_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    ABC_ENG = 'abcdefghijklmnopqrstuvwxyz'
    OTHER_SYMBOL = '.,<>?!()'

    def __init__(self, text: str = None, key=None):
        self.text = text
        self.key = key

    @staticmethod
    @abstractmethod
    def encrypt(text: str, key) -> str:
        pass

    @staticmethod
    @abstractmethod
    def decrypt(text: str, key) -> str:
        pass


class Caesar(Cipher):
    def __init__(self, text: str = None, key=None):
        super().__init__()
        self.text = text
        self.key = key

    @staticmethod
    def encrypt(text: str, key=4) -> str:
        new_message = ''
        new_abc = Caesar.ABC_RUS
        if text.isalpha():

        elif text.isdigit():
            ...
        else:
            return ''

        pass

    @staticmethod
    def decrypt(text: str, key=None) -> str:
        pass


class Replace(Cipher):
    def __init__(self, text: str = None, key=None):
        super().__init__()
        self.text = text
        self.key = key

    @staticmethod
    def encrypt(text: str, key=None) -> str:
        pass

    @staticmethod
    def decrypt(text: str, key=None) -> str:
        pass


class Vigenere(Cipher):
    def __init__(self, text: str = None, key=None):
        super().__init__()
        self.text = text
        self.key = key

    @staticmethod
    def encrypt(text: str, key=None) -> str:
        pass

    @staticmethod
    def decrypt(text: str, key=None) -> str:
        pass


class Becon(Cipher):
    def __init__(self, text: str = None, key=None):
        super().__init__()
        self.text = text
        self.key = key

    @staticmethod
    def encrypt(text: str, key=None) -> str:
        pass

    @staticmethod
    def decrypt(text: str, key=None) -> str:
        pass


class Atbash(Cipher):
    def __init__(self, text: str = None, key=None):
        super().__init__()
        self.text = text
        self.key = key

    @staticmethod
    def encrypt(text: str, key=None) -> str:
        pass

    @staticmethod
    def decrypt(text: str, key=None) -> str:
        pass

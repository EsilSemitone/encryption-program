from tkinter import Label


class Cipher:
    ABC_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    ABC_ENG = 'abcdefghijklmnopqrstuvwxyz'
    OTHER_SYMBOL = '.,<>?!()'

    def __init__(self, text: str = None, key=None):
        self.text = text
        self.key = key

    def encrypt(self, text: str=None, key=None) -> str:
        pass

    def decrypt(self, text: str=None, key=None) -> str:
        pass

    def caesar(self, input_text=None, key=4) -> str:
        pass

    def replace_enc(self, input_text=None, key=3241) -> str:
        pass

    def vigenere(self, input_text=None, key='Привет') -> str:
        pass

    def becon(self, input_text=None, key=None):
        pass
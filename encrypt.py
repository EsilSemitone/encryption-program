from tkinter import Label


class Encrypt:
    ABC_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    ABC_ENG = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, text: str = None):
        self.text = text

    def caesar(self, input_text=None, key=4) -> str:
        pass

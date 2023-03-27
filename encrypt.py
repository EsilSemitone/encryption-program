from abc import ABC, abstractmethod


class Cipher(ABC):
    _ABC = {
        'Rus': 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
        'Eng': 'abcdefghijklmnopqrstuvwxyz'
    }

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
        text = text.replace('\n', '')
        print('\n' in text)
        if text.isalpha():
            language = 'Rus' if text[0] in Caesar._ABC['Rus'] else 'Eng'

            if key.isalpha():

                if 1 > len(key) > Caesar._ABC[language]:
                    raise KeyError(
                        f'Внимание! Ключевое слово должно '
                        f'быть длинее 1 символа но короче {len(Caesar._ABC[language])}!')

                pos = len(key) * 2 if (len(key) * 2) < len(Caesar._ABC[language]) else len(key)
                
                new_abc = Caesar.generate()
                
                return new_abc
            elif key.isdigit():
                pass
            raise KeyError('Ключ содержит недопустимые символы или имеет одновременно цифры и буквы')
        raise ValueError('Внимание! Не верно введен текст. Шифруемое сообщение не может быть пустым'
                         ' Текст должен быть на одном языке.'
                         ' Без цифр и других знаков')

    
    def generate(self, abc, count_start, count_end) -> str:
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

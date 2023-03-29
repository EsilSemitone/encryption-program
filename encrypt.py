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
        '''encrypting message'''

        new_message = ''
        text = text.replace('\n', '')
        assert not ('\n' in text), "в тексте перевод строки"
        if text.isalpha():
            language = 'Rus' if text[0] in Caesar._ABC['Rus'] else 'Eng'
            lenght = len(Caesar._ABC[language])

            if key.isalpha():
                key = Caesar.delete_duplicates(key)
                print(f'key = {key}')

                if 2 > len(set(key)) > len(Caesar._ABC[language]):
                    raise KeyError(
                        f'Внимание! Ключевое слово должно '
                        f'быть длинее 1 символа но короче {len(Caesar._ABC[language])}!')
                else:
                    index_pos = (len(set(key)) * 2 if (len(set(key))) * 2 < lenght else len(set(key))) - 1
                    print(f'index pos = {index_pos}')

                new_abc = Caesar.generate_abc(
                    Caesar._ABC[language],
                    index_pos + 1,
                    lenght - (index_pos + len(set(key)) + 1), key)
                assert len(new_abc) == len(Caesar._ABC[language]),\
                    f'alphabet eror lenght {len(new_abc)} != {len(Caesar._ABC[language])}'

                return new_abc
            elif key.isdigit():
                pass

            raise KeyError('Ключ содержит недопустимые символы или имеет одновременно цифры и буквы')

        raise ValueError('Внимание! Не верно введен текст. Шифруемое сообщение не может быть пустым'
                         ' Текст должен быть на одном языке.'
                         ' Без цифр и других знаков')

    @staticmethod
    def generate_abc(abc: str, count_start: int, count_end: int, key) -> str:
        '''generate alphabet on key-word'''
        # key = ''.join([i for i in set(key)])
        # print(key)
        res = key
        for i in key:
            abc = abc.replace(i, '')
        abc = iter(abc)

        for i in range(count_end):
            res += next(abc)
        for i in range(count_start):
            res = next(abc) + res

        # res = res + abc[count_end:]
        # res = abc[0:count_start] + res
        assert len(res) == len(set(res)), f'duplecate error in generate {len(res)} != {len(set(res))}'
        return res

    @staticmethod
    def generate_int():
        '''generate alphabet on numerical key'''
        pass

    @staticmethod
    def delete_duplicates(string: str) -> str:
        """function for delete duplicates on key"""
        duplicates = []
        new_str = ''
        for i in string:
            if string.count(i) > 1:
                if not(i in duplicates):
                    duplicates.append(i)
                    new_str += i
            else:
                new_str += i
        return new_str

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

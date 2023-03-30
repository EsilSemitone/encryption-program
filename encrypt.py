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

    @staticmethod
    def delete_in_text(text: str, *args, low=False, other=None) -> str:

        for i in args:
            text = text.replace(f'{i}', '')
        if other:
            for i in other:
                text = text.replace(f'{i}', '')
        if low:
            text = text.lower()

        return text


class Caesar(Cipher):
    def __init__(self, text: str = None, key=None):
        super().__init__()
        self.text = text
        self.key = key

    @staticmethod
    def encrypt(text: str, key=4) -> str:
        '''encrypting message'''

        new_message = ''
        text = Caesar.delete_in_text(text, '\n', ' ', other=Caesar.OTHER_SYMBOL, low=True)

        try:
            key = Caesar.delete_in_text(key, ' ', low=True)
            print(key)
        except TypeError:
            pass

        assert not ('\n' in text), "в тексте перевод строки"

        if not text.isalpha():
            raise ValueError('Внимание! Не верно введен текст. Шифруемое сообщение не может быть пустым'
                             ' Текст должен быть на одном языке.'
                             ' Без цифр и других знаков')

        language = 'Rus' if text[0] in Caesar._ABC['Rus'] else 'Eng'
        length = len(Caesar._ABC[language])

        if key.isalpha():

            key = Caesar.delete_duplicates(key)
            print(f'key = {key}')

            if len(key) > len(Caesar._ABC[language]):
                raise KeyError(
                    f'Внимание! Ключевое слово должно '
                    f'быть длинее 0 символов, но короче {len(Caesar._ABC[language])}!')

            len_key = len(key)

            pos = len_key if (length - len_key * 2) > 0 else len_key // 2

            count_end = length - (pos + len(key))

            #print(f'index pos = {pos}')
            #print(f'len key {len(key)}')

            new_abc = Caesar.generate_abc(
                Caesar._ABC[language],
                count_end,
                key)

            assert len(new_abc) == len(Caesar._ABC[language]), \
                f'alphabet error length my -> {len(new_abc)} !=  normal ->{len(Caesar._ABC[language])}'

            for i in text:
                new_message += new_abc[Caesar._ABC[language].index(i)]
            print(f'old abs -> {Caesar._ABC[language]}')
            print(f'new abs -> {new_abc}')
            return new_message

        elif key.isdigit():
            pass

        raise KeyError('Ключ содержит недопустимые символы или имеет одновременно цифры и буквы')

    @staticmethod
    def decrypt(text: str, key=None) -> str:
        """По началу я хотел избежать повторений ниже, но подумав понял что
                        код станет сильно непонятным"""
        new_message = ''
        text = Caesar.delete_in_text(text, '\n', low=True)

        if not text.isalpha():
            raise ValueError('Внимание! Не верно введен текст. Разшифровываемое сообщение не может быть пустым'
                             ' Текст должен быть на одном языке.'
                             ' Без цифр и других знаков')

        language = 'Rus' if text[0] in Caesar._ABC['Rus'] else 'Eng'
        length = len(Caesar._ABC[language])

        if key.isalpha():
            key = Caesar.delete_duplicates(key)
            if len(key) > len(Caesar._ABC[language]):
                raise KeyError(
                    f'Внимание! Ключевое слово должно '
                    f'быть длинее 0 символов, но короче {len(Caesar._ABC[language])}!')

            len_key = len(key)
            pos = len_key if (length - len_key * 2) > 0 else len_key // 2
            count_end = length - (pos + len(key))

            new_abc = Caesar.generate_abc(
                Caesar._ABC[language],
                count_end,
                key)

            assert len(new_abc) == len(Caesar._ABC[language]), \
                f'alphabet error length my -> {len(new_abc)} !=  normal ->{len(Caesar._ABC[language])}'

            for i in text:
                new_message += Caesar._ABC[language][new_abc.index(i)]
            return new_message

    @staticmethod
    def generate_abc(abc: str, count_end: int, key) -> str:
        """generate alphabet on key-word"""

        res = key
        abc = ''.join([i for i in abc if not (i in key)])

        res = res + abc[0:count_end + 1] if count_end > 0 else res
        print(f'В конце {abc[0:count_end + 1]} {count_end} символов')
        res = abc[count_end + 1:] + res if count_end > 0 else abc + res
        print(f"В начале {abc[count_end + 1:]} {len(abc[count_end + 1:])} символов")
        assert len(res) == len(set(res)), f'duplicate error in generate {len(res)} != {len(set(res))}'
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
                if not (i in duplicates):
                    duplicates.append(i)
                    new_str += i
            else:
                new_str += i
        return new_str



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

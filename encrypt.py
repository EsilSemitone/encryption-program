from abc import ABC, abstractmethod
import re

from tools import delete_in_text, delete_duplicates, split_text


class Cipher(ABC):
    ABC_ = {
        'Rus': 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
        'Eng': 'abcdefghijklmnopqrstuvwxyz'
    }

    OTHER_SYMBOL = ('.', ',', '<', '>', '?', '!', '(', ')', ' ', '\n')

    def __init__(self, modl: str, text: str = None, key=None):
        self.modl = modl

        self.text = text
        self.text = delete_in_text(self.text, low=True, other=Cipher.OTHER_SYMBOL)
        if not self.text.isalpha():
            raise ValueError('Внимание! Не верно введен текст. Cообщение не может быть пустым'
                             ' Текст должен быть на одном языке.'
                             ' Без цифр и других знаков')
        if re.search(r'[A-Za-z]+[А-Яа-я]+', self.text):
            raise ValueError('Текст должен быть на одном языке.')
        elif re.search(r'\d+', text):
            raise ValueError('К сожаления программа не может зашифровывать текст с цифрами.')
        elif re.search(r"[A-Za-z]+", text):
            self.language = Cipher.ABC_['Eng']
        elif re.search(r"[А-Яа-я]+", text):
            self.language = Cipher.ABC_['Rus']

        assert not ('\n' in self.text), "в тексте перевод строки"

        self.key = key
        self.new_message = ''

    @abstractmethod
    def main_func(self) -> str:
        pass

    def __str__(self):
        return self.new_message


class Caesar(Cipher):
    def __init__(self, modl: str, text: str = None, key: str | int = 4):
        super().__init__(modl, text, key)

        self.pos = None

        if self.key == '':
            self.key = '4'

        else:

            if re.search(r"\W+", self.key):
                self.key = delete_in_text(self.key, low=True, other=Caesar.OTHER_SYMBOL)
                if re.search(r'\w+\d+', self.key):
                    raise KeyError('Внимание! Ключ не может содержать одновременно цифры и буквы!')
                if re.search(r'\W+', self.key):
                    raise KeyError("Внимание! Ключ не может содержать что-либо кроме букв или цифр!")

        self.new_message = self.main_func()

    def main_func(self) -> str:
        '''Шифруем/Расшифровываем'''

        new_message = ''

        if self.key.isalpha():

            if re.search(r'[A-Za-z]+[А-Яа-я]+', self.key):
                raise ValueError('Текст ключа должен быть на одном языке.')

            self.key = delete_duplicates(self.key)
            print(f'key = {self.key}')

            if len(self.key) > len(self.language):
                raise KeyError(
                    f'Внимание! Ключевое слово должно '
                    f'быть длинее 0 символов, но короче {len(self.language)}!')

            self.pos = len(self.key) if (len(self.language) - len(self.key) * 2) > 0 else len(self.key) // 2

            self.count_end = len(self.language) - (self.pos + len(self.key))

            self.new_abc = Caesar.generate_abc(
                self.language,
                self.count_end,
                self.key)

            assert len(self.new_abc) == len(self.language), \
                f'alphabet error length my -> {len(self.new_abc)} !=  normal ->{len(self.language)}'

            if self.modl == 'encrypt':

                for i in self.text:
                    new_message += self.new_abc[self.language.index(i)]
                print(f'old abs -> {self.language}')
                print(f'new abs -> {self.new_abc}')
                return new_message
            else:
                for i in self.text:
                    new_message += self.language[self.new_abc.index(i)]
                print(f'new abs -> {self.new_abc}')
                print(f'old abs -> {self.language}')
                return new_message

        elif self.key.isdigit():

            self.key = int(self.key)

            if self.modl == 'encrypt':
                for i in self.text:
                    index = (self.language.index(i) + self.key) % len(self.language)
                    new_message += self.language[index]
                return new_message
            else:
                for i in self.text:
                    index = (self.language.index(i) - self.key) % len(self.language)
                    new_message += self.language[index]
                return new_message

    @staticmethod
    def generate_abc(abc: str, count_end: int, key) -> str:
        """Создаем алфавить для шифровки"""

        res = key
        abc = ''.join([i for i in abc if not (i in key)])

        if count_end > 0:
            res = res + abc[0:count_end + 1]
            print(f'В конце {abc[0:count_end + 1]} {count_end} символов')
            res = abc[count_end + 1:] + res
            print(f"В начале {abc[count_end + 1:]} {len(abc[count_end + 1:])} символов")
        else:
            res = abc + res
        assert len(res) == len(set(res)), f'duplicate error in generate {len(res)} != {len(set(res))}'
        return res


class Replace(Cipher):
    def __init__(self, modl: str, text: str = None, key=None):
        super().__init__(modl, text, key)

        self.digit = False

        if re.search(r"\D+", self.key):
            raise ValueError('Ключ должен быть только из цифр!')
        elif re.search(r'\d+', self.key):
            self.key = delete_in_text(self.key, low=False, other=Cipher.OTHER_SYMBOL)
            if self.key.isdigit():
                if len(self.key) > 20:
                    raise ValueError('Слишком длинный ключ!')
                elif len(self.key) == 1:
                    raise ValueError('Слишком короткий ключ!')
                else:
                    self.digit = True
            else:
                raise ValueError('Ключ должен быть только из цифр!')

        self.new_message = self.main_func()

        if self.digit:
            self.key = self.key.split(',')

    def main_func(self) -> str:
        '''Шифруем/Расшифровываем'''

        new_message = ''
        if self.modl == 'encrypt':

            if self.digit:
                self.text_gen = split_text(self.text, len(self.key))
                print(self.key)

            else:

                self.text_gen = split_text(self.text)
                print(f'Разбитый текст -> {self.text_gen}')
                max_len = 3
                new_message = ''.join([i[index] for index in range(max_len) for i in self.text_gen if len(i) > index])
                print(new_message)
                return new_message

        else:
            if self.digit:
                self.text_gen = split_text(self.text, len(self.key))
                pass

            else:
                max_len = len(self.text) // 3
                if len(self.text) % 3 > 0:
                    max_len += 1
                self.text_gen = split_text(self.text, length=max_len)
                print(f'Разбитый текст -> {self.text_gen}')
                new_message = ''.join([i[index] for index in range(max_len) for i in self.text_gen if len(i) > index])
                print(new_message)
                return new_message


class Vigenere(Cipher):
    def __init__(self, text: str = None, key=None):
        super().__init__(text, key)

    def main_func(self) -> str:
        '''Шифруем/Расшифровываем'''

        new_message = ''


class Becon(Cipher):
    def __init__(self, text: str = None, key=None):
        super().__init__(text, key)

    def main_func(self) -> str:
        '''Шифруем/Расшифровываем'''

        new_message = ''


class Atbash(Cipher):
    def __init__(self, text: str = None, key=None):
        super().__init__(text, key)

    def main_func(self) -> str:
        '''Шифруем/Расшифровываем'''

        new_message = ''

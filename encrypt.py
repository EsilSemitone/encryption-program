from abc import ABC, abstractmethod
from random import choice
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
        self.key = key
        self.text = text
        self.text = delete_in_text(self.text, low=True, sumbols=Cipher.OTHER_SYMBOL)
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
                self.key = delete_in_text(self.key, low=True, sumbols=Caesar.OTHER_SYMBOL)
                if re.search(r'\w+\d+', self.key):
                    raise KeyError('Внимание! Ключ не может содержать одновременно цифры и буквы!')
                elif re.search(r'\W+', self.key):
                    raise KeyError("Внимание! Ключ не может содержать что-либо кроме букв или цифр!")

        self.new_message = self.main_func()

    def main_func(self) -> str:
        '''Шифруем/Расшифруем'''

        new_message = ''

        if self.key.isalpha():

            if re.search(r'[A-Za-z]+[А-Яа-я]+', self.key):
                raise ValueError('Текст ключа должен быть на одном языке.')

            self.key = delete_duplicates(self.key)

            if len(self.key) > len(self.language):
                raise KeyError(
                    f'Внимание! Ключевое слово должно '
                    f'быть длинее 0 символов, но короче {len(self.language)}!')

            self.pos = len(self.key) if (len(self.language) - len(self.key) * 2) > 0 else len(self.key) // 2

            #Определяю сколько символов остается после ключа в алфавите
            self.count_end = len(self.language) - (self.pos + len(self.key))

            #Геренрация нового алфавита
            self.new_abc = Caesar.generate_abc(self.language, self.count_end, self.key)

            assert len(self.new_abc) == len(self.language), \
                f'alphabet error length my -> {len(self.new_abc)} !=  normal ->{len(self.language)}'

            if self.modl == 'encrypt':

                for i in self.text:
                    new_message += self.new_abc[self.language.index(i)]
                #print(f' old abs -> {self.language}')
                #print(f' new abs -> {self.new_abc}')

            else:

                for i in self.text:
                    new_message += self.language[self.new_abc.index(i)]
                #print(f'new abs -> {self.new_abc}')
                #print(f'old abs -> {self.language}')

            return new_message

        elif self.key.isdigit():

            self.key = int(self.key)

            if self.modl == 'encrypt':
                for i in self.text:
                    index = (self.language.index(i) + self.key) % len(self.language)
                    new_message += self.language[index]

            else:
                for i in self.text:
                    index = (self.language.index(i) - self.key) % len(self.language)
                    new_message += self.language[index]

            return new_message

    @staticmethod
    def generate_abc(abc: str, count_end: int, key) -> str:
        """Создаем алфавить для шифровки"""

        new_alphabet = key
        abc = ''.join([i for i in abc if not (i in key)])

        if count_end > 0:
            new_alphabet = new_alphabet + abc[0:count_end + 1]
            #print(f'В конце {abc[0:count_end + 1]} {count_end} символов')
            new_alphabet = abc[count_end + 1:] + new_alphabet
            #print(f"В начале {abc[count_end + 1:]} {len(abc[count_end + 1:])} символов")
            res = new_alphabet
        else:
            res = abc + new_alphabet

            assert len(res) == len(set(res)), f'duplicate error in generate {len(res)} != {len(set(res))}'

        return res


class Replace(Cipher):
    def __init__(self, modl: str, text: str = None, key=None):
        super().__init__(modl, text, key)

        #Переменная-макркер, если ключ валидный набор цифр -> True
        self.digit = False

        #Проверка ключа на валидность
        if re.search(r"\D+", self.key):
            raise ValueError('Ключ должен быть только из цифр!')
        elif re.search(r'\d+', self.key):
            self.key = delete_in_text(self.key, low=False, sumbols=Cipher.OTHER_SYMBOL)
            if self.key.isdigit():
                max_number = max(map(int, self.key))
                if set(map(int, self.key)) != set(range(1, max_number + 1)):
                    raise ValueError('В ключе пропущены цифры')
                elif len(self.key) > len(self.text) // 2 or len(self.key) > 9:
                    raise ValueError('Слишком длинный ключ!')
                elif len(self.key) == 1:
                    raise ValueError('Слишком короткий ключ!')
                elif len(self.key) != len(set(self.key)):
                    raise ValueError('Некорректно введен ключ!')
                else:
                    self.digit = True
            else:
                raise ValueError('Ключ должен быть только из цифр!')

        self.new_message = self.main_func()

    def main_func(self) -> str:
        '''Шифруем/Расшифруем'''

        new_message = ''
        if self.modl == 'encrypt':

            if self.digit:
                #Разбиваем текст на матрицу где длина стоки равняется длине ключа
                self.text_split = split_text(self.text, len(self.key))
                #print(self.key)

                #С каждой строки берется символ по ключу
                new_message = ''.join([
                    i[int(index) - 1] for index in self.key
                    for i in self.text_split if len(i) > int(index) - 1
                ])

                return new_message

            else:
                # Разбиваем текст на матрицу где длина стоки равняется трем
                self.text_split = split_text(self.text)
                #print(f'Разбитый текст -> {self.text_split}')

                average_len = 3

                # С каждой строки берется символ по нарастающей
                new_message = ''.join([
                    i[index] for index in range(average_len)
                    for i in self.text_split if len(i) > index
                ])

                return new_message

        else:
            if self.digit:
                #Узнаю среднюю длину столбца в матрице
                average_len = len(self.text) // len(self.key)

                #Сколько столбцов с длиной выше среднего
                full_count = len(self.text) % len(self.key)

                self.text_split = []

                #отмечаю шаг
                step = 0

                for i in self.key:

                    #здесь я определяю будет ключ максимальной длины или средней
                    if int(i) > full_count:
                        #Средней т.к порядковый номер столбца не попадает в диапазон с максимальным кол-вом
                        self.text_split.append(self.text[step:step + average_len])
                        step += average_len
                    else:
                        #обратная ситуация
                        self.text_split.append((self.text[step: step + average_len + 1]))
                        step += average_len + 1

                #Это нужно чтобы ниже плясать от максимально возможной длины
                if len(self.text) % len(self.key):
                    average_len += 1

                #Сортирую блоки чтобы похже легче было вытаскивать по индексам
                new_message = sorted(zip(self.key, self.text_split))
                #print(new_message)

                self.text_split = [i[1] for i in new_message]

                new_message = ''.join([
                    i[index] for index in range(average_len)
                    for i in self.text_split if len(i) > index
                ])
                return new_message

            else:
                # Если ключ не введен
                average_len = len(self.text) // 3

                # Сколько столбцов с длиной выше среднего
                full_count = len(self.text) % 3
                step = 0
                self.text_split = []

                for i in range(3):
                    if full_count:
                        full_count -= 1
                        self.text_split.append(self.text[step:step + average_len + 1])
                        step += average_len + 1
                    else:
                        self.text_split.append(self.text[step:step + average_len])
                        step += average_len

                if len(self.text) % 3:
                    average_len += 1

                #print(f'Разбитый текст -> {self.text_split}')
                new_message = ''.join([
                    i[index] for index in range(average_len)
                    for i in self.text_split if len(i) > index
                ])
                #print(new_message)
                return new_message


class Vigenere(Cipher):
    def __init__(self, modl: str, text: str = None, key=None):
        super().__init__(modl, text, key)

        #Проверка на ключ
        if self.key == '':
            raise KeyError('Не введен ключ')
        elif re.search(r'/d+', self.key) or any([i in self.key for i in Cipher.OTHER_SYMBOL]):
            raise KeyError('Ключ не может содержать цифры или или другие знаки')
        elif len(self.key) > len(self.language):
            raise KeyError('Ключ не может быть длинее текста')
        elif len(self.key) < 2:
            raise KeyError('Слишком короткий ключ')

        self.language_key = ''

        if re.search(r'[A-Za-z]+', self.key):
            self.language_key = Cipher.ABC_['Eng']
        elif re.search(r'[А-Яа-я]', self.key):
            self.language_key = Cipher.ABC_['Rus']

        if self.language_key != self.language:
            raise KeyError('Язык ключа не совпадает с текстом')

        self.new_message = self.main_func()


    def main_func(self) -> str:
        '''Шифруем/Расшифуем'''

        new_message = ''
        self.key = self.key_gen(self.key)

        if self.modl == 'encrypt':

            for i in self.text:
                new_index = self.language_key.index(i) + self.language.index(next(self.key))
                new_message += self.language[new_index % len(self.language)]
                print('new message ' + new_message)

        else:
            for i in self.text:
                new_index = self.language_key.index(i) - self.language.index(next(self.key))
                new_message += self.language[new_index % len(self.language)]
                print(new_message)

        return new_message


    @staticmethod
    def key_gen(key):

        while True:
            yield from key


class Becon(Cipher):
    def __init__(self, modl: str, text: str = None, key=None):
        super().__init__(modl, text, key)

        self.even_letters = [i for i in self.language if self.language.index(i) % 2 == 0]
        self.not_even_letters = [i for i in self.language if self.language.index(i) % 2 > 0]

        self.new_alphabet = self.bin_list(self.language)
        self.new_alphabet_keys = self.bin_list_key(self.language)

        self.new_message = self.main_func()


    def main_func(self) -> str:
        '''Шифруем/Расшифруем'''

        new_message = ''
        intermediate_message = ''

        if self.modl == 'encrypt':
            for i in self.text:
                intermediate_message += self.new_alphabet[i]

            for i in intermediate_message:
                if i == "0":
                    new_message += choice(self.even_letters)
                else:
                    new_message += choice(self.not_even_letters)


        else:

            for i in self.text:
                if i in self.even_letters:
                    intermediate_message += '0'
                else:
                    intermediate_message += '1'

            intermediate_message = split_text(intermediate_message, 6)

            for letter in intermediate_message:
                new_message += self.new_alphabet_keys[letter]

        return new_message

    def bin_list(self, abc: str) -> dict:
        '''Function for make Becon's alphabet'''
        res = {}
        for i in abc:
            number = format(abc.index(i), 'b')
            if len(number) < 6:
                number = '0' * (6 - len(number)) + number
            res[i] = number
        return res

    def bin_list_key(self, abc: str) -> dict:
        '''Function for make Becon's alphabet'''
        res = {}
        for i in abc:
            number = format(abc.index(i), 'b')
            if len(number) < 6:
                number = '0' * (6 - len(number)) + number
            res[number] = i
        return res


class Atbash(Cipher):
    def __init__(self, modl: str, text: str = None, key=None):
        super().__init__(modl, text, key)

        self.alphabet = self.language[::-1]

        self.new_message = self.main_func()

    def main_func(self) -> str:
        '''Шифруем/Расшифруем'''

        new_message = ''

        if self.modl == 'encrypt':
            for i in self.text:
                new_message += self.alphabet[self.language.index(i)]

        else:
            for i in self.text:
                new_message += self.language[self.alphabet.index(i)]

        return new_message

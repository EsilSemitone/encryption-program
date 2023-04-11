from tkinter import Frame, WORD, SW, Button, \
    Tk, Text, END, Menu, PhotoImage, Scrollbar, \
    StringVar, Entry, messagebox
from tkinter.ttk import Label, Radiobutton

from encrypt import Caesar, Replace, Vigenere, Becon, Atbash


class MainWindow:
    HEIGHT = 500
    WIDTH = 1000
    root = Tk()
    POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
    POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
    root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')
    icon = PhotoImage(file='images//icon.png')
    root.iconphoto(False, icon)
    root.resizable(False, False)

    def __init__(self, title: str = 'Шифровщик'):
        self.root.title(title)

        self.app = MainWindowFrame(self.root)

        self.main_menu = Menu(self.root, tearoff=0)
        self.root.config(menu=self.main_menu)

        self.file_menu = Menu(self.main_menu, tearoff=0)
        self.file_menu.add_command(label='Зашифровать файл')
        self.file_menu.add_command(label='Расшифровать файл')
        self.main_menu.add_cascade(label='Работа с файлами', menu=self.file_menu)
        self.main_menu.add_cascade(label='Продвинутое шифрование')

        self.app.mainloop()

    def update_window(self) -> None:
        ''''Пока что не помню зачем ее создал'''
        self.app = MainWindowFrame(self.root)


class MainWindowFrame(Frame):
    ENCRYPT_LAB_INFO = {
        'Шифр Цезаря': 'Это шифр в котором каждый символ\n'
                       'заменяется символом, находящимся\n'
                       'на некотором постоянном числе\n'
                       'позиций левее или правее него\n'
                       'в алфавите. Ключем может служить\n'
                       'число (в таком случае сдвиг\n'
                       'будет равен этому числу),\n'
                       'или слово\фразу.\n'
                       'Сдвиг без ключа равен 4',

        'Перестановка': 'Это метод симметричного\n'
                        'шифрования в котором элементы\n'
                        'исходного открытого текста\n'
                        'меняют местами\n'
                        'Ключом может служить набор цифр\n'
                        'длинее 2 \n'
                        'По умолчанию будет использоваться \n'
                        'Табличная маршрутная перестановка.',

        'Шифр Виженера': 'Шифр Виженера состоит из\n'
                         'последовательности нескольких\n '
                         'шифров Цезаря с различными\n '
                         'значениями сдвига. Ключем\n'
                         'служит фраза или набор букв\n'
                         'По умолчанию "Привет"',

        'Шифр Бэкона': 'Шифр базируется на двоичном\n'
                       'кодировании алфавита. Затем\n'
                       'секретное послание «прячется»\n'
                       'в открытом тексте',

        'Атбаш': 'Простой шифр подстановки\n'
                 'для алфавитного письма. Впервые\n'
                 'встречается в древнееврейском\n'
                 'тексте Библии / Танаха.\n'
                 'Ключ не требуется'

    }

    def __init__(self, root=None):
        super().__init__(root)
        self.pack()

        Label(text='Поле для ввода').pack(anchor=SW, padx=5, pady=5)
        self.try_text = Text(height=13, width=70, wrap=WORD)
        self.try_text.pack(anchor=SW, fill=None)
        self.scroll_try = Scrollbar(width=23, command=self.try_text.yview)
        self.try_text["yscrollcommand"] = self.scroll_try.set
        self.scroll_try.place(x=542, y=31, height=211)

        Label(text='Поле вывода').pack(anchor=SW, padx=5, pady=5)
        self.output_text = Text(height=13, width=70, wrap=WORD)
        self.output_text.pack(anchor=SW, fill=None)
        self.scroll_out = Scrollbar(width=23, command=self.try_text.yview)
        self.output_text["yscrollcommand"] = self.scroll_out.set
        self.scroll_out.place(x=542, y=272, height=211)

        self.textMenu = Menu(tearoff=False)
        self.textMenu.add_command(label='Очистить', command=self.clear)
        self.textMenu.add_command(label='Скопировать', command=self.copy)
        self.textMenu.add_command(label='Вставить', command=self.paste)

        self.try_text.bind('<Button-3>', lambda place, text='try': self.set_menu_pos(text, place))
        self.output_text.bind('<Button-3>', lambda place, text='out': self.set_menu_pos(text, place))

        self.encrypt_button = Button(text='Шифровать', width=38, font='arial 15', command=self.encrypt)
        self.encrypt_button.place(x=568, y=30)
        self.decrypt_button = Button(text='Расшифровать', width=38, font='arial 15', command=self.decrypt)
        self.decrypt_button.place(x=568, y=70)

        self.choice_encrypt_var = StringVar(value='Шифр Цезаря')

        self.caesar_but = Radiobutton(
            text='Шифр Цезаря',
            value='Шифр Цезаря',
            variable=self.choice_encrypt_var,
            command=self.addition_to_radiobutton
        )
        self.caesar_but.place(x=586, y=150)

        self.replace_but = Radiobutton(
            text='Перестановка',
            value='Перестановка',
            variable=self.choice_encrypt_var,
            command=self.addition_to_radiobutton
        )
        self.replace_but.place(x=586, y=180)

        self.vigenere_but = Radiobutton(
            text='Шифр Виженера',
            value='Шифр Виженера',
            variable=self.choice_encrypt_var,
            command=self.addition_to_radiobutton
        )
        self.vigenere_but.place(x=586, y=210)

        self.becon_but = Radiobutton(
            text='Шифр Бэкона',
            value='Шифр Бэкона',
            variable=self.choice_encrypt_var,
            command=self.addition_to_radiobutton
        )
        self.becon_but.place(x=586, y=240)

        self.atbash_but = Radiobutton(
            text='Атбаш',
            value='Атбаш',
            variable=self.choice_encrypt_var,
            command=self.addition_to_radiobutton
        )
        self.atbash_but.place(x=586, y=270)

        self.info_lab = Label(text=self.ENCRYPT_LAB_INFO['Шифр Цезаря'])
        self.info_lab.place(x=730, y=150)

        Label(text='Ключ', font='arial 13').place(x=760, y=320)
        self.key_input = Entry(width=50)
        self.key_input.place(x=580, y=350, height=25)

        self.ENCRYPT_LIST = {
            'Шифр Цезаря': Caesar,
            'Перестановка': Replace,
            'Шифр Виженера': Vigenere,
            'Шифр Бэкона': Becon,
            'Атбаш': Atbash
        }

    class PlaceMenu:
        '''Хранит в себе информацию по какому окну я вызвал меню'''
        place: str = ''

        @classmethod
        @property
        def get_place(cls):
            return cls.place

    def addition_to_radiobutton(self) -> None:
        """Функция вызываемая при активации radiobuton"""
        self.info_lab.destroy()
        self.info_lab = Label(text=self.ENCRYPT_LAB_INFO[self.choice_encrypt_var.get()])
        self.info_lab.place(x=730, y=150)

    def encrypt(self):
        '''Шифруем'''
        self.output_text.delete(0.0, END)

        try:
            print('Изначальный текст')
            print(self.try_text.get(0.0, END))
            self.new_text = self.ENCRYPT_LIST[self.choice_encrypt_var.get()]('encrypt',
                                                                             self.try_text.get(0.0, END),
                                                                             self.key_input.get()
                                                                             )
            self.output_text.insert(0.0, self.new_text)
        except ValueError as er:
            messagebox.showerror('Внимание!', str(er))
            print(er)
        except KeyError as er:
            messagebox.showerror('Внимание!', str(er))

    def decrypt(self):
        '''Раcшифровываем'''

        self.output_text.delete(0.0, END)

        try:
            self.new_text = self.ENCRYPT_LIST[self.choice_encrypt_var.get()]('decrypt', self.try_text.get(0.0, END),
                                                                             self.key_input.get()
                                                                             )
            self.output_text.insert(0.0, self.new_text)
        except ValueError as er:
            messagebox.showerror('Внимание!', str(er))
            print(er)
        except KeyError as er:
            messagebox.showerror('Внимание!', str(er))

    def paste(self) -> None:
        '''Вставка в поле текста из буфера обмена'''

        match self.PlaceMenu.get_place:
            case 'try':
                self.try_text.insert(END, self.clipboard_get())
            case 'out':
                self.output_text.insert(END, self.clipboard_get())

    def clear(self) -> None:
        '''Очистка окна с текстом'''

        match self.PlaceMenu.get_place:
            case 'try':
                self.try_text.delete(0.0, END)
            case 'out':
                self.output_text.delete(0.0, END)

    def copy(self) -> None:
        '''Копирование в буфер обмена содержимого окна'''

        self.clipboard_clear()
        match self.PlaceMenu.get_place:
            case 'try':
                self.clipboard_append(self.try_text.get(0.0, END))
            case 'out':
                self.clipboard_append(self.output_text.get(0.0, END))

    def set_menu_pos(self, where: str, event) -> None:
        '''Вызов меню по координатам клика мыши'''
        self.PlaceMenu.place = where
        self.textMenu.post(event.x_root, event.y_root)

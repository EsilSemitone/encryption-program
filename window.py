from tkinter import Frame, WORD, SW, Button, Tk, Text, END, Menu, PhotoImage, Scrollbar, StringVar
from tkinter.ttk import Label, Radiobutton

from encrypt import Encrypt


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
        self.main_menu.add_cascade(label='Работа с файлами', menu=self.file_menu)

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
                        'или фраза\n'
                        'Ключ по умолчанию 3241',

        'Шифр Виженера': 'Шифр Виженера состоит из\n'
                         'последовательности нескольких\n '
                         'шифров Цезаря с различными\n '
                         'значениями сдвига. Ключем\n'
                         'служит фраза или набор букв\n'
                         'По умолчанию "Привет"',

        'Шифр Бэкона': 'Шифр базируется на двоичном\n'
                        'кодировании алфавита. Затем\n'
                        'секретное послание «прячется»\n'
                        'в открытом тексте'

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

        self.try_text.bind('<Button-3>', lambda e, text='try': self.set_menu_pos(text, e))
        self.output_text.bind('<Button-3>', lambda e, text='out': self.set_menu_pos(text, e))

        self.encrypt_button = Button(text='Шифровать', width=38, font='arial 15', command=self.encrypt)
        self.encrypt_button.place(x=568, y=30)
        self.decrypt_button = Button(text='Расшифровать', width=38, font='arial 15', command=self.decrypt)
        self.decrypt_button.place(x=568, y=70)

        self.choice_encrypt_var = StringVar(value='Шифр Цезаря')

        self.caesar_but = Radiobutton(
            text='Шифр Цезаря',
            value='Шифр Цезаря',
            variable=self.choice_encrypt_var,
            command=lambda lab='Шифр Цезаря': self.addition_to_radiobutton(lab)
        )
        self.caesar_but.place(x=586, y=150)

        self.replace_but = Radiobutton(
            text='Перестановка',
            value='Перестановка',
            variable=self.choice_encrypt_var,
            command=lambda lab='Шифр Цезаря': self.addition_to_radiobutton(lab)
        )
        self.replace_but.place(x=586, y=180)

        self.vigenere_but = Radiobutton(
            text='Шифр Виженера',
            value='Шифр Виженера',
            variable=self.choice_encrypt_var,
            command=lambda lab='Шифр Виженера': self.addition_to_radiobutton(lab)
        )
        self.vigenere_but.place(x=586, y=210)

        self.becon_but = Radiobutton(
            text='Шифр Бэкона',
            value='Шифр Бэкона',
            variable=self.choice_encrypt_var,
            command=lambda lab='Шифр Бэкона': self.addition_to_radiobutton(lab)
        )
        self.becon_but.place(x=586, y=240)

        self.info_lab = Label(text=self.ENCRYPT_LAB_INFO['Шифр Цезаря'])
        self.info_lab.place(x=730, y=150)

    class PlaceMenu:
        '''Хранит в себе информацию по какому окне я вызвал меню'''
        place: str = ''

        @classmethod
        @property
        def get_place(cls):
            return cls.place

    def addition_to_radiobutton(self, lab) -> None:
        self.info_lab.destroy()
        self.info_lab = Label(text=self.ENCRYPT_LAB_INFO[self.choice_encrypt_var.get()])
        self.info_lab.place(x=730, y=150)

    def encrypt(self):
        '''Шифруем'''

        ...

    def decrypt(self):
        '''Раcшифровываем'''
        ...

    def paste(self, place=PlaceMenu.place) -> None:
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

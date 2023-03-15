from tkinter import Frame, WORD, SW, Button, Tk, Text, END, Menu, PhotoImage, Scrollbar, StringVar
from tkinter import ttk


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
        self.app.mainloop()

    def update_window(self) -> None:
        ''''Пока что не помню зачем ее создал'''
        self.app = MainWindowFrame(self.root)


class MainWindowFrame(Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.pack()

        ttk.Label(text='Поле для ввода').pack(anchor=SW, padx=5, pady=5)
        self.try_text = Text(height=13, width=70, wrap=WORD)
        self.try_text.pack(anchor=SW, fill=None)
        self.scroll_try = Scrollbar(width=23, command=self.try_text.yview)
        self.try_text["yscrollcommand"] = self.scroll_try.set
        self.scroll_try.place(x=542, y=31, height=211)

        ttk.Label(text='Поле вывода').pack(anchor=SW, padx=5, pady=5)
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

        ttk.Label(text='Ключ').place(x=810, y=120)

        self.choice_encrypt = StringVar(value='Шифр Цезаря')

        self.caesar_but = ttk.Radiobutton(text='Шифр Цезаря', value='Шифр Цезаря', variable=self.choice_encrypt)
        self.caesar_but.place(x=586, y=150)

        self.replace_but = ttk.Radiobutton(text='Перестановка', value='Перестановка', variable=self.choice_encrypt)
        self.replace_but.place(x=586, y=180)

    class PlaceMenu:
        '''Хранит в себе информацию по какому окну я вызвал меню'''
        place: str = ''

        @classmethod
        @property
        def get_place(cls):
            return cls.place

    def encrypt(self):
        '''Шифруем'''
        ...

    def decrypt(self):
        '''Разшифровываем'''
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







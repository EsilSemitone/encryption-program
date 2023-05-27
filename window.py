from tkinter import Frame, WORD, SW, Button, \
    Tk, Text, END, Menu, PhotoImage, Scrollbar, \
    StringVar, Entry, messagebox
from tkinter.ttk import Label, Radiobutton
from tkinter import filedialog as fd

from encrypt import Caesar, Replace, Vigenere, Becon, Atbash
from encrypt_file import Crypt


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
        self.file_menu.add_command(label='Encrypt file', command=lambda x='encrypt': self.make_encrypt(x))
        self.file_menu.add_command(label='Decrypt file', command=lambda x='dencrypt': self.make_encrypt(x))
        self.main_menu.add_cascade(label='Working with files', menu=self.file_menu)

        self.app.mainloop()


    def make_encrypt(self, command):

        file = fd.askopenfilename()
        if file is None:
            messagebox.showerror('Attention!', 'file is not selected!')
        else:
            file = Crypt(file)

            if command == 'encrypt':
                messagebox.showinfo('Attention!', f"Do you really want to encrypt this file {file.path}?")
                file.encrypt_file()
                messagebox.showinfo('Attention!', 'Done!')
            else:
                messagebox.showinfo('Attention!', f"Do you really want to decrypt this file {file.path}?")
                file.decrypt_file()
                messagebox.showinfo('Attention!', 'Done!')

    def update_window(self) -> None:
        ''''I dont remember why i making this function'''
        self.app = MainWindowFrame(self.root)


class MainWindowFrame(Frame):
    ENCRYPT_LAB_INFO = {
        'Caesar cipher': 'This is a cipher in which each character\n'
                       'replaced by symbol, moving\n'
                       'always on\n'
                       'positions left or right of it\n'
                       'in the alphabet. The key can serve\n'
                       'number (in this case the increment\n'
                       'will be equal to this equality),\n'
                       'or word\phrase.\n'
                       'Shift without key is 4',

        'Replace': 'This is a method of symmetrical\n'
                        'encryption in which elements\n'
                        'original plaintext\n'
                        'swap\n'
                        'The key can be a set of numbers\n'
                        'longer than 2 \n'
                        'Default will be \n'
                        'Table route permutation.',

        'Vigenere cipher': 'The Vigenère cipher consists of\n'
                         'sequences of several\n '
                         'Caesar ciphers with various\n '
                         'shift values. Key\n'
                         'serves as a phrase or set of letters\n'
                         'Default "Hello"',

        'Becon cipher': 'Cipher based on binary\n'
                       'coding of the alphabet. Then\n'
                       'secret message <<hidden>>\n'
                       'in plaintext',

        'Atbash': 'Simple substitution cipher\n'
                 'for alphabetical writing. First time\n'
                 'occurs in Hebrew\n'
                 'text of the Bible / Tanakh.\n'
                 'Key not required'

    }

    def __init__(self, root=None):
        super().__init__(root)
        self.pack()

        Label(text='Input field').pack(anchor=SW, padx=5, pady=5)
        self.try_text = Text(height=13, width=70, wrap=WORD)
        self.try_text.pack(anchor=SW, fill=None)
        self.scroll_try = Scrollbar(width=23, command=self.try_text.yview)
        self.try_text["yscrollcommand"] = self.scroll_try.set
        self.scroll_try.place(x=542, y=31, height=211)

        Label(text='Outpud field').pack(anchor=SW, padx=5, pady=5)
        self.output_text = Text(height=13, width=70, wrap=WORD)
        self.output_text.pack(anchor=SW, fill=None)
        self.scroll_out = Scrollbar(width=23, command=self.try_text.yview)
        self.output_text["yscrollcommand"] = self.scroll_out.set
        self.scroll_out.place(x=542, y=272, height=211)

        self.textMenu = Menu(tearoff=False)
        self.textMenu.add_command(label='Clean', command=self.clear)
        self.textMenu.add_command(label='Copy', command=self.copy)
        self.textMenu.add_command(label='Insert', command=self.paste)

        self.try_text.bind('<Button-3>', lambda place, text='try': self.set_menu_pos(text, place))
        self.output_text.bind('<Button-3>', lambda place, text='out': self.set_menu_pos(text, place))

        self.encrypt_button = Button(text='Encrypt', width=38, font='arial 15', command=self.encrypt)
        self.encrypt_button.place(x=568, y=30)
        self.decrypt_button = Button(text='Decrypt', width=38, font='arial 15', command=self.decrypt)
        self.decrypt_button.place(x=568, y=70)

        self.choice_encrypt_var = StringVar(value='Caesar cipher')

        self.caesar_but = Radiobutton(
            text='Caesar cipher',
            value='Caesar cipher',
            variable=self.choice_encrypt_var,
            command=self.addition_to_radiobutton
        )
        self.caesar_but.place(x=586, y=150)

        self.replace_but = Radiobutton(
            text='Replace',
            value='Replace',
            variable=self.choice_encrypt_var,
            command=self.addition_to_radiobutton
        )
        self.replace_but.place(x=586, y=180)

        self.vigenere_but = Radiobutton(
            text='Vigenere cipher',
            value='Vigenere cipher',
            variable=self.choice_encrypt_var,
            command=self.addition_to_radiobutton
        )
        self.vigenere_but.place(x=586, y=210)

        self.becon_but = Radiobutton(
            text='Becon cipher',
            value='Becon cipher',
            variable=self.choice_encrypt_var,
            command=self.addition_to_radiobutton
        )
        self.becon_but.place(x=586, y=240)

        self.atbash_but = Radiobutton(
            text='Atbash',
            value='Atbash',
            variable=self.choice_encrypt_var,
            command=self.addition_to_radiobutton
        )
        self.atbash_but.place(x=586, y=270)

        self.info_lab = Label(text=self.ENCRYPT_LAB_INFO['Caesar cipher'])
        self.info_lab.place(x=730, y=150)

        Label(text='Ключ', font='arial 13').place(x=760, y=320)
        self.key_input = Entry(width=50)
        self.key_input.place(x=580, y=350, height=25)

        self.ENCRYPT_LIST = {
            'Caesar cipher': Caesar,
            'Replace': Replace,
            'Vigenere cipher': Vigenere,
            'Becon cipher': Becon,
            'Atbash': Atbash
        }

    class PlaceMenu:
        '''Keep it inself information on wich window i called'''
        place: str = ''

        @classmethod
        @property
        def get_place(cls):
            return cls.place

    def addition_to_radiobutton(self) -> None:
        '''Function called when radiobuton activated'''

        self.info_lab.destroy()
        self.info_lab = Label(text=self.ENCRYPT_LAB_INFO[self.choice_encrypt_var.get()])
        self.info_lab.place(x=730, y=150)

    def encrypt(self):
        '''Encrypt'''
        self.output_text.delete(0.0, END)

        try:
            print(f'Original text {self.try_text.get(0.0, END)}')
            self.new_text = self.ENCRYPT_LIST[self.choice_encrypt_var.get()]('encrypt',
                                                                             self.try_text.get(0.0, END),
                                                                             self.key_input.get()
                                                                             )
            self.output_text.insert(0.0, self.new_text)
        except ValueError as er:
            messagebox.showerror('Attention!', str(er))
            print(er)
        except KeyError as er:
            messagebox.showerror('Attention!', str(er))
        except AssertionError as er:
            messagebox.showerror('Attention!',str(er))

    def decrypt(self):
        '''Decrypt'''

        self.output_text.delete(0.0, END)

        try:
            self.new_text = self.ENCRYPT_LIST[self.choice_encrypt_var.get()]('decrypt', self.try_text.get(0.0, END),
                                                                             self.key_input.get()
                                                                             )
            self.output_text.insert(0.0, self.new_text)
        except ValueError as er:
            messagebox.showerror('Attention!', str(er))
        except KeyError as er:
            messagebox.showerror('Attention!', str(er))
        except AssertionError as er:
            messagebox.showerror('Attention!', str(er))

    def paste(self) -> None:
        '''Insert in text fild from the clipboard'''

        match self.PlaceMenu.get_place:
            case 'try':
                self.try_text.insert(END, self.clipboard_get())
            case 'out':
                self.output_text.insert(END, self.clipboard_get())

    def clear(self) -> None:
        '''Clean window with text'''

        match self.PlaceMenu.get_place:
            case 'try':
                self.try_text.delete(0.0, END)
            case 'out':
                self.output_text.delete(0.0, END)

    def copy(self) -> None:
        '''Copy window content into clipboard'''

        self.clipboard_clear()
        match self.PlaceMenu.get_place:
            case 'try':
                self.clipboard_append(self.try_text.get(0.0, END))
            case 'out':
                self.clipboard_append(self.output_text.get(0.0, END))

    def set_menu_pos(self, where: str, event) -> None:
        '''Called menu on coordinates'''

        self.PlaceMenu.place = where
        self.textMenu.post(event.x_root, event.y_root)

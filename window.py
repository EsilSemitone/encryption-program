import tkinter as tk
from tkinter import ttk


class MainWindow:
    HEIGHT = 500
    WIDTH = 1000
    root = tk.Tk()
    POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
    POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
    root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')
    icon = tk.PhotoImage(file='images//icon.png')
    root.iconphoto(False, icon)
    root.resizable(False, False)

    def __init__(self, title: str = 'Шифровальщик'):
        self.root.title(title)

        self.app = MainWindowFrame(self.root)

        self.app.mainloop()


class MainWindowFrame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.pack()

        ttk.Label(text='Поле для ввода').pack(anchor=tk.SW, padx=5, pady=5)
        self.try_text = tk.Text(height=10, width=50, wrap=tk.WORD)
        self.try_text.pack(anchor=tk.SW, fill=None)
        self.scroll_try = tk.Scrollbar(width=23, command=self.try_text.yview)
        self.try_text["yscrollcommand"] = self.scroll_try.set
        self.scroll_try.place(x=481, y=36, height=203)

        ttk.Label(text='Поле вывода').pack(anchor=tk.SW, padx=5, pady=5)
        self.try_text = tk.Text(height=10, width=50, wrap=tk.WORD)
        self.try_text.pack(anchor=tk.SW, fill=None)
        self.scroll_try = tk.Scrollbar(width=23, command=self.try_text.yview)
        self.try_text["yscrollcommand"] = self.scroll_try.set
        self.scroll_try.place(x=481, y=274, height=203)


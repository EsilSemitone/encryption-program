import tkinter as tk
from tkinter import ttk


class MainWindow:
    HEIGHT = 500
    WIDTH = 1000

    def __init__(self, title: str ='Шифровальщик'):

        self.root = tk.Tk()

        self.root.title(title)
        self.POS_X = self.root.winfo_screenwidth() // 2 - self.WIDTH // 2
        self.POS_Y = self.root.winfo_screenheight() // 2 - self.HEIGHT // 2
        self.root.geometry(f'{self.WIDTH}x{self.HEIGHT}+{self.POS_X}+{self.POS_Y}')
        self.icon = tk.PhotoImage(file='images//icon.png')
        self.root.iconphoto(False, self.icon)
        self.root.resizable(False, False)

        self.app = MainWindowFrame(self.root)

        self.app.mainloop()


class MainWindowFrame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.pack()

        ttk.Label(text='Поле для ввода').pack(anchor=tk.SW, padx=5, pady=5)
        self.try_text = tk.Text(height=10, width=50, wrap=tk.WORD).pack(anchor=tk.SW, fill=None)
        #self.scroll_try = tk.Scrollbar()

import tkinter as tk
from tkinter import ttk, simpledialog


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

        self.app = WindowFrame(self.root)

        self.app.mainloop()


class WindowFrame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.exit = ttk.Button(text='Cleack me', command=self.click)
        self.exit.pack(anchor='center', expand=2)
        self.pack()

    def click(self) -> None:
        self.dialog = simpledialog.askfloat('oh noo', 'no\t\t\t\t')
        print(self.dialog)


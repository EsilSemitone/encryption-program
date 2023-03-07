import tkinter as tk
from tkinter import ttk, simpledialog

class MainWindow:
    HEIGHT = 1200
    WIDTH = 500

    def __init__(self):
        self.root = tk.Tk()
        self.app = WindowFrame(self.root)

        self.root.title('Окно')
        self.pos = self.root.winfo_screenheight()
        self.root.geometry(f'{self.HEIGHT}x{self.WIDTH}-{}//2 ')
        self.icon = tk.PhotoImage(file='images//icon.png')
        self.root.iconphoto(False, self.icon)

        self.app.mainloop()


class WindowFrame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.exit = ttk.Button(text='Cleack me', command=self.click)
        self.exit.pack(anchor='center', expand=2)
        self.pack()

    def click(self) -> None:
        self.dialog = simpledialog.askfloat('oh noo', 'no\t\t\t\t')
        self.di

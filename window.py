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

    def __init__(self, title: str = 'Шифровщик'):
        self.root.title(title)

        self.app = MainWindowFrame(self.root)
        self.app.mainloop()

    def update_window(self, ) -> None:
        self.app = MainWindowFrame(self.root)


class MainWindowFrame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.pack()

        ttk.Label(text='Поле для ввода').pack(anchor=tk.SW, padx=5, pady=5)
        self.try_text = tk.Text(height=13, width=70, wrap=tk.WORD)
        self.try_text.pack(anchor=tk.SW, fill=None)
        self.scroll_try = tk.Scrollbar(width=23, command=self.try_text.yview)
        self.try_text["yscrollcommand"] = self.scroll_try.set
        self.scroll_try.place(x=542, y=31, height=211)

        ttk.Label(text='Поле вывода').pack(anchor=tk.SW, padx=5, pady=5)
        self.output_text = tk.Text(height=13, width=70, wrap=tk.WORD)
        self.output_text.pack(anchor=tk.SW, fill=None)
        self.scroll_out = tk.Scrollbar(width=23, command=self.try_text.yview)
        self.output_text["yscrollcommand"] = self.scroll_out.set
        self.scroll_out.place(x=542, y=272, height=211)

        self.textMenu = tk.Menu(tearoff=False)
        self.textMenu.add_command(label='Отчистить', command=self.clear)
        #self.textMenu.add_command(label='Test', lambda x = self.setMenuPos.event.x_root: )
        self.try_text.bind('<Button-3>', lambda e, text='try': self.setMenuPos(text, e))
        self.output_text.bind('<Button-3>', lambda e, text='out': self.setMenuPos(text, e))


    def clear(self) -> None:
        pass

    def setMenuPos(self, where: str, event) -> None:

        self.textMenu.post(event.x_root, event.y_root)




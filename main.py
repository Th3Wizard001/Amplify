import tkinter as tk
from Base.top import Top
from Base.bottom import Bottom


class Container(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, bg='white', *args, **kwargs)

        self.top = Top(self)
        self.bottom = Bottom(self)

        self.top.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
        self.bottom.grid(row=1, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

        self.grid_rowconfigure(0, weight=8)
        self.grid_rowconfigure(1, weight=2)
        self.grid_columnconfigure(0, weight=1)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('TK-Player')

    container = Container(root)
    container.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.state('zoomed')

    root.mainloop()

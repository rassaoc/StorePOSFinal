from tkinter import *
from tkinter import ttk

class StorePOS:

    def __init__(self, root):

        root.title("General Store POS")

        s = ttk.Style()
        s.configure('Frame1.TFrame', background='lightgrey')

        mainframe = ttk.Frame(root, padding="5", style='Frame1.TFrame')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        s.configure('Frame2.TFrame', background='grey')
        checkoutFrame = ttk.Frame(mainframe, padding="5", style='Frame2.TFrame')
        checkoutFrame.grid(column=4, row=0)

root = Tk()
StorePOS(root)
root.mainloop()

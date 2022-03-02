from tkinter import *
from tkinter import ttk

class StorePOS:

    def __init__(self, root):

        root.title("General Store POS") # Sets application title

        mainFrame = ttk.Frame(root, padding="5")
        mainFrame.grid(column=0, row=0, sticky=(N,W,E,S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

root = Tk()
StorePOS(root)
root.mainloop()

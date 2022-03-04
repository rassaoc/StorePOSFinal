from tkinter import *
from tkinter import ttk

class StorePOS:

    def __init__(self, root):

        root.title("General Store POS")

        s = ttk.Style()
        s.configure('Frame1.TFrame', background='lightgrey')

        """ Creates Main Frame """
        mainframe = ttk.Frame(root, padding="5", style='Frame1.TFrame')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        """ First Column of Item Buttons """
        s.configure('TButton', background='lightgrey')
        ttk.Button(mainframe, text="Button 1", padding="10", command=self.addToCart).grid(column=0, row=0)
        ttk.Button(mainframe, text="Button 2", padding="10", command=self.addToCart).grid(column=0, row=1)
        ttk.Button(mainframe, text="Button 3", padding="10", command=self.addToCart).grid(column=0, row=2)
        ttk.Button(mainframe, text="Button 4", padding="10", command=self.addToCart).grid(column=0, row=3)
        ttk.Button(mainframe, text="Button 5", padding="10", command=self.addToCart).grid(column=0, row=4)
        ttk.Button(mainframe, text="Button 6", padding="10", command=self.addToCart).grid(column=0, row=5)

        """ Second Column of Item Buttons """
        ttk.Button(mainframe, text="Button 7", padding="10", command=self.addToCart).grid(column=1, row=0)
        ttk.Button(mainframe, text="Button 8", padding="10", command=self.addToCart).grid(column=1, row=1)
        ttk.Button(mainframe, text="Button 9", padding="10", command=self.addToCart).grid(column=1, row=2)
        ttk.Button(mainframe, text="Button 10", padding="10", command=self.addToCart).grid(column=1, row=3)
        ttk.Button(mainframe, text="Button 11", padding="10", command=self.addToCart).grid(column=1, row=4)
        ttk.Button(mainframe, text="Button 12", padding="10", command=self.addToCart).grid(column=1, row=5)

        """ Third Column of Item Buttons """
        ttk.Button(mainframe, text="Button 13", padding="10", command=self.addToCart).grid(column=2, row=0)
        ttk.Button(mainframe, text="Button 14", padding="10", command=self.addToCart).grid(column=2, row=1)
        ttk.Button(mainframe, text="Button 15", padding="10", command=self.addToCart).grid(column=2, row=2)
        ttk.Button(mainframe, text="Button 16", padding="10", command=self.addToCart).grid(column=2, row=3)
        ttk.Button(mainframe, text="Button 17", padding="10", command=self.addToCart).grid(column=2, row=4)
        ttk.Button(mainframe, text="Button 18", padding="10", command=self.addToCart).grid(column=2, row=5)

        """ Creates Checkout Frame on right """
        s.configure('Frame2.TFrame', background='grey')
        checkoutFrame = ttk.Frame(mainframe, padding="5", style='Frame2.TFrame')
        checkoutFrame.grid(column=3, row=0)

        """ Checkout Frame Buttons """
        global checkoutImage
        global cancelSaleImage
        checkoutImage = PhotoImage(file="Checkout.png")
        cancelSaleImage = PhotoImage(file="CancelSale.png")
        manualInputBtn = ttk.Button(mainframe, text="Manual Input", padding = "20", command=self.manualInput).grid(column=3, row=0, rowspan=2)
        cancelSaleBtn = ttk.Button(mainframe, image=cancelSaleImage, command=self.cancelSale).grid(column=3, row=2, rowspan=2)
        checkoutBtn = ttk.Button(mainframe, image=checkoutImage, command=self.checkout).grid(column=3, row=4, rowspan=2)

    def addToCart(self):
        print("Item added to cart")

    def manualInput(self, *args):
        # Open a new window with entry Box
        print("Input Item")

    def cancelSale(self):
        # Remove all items from checkout list
        print("Sale Canceled")

    def checkout(self):
        # Open new window with total price and finsh button
        print("Checkout")

root = Tk()
StorePOS(root)
root.mainloop()

from tkinter import *
from tkinter import ttk

class StorePOS:

    def __init__(self, root):

        self.itemDict = {'Apple': 1.32, 'Banana': 1.85, 'Orange': 1.95, 'Kiwi': 1.68, 'Mango': 2.10, 'Watermelon': 2.55,
                        'Wrench': 4.50, 'Pliers': 4.8, 'Battery': 3.65, 'Screwdriver': 4.25, 'Hammer': 7.0, 'Drill': 12.50,
                        }
        self.shoppingCart = []

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
        ttk.Button(mainframe, text="Apple", padding="10", command=lambda : self.addToCart("Apple")).grid(column=0, row=0)
        ttk.Button(mainframe, text="Banana", padding="10", command=lambda : self.addToCart("Banana")).grid(column=0, row=1)
        ttk.Button(mainframe, text="Orange", padding="10", command=lambda : self.addToCart("Orange")).grid(column=0, row=2)
        ttk.Button(mainframe, text="Kiwi", padding="10", command=lambda : self.addToCart("Kiwi")).grid(column=0, row=3)
        ttk.Button(mainframe, text="Mango", padding="10", command=lambda : self.addToCart("Mango")).grid(column=0, row=4)
        ttk.Button(mainframe, text="Watermelon", padding="10", command=lambda : self.addToCart("Watermelon")).grid(column=0, row=5)

        """ Second Column of Item Buttons """
        ttk.Button(mainframe, text="Wrench", padding="10", command=lambda : self.addToCart("Wrench")).grid(column=1, row=0)
        ttk.Button(mainframe, text="Pliers", padding="10", command=lambda : self.addToCart("Pliers")).grid(column=1, row=1)
        ttk.Button(mainframe, text="Battery", padding="10", command=lambda : self.addToCart("Battery")).grid(column=1, row=2)
        ttk.Button(mainframe, text="Screwdriver", padding="10", command=lambda : self.addToCart("Screwdriver")).grid(column=1, row=3)
        ttk.Button(mainframe, text="Hammer", padding="10", command=lambda : self.addToCart("Hammer")).grid(column=1, row=4)
        ttk.Button(mainframe, text="Drill", padding="10", command=lambda : self.addToCart("Drill")).grid(column=1, row=5)

        """ Third Column of Item Buttons """
        ttk.Button(mainframe, text="Button 13", padding="10", command=self.addToCart).grid(column=2, row=0)
        ttk.Button(mainframe, text="Button 14", padding="10", command=self.addToCart).grid(column=2, row=1)
        ttk.Button(mainframe, text="Button 15", padding="10", command=self.addToCart).grid(column=2, row=2)
        ttk.Button(mainframe, text="Button 16", padding="10", command=self.addToCart).grid(column=2, row=3)
        ttk.Button(mainframe, text="Button 17", padding="10", command=self.addToCart).grid(column=2, row=4)
        ttk.Button(mainframe, text="Button 18", padding="10", command=self.addToCart).grid(column=2, row=5)

        """ Checkout Frame Buttons """
        global checkoutImage # Makes the images global variables to avoid garbage collection
        global cancelSaleImage
        checkoutImage = PhotoImage(file="Checkout.png") # Set unset global variables to their images
        cancelSaleImage = PhotoImage(file="CancelSale.png")
        manualInputBtn = ttk.Button(mainframe, text="Manual Input", padding = "20", command=self.manualInput).grid(column=3, row=0, rowspan=2)
        cancelSaleBtn = ttk.Button(mainframe, image=cancelSaleImage, command=self.cancelSale).grid(column=3, row=2, rowspan=2)
        checkoutBtn = ttk.Button(mainframe, image=checkoutImage, command=self.checkout).grid(column=3, row=4, rowspan=2)

    def addToCart(self, item):
        print(item, "added to cart")
        self.shoppingCart.append(self.itemDict.get(item)) # Adds the price of the item to the shopping cart list

    def manualInput(self, *args):
        # Open a new window with entry Box
        print("Input Item")

    def cancelSale(self):
        print("Sale Canceled")
        self.shoppingCart.clear() # Remove all items from shopping cart

    def checkout(self):
        # Open new window with total price and finsh button
        total = 0
        for item in self.shoppingCart:
            total += item
        print("Total: ", total)
        self.shoppingCart.clear()


root = Tk()
StorePOS(root)
root.mainloop()

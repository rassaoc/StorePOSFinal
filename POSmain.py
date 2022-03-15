from tkinter import *
from tkinter import ttk

class StorePOS:

    def __init__(self, root):

        """ Dictionary of every preset item in POS """
        self.itemDict = {'Apple': 1.32, 'Banana': 1.85, 'Orange': 1.95, 'Kiwi': 1.68, 'Mango': 2.10, 'Watermelon': 2.55,
                        'Wrench': 4.50, 'Pliers': 4.8, 'Battery': 3.65, 'Screwdriver': 4.25, 'Hammer': 7.0, 'Drill': 12.50,
                        'Bat': 5.30, 'Baseball' : 3.2, 'Football' : 6.10, 'Helmet' : 10.25, 'Glove' : 4.50, "Skateboard" : 15.70}

        self.shoppingCart = [] # This list holds all of the items that are getting ready to be finalized (The shopping cart)

        root.title("General Store POS") # Sets window title

        """ Creates a style for the main frame to use"""
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
        ttk.Button(mainframe, text="Bat", padding="10", command=lambda : self.addToCart("Bat")).grid(column=2, row=0)
        ttk.Button(mainframe, text="Baseball", padding="10", command=lambda : self.addToCart("Baseball")).grid(column=2, row=1)
        ttk.Button(mainframe, text="Football", padding="10", command=lambda : self.addToCart("Football")).grid(column=2, row=2)
        ttk.Button(mainframe, text="Helmet", padding="10", command=lambda : self.addToCart("Helmet")).grid(column=2, row=3)
        ttk.Button(mainframe, text="Glove", padding="10", command=lambda : self.addToCart("Glove")).grid(column=2, row=4)
        ttk.Button(mainframe, text="Skateboard", padding="10", command=lambda : self.addToCart("Skateboard")).grid(column=2, row=5)

        """ Checkout Frame Buttons """
        global checkoutImage # Makes the images global variables to avoid garbage collection
        global cancelSaleImage
        checkoutImage = PhotoImage(file="Checkout.png") # Set unset global variables to their images
        cancelSaleImage = PhotoImage(file="CancelSale.png")
        manualInputBtn = ttk.Button(mainframe, text="Manual Input", padding = "20", command=self.manualInput).grid(column=3, row=0, rowspan=2)
        cancelSaleBtn = ttk.Button(mainframe, image=cancelSaleImage, command=self.cancelSale).grid(column=3, row=2, rowspan=2)
        checkoutBtn = ttk.Button(mainframe, image=checkoutImage, command=self.checkout).grid(column=3, row=4, rowspan=2)

    """ Adds items to the shopping cart list """
    def addToCart(self, item):
        print(item, "added to cart")
        self.shoppingCart.append(self.itemDict.get(item)) # Adds the price of the item to the shopping cart list

    """Open a new window for entry box"""
    def manualInput(self, *args):
        inputWindow = Toplevel(root) # Creates a new window
        inputWindow.title("Item Input") # Assigns new window a name
        inputWindow.columnconfigure(0, weight=1) # Configures columns for new window
        inputWindow.rowconfigure(0, weight=1) # Configures rows for new window

        ttk.Label(inputWindow, text = "Enter Item and Price").grid(column=1, row=0)

        """ Creates item entry box"""
        self.itemInput = StringVar() # Creates item variable to be assigned a value later by the entry box
        ttk.Label(inputWindow, text="Item to add: ").grid(column=0,row=1)
        itemEntry = ttk.Entry(inputWindow, textvariable=self.itemInput)
        itemEntry.grid(column=1, row=1)

        """ Creates price entry box"""
        self.priceInput = StringVar() # Creates price variable to be assigned a value later by the entry box
        ttk.Label(inputWindow, text="Price of item: ").grid(column=0,row=2)
        priceEntry = ttk.Entry(inputWindow, textvariable=self.priceInput)
        priceEntry.grid(column=1, row=2)

        inputButton = ttk.Button(inputWindow, text="Add to Cart", command=lambda : self.manualAddToCart()).grid(column=1, row=3) # Calls the manualAddToCart function when the user clicks

    """ Adds the users manual input to the shopping cart """
    def manualAddToCart(self):
        try:
            price = float(self.priceInput.get())
            item = str(self.itemInput.get())
            self.shoppingCart.append(price)
            print(item, "added to cart!")
        except ValueError:
            print("Input not recognized. Please try again.")
            pass

    def cancelSale(self):
        print("Sale Canceled")
        self.shoppingCart.clear() # Remove all items from shopping cart list

    """ Prints the total for the sale and clears the shopping cart """
    def checkout(self):
        total = 0
        for item in self.shoppingCart:
            total += item
        print("Total: ", total)
        self.shoppingCart.clear()


root = Tk()
StorePOS(root)
root.mainloop()

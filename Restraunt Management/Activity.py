import tkinter as tk
from tkinter import ttk, messagebox

class RestrauntOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title ("Restraunt Mangagement Application")

        self.menu_items = {
            "Fries Meal": 2,
            "Lunch Meal": 2,
            "Burger Meal": 3,
            "Pizza Meal": 4,
            "Chesse Burger": 2.5,
            "Drinks":1
        }

        self.exchange_rate = 82
        self.setup_background(root)

        frame = ttk.Frame(root)
        frame.place(relx = 0.5, rely= 0.5,anchor= tk.CENTER)

        ttk.Label(frame, text= "Restraunt Order Management",
                  font= ("Arial", 20, "bold")).grid(row= 0, columnspan= 3, padx= 10, pady= 10)
        self.menu_labels = {}
        self.menu_qunatities = {}

        for i, (item, price ) in enumerate (self.menu_items.items(), start= 1):
            label = ttk.Label(frame, 
                 text=f"{item} ({price})", 
                 font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

# Currency selection
            self.currency_var = tk.StringVar()

            ttk.Label(frame, 
         text="Currency:", 
         font=("Arial", 12)).grid(row=len(self.menu_items) + 1, 
                                 column=0, 
                                 padx=10, 
                                 pady=5)
    def setup_background(self, root):
        bg_width , bg_height = 800, 600
        canvas = tk.Canvas(root, width=bg_width, height=bg_height)
        canvas.pack()
        original_image = tk.PhotoImage(file= "background.png")
        background_image = original_image.subsample(original_image.width() // bg_width(), original_image.height() // bg_height())
        canvas.create_image(0, 0, anchor= tk.NW, image= background_image)
        canvas.image = background_image
    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "₹" if currency ==  "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else "1"
        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text= f"{item} ({symbol}{price}):")

    def place_order(self):
        #To be continued
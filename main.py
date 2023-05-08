import tkinter as tk

class PizzaOrderForm:
    def __init__(self, master):
        self.master = master
        master.title("Pizza Order Form")

        # Pizza size label and radio buttons
        self.size_label = tk.Label(master, text="Select pizza size:")
        self.size_label.grid(row=0, column=0, sticky="w")
        self.size_var = tk.StringVar()
        self.size_var.set("Small")
        self.small_radio = tk.Radiobutton(master, text="Small", variable=self.size_var, value="Small")
        self.small_radio.grid(row=1, column=0)
        self.medium_radio = tk.Radiobutton(master, text="Medium", variable=self.size_var, value="Medium")
        self.medium_radio.grid(row=2, column=0)
        self.large_radio = tk.Radiobutton(master, text="Large", variable=self.size_var, value="Large")
        self.large_radio.grid(row=3, column=0)

        # Pizza toppings label and checkbuttons
        self.toppings_label = tk.Label(master, text="Select toppings:")
        self.toppings_label.grid(row=0, column=1, sticky="w")
        self.pepperoni_var = tk.BooleanVar()
        self.pepperoni_check = tk.Checkbutton(master, text="Pepperoni", variable=self.pepperoni_var)
        self.pepperoni_check.grid(row=1, column=1)
        self.mushrooms_var = tk.BooleanVar()
        self.mushrooms_check = tk.Checkbutton(master, text="Mushrooms", variable=self.mushrooms_var)
        self.mushrooms_check.grid(row=2, column=1)
        self.onions_var = tk.BooleanVar()
        self.onions_check = tk.Checkbutton(master, text="Onions", variable=self.onions_var)
        self.onions_check.grid(row=3, column=1)

        # Delivery options label and dropdown
        self.delivery_label = tk.Label(master, text="Delivery:")
        self.delivery_label.grid(row=0, column=2, sticky="w")
        self.delivery_var = tk.StringVar()
        self.delivery_var.set("Pickup")
        self.delivery_dropdown = tk.OptionMenu(master, self.delivery_var, "Pickup", "Delivery")
        self.delivery_dropdown.grid(row=1, column=2)

        # Name and phone number labels and entries
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=4, column=0, sticky="w")
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=4, column=1)
        self.phone_label = tk.Label(master, text="Phone number:")
        self.phone_label.grid(row=5, column=0, sticky="w")
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=5, column=1)

        # Submit button
        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.grid(row=6, column=1)

    def submit(self):
        size = self.size_var.get()
        toppings = []
        if self.pepperoni_var.get():
            toppings.append("Pepperoni")
        if self.mushrooms_var.get():
            toppings.append("Mushrooms")
        if self.onions_var.get():
            toppings.append("Onions")
        delivery = self.delivery_var.get()
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        # Print order details
        print("Order details:")
        print("Size: {}".format(size))
        print("Toppings: {}".format(", ".join(toppings)))
        print("Delivery: {}".format(delivery))
        print("Name: {}".format(name))
        print("Phone number: {}".format(phone))

        # Reset form
        self.size_var.set("Small")
        self.pepperoni_var.set(False)
        self.mushrooms_var.set(False)
        self.onions_var.set(False)
        self.delivery_var.set("Pickup")
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
def main():
    root = tk.Tk()
    app = PizzaOrderForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()
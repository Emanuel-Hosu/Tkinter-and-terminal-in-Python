import engine as engine
class Graphic():
   
    def __init__(self):
        import tkinter as tk
        self.engine = engine.Engine()

        self.ventana = tk.Tk()
        self.insideTitle = tk.Label()
        # Usado para el costado de la ventana
        self.info = tk.Label()
        self.details = tk.Label()
        self.details2 = tk.Label()
        # Usado para los botones que hay
        self.button1 = tk.Button()
        self.button2 = tk.Button()
        self.button3 = tk.Button()
        self.button4 = tk.Button()
        self.button5 = tk.Button()
        self.button6 = tk.Button()
        self.button7 = tk.Button()
        self.button0 = tk.Button()
        self.insert = tk.Button()
        # Entradas en caso de add product
        self.entry1Label = tk.Label()
        self.entry1 = tk.Entry()
        self.entry2Label = tk.Label()
        self.entry2 = tk.Entry()
        self.entry3Label = tk.Label()
        self.entry3 = tk.Entry()
        self.entry4Label = tk.Label()
        self.entry4 = tk.Entry()

        self.decision = 0

    def set_interface_settings(self):
        self.ventana.title("Emis Burger")
        
        self.insideTitle.config(text="Emis burger")
        self.insideTitle.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.button1.config(text="Show inventory", width=20, height=2, command=self.show_inventory)
        self.button1.grid(row=1, column=0, padx=10, pady=10)

        self.button2.config(text="Add product", width=20, height=2, command=self.add_product)
        self.button2.grid(row=1, column=1, padx=10, pady=10)

        self.button3.config(text="Delete product", width=20, height=2, command=self.remove_product)
        self.button3.grid(row=2, column=0, padx=10, pady=10)

        self.button4.config(text="Update product", width=20, height=2, command=self.update_product)
        self.button4.grid(row=2, column=1, padx=10, pady=10)

        self.button5.config(text="Umbral Price", width=20, height=2, command=self.umbral_price)
        self.button5.grid(row=3, column=0, padx=10, pady=10)

        self.button6.config(text="Search product", width=20, height=2, command=self.search_product)
        self.button6.grid(row=3, column=1, padx=10, pady=10)

        self.button7.config(text="Estadistics resume", width=20, height=2, command=self.estadistics_resume)
        self.button7.grid(row=4, column=0, padx=10, pady=10)

        self.button0.config(text="Exit", width=20, height=2, command=self.ventana.quit)
        self.button0.grid(row=4, column=1, padx=10, pady=10)

        self.info.config(text="Please choose an option")
        self.info.grid(row=0, column=4, columnspan=6, padx= 100, pady= 10)

        self.details.config(text="")
        self.details.grid(row=1, column=4, columnspan=6, padx= 10, pady= 10)

        self.ventana.mainloop()

    def show_inventory(self):
        self.clear_right()
        # Title 
        self.info.config(text="Inventory")

        #Label CATEGORY (burgers, stock, drinks)
        self.entry4Label.config(text="Insert category (has to be, burger, drink, potatoe)")
        self.entry4Label.grid(row=1, column=4)
        #Input PRICE (burgers, stock, drinks)
        self.entry4.config()
        self.entry4.grid(row=2, column=4)

        # Insert into array button
        self.insert.config(text="Check", command=self.back_show_inventory)
        self.insert.grid(row = 3, column=4)

        tempText = self.engine.inteface_show_inventory()
        self.details.config(text=tempText)
        self.details.grid(row=1, column=4, columnspan=6)  

    def back_show_inventory(self):
        try:
            category = str(self.entry4.get())
        except:
            self.details2.config(text="An error has ocurred while showing inventory")
            self.details2.grid(row= 1, column= 5)
        
        tempText = self.engine.inteface_show_inventory(category)
        self.details.config(text=tempText)
        self.details.grid(row=1, column=5, columnspan=6, padx=10, pady=10)

    def add_product(self):
        self.clear_right()
        self.info.config(text="Add product")

        #Label NAME
        self.entry1Label.config(text="Insert name")
        self.entry1Label.grid(row=1, column=4, padx= 10)
        #Input NAME
        self.entry1.config()
        self.entry1.grid(row=2, column=4, padx= 10)
        #Label STOCK
        self.entry2Label.config(text="Insert stock")
        self.entry2Label.grid(row=3, column=4, padx= 10)
        #Input STOCK
        self.entry2.config()
        self.entry2.grid(row=4, column=4, padx= 10)
        #Label PRICE
        self.entry3Label.config(text="Insert price")
        self.entry3Label.grid(row=5, column=4, padx= 10)
        #Input PRICE
        self.entry3.config()
        self.entry3.grid(row=6, column=4, padx= 10)
        #Label CATEGORY (burgers, stock, drinks)
        self.entry4Label.config(text="Insert category (has to be, burger, drink, potatoe)")
        self.entry4Label.grid(row=7, column=4, padx= 10)
        #Input PRICE (burgers, stock, drinks)
        self.entry4.config()
        self.entry4.grid(row=8, column=4, padx= 10)
    
        # Insert into array button
        self.insert.config(text="Add", command=self.back_add_product)
        self.insert.grid(row = 10, column=4, padx=10)

    def back_add_product(self):
        try:
            name = str(self.entry1.get())
            stock = int(self.entry2.get())
            price = float(self.entry2.get())
            category = str(self.entry4.get())
        except:
            self.details2.config(text="An error has ocurred while adding product")
            self.details2.grid(row= 1, column= 5, padx=10, pady=10)
       
        booleanEngineInfo = self.engine.interface_add(name, stock, price, category) # En caso de que el producto no exista en engine lo añade sino no.

        if booleanEngineInfo == False: # En caso de que NO SE ha encontrado el producto lo añade
            self.details2.config(text=f"Product ADDED, Name: {name}, Stock: {stock}, Price: {price}")
        else:
            self.details2.config(text=f"Product already exist in iventory")
        self.details2.grid(row= 1, column= 5, padx=10, pady=10)

    def remove_product(self):
        self.clear_right()

        #Label NAME
        self.entry1Label.config(text="Insert name")
        self.entry1Label.grid(row=1, column=4, padx= 10)
        #Input NAME
        self.entry1.config()
        self.entry1.grid(row=2, column=4, padx= 10)
        #Label CATEGORY (burgers, stock, drinks)
        self.entry4Label.config(text="Insert category (has to be, burger, drink, potatoe)")
        self.entry4Label.grid(row=3, column=4, padx= 10)
        #Input PRICE (burgers, stock, drinks)
        self.entry4.config()
        self.entry4.grid(row=4, column=4, padx= 10)
    
        # Insert into array button
        self.insert.config(text="Remove", command=self.back_remove_product)
        self.insert.grid(row = 5, column=4, padx=10)
    
    def back_remove_product(self):
        try:
            name = str(self.entry1.get())
            category = str(self.entry4.get())
        except:
            self.details2.config(text="An error has ocurred while removing product")
            self.details2.grid(row= 1, column= 5, padx=10, pady=10)
       
        booleanEngineInfo = self.engine.interface_remove(name, category) # En caso de que el producto exita en engine lo elimina
        if (booleanEngineInfo == True):
            self.details2.config(text=f"Product {name} removed")
        else:
            self.details2.config(text=f"Product {name} not found")
        self.details2.grid(row= 1, column= 5, padx=10, pady=10)
    
    def update_product(self):
        self.clear_right()

        #Label NAME
        self.entry1Label.config(text="Insert name")
        self.entry1Label.grid(row=1, column=4, padx= 10)
        #Input NAME
        self.entry1.config()
        self.entry1.grid(row=2, column=4, padx= 10)
        #Label STOCK
        self.entry2Label.config(text="Insert stock")
        self.entry2Label.grid(row=3, column=4, padx= 10)
        #Input STOCK
        self.entry2.config()
        self.entry2.grid(row=4, column=4, padx= 10)
        #Label PRICE
        self.entry3Label.config(text="Insert price")
        self.entry3Label.grid(row=5, column=4, padx= 10)
        #Input PRICE
        self.entry3.config()
        self.entry3.grid(row=6, column=4, padx= 10)
        #Label CATEGORY (burgers, stock, drinks)
        self.entry4Label.config(text="Insert category (has to be, burger, drink, potatoe)")
        self.entry4Label.grid(row=7, column=4, padx= 10)
        #Input PRICE (burgers, stock, drinks)
        self.entry4.config()
        self.entry4.grid(row=8, column=4, padx= 10)
    
        # Insert into array button
        self.insert.config(text="Update", command=self.back_update_product)
        self.insert.grid(row = 10, column=4, padx=10)

    def back_update_product(self):
        try:
            name = str(self.entry1.get())
            stock = int(self.entry2.get())
            price = float(self.entry2.get())
            category = str(self.entry4.get())
        except:
            self.details2.config(text="An error has ocurred while updating product")
            self.details2.grid(row= 1, column= 5, padx=10, pady=10)
       
        booleanEngineInfo = self.engine.interface_update(name, stock, price, category)
        if (booleanEngineInfo == True):
            self.details2.config(text=f"Product {name} updated")
        else:
            self.details2.config(text=f"Product {name} not found")
        self.details2.grid(row= 1, column= 5, padx=10, pady=10)

    def umbral_price(self):
        self.clear_right()

        #Label PRICE
        self.entry1Label.config(text="Insert price")
        self.entry1Label.grid(row=1, column=4, padx= 10)
        #Input PRICE
        self.entry1.config()
        self.entry1.grid(row=2, column=4, padx= 10)

        #Label category
        self.entry4Label.config(text="Insert category (has to be, burger, drink, potatoe)")
        self.entry4Label.grid(row=3, column=4, padx= 10)
        #Input PRICE (burgers, stock, drinks)
        self.entry4.config()
        self.entry4.grid(row=4, column=4, padx= 10)
    
        # Insert into array button
        self.insert.config(text="Check", command=self.back_umbral_price)
        self.insert.grid(row = 5, column=4, padx=10)

    def back_umbral_price(self):
        try:
            price = float(self.entry1.get())
            category = str(self.entry4.get())
        except:
            self.details2.config(text="An error has ocurred while checking umbral price")
            self.details2.grid(row= 1, column= 5, padx=10, pady=10)
       
        tempText = self.engine.interface_umbral_price(price, category) # Enigne
        if tempText == "":
            self.details2.config(text="No products found")
        else:
            self.details2.config(text=tempText)
        self.details2.grid(row=1, column=5, columnspan=6, padx=10, pady=10)        

    def search_product(self):
        self.clear_right()

        self.info.config(text="Search product")
        self.info.grid(row=0, column=4, columnspan=6, padx= 100, pady= 10)
        #Label NAME
        self.entry1Label.config(text="Insert name")
        self.entry1Label.grid(row=1, column=4, padx= 10)
        #Input NAME
        self.entry1.config()
        self.entry1.grid(row=2, column=4, padx= 10)
        #Label CATEGORY (burgers, stock, drinks)
        self.entry4Label.config(text="Insert category (has to be, burger, drink, potatoe)")
        self.entry4Label.grid(row=3, column=4, padx= 10)
        #Input PRICE (burgers, stock, drinks)
        self.entry4.config()
        self.entry4.grid(row=4, column=4, padx= 10)
    
        # Insert into array button
        self.insert.config(text="Search", command=self.back_search_product)
        self.insert.grid(row = 5, column=4, padx=10)
    
    def back_search_product(self):
        try:
            name = str(self.entry1.get())
            category = str(self.entry4.get())
        except:
            self.details2.config(text="An error has ocurred while searching product")
            self.details2.grid(row= 1, column= 5, padx=10, pady=10)
       
        tempText = self.engine.interface_search(name, category)
        if tempText == "":
            self.details2.config(text="No products found")
            self.details2.grid(row=1, column=5, columnspan=6, padx=10, pady=10)
        else:
            self.details2.config(text=tempText)
            self.details2.grid(row=1, column=5, columnspan=6, padx=10, pady=10)

    def estadistics_resume(self):
        self.clear_right()
        self.info.config(text="Estadistics resume")
        self.info.grid(row=0, column=4, columnspan=6, padx= 100, pady= 10)

        tempText = self.engine.interface_estadistics_resume()
        if tempText == "":
            self.details2.config(text="No products found")
            self.details2.grid(row=1, column=5, columnspan=6, padx=10, pady=10)
        else:
            self.details2.config(text=tempText)
            self.details2.grid(row=1, column=5, columnspan=6, padx=10, pady=10)

    def clear_right(self):
        self.info.grid_forget()
        self.details.grid_forget()
        self.details2.grid_forget()
        self.entry1Label.grid_forget()
        self.entry1.grid_forget()
        self.entry2Label.grid_forget()
        self.entry2.grid_forget()
        self.entry3Label.grid_forget()
        self.entry3.grid_forget()
        self.entry4Label.grid_forget()
        self.entry4.grid_forget()
        self.insert.grid_forget()
class Engine:
    def __init__(self):
        #Name, disponible burgers, price
        #Burgers
        self.burgers = [["La Clásica Emi", 50, 8],
                  ["La Emi Supreme", 30, 12],
                  ["La Emizilla", 30, 18],
                  ["La Emición Imposible", 2, 25],
                  ["Emi-tame Esta", 10, 12]]
        # Bebidas
        self.drinks = [
            ["Emi-Cola", 50, 2.5],
            ["Limo-Emi", 20, 3],
            ["Emi-BOOM", 30, 5.5],
            ["H2Emi", 60, 2],
            ["Té Emi-licioso", 15, 4]
        ]

        # Patatas
        self.potatoes = [
            ["Emi-Fritas", 50, 2.5],
            ["Papa-Emi", 30, 3],
            ["Cruji-Emi", 30, 3.3],
            ["Emi-Tatas", 10, 3.5],
            ["Papotas Emi-zadas", 5, 4]
        ]

        # Var for exiting_or_do
        self.choosedNum = 0
        self.exiting = False
        
    def pause(self):
        input("\nPress Enter to continue...")

    def menu(self):
        print("""
                                    (                                
            (       )    (        ( )\\    (   (    (  (     (   (    
            )\\     (     )\\  (    )((_)  ))\\  )(   )\\))(   ))\\  )(   
            ((_)    )\\  '((_) )\\  ((_)_  /((_)(()\\ ((_))\\  /((_)(()\\  
            | __| _((_))  (_)((_)  | _ )(_))(  ((_) (()(_)(_))   ((_) 
            | _| | '  \\() | |(_-<  | _ \\| || || '_|/ _` | / -_) | '_| 
            |___||_|_|_|  |_|/__/  |___/ \\_,_||_|  \\__, | \\___| |_|   
                                                    |___/              
            """)    
        print("1. Show inventory")
        print("2. Add item")
        print("3. Remove item")
        print("4. Search item")
        print("5. Update item")
        print("0. Exit")

    def run(self):
        while True:
            self.menu()
            user = input("Enter your choice: ")

            if user == "1":
                self.show_inventory()
            elif user == "2":
                self.add_item()
            elif user == "3":
                self.remove_item()
            elif user == "4":
                self.search_item()
            elif user == "5":
                self.update_item()
            elif user == "0":
                break
            else:
                print("Invalid choice")
                continue
    
    def show_inventory(self):
        print("""\n
    _____                     _                   
    |_   _|                   | |                  
    | | _ ____   _____ _ __ | |_ ___  _ __ _   _ 
    | || '_ \ \ / / _ \ '_ \| __/ _ \| '__| | | |
    _| || | | \ V /  __/ | | | || (_) | |  | |_| |
    \___/_| |_|\_/ \___|_| |_|\__\___/|_|   \__, |
                                            __/ |
                                            |___/ 
    """)    
        while self.exiting == False:
            self.exit_or_do("inventory", "view")
            
            #Comprobacion si el usuario decide salir del programa:
            if self.exiting == True:
                self.exiting = False
                break
        
            print("")
            #Imprime el inventario de lo elegido
            if self.choosedNum == 1:
                print("Cheking BURGERS:\n")
                for burger in self.burgers:
                    print("Name: ", burger[0] + "\nDisponible menus: ", burger[1], "\nPrice: ", burger[2], "€\n")
                break
            elif self.choosedNum == 2:
                print("Cheking DRINKS:\n")
                for drink in self.drinks:
                    print("Name: ", drink[0] + "\nStock: ", drink[1], "\nPrice: ", drink[2], "€\n")
                break
            elif self.choosedNum == 3:
                print("Cheking POTATOES:\n")
                for potatoe in self.potatoes:
                    print("Name: ", potatoe[0] + "\nStock: ", potatoe[1], "\nPrice: ", potatoe[2], "€\n")
                break
        
        self.choosedNum = 0

        while True:
            user = input("\nCONTINUE checking? y/n: ")
            if user == "y" or user == "Y":
                self.show_inventory()
                break
            elif user == "n" or user == "N":
                self.pause()
                break

    # Funcion que se menciona al principio de cada funcion para ahorrar codigo y no repetirlo
    def exit_or_do(self, type, do):
        while True:
            print("Type EXIT to go back to the menu:")
            print(f"\nWhat {type} do you want to {do}?\n1. Burgers\n2. Drinks\n3. Potatoes")

            while True:
                try:
                    user = input()
                    if user == 'exit' or user == "EXIT":
                        self.exiting = True
                        break
                    
                    #Comprobar que esta en el mismo rango
                    if int(user) > 0 and int(user) <= 3:
                        self.choosedNum = int(user) #Variable que uso varias veces mas abajo para saber exactamente que "burger" esta el usuario editando y saber cuantos campos tiene esa burger
                        break
                    else:
                        print("INVALID input, has to be a number from 1 to 3 or type EXIT to go back to the menu.")
                except:
                    print("INVALID input, has to be a number from 1 to 3 or type EXIT to go back to the menu.")
            if (self.exiting == True):
                break
            elif (self.choosedNum != 0):
                break
   

    def add_item(self):
        print("""\n
  ___      _     _   _____ _                 
 / _ \    | |   | | |_   _| |                
/ /_\ \ __| | __| |   | | | |_ ___ _ __ ___  
|  _  |/ _` |/ _` |   | | | __/ _ \ '_ ` _ \ 
| | | | (_| | (_| |  _| |_| ||  __/ | | | | |
\_| |_/\__,_|\__,_|  \___/ \__\___|_| |_| |_|
                                             
                                             
""")    
        while True:
            self.exit_or_do("product", "add")

            # Resetear la variable y salir del bucle
            if(self.exiting == True):
                self.exiting = False
                break

            error = False
            productName = ""
            # Comprobamos si el producto ya existe
            if(self.choosedNum == 1):
                productName = input("Introduce burger NAME: " )
                for burger in self.burgers:
                    if burger[0] == productName:
                        error = True
                        print("Product already exist, please try again.")
            elif(self.choosedNum == 2):
                productName = input("Introduce drink NAME: " )
                for drink in self.drinks:
                    if drink[0] == productName:
                        error = True
                        print("Product already exist, please try again.")
            elif(self.choosedNum == 3):
                productName = input("Introduce potato NAME: " )
                for potato in self.potatoes:
                    if potato[0] == productName:
                        error = True
                        print("Product already exist, please try again.")

            items = self.add_item_back()

            if error == False:# Si no hay error nos salimos del bucle while :)
                break
        
        # Añadimos el producto dependiendo de lo que ha elegiod el usuario
        if(self.choosedNum == 1):
            self.burgers.append([productName, items[0], items[1]])
            print("\nSuccesful PRODUCT ADDED in BURGERS:\nName: ", productName, "\nDisponible menus: ", items[0], "\nPrice: ", items[1], "€")
        elif(self.choosedNum == 2):
            self.drinks.append([productName, items[0], items[1]])
            print("\nSuccesful PRODUCT ADDED in DRINKS:\nName: ", productName, "\nStock: ", items[0], "\nPrice: ", items[1], "€")
        elif(self.choosedNum == 3):
            self.potatoes.append([productName, items[0], items[1]])
            print("\nSuccesful PRODUCT ADDED in POTATOES:\nName: ", productName, "\nStock: ", items[0], "\nPrice: ", items[1], "€")
        
        # Reset the variable
        self.choosedNum = 0

        while True:
            user = input("\nCONTINUE adding? y/n: ")
            if user == "y" or user == "Y":
                self.add_item()
                break
            elif user == "n" or user == "N":
                self.pause()
                break
    
    # Funcion adicional que se encarga de añadir un producto
    def add_item_back(self):
        item2 = 0
        item3 = 0
        if (self.choosedNum == 1):
            string1 = "DISPONIBLE MENUS"
            string2 = "PRICE"
        elif (self.choosedNum == 2):
            string1 = "STOCK"
            string2 = "PRICE"
        elif(self.choosedNum == 3):
            string1 = "STOCK"
            string2 = "PRICE"

        while item2 <= 0:
            try:
                item2 = int(input(f"\nIntroduce {string1}: "))

                if item2 < 0:
                    print(f"WRONG input in {string1}, it has to be a positive NUMBER.")
            except:
                print(f"WRONG input in {string1}, it has to be a NUMBER.")
        while item3 <= 0:
            try:
                item3 = int(input(f"\nIntroduce {string2}: "))

                if item3 < 0:
                    print(f"WRONG input PRICE, it has to be a positive {string2}.")
            except:
                print(f"WRONG input PRICE, it has to be a {string2}.")
        
        return [item2, item3]
        

    def search_item(self):
        print("""\n _____                     _     
/  ___|                   | |    
\ `--.  ___  __ _ _ __ ___| |__  
 `--. \/ _ \/ _` | '__/ __| '_ \ 
/\__/ /  __/ (_| | | | (__| | | |
\____/ \___|\__,_|_|  \___|_| |_|
                                 
                                 """)
        
        
        encontrado = False
        while encontrado == False and self.exiting == False:
            self.exit_or_do("product", "SEARCH")

            # Resetear la variable y salir del bucle
            if(self.exiting == True):
                self.exiting = False
                break

            if(self.choosedNum == 1):
                burgerName = input("Introduce burger NAME: ")
                for burger in self.burgers:
                    if burger[0] == burgerName:
                        encontrado = True
                        print("\nSuccesful product FOUND:")
                        print("Name: ", burger[0] + "\nDisponible menus: ", burger[1], "\nPrice: ", burger[2], "€\n")
                        break
            elif(self.choosedNum == 2):
                drinkName = input("Introduce drink NAME: ")
                for drink in self.drinks:
                    if drink[0] == drinkName:
                        encontrado = True
                        print("\nSuccesful product FOUND:")
                        print("Name: ", drink[0] + "\nDisponible menus: ", drink[1], "\nPrice: ", drink[2], "€\n")
                        break
            elif(self.choosedNum == 2):
                potatoeName = input("Introduce potatoe NAME: ")
                for potatoe in self.potatoes:
                    if potatoe[0] == potatoeName:
                        encontrado = True
                        print("\nSuccesful product FOUND:")
                        print("Name: ", potatoe[0] + "\nDisponible menus: ", potatoe[1], "\nPrice: ", potatoe[2], "€\n")
                        break

            if encontrado == False:
                print("Product NOT FOUND, please try again.\n")

        # Reset the variable
        self.choosedNum = 0

        while True:
            user = input("\nCONTINUE searching? y/n: ")
            if user == "y" or user == "Y":
                self.search_item()
                break
            elif user == "n" or user == "N":
                self.pause()
                break

    def update_item(self):
        print("""\n
 _   _           _       _         _ _                 
| | | |         | |     | |       (_) |                
| | | |_ __   __| | __ _| |_ ___   _| |_ ___ _ __ ___  
| | | | '_ \ / _` |/ _` | __/ _ \ | | __/ _ \ '_ ` _ \ 
| |_| | |_) | (_| | (_| | ||  __/ | | ||  __/ | | | | |
 \___/| .__/ \__,_|\__,_|\__\___| |_|\__\___|_| |_| |_|
      | |                                              
      |_|                                              
""")
    
        index = 0
        exiting = False
        
        while self.exiting == False:
            self.exit_or_do("product", "UPDATE")

            #Resetear la variable y salir del bucle
            if self.exiting == True:
                self.exiting = False
                break

            print("\nDISPONIBLE products: \n")
            index = self.print_disponible_items()

            #Comprobacion si el usuario decide salir del programa:
            print("Select the item you want to update from 1 at", index)
            #Comprobamos errores
            while True:
                try:
                    user = input()
                    
                    #Comprobar que esta en el mismo rango
                    if int(user) <= index and int(user) > 0:
                        choosedNum = int(user) #Variable que uso varias veces mas abajo para saber exactamente que "burger" esta el usuario editando y saber cuantos campos tiene esa burger
                        break
                    else:
                        print("INVALID input, has to be a number from 1 to", index, "or type EXIT to go back to the menu.")
                except:
                    print("INVALID input, has to be a number from 1 to", index, "or type EXIT to go back to the menu.")

            #Comprobacion si el usuario decide salir del programa:
            if exiting == True:
                break

            #Si el producto ha sido encontrado
            print("\nProduct FOUND you have select:")
            if (self.choosedNum == 1):
                print("1. Name: ", self.burgers[choosedNum - 1][0] + "\n2. Disponible menus:", self.burgers[choosedNum - 1][1], "\n3. Price: ", self.burgers[choosedNum - 1][2], "€\n")
                #Ver que campo quiere editar el usuario
                print("What field do you want to edit? type a number from 1 to", len(self.burgers[choosedNum]))
            elif (self.choosedNum == 2):
                print("1. Name: ", self.drinks[choosedNum - 1][0] + "\n2. Stock:", self.drinks[choosedNum - 1][1], "\n3. Price: ", self.drinks[choosedNum - 1][2], "€\n")
                #Ver que campo quiere editar el usuario
                print("What field do you want to edit? type a number from 1 to", len(self.drinks[choosedNum]))
            elif (self.choosedNum == 2):
                print("1. Name: ", self.potatoes[choosedNum - 1][0] + "\n2. Stock:", self.potatoes[choosedNum - 1][1], "\n3. Price: ", self.potatoes[choosedNum - 1][2], "€\n")
                #Ver que campo quiere editar el usuario
                print("What field do you want to edit? type a number from 1 to", len(self.potatoes[choosedNum]))
            
            #Comprobacion de errores de eleccion de campos entre "Name, Stock y Price"
            while True:
                try:
                    # Por si en un futuro habrian mas opciones que que Name, Stock y Price para que no haya conflictos al elegir el campo
                    user = input()
                    length = 0
                    if (choosedNum == 1):
                        length = len(self.burgers[choosedNum])
                    elif (choosedNum == 2):
                        length = len(self.drinks[choosedNum])
                    elif (choosedNum == 3):
                        length = len(self.potatoes[choosedNum])

                    if int(user) > 0 and int(user) <= length:
                        option = int(user) #Variable que usare mas abajo para saber que es lo que va a editar exactamente el usuario
                        break
                    else:
                        print("INVALID input, number its lower or higher then 1 to", length)
                except:
                    print("INVALID input, has to be a number from 1 to", length)

            #Recoger el Stirng de el campo elegido
            if option == 1:
                field = "Name"
            elif option == 2:
                if choosedNum == 1:
                    field = "Disponible menus"
                else:
                    field = "Stock"
            else:
                field = "Price"

            #En caso de encontrar la opcion correcta
            print(f"SUCCESFUL choosed, {field}, acctual value:")
            if (self.choosedNum == 1):
                print(field, ":", self.burgers[choosedNum - 1][option - 1]) #Ajustarlo a tamaño array jeje god
            elif(self.choosedNum == 2):
                print(field, ":", self.drinks[choosedNum - 1][option - 1])
            elif(self.choosedNum == 3):
                print(field, ":", self.potatoes[choosedNum - 1][option - 1])

            #Comprobacion de errores de eleccion de campos entre "Name, Stock y Price"
            print("\nIntroduce the new value for", field)
            while True:
                try:
                    user = input() #En caso de que sea texto
                    if (option == 1):
                        if (self.choosedNum == 1):
                            self.burgers[choosedNum - 1][option - 1] = user #Ajustarlo a tamaño array jeje god
                        elif (self.choosedNum == 2):
                            self.drinks[choosedNum - 1][option - 1] = user
                        elif (self.choosedNum == 3):
                            self.potatoes[choosedNum - 1][option - 1] = user
                        break
                    else:
                        user = int(user) #En caso de que sea un numero
                        if user >= 0: # Comprobar que el numero es positivo
                            if (self.choosedNum == 1):
                                self.burgers[choosedNum - 1][option - 1] = user #Ajustarlo a tamaño array jeje god
                            elif (self.choosedNum == 2):
                                self.drinks[choosedNum - 1][option - 1] = user
                            elif (self.choosedNum == 3):
                                self.potatoes[choosedNum - 1][option - 1] = user
                            break
                        else:
                            print("INVALID input, has to be a positive number.")
                except:
                    print("INVALID input, has to be a number.")
            
            print("\nSuccesful PRODUCT UPDATED:")
            # Reset the variable
            self.choosedNum = 0
            break
        
        # Ver si el usuario desea seguir actualizando o no
        while True:
            user = input("\nCONTINUE updating? y/n: ")
            if user == "y" or user == "Y":
                self.update_item()
                break
            elif user == "n" or user == "N":
                self.pause()
                break

    # Funcion que imprime todos los productos disponibles y devuelve el inidice de productos de cada uno, de momento la uso en (remove y update)
    def print_disponible_items(self):
        index = 0
        if self.choosedNum == 1:
            for burger in self.burgers:
                index += 1
                print("Number ", index , ":")
                print("Name: ", burger[0] + "\nDisponible menus: ", burger[1], "\nPrice: ", burger[2], "€\n")
        elif self.choosedNum == 2:
            for drink in self.drinks:
                index += 1
                print("Number ", index , ":")
                print("Name: ", drink[0] + "\nStock: ", drink[1], "\nPrice: ", drink[2], "€\n")
        elif self.choosedNum == 3:
            for potatoe in self.potatoes:
                index += 1
                print("Number ", index , ":")
                print("Name: ", potatoe[0] + "\nStock: ", potatoe[1], "\nPrice: ", potatoe[2], "€\n")
        
        return index

    def remove_item(self):
        print("""\n
______                              
| ___ \                             
| |_/ /___ _ __ ___   _____   _____ 
|    // _ \ '_ ` _ \ / _ \ \ / / _ \
| |\ \  __/ | | | | | (_) \ V /  __/
\_| \_\___|_| |_| |_|\___/ \_/ \___|
                                    
                                    """)
        index = 0
        while self.exiting == False:
            self.exit_or_do("product", "REMOVE")

            #Resetear la variable y salir del bucle en caso de salir de este 
            if self.exiting == True:
                self.exiting = False
                break

            print("\nDISPONIBLE products: \n")
            index = self.print_disponible_items()

            #Comprobacion si el usuario decide salir del programa:
            while True:
                try:
                    print("Select the item you want to remove from 1 at", index)
                    user = int(input())
                except:
                    print("INVALID input, has to be a number from 1 to", index)
            
            
    

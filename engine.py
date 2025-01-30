class Engine:
    def __init__(self):
        #Name, disponible burgers, price
        #Burgers
        self.burgers = [["La Clásica Emi", 50, 8],
                  ["La Emi Supreme", 30, 12],
                  ["La Emizilla", 30, 18],
                  ["La Emición Imposible", 2, 25],
                  ["Emi-tame Esta", 10, 25]]
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
        """
        Pausa la ejecución del programa hasta que el usuario presione Enter.
        """
        input("\nPress Enter to continue...")

    def menu(self):
        """
        Muestra el menú principal con las opciones disponibles para el usuario.
        """
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
        print("6. Umbral price")
        print("7. Estadistics resume")
        print("0. Exit")

    def run(self):
        """
        Ejecuta el bucle principal del programa, mostrando el menú y esperando la selección del usuario.
        """
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
            elif user == "6":
                self.ubral_price()
            elif user == "7":
                self.estadistics_resume()
            elif user == "0":
                break
            else:
                print("Invalid choice")
                continue
    
    def show_inventory(self):
        """
        Muestra el inventario de productos. El usuario puede elegir entre ver los productos de tipo hamburguesa, bebida o patatas, a través del metodo
        exit_or_do, que se encarga de mostrar un mensaje y comprobar si el usuario quiere salir del programa, o que producto quiere ver.
        """
        print("""\n
  _____                      _                   
  \_   \_ ____   _____ _ __ | |_ ___  _ __ _   _ 
   / /\/ '_ \ \ / / _ \ '_ \| __/ _ \| '__| | | |
/\/ /_ | | | \ V /  __/ | | | || (_) | |  | |_| |
\____/ |_| |_|\_/ \___|_| |_|\__\___/|_|   \__, |
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
        """
        Método encargado de mostrar un mensaje y comprobar si el usuario quiere salir del programa, o que producto quiere ver. Usado en varios métodos,
        como show_inventory, add_item, search_item, update_item, remove_item, ubral_price y estadistics_resume.
        """
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
        """
        Método encargado de añadir un producto al inventario. El usuario puede elegir entre añadir un producto de tipo hamburguesa, bebida o patatas, a través del metodo exit_or_do.
        Ademas de tener otro metodo llamado add_item_back que se encarga de añadir un producto dependiendo de lo que ha elegido el usuario. (Para ahorrar codigo y no repetirlo)
        """
        print("""\n
   _       _     _    _____ _                 
  /_\   __| | __| |   \_   \ |_ ___ _ __ ___  
 //_\\ / _` |/ _` |    / /\/ __/ _ \ '_ ` _ \ 
/  _  \ (_| | (_| | /\/ /_ | ||  __/ | | | | |
\_/ \_/\__,_|\__,_| \____/  \__\___|_| |_| |_|
                                                                              
""")    
        self.exit_or_do("product", "add")
        while True:
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
                    if str(burger[0]).lower() == productName.lower():
                        error = True
                        print("Product already exist, please try again.")
            elif(self.choosedNum == 2):
                productName = input("Introduce drink NAME: " )
                for drink in self.drinks:
                    if drink[0] == productName.lower():
                        error = True
                        print("Product already exist, please try again.")
            elif(self.choosedNum == 3):
                productName = input("Introduce potato NAME: " )
                for potato in self.potatoes:
                    if potato[0] == productName.lower():
                        error = True
                        print("Product already exist, please try again.")

            if error == False:# Si no hay error nos salimos del bucle while :)
                break

        items = self.add_item_back()

        
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
        """
        Método usado en add_item, encargado de añadir un producto al inventario. Devuelve una lista con los valores introducidos por el usuario.
        """
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
                item3 = float(input(f"\nIntroduce {string2}: "))

                if item3 < 0:
                    print(f"WRONG input PRICE, it has to be a positive {string2}.")
            except:
                print(f"WRONG input PRICE, it has to be a {string2}.")
        
        return [item2, item3]
        

    def search_item(self):
        """
        Método encargado de buscar un producto en el inventario. El usuario puede elegir entre buscar un producto de tipo hamburguesa, bebida o patatas, a través del metodo
        """
        print("""\n 
 __                     _     
/ _\ ___  __ _ _ __ ___| |__  
\ \ / _ \/ _` | '__/ __| '_ \ 
_\ \  __/ (_| | | | (__| | | |
\__/\___|\__,_|_|  \___|_| |_|
                              
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
        """
        Metodo encargado de actualizar un producto en el inventario. El usuario puede elegir entre actualizar un producto de tipo hamburguesa, bebida o patatas, a través del metodo exit_or_do.
        Adémas de updatear los datos de un producto, por separado, como el nombre, stock o precio.
        """
        print("""\n
                 _       _         _ _                 
 /\ /\ _ __   __| | __ _| |_ ___  (_) |_ ___ _ __ ___  
/ / \ \ '_ \ / _` |/ _` | __/ _ \ | | __/ _ \ '_ ` _ \ 
\ \_/ / |_) | (_| | (_| | ||  __/ | | ||  __/ | | | | |
 \___/| .__/ \__,_|\__,_|\__\___| |_|\__\___|_| |_| |_|
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
                    if (self.choosedNum == 1):
                        length = len(self.burgers[choosedNum])
                    elif (self.choosedNum == 2):
                        length = len(self.drinks[choosedNum])
                    elif (self.choosedNum == 3):
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
                    elif option == 2:
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
                    else:
                        user = float(user) #En caso de que sea un numero
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
        """
        Método que imprime todos los productos disponibles y devuelve el índice de productos de cada uno. Usado en metodos como remove_item y update_item.
        """
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
        """
        Método encargado de eliminar un producto del inventario. El usuario puede elegir entre eliminar un producto de tipo hamburguesa, bebida o patatas, a través del metodo exit_or_do. 
        """
        print("""\n
   __                               
  /__\ ___ _ __ ___   _____   _____ 
 / \/// _ \ '_ ` _ \ / _ \ \ / / _ \\
/ _  \  __/ | | | | | (_) \ V /  __/
\/ \_/\___|_| |_| |_|\___/ \_/ \___|
                                    
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
            while self.exiting == False:
                try:
                    print("Select the item you want to remove from 1 at", index)
                    user = input()

                    if int(user) > 0 and int(user) <= index:
                        option = int(user) # Variable que vamos a utilizar mas abajo para saber que producto va a eliminar el usuario
                        break
                    else:
                        print("INVALID input, has to be a number from 1 to", index)
                except:
                    print("INVALID input, has to be a number from 1 to", index)
            
            #Borramos el producto
            print("REMOVED PRODUCT:")
            match self.choosedNum:
                case 1:
                    #Cambiar esto
                    print("Name: ", self.burgers[option - 1][0] + "\nDisponible menus: ", self.burgers[option - 1][1], "\nPrice: ", self.burgers[option - 1][2], "€\n")
                    self.burgers.remove(self.burgers[0])
                    break
                case 2: 
                    print("Name: ", self.drinks[option - 1][0] + "\nStock: ", self.drinks[option - 1][1], "\nPrice: ", self.drinks[option - 1][2], "€\n")
                    self.drinks.remove(option - 1)
                    break
                case 3: 
                    print("Name: ", self.drinks[option - 1][0] + "\nStock: ", self.drinks[option - 1][1], "\nPrice: ", self.drinks[option - 1][2], "€\n")
                    self.potatoes.remove(option - 1)
                    break
        # Reset the variable
        self.choosedNum = 0

        # Ver si el usuario desea seguir actualizando o no
        while True:
            user = input("\nCONTINUE removing? y/n: ")
            if user == "y" or user == "Y":
                self.remove_item()
                break
            elif user == "n" or user == "N":
                self.pause()
                break
    
    def ubral_price(self):
        """
        Método encargado de buscar productos con un precio inferior al umbral introducido por el usuario. El usuario puede elegir entre buscar productos de tipo hamburguesa, bebida o patatas, a través del metodo exit_or_do.
        """
        print("""
                 _               _ 
 /\ /\ _ __ ___ | |__  _ __ __ _| |
/ / \ \ '_ ` _ \| '_ \| '__/ _` | |
\ \_/ / | | | | | |_) | | | (_| | |
 \___/|_| |_| |_|_.__/|_|  \__,_|_|
                                   
""")
        while self.exiting == False:
            self.exit_or_do("product", "REMOVE")

            #Resetear la variable y salir del bucle en caso de salir de este 
            if self.exiting == True:
                self.exiting = False
                break
            
            while self.exiting == False:
                try: 
                    user = input("Introduce the umbral price: ")

                    if float(user) > 0:
                        price = float(user)
                        break
                    else:
                        print("INVALID input, has to be a positive number.")
                except:
                    print("INVALID input, has to be a number.")
            
            print("\nProducts with a price lower than", price, "€:\n")
            text = [] #Texto para saber si existe algun producto con un precio menor al que ha introducido el usuario sino se mostarara otro error
            match self.choosedNum:
                case 1:
                    for burger in self.burgers:
                        if burger[2] < price:
                            text += {f"Name: {burger[0]} \nDisponible menus: {burger[1]} \nPrice: {burger[2]}€\n"} # Array de objetos de tipo texto para poder imprimirlos bien
                case 2:
                    for drink in self.drinks:
                        if drink[2] < price:
                            text += {f"Name: {drink[0]} \nDisponible menus: {drink[1]} \nPrice: {drink[2]}€\n"}
                case 3:
                    for potato in self.potatoes:
                        if potato[2] < price:
                            text += {f"Name: {drink[0]} \nDisponible menus: {drink[1]} \nPrice: {drink[2]}€\n"}
                    break
            
            #Comprobar si hay algo en el texto y sino que muestre un mensaje
            if len(text) == 0:
                print("NO products with a price lower than", price, "€.")
            else:
                for t in text:
                    print(t)

            # Reset the variable
            self.choosedNum = 0
            break

        # Ver si el usuario desea seguir actualizando o no
        while True:
            user = input("\nCONTINUE searching? y/n: ")
            if user == "y" or user == "Y":
                self.ubral_price()
                break
            elif user == "n" or user == "N":
                self.pause()
                break
    
    def estadistics_resume(self):
        """
        Método que utiliza otros métodos para mostrar estadísticas del inventario. El usuario puede elegir entre ver el total de productos, los productos más baratos y caros, o el valor total del inventario.
        A través de los métodos total_for_each, most_expensive, most_cheaper y total_inventory.
        """
        print("""\n
   __    _            _ _     _   _          
  /__\__| |_ __ _  __| (_)___| |_(_) ___ ___ 
 /_\/ __| __/ _` |/ _` | / __| __| |/ __/ __|
//__\__ \ || (_| | (_| | \__ \ |_| | (__\__ \\
\__/|___/\__\__,_|\__,_|_|___/\__|_|\___|___/
                                             """)

        while self.exiting == False:
            print("Type EXIT to go back to the menu:")
            print("1. Total products\n2. Most cheeper and most expensive\n3. Inventory value")
            while self.exiting == False:
                try:
                    user = input()

                    if user == "exit" or user == "EXIT":
                        self.exiting = True
                        break

                    if int(user) > 0 and int(user) <= 3:
                        choosedNum = int(user)
                        break
                    else:
                        print("INVALID input, has to be a number from 1 to 3 or type EXIT to go back to the menu.")
                except:
                    print("INVALID input, has to be a number from 1 to 3 or type EXIT to go back to the menu.")
            
            #Comprobacion si el usuario decide salir del programa y reiniciamos la variable
            if self.exiting == True:
                self.exiting = False
                break

            match choosedNum:
                case 1:
                    print("\nTOTAL PRODUCTS")
                    totalBurgers = self.total_for_each("burgers")
                    totalDrinks = self.total_for_each("drinks")
                    totalPotatoes = self.total_for_each("potatoes")
                    totalGeneral = totalBurgers + totalDrinks + totalPotatoes

                    print("Total burgers:", totalBurgers,"\nTotal drinks:", totalDrinks, "\nTotal potatoes:", totalPotatoes, "\nTotal general:", totalGeneral)
                    break
                case 2:
                    print("\nMOST CHEAPER AND MOST EXPENSIVE\n")
                    expensive = self.most_expensive() # Llamada a funcion que se encarga de encontrar el valor mas caro de los arrays de arriba
                    cheaper = self.most_cheaper(expensive) # Le pasa el valor mas caro para que pueda encontrar el valor mas barato

                    #Productos mas caros
                    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                    print("----- Most EXPENSIVE: products", expensive, "€ -----")
                    for burger in self.burgers:
                        if burger[2] == expensive:
                            print("Name: ", burger[0], "\nPrice: ", burger[2], "€\n")
                    for drink in self.drinks:
                        if drink[2] == expensive:
                            print("Name: ", drink[0], "\nPrice: ", drink[2], "€\n")
                    for potato in self.potatoes:
                        if potato[2] == expensive:
                            print("Name: ", potato[0], "\nPrice: ", potato[2], "€\n")
                    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                    #Productos mas barators
                    print("----- Most CHEAPER: products", cheaper, "€ -----")
                    for burger in self.burgers:
                        if burger[2] == cheaper:
                            print("Name: ", burger[0], "\nPrice: ", burger[2], "€\n") 
                    for drink in self.drinks:
                        if drink[2] == cheaper:
                            print("Name: ", drink[0], "\nPrice: ", drink[2], "€\n")
                    for potato in self.potatoes:
                        if potato[2] == cheaper:
                            print("Name: ", potato[0], "\nPrice: ", potato[2], "€\n")
                    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                    break
                case 3:
                    print("\nTOTAL INVENTORY VALUE")
                    total = self.total_inventory()
                    print("Total inventory value:", total, "€")
                    break
            
        # Ver si el usuario desea seguir actualizando o no
        while True:
            user = input("\nCONTINUE searching? y/n: ")
            if user == "y" or user == "Y":
                self.estadistics_resume()
                break
            elif user == "n" or user == "N":
                self.pause()
                break

    #Funcion encargada de dar todo el total del inventario
    def total_inventory(self):
        """
        Método que devuelve el valor total del inventario. Usado en el método estadistics_resume.
        """
        total = 0
        if len(self.burgers) > 0:
            for burger in self.burgers:
                total += burger[1] * burger[2]
        if len(self.drinks) > 0:
            for drink in self.drinks:
                total += drink[1] * drink[2]
        if len(self.potatoes) > 0:
            for potato in self.potatoes:
                total += potato[1] * potato[2]
        
        return total
    
    # Funcion encargada de sumar el total de cada producto, y no ensuciar la funcion estadistics_resume
    def total_for_each(self, item):
        """
        Método que devuelve el total de productos de un tipo concreto. Usado en el método estadistics_resume.
        """
        totalItem = 0
        if (item == "burgers"):
            for burger in self.burgers:
                totalItem += burger[1]
        elif (item == "drinks"):
            for drink in self.drinks:
                totalItem += drink[1]
        elif (item == "potatoes"):
            for potato in self.potatoes:
                totalItem += potato[1]
        
        return totalItem
    
    def most_expensive(self):
        """
        Método que devuelve el producto más caro del inventario. Usado en el método estadistics_resume.
        """
        # Comprobar si hay algo en el array de burgers, drinks y potatoes
        if len(self.burgers) > 0:
            expensive = self.burgers[0][2] # Recogemos el primer valor de burgeres para comparar
        elif len(self.drinks) > 0:
            expensive = self.drinks[0][2] 
        elif len(self.potatoes) > 0:
            expensive = self.potatoes[0][2] 

        # Comprobar si hay valores en el array y luego ver cual es el mas caro
        if len(self.burgers) > 0:
            for burger in self.burgers:
                if burger[2] > expensive:
                    expensive = burger[2]

        if len(self.drinks) > 0:
            for drink in self.drinks:
                if drink[2] > expensive:
                    expensive = drink[2]

        if len(self.potatoes) > 0:
            for potato in self.potatoes:
                if potato[2] > expensive:
                    expensive = potato[2]

        return expensive

    def most_cheaper(self, expensive):
        """
        Método que devuelve el producto más barato del inventario. Usado en el método estadistics_resume.
        """
        cheaper = expensive
        for burger in self.burgers:
            if burger[2] < cheaper:
                cheaper = burger[2]
        for drink in self.drinks:
            if drink[2] < cheaper:
                cheaper = drink[2]
        for potato in self.potatoes:
            if potato[2] < cheaper:
                cheaper = potato[2]
        
        return cheaper
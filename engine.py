class Engine:
    def __init__(self):
        self.inventory = [["La Clásica Emi", 100, 8],
                  ["La Emi Supreme", 200, 12],
                  ["La Emizilla", 400, 18],
                  ["La Emición Imposible", 800, 25],
                  ["Emi-tame Esta", 200, 12]]
        
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
        print("1. Show burgers inventory")
        print("2. Add burger")
        print("3. Remove burger")
        print("4. Search burger")
        print("5. Update burger")
        print("0. Exit")

    def run(self):
        while True:
            self.menu()
            user = input("Enter your choice: ")

            if user == "1":
                self.show_inventory()
            elif user == "2":
                self.add_burger()
            elif user == "3":
                self.remove_burger()
            elif user == "4":
                self.search_burger()
            elif user == "5":
                self.update_burger()
            elif user == "0":
                break
            else:
                print("Invalid choice")
                continue
    
    def show_inventory(self):
        print("""\n
______                             _____                     _                   
| ___ \                           |_   _|                   | |                  
| |_/ /_   _ _ __ __ _  ___ _ __    | | _ ____   _____ _ __ | |_ ___  _ __ _   _ 
| ___ \ | | | '__/ _` |/ _ \ '__|   | || '_ \ \ / / _ \ '_ \| __/ _ \| '__| | | |
| |_/ / |_| | | | (_| |  __/ |     _| || | | \ V /  __/ | | | || (_) | |  | |_| |
\____/ \__,_|_|  \__, |\___|_|     \___/_| |_|\_/ \___|_| |_|\__\___/|_|   \__, |
                  __/ |                                                     __/ |
                 |___/                                                     |___/ 
""")
        for burger in self.inventory:
            print("Name: ", burger[0] + "\nMeat: ", burger[1], "g", "\nPrice: ", burger[2], "€\n")
        
        self.pause()

    def add_burger(self):
        print("""\n  ___      _     _  ______                           
 / _ \    | |   | | | ___ \                          
/ /_\ \ __| | __| | | |_/ /_   _ _ __ __ _  ___ _ __ 
|  _  |/ _` |/ _` | | ___ \ | | | '__/ _` |/ _ \ '__|
| | | | (_| | (_| | | |_/ / |_| | | | (_| |  __/ |   
\_| |_/\__,_|\__,_| \____/ \__,_|_|  \__, |\___|_|   
                                      __/ |          
                                     |___/           """)
        while True:
            error = False
            burgerName = input("Introduce burger NAME: " )
            for burger in self.inventory:
                if burger[0] == burgerName:
                    error = True
                    print("Product already exist, please try again.")

            while error != True:
                try:
                    meat = int(input("\nIntroduce MEAT grams: "))
                    break
                except:
                    print("WRONG input in MEAT grams, it has to be a NUMBER without 'g'.")
            while error != True:
                try:
                    price = int(input("\nIntroduce burger PRICE: "))
                    break
                except:
                    print("WRONG input PRICE, it has to be a number.")
            if error == False:
                break
        
        self.inventory.append([burgerName, meat, price])
        print("\nSuccesful PRODUCT ADDED:\nName: ", burgerName, "\nMeat: ", meat, "g\nPrice: ", price, "€")
        
        while True:
            user = input("\nCONTINUE adding? y/n: ")
            if user == "y" or user == "Y":
                self.add_burger()
                break
            elif user == "n" or user == "N":
                self.pause()
                break

        

    def search_burger(self):
        print("""\n _____                     _     
/  ___|                   | |    
\ `--.  ___  __ _ _ __ ___| |__  
 `--. \/ _ \/ _` | '__/ __| '_ \ 
/\__/ /  __/ (_| | | | (__| | | |
\____/ \___|\__,_|_|  \___|_| |_|
                                 
                                 """)
        encontrado = False
        while encontrado == False:
            print("Type EXIT to go back to the menu:")
            burgerName = input("\nInput burger NAME: ")

            if user.lower == "exit":
                break
    
            for burger in self.inventory:
                if burger[0] == burgerName:
                    encontrado = True
                    print("\nSuccesful product FOUND:")
                    print("Name: ", burger[0] + "\nMeat: ", burger[1], "g", "\nPrice: ", burger[2], "€\n")
                    break
            if encontrado == False:
                print("Product NOT FOUND, please try again.\n")
        
        while True:
            user = input("\nCONTINUE searching? y/n: ")
            if user == "y" or user == "Y":
                self.search_burger()
                break
            elif user == "n" or user == "N":
                self.pause()
                break

    def update_burger(self):
        print("""\n _   _           _       _        ______                           
| | | |         | |     | |       | ___ \                          
| | | |_ __   __| | __ _| |_ ___  | |_/ /_   _ _ __ __ _  ___ _ __ 
| | | | '_ \ / _` |/ _` | __/ _ \ | ___ \ | | | '__/ _` |/ _ \ '__|
| |_| | |_) | (_| | (_| | ||  __/ | |_/ / |_| | | | (_| |  __/ |   
 \___/| .__/ \__,_|\__,_|\__\___| \____/ \__,_|_|  \__, |\___|_|   
      | |                                           __/ |          
      |_|                                          |___/           """)
    
        index = 0
        exiting = False
        while True:
            print("\nDISPONIBLE products: \n")
            for burger in self.inventory:
                index += 1
                print("Number ", index , ":")
                print("Name: ", burger[0] + "\nMeat: ", burger[1], "g", "\nPrice: ", burger[2], "€\n")

            print("Type EXIT to go back to the menu.")
            print("Select the burger you want to update from 1 at", index)

        self.pause()

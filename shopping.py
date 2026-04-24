import random
import sklep as yes
import sklepikarz as sklepowy
class actions:
    def __init__(self):
        self.actions = ['add_product', 'generate_shopper', 'generate whole shop', 'exit']
        self.shop = yes.shop()
        self.shopkeeper = sklepowy.shopkeeper()
        
    def choose_action(self):
        addon = 0
        print("Available actions:")
        for i, action in enumerate(self.actions, start=1):
            print(f"{i}. {action}")
            addon +=1
        choice = input(f"Choose an action (1-{addon}): ")
        return choice
    def generate_shop(self):
        shop_data = {}
        # Open file first before reading
        self.shop.open_file("lista.txt")
        master = self.shopkeeper.generate_data() 
        productlist = random.sample(self.shop.read_lines(), random.randint(1, len(self.shop.lines)))
        for product in productlist:
            shop_data[product] = {"price": random.randint(1, 100)}
        shop_data[len(shop_data) + 1] = master
        return shop_data
    def perform_action(self, choice):
        if choice == '1':
            product = input("Enter the name of the product to add: ")
            self.shop.dopisuj_do_pliku("lista.txt", product)
        elif choice == '2':
            data = self.shopkeeper.generate_data()
            self.shopkeeper.dopisz_do_pliku("shoppers.txt", data)
        elif choice == '3':
            shop_data = self.generate_shop()
            print("Generated shop:", shop_data)
        elif choice == '4':
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please try again.")
        
app = actions()
while True:
    user_choice = app.choose_action()
    app.perform_action(user_choice)

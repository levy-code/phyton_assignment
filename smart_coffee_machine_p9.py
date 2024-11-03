class KitchenAppliance:
    def __init__(self, model_number, brand):
        self.model_number = model_number
        self.brand = brand

    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)

class SmartCoffeeMachine(KitchenAppliance):
    def __init__(self, model_number, brand, coffee_menu=['latte', 'cappuccino', 'flat white']):
        KitchenAppliance.__init__(self, model_number, brand)
        self.coffee_menu = coffee_menu

    def update_menu(self, new_coffee):
        if new_coffee not in self.coffee_menu:
            self.coffee_menu.append(new_coffee)
            print(f"{new_coffee} has been added to the menu.")
        else:
            print(f"{new_coffee} is already in the menu.")

    def make_coffee(self, coffee_type):
        if coffee_type in self.coffee_menu:
            print(f"Making your {coffee_type}!")
        else:
            print(f"Sorry, {coffee_type} is not in the menu.")
            print("Available options:", ', '.join(self.coffee_menu))


my_coffee_machine = SmartCoffeeMachine(101395, 'Les')
my_coffee_machine.report()

my_coffee_machine.update_menu('latte')
my_coffee_machine.update_menu('hazelnut latte')

my_coffee_machine.make_coffee('hazelnut latte')
my_coffee_machine.make_coffee('salted caramel latte')

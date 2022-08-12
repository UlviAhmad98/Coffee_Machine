class CoffeeMachine:
    resource = {"water": 400, "milk": 540, "beans": 120, "cups": 9, "money": 550}
    latte_ing = {"water": 350, "milk": 75, "beans": 20, "cups": 1, "money": 7}
    espresso_ing = {"water": 250, "milk": 0, "beans": 16, "cups": 1, "money": 4}
    cappuccino_ing = {"water": 200, "milk": 100, "beans": 12, "cups": 1, "money": 6}

    def __init__(self):
        self.option = None
        self.order = None
        self.add_water = None
        self.add_milk = None
        self.add_beans = None
        self.add_cups = None

    def make_coffee(self, latte_ing):
        self.resource['water'] -= latte_ing['water']
        self.resource['milk'] -= latte_ing['milk']
        self.resource['beans'] -= latte_ing['beans']
        self.resource['cups'] -= latte_ing["cups"]
        self.resource['money'] += latte_ing['money']
        print("I have enough resources, making you a coffee!")

    def check_resources(self, latte_ing):
        for key in self.resource.keys():
            if self.resource[key] < latte_ing[key]:
                print(f"Sorry, not enough {key}!")
                return False
        return True

    def remaining(self):
        print("The coffee machine has:")
        print(f"{self.resource['water']} ml of water")
        print(f"{self.resource['milk']} ml of milk")
        print(f"{self.resource['beans']} g of coffee beans")
        print(f"{self.resource['cups']} disposable cups")
        print(f"${self.resource['money']} of money")

    def espresso(self):
        if not self.check_resources(self.espresso_ing):
            return
        self.make_coffee(self.espresso_ing)

    def latte(self):
        if not self.check_resources(self.latte_ing):
            return
        self.make_coffee(self.latte_ing)

    def cappuccino(self):
        if not self.check_resources(self.cappuccino_ing):
            return
        self.make_coffee(self.cappuccino_ing)

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        self.order = input()
        if self.order == "1":
            return self.espresso()
        elif self.order == "2":
            return self.latte()
        elif self.order == "3":
            return self.cappuccino()
        elif self.order == "back":
            return

    def fill(self):
        print("Write how many ml of water you want to add:")
        self.add_water = int(input())
        print("Write how many ml of milk you want to add:")
        self.add_milk = int(input())
        print("Write how many grams of coffee beans you want to add:")
        self.add_beans = int(input())
        print("Write how many disposable cups of coffee you want to add:")
        self.add_cups = int(input())

        self.resource['water'] += self.add_water
        self.resource['milk'] += self.add_milk
        self.resource['beans'] += self.add_beans
        self.resource['cups'] += self.add_cups

    def take(self):
        print(f"I gave you ${self.resource['money']}")
        self.resource['money'] = 0

    def action(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            self.option = input()
            if self.option == "buy":
                self.buy()
            elif self.option == "fill":
                self.fill()
            elif self.option == "take":
                self.take()
            elif self.option == "remaining":
                self.remaining()
            elif self.option == "exit":
                break
            print()


coffee_machine = CoffeeMachine()
coffee_machine.action()

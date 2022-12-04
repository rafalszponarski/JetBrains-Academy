class CoffeeMachine:
    def __init__(self):
        self.supplies = {'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'money': 550}
        self.coffee = {
            '1': {'water': 250, 'milk': 0, 'beans': 16, 'cost': 4},
            '2': {'water': 350, 'milk': 75, 'beans': 20, 'cost': 7},
            '3': {'water': 200, 'milk': 100, 'beans': 12, 'cost': 6}
        }

    def start(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):")

            if action == 'buy':
                option = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
                if option in ['1', '2', '3']:

                    if self.supplies['water'] >= self.coffee[option]['water'] \
                            and self.supplies['milk'] >= self.coffee[option]['milk'] \
                            and self.supplies['beans'] >= self.coffee[option]['beans'] \
                            and self.supplies['money'] >= self.coffee[option]['cost'] \
                            and self.supplies['cups'] >= 1:

                        print("I have enough resources, making you a coffee!")
                        self.supplies['water'] -= self.coffee[option]['water']
                        self.supplies['milk'] -= self.coffee[option]['milk']
                        self.supplies['beans'] -= self.coffee[option]['beans']
                        self.supplies['money'] += self.coffee[option]['cost']
                        self.supplies['cups'] -= 1
                    else:
                        print("Sorry, not enough resources!")

            elif action == 'fill':
                self.supplies['water'] += int(input("Write how many ml of water you want to add:"))
                self.supplies['milk'] += int(input("Write how many ml of milk you want to add:"))
                self.supplies['beans'] += int(input("Write how many grams of coffee beans you want to add:"))
                self.supplies['cups'] += int(input("Write how many disposable cups you want to add:"))

            elif action == 'take':
                print(f"I gave you ${self.supplies['money']}")
                self.supplies['money'] = 0

            elif action == 'remaining':
                print("The coffee machine has:")
                print(f"{self.supplies['water']} ml of water")
                print(f"{self.supplies['milk']} ml of milk")
                print(f"{self.supplies['beans']} g of coffee beans")
                print(f"{self.supplies['cups']} disposable cups")
                print(f"${self.supplies['money']} of money")

            elif action == 'exit':
                break


if __name__ == "__main__":
    CoffeeMachine().start()

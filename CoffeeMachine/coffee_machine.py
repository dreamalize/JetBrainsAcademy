class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550
        self.stock = [["water", self.water],
                      ["milk", self.milk],
                      ["coffee_beans", self.coffee],
                      ["disposable cups", self.cups]]

    def __repr__(self):
        return f"{self.water}, {self.milk}"

    def current_state(self):
        return self.state

    def take_money(self):
        print("I gave you ${}". format(self.money))
        self.money -= self.money

    def fill(self):
        filling = []
        print()
        print("Write how many ml of water do you want to add:")
        filling.append(int(input()))

        print("Write how many ml of milk do you want to add:")
        filling.append(int(input()))

        print("Write how many grams of coffee beans do you want to add:")
        filling.append(int(input()))

        print("Write how many disposable cups of coffee do you want to add:")
        filling.append(int(input()))
        print()

        for x in range(len(self.stock)):
            self.stock[x][1] += filling[x]

    def status(self):
        print()
        print("The coffee machine has:")
        for x in self.stock:
            print(f"{x[1]} of {x[0]}")
        print(f"${self.money} of money")
        print()

    def action(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            user_input = input()
            self.state = user_input
            if self.current_state() == "buy":
                self.buy()
            elif self.current_state() == "remaining":
                self.status()
            elif self.current_state() == "fill":
                self.fill()
            elif self.current_state() == "take":
                self.take_money()
            elif self.current_state() == "exit":
                break
            else:
                continue

    def out_of_stock(self, ingredients):
        out_ = []
        for x in range(len(self.stock)):
            self.stock[x][1] -= ingredients[x][1]
            if self.stock[x][1] < 0:
                out_.append(ingredients[x][0])
            if len(out_) != 0:
                self.stock[x][1] += ingredients[x][1]
        return out_

    def response(self, check, coffee_type):
        if len(check) > 0:
            print("Sorry, not enough {}!".format("".join(check)))
            print()
        else:
            print("I have enough resources, making you a coffee!")
            print()
            if coffee_type == "1":
                self.money += 4
            elif coffee_type == "2":
                self.money += 7
            elif coffee_type == "3":
                self.money += 6

    def making_coffee(self, coffee_type):
        if coffee_type == "1":
            ingredients = [["water", 250],
                           ["milk", 0],
                           ["coffee beans", 16],
                           ["disposable cups", 1]]
            check = self.out_of_stock(ingredients)
            self.response(check, coffee_type)

        elif coffee_type == "2":
            ingredients = [["water", 350],
                           ["milk", 75],
                           ["coffee beans", 20],
                           ["disposable cups", 1]]
            check = self.out_of_stock(ingredients)
            self.response(check, coffee_type)

        elif coffee_type == "3":
            ingredients = [["water", 200],
                           ["milk", 100],
                           ["coffee beans", 12],
                           ["disposable cups", 1]]
            check = self.out_of_stock(ingredients)
            self.response(check, coffee_type)

        elif coffee_type == "back":
            pass

    def buy(self):
        print()
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        buy_input = input()
        self.making_coffee(buy_input)


coffee_machine = CoffeeMachine()
coffee_machine.action()

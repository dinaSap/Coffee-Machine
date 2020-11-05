class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def print_state(self):
        print('The coffee machine has:')
        print(self.water, 'of water')
        print(self.milk, 'of milk')
        print(self.beans, 'of coffee beans')
        print(self.cups, 'of disposable cups')
        print(self.money, 'of money')

    def espresso(self):
        if self.water // 250 and self.beans // 16 and self.cups // 1:
            print('I have enough resources, making you a coffee!')
            self.water -= 250
            self.beans -= 16
            self.money += 4
            self.cups -= 1
        else:
            if not self.water // 250:
                print('Sorry, not enough water!')
            elif not self.beans // 16:
                print('Sorry, not enough coffee beans!')
            else:
                print('Sorry, not enough cups!')

    def latte(self):
        if self.water // 350 and self.beans // 20 and self.milk // 75 and self.cups // 1:
            print('I have enough resources, making you a coffee!')
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.money += 7
            self.cups -= 1
        else:
            if not self.water // 350:
                print('Sorry, not enough water!')
            elif not self.beans // 20:
                print('Sorry, not enough coffee beans!')
            elif not self.milk // 75:
                print('Sorry, not enough milk!')
            else:
                print('Sorry, not enough cups!')

    def cappuccino(self):
        if self.water // 200 and self.beans // 12 and self.milk // 100 and self.cups // 1:
            print('I have enough resources, making you a coffee!')
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.money += 6
            self.cups -= 1
        else:
            if not self.water // 200:
                print('Sorry, not enough water!')
            elif not self.beans // 12:
                print('Sorry, not enough coffee beans!')
            elif not self.milk // 100:
                print('Sorry, not enough milk!')
            else:
                print('Sorry, not enough cups!')

    def buy(self):
        num = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        if num == '1':
            self.espresso()
        elif num == '2':
            self.latte()
        elif num == '3':
            self.cappuccino()

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:'))
        self.milk += int(input('Write how many ml of milk do you want to add:'))
        self.beans += int(input('Write how many grams of coffee beans do you want to add:'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:'))

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def operate(self):
        while True:
            user_input = input('Write action (buy, fill, take, remaining, exit):')
            if user_input == 'exit':
                break
            elif user_input == 'buy':
                self.buy()
            elif user_input == 'fill':
                self.fill()
            elif user_input == 'take':
                self.take()
            elif user_input == 'remaining':
                self.print_state()
            else:
                break
new_machine = CoffeeMachine()
new_machine.operate()

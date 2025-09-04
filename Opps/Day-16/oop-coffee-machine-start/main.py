from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
cofee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    print(options)
    input_user = input(f"What whould you like?({options}):").lower()
    if input_user == 'off':
        is_on = False
    elif input_user == 'report':
        cofee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(input_user)
        if drink and cofee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                cofee_maker.make_coffee(drink)
            
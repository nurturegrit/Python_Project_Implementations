from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys


def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    while True:
        order = input(f"What would you like? ({menu.get_items()})").strip().lower()
        if order == 'off':
            sys.exit("The Coffee Machine is turning off....")
        elif order == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(order)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)


main()
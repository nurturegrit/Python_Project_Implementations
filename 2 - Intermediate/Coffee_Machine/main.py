from machine_resources import MENU, resources
import sys


def insert_coins():
    quarter = int(input("How many quarters do you want to insert?"))
    dimes = int(input("How many dimes do you want to insert?"))
    nickels = int(input("How many nickels do you want to insert?"))
    pennies = int(input("How many pennies do you want to insert?"))
    payment = ((quarter * 25) + (dimes * 10) + (nickels * 5) + (pennies * 1))/100
    return round(payment, 2)


def make_drink(drink):
    for key, value in MENU[drink]['ingredients'].items():
        resources[key] -= value
    print(f"Your {drink} is ready!")
    return


def order():
    while True:
        print("What would you like? (espresso/latte/cappuccino)")
        choice = input().lower()
        available = True
        not_available = ''
        match choice:
            case 'report':
                choice = None
                for category, value in resources.items():
                    if category == 'money':
                        print(f"Money : ${value:.2f}")
                    else:
                        print(category.title(), ':', value)
            case 'off':
                sys.exit("Machine Turns Off")
            case _:
                if choice in MENU.keys():
                    for key, value in MENU[choice]['ingredients'].items():
                        if resources[key] - value < 0:
                            available = False
                            not_available += key + ' '
                else:
                    print("Enter A Valid Input.")
                    return
        if available and choice:
            payment = insert_coins()
            if payment < MENU[choice]['cost']:
                print("Insert Enough Money!")
                print("Money Refunded!")
            else:
                make_drink(choice)
                refund = payment - MENU[choice]['cost']
                print(f"Here is your refund of ${round(refund,2)}")
                resources['money'] += MENU[choice]['cost']
        elif choice:
            print(f"There is not enough {not_available.strip().replace(' ',', ')} to make your {choice}!")
        continue


def main():
    order()


if __name__ == '__main__':
    order()

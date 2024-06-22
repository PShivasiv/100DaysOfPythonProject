from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    order = menu.get_items()
    order_name = input(f"What would you like to drink? {order}: ")
    if order_name == "off":
        print("Sorry the machine is out of resources please come after some time!")
        is_on = False
    elif order_name == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order_name)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)

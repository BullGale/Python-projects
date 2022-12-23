from random import choices


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ing):
    for item in order_ing:
        if order_ing[item] >= resources[item]:
            print(f"Sorry not enough {item}.")  
            return False 
    return True     


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quaters?:")) * 0.25 
    total += int(input("how many dimes?:")) * 0.1 
    total += int(input("how many nickles?:")) * 0.05 
    total += int(input("how many pennies?:")) * 0.01
    return total 


def transction_success(money_recieve, drink_cost):
    if money_recieve >= drink_cost:
        change = round(money_recieve - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry thats not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True
while is_on:
    choice = input("What whould you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transction_success(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
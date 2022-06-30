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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
another_coffee = True
def PrintResources():
    print(f"Coffee left: {resources['coffee']}")
    print(f"Water left: {resources['water']}")
    print(f"Milk left: {resources['milk']}")


while another_coffee == True:
    user_input = input('Would you like to order espresso, latte, or cappuccino?').lower()
    if user_input == 'espresso':
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        PrintResources()
    if user_input == "latte":
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["latte"]["ingredients"]["millk"]
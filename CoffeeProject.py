import os
from tkinter import Menu
import time

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
latte_count = 0
cappuccino_count = 0
espresso_count = 0

def PrintResources():
    print(f"Coffee left: {resources['coffee']}")
    print(f"Water left: {resources['water']}")
    print(f"Milk left: {resources['milk']}")


def MakeDrink(drink_type):
    
    enough_resources = True
    if resources["water"] - MENU[drink_type]["ingredients"]["water"] < 0:
        print("Not enought water")
        enough_resources = False
    if resources["coffee"] - MENU[drink_type]["ingredients"]["coffee"] < 0:
        print("Not enough coffee")
        enough_resources = False
    if "milk" in MENU[drink_type]:
        if resources["milk"] - MENU[drink_type]["ingredients"]["milk"] < 0:
            print("Not enough milk")
            enough_resources = False
    if enough_resources == True:
        resources["coffee"] -= MENU[drink_type]["ingredients"]["coffee"]
        resources["water"] -= MENU[drink_type]["ingredients"]["water"]
        resources["milk"] -= MENU[drink_type]["ingredients"]["milk"]


    return enough_resources



while another_coffee == True:
    os.system('cls')
    drink_choice = input("Would you like a latte, cappuccino, or espresso? ").lower()
    if drink_choice == "latte" or drink_choice == "espresso" or drink_choice == "cappuccino":
        if MakeDrink(drink_choice) == True:
            if drink_choice == "latte":
                latte_count += 1
            elif drink_choice == "espresso":
                espresso_count += 1
            elif drink_choice == "cappuccino":
                cappuccino_count += 1
        print()
        PrintResources()
        print()
        print(f"Cart: \n Lattes: {latte_count} \n Cappuccinos: {cappuccino_count} \n Espressos: {espresso_count} \n")
        another_coffee_input = input("Would you like to make another drink? y or n: ").lower()
        if(another_coffee_input == "n"):
            another_coffee = False
    else:
        print("INVALID INPUT")
        time.sleep(1)
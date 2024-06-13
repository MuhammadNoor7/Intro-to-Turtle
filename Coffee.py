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

def print_report():
    """Prints a report of the current resources."""
    print("Resources:")
    for key, value in resources.items():
        print(f"{key.capitalize()}: {value}ml" if key != "coffee" else f"{key.capitalize()}: {value}g")

def check_resources(drink):
    """Checks if there are enough resources to make the drink."""
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Processes the coins inserted by the user and returns the total amount."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def make_coffee(drink):
    """Deducts the required resources to make the coffee."""
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}. Enjoy!")

def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            break
        elif choice == "report":
            print_report()
        elif choice in MENU:
            if check_resources(choice):
                payment = process_coins()
                if payment >= MENU[choice]["cost"]:
                    change = round(payment - MENU[choice]["cost"], 2)
                    print(f"Here is ${change} in change.")
                    make_coffee(choice)
                else:
                    print("Sorry, that's not enough money. Money refunded.")
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    coffee_machine()
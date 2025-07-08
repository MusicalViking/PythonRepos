"""
Author: Arthur Belanger
Program: Tax and Tip
Description: The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.
Notes:
"""

import time
divider = ("---")

# menu_ordering_improved.py

meals = {
    'Chicken Salad': 12.75,
    'Pasta': 12.75,
    'Turkey': 12.75,
    'Steak': 12.75,
    'Hamburger': 12.75
}

sides = {
    'Breadsticks': 6.25,
    'Fries': 6.25,
    'Corn': 6.25,
    'Cheese Sticks': 6.25
}

drinks = {
    'Water': 3.75,
    'Soda': 3.75,
    'Wine': 3.75,
    'Beer': 3.75
}

def getSelection(categoryName, items):
    print(f"\n{categoryName} Options:")
    itemList = list(items.items())
    for i, (item, price) in enumerate(itemList, start=1):
        print(f"{i}. {item} - ${price:.2f}")

    selection = input(f"Enter the numbers of the {categoryName.lower()} you want (comma separated): ")
    selectedItems = []

    for choice in selection.split(','):
        choice = choice.strip()
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(itemList):
                selectedItems.append(itemList[index])
            else:
                print(f"Invalid selection: {choice} (out of range)")
        else:
            print(f"Invalid input: '{choice}' is not a number")

    return selectedItems

def printSummary(title, items):
    if items:
        print(f"{title}:")
        for name, _ in items:
            print(f"- {name}")
    else:
        print(f"No {title.lower()} selected.")

def calculateTotal(items):
    return sum(price for _, price in items)

def saveOrderToFile(meals, sides, drinks, total):
    with open("orderSummary.txt", "w") as f:
        f.write("=== ORDER SUMMARY ===\n")
        for title, items in [("Meals", meals), ("Sides", sides), ("Drinks", drinks)]:
            f.write(f"{title}:\n")
            if items:
                for name, _ in items:
                    f.write(f"- {name}\n")
            else:
                f.write("None selected.\n")
        f.write(f"\nTotal cost: ${total:.2f}\n")
    print("Order summary saved to 'orderSummary.txt'.")

def main():
    print("WELCOME TO THE MENU ORDERING SYSTEM")

    chosenMeals = getSelection("Meals", meals)
    chosenSides = getSelection("Sides", sides)
    chosenDrinks = getSelection("Drinks", drinks)

    total = (
        calculateTotal(chosenMeals) +
        calculateTotal(chosenSides) +
        calculateTotal(chosenDrinks)
    )

    print("\n=== ORDER SUMMARY ===")
    printSummary("Meals", chosenMeals)
    printSummary("Sides", chosenSides)
    printSummary("Drinks", chosenDrinks)
    print(f"\nTotal cost: ${total:.2f}")

    save = input("\nWould you like to save your order summary to a file? (y/n): ").strip().lower()
    if save == 'y':
        saveOrderToFile(chosenMeals, chosenSides, chosenDrinks, total)

if __name__ == '__main__':
    main()



print("Arthur Belanger")
print(time.ctime())
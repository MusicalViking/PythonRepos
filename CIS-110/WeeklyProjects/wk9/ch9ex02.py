"""
List Input Program
This program allows the user to create a list by specifying how many items they want to add
and then entering each item one by one.
Author: Arthur Belanger
Date created: 2025-04-04

Notes:
- The program asks the user how many items they want to add to the list
- The user then enters each item one by one
- The program displays the final list
"""
print("--------------------------------")
import time

def create_list_from_input():
    # Ask the user how many items they want to add to the list
    while True:
        try:
            num_items = int(input("How many items do you want to add to the list? "))
            if num_items <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Create an empty list
    user_list = []
    
    # Get each item from the user
    for i in range(num_items):
        item = input(f"Enter item {i+1}: ")
        
        # Try to convert to int or float if possible
        try:
            # Try to convert to int first
            item = int(item)
        except ValueError:
            # If not an int, try to convert to float
            try:
                item = float(item)
            except ValueError:
                # If not a number, keep it as a string
                pass
        
        # Add the item to the list
        user_list.append(item)
    
    return user_list

# Main program
print("Welcome to the List Creator!")

# Check if we should run in demo mode
import sys
if len(sys.argv) > 1 and sys.argv[1] == "demo":
    # Demo mode with default values
    print("Running in demo mode with default values")
    num_items = 4
    print(f"Number of items to add: {num_items}")
    
    # Create a demo list
    my_list = []
    demo_items = [10, 20, "hello", 3.14]
    
    for i, item in enumerate(demo_items):
        print(f"Item {i+1}: {item}")
        my_list.append(item)
        
    print("\nYour list contains the following items:")
    print(my_list)
    print(f"Number of items in the list: {len(my_list)}")
else:
    # Interactive mode
    my_list = create_list_from_input()
    
    # Display the list
    print("\nYour list contains the following items:")
    print(my_list)
    print(f"Number of items in the list: {len(my_list)}")

print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - Program # ")
print(time.ctime())

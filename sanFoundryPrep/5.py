"""
Program Name
Program description
Author: Arthur Belanger
Date created: 
Notes:Write a Python Program to reverse a given number.
"""

import time
divider = ("_ _ _ ")
print(divider * 3)

def main():
    num = input("Please enter a number to reverse: ").strip()
    
    if not num.lstrip('-').isdigit():
        print("Invalid input. Please enter a valid integer.")
        return

    reversed_num = num[::-1] if num[0] != '-' else '-' + num[:0:-1]
    print(f"Reversed number: {reversed_num}")

if __name__ == '__main__':
    main()






print(divider * 3)
print("Arthur Belanger")
print(time.ctime())
    
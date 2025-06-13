"""
Program Name
Program description:
Author: Arthur Belanger
Date created:6-2-25
Notes:Write program that takes a number and checks whether it is positive or negative
"""

import time

divider = "_ _ _ "
print(divider * 3)

def main():
    n = float(input("What is the number you are checking? "))
    if n > 0:
        print(f"{n} is a positive number.")
    else:
        print(f"{n} is a negative number")

if __name__ == "__main__":
    main()

print(divider * 3)
print("Arthur Belanger")
print(time.ctime())
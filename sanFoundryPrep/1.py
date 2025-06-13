"""
Program Name
Program description: Write a Python Program to check whether a given number is even or odd
Author: Arthur Belanger
Date created: 6-2-25
Notes:
"""

import time

divider = "_ _ _ "
print(divider * 3)


def main():
    n = int(input("What is the number you want to figure? "))
    if n % 2 == 0:
        print(f"{n} is even number")
    else:
        print(f"{n} is odd number")


if __name__ == '__main__':
    main()


print(divider * 3)
print("Arthur Belanger")
print(time.ctime())
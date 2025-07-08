"""
Program Name
Program description
Author: Arthur Belanger
Date created: 
Notes:This is a Python Program to print all numbers in a range divisible by a given number.

Problem Description
The program prints all numbers in a range divisible by a given number.

Problem Solution
1. Take in the upper range and lower range limit from the user.
2. Take in the number to be divided by from the user.
3. Using a for loop, print all the factors which is divisible by the number.
4. Exit.
"""

import time
divider = ("_ _ _ ")
print(divider * 3)

upperRange = input("Upper range: ")
lowerRange = input("Lower range: ")
num = input("What is the number you want to be divided: ")


def main():
    for x in range(lowerRange, upperRange):
        if num % x == 0:
            print(num)



if __name__ == '__main__':
    main()






print(divider * 3)
print("Arthur Belanger")
print(time.ctime())
    
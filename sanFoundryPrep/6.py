"""
Program Name
Program description
Author: Arthur Belanger
Date created: 
Notes:his is a Python Program to print all integers that aren't divisible by either 2 or 3 and lies between 1 and 50.

Problem Description
The program prints all integers that aren't divisible by either 2 or 3 and lies between 1 and 50.

Problem Solution
1. Use a for-loop ranging from 0 to 51.
2. Then use an if statement to check if the number isn't divisible by both 2 and 3.
3. Print the numbers satisfying the condition.
4. Exit.
"""

import time
divider = ("_ _ _ ")
print(divider * 3)

def main():
    num = 0
    for num in range(51):
        num = num + 1
        if num % 2 != 0 and num % 3 != 0:
            print(num)

if __name__ == '__main__':
    main()


print(divider * 3)
print("Arthur Belanger")
print(time.ctime())
    
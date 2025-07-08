"""
Program Name
Program description
Author: Arthur Belanger
Date created: 
Notes:This is a Python Program to find those numbers which are divisible by 7 
and multiple of 5 in a given range of numbers.

Problem Description
The program takes an upper range and lower range and finds those numbers within 
the range which are divisible by 7 and multiple of 5.

Problem Solution
1. Take in the upper and lower range and store it in separate variables.
2. Use a for loop which ranges from the lower range to the upper range.
3. Then find the numbers which are divisible by both 5 and 7.
4. Print those numbers
5. Exit.
"""

import time
divider = ("_ _ _ ")
print(divider * 3)

upperRange = 150
lowerRange = 0


def main():
    for x in range(lowerRange, upperRange, 7):
        if x % 5 == 0:
                print(x)




if __name__ == '__main__':
    main()






print(divider * 3)
print("Arthur Belanger")
print(time.ctime())
    
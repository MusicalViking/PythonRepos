"""
Program Name
Program description: Write program that takes the upper and lower limit and prints all odd numbers within a given range.
Author: Arthur Belanger
Date created: 6-3-25
Notes:
"""

import time

divider = "_ _ _ "
print(divider * 3)

lower = int(input("What is the lower number? "))
upper = int(input("What is the upper number? "))

def main():
	for num in range(lower + 1, upper):
		if num % 2 != 0:
			print(num)


if __name__ == '__main__':
	main()


print(divider * 3)
print("Arthur Belanger")
print(time.ctime())
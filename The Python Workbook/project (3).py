"""
Author: Arthur Belanger
Program: Area of a field
Description: Create a program that reads the length and width of a farmers field 
from the user in feet. Display the area of the field in acres.
Notes: There are 43,560 square feet in an acre.
"""

import time
divider = ("---")
def main():
	width = float(input("What is the width of the field? "))
	length = float(input("What is the length of the field? "))
	sqFeet = width * length
	acres = sqFeet / 43560
	print(f"The total acreage for the farm is {acres:.2f} acres.")


if __name__ == '__main__':
	main()


print("Arthur Belanger")
print(time.ctime())
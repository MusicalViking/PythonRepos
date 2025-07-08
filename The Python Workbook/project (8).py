"""
Author: Arthur Belanger
Program: Area of a room
Description: Write a program that asks the user to enter the width and length of a room.
Once the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.
Notes:
"""

import time
divider = ("---")
def main():
	width = float(input("Enter the width of the room in meters: "))
	length = float(input("Enter the length of the room in meters: "))
	area = width * length
	print(f"The area of the room is: {area} square meters.")



if __name__ == '__main__':
	main()


print("Arthur Belanger")
print(time.ctime())
"""
Author: Arthur Belanger
Program: Hello
Description: Write a program that asks the user to enter his or her name. 
The program should respond with a message that says hello to the user, 
using his or her name.
Notes:
"""

import time
divider = ("---")

def main():
	name = input("What is your preferred name? ")
	greeting = f"Hello {name}, it is nice to have you here today."
	print(greeting)


if __name__ == '__main__':
	main()


print("Arthur Belanger")
print(time.ctime())
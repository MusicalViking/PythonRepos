"""
Program Name: Program #6
Program description: Convert ASCII code to a readable string
Author: Arthur Belanger
Date created: 3-31-25
Notes:

"""
print("--------------------------------")
import time

def decode_poem(filename="poem.txt"):
    try:
        with open(filename, 'r') as file:
            numbers_str = file.read().split()

            for num_str in numbers_str:
                try:
                    num = int(num_str)
                    char = chr(num)
                    print(char, end='')
                except ValueError:
                    print(f"Invalid number in file: {num_str}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
decode_poem()

print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - Program #6 ")
print(time.ctime())
    


"""
Program Name : ch8ex04
Program description : converts the letters in your name to numbers, then sum.
Author: Arthur Belanger
Date created: 3-27-25
Notes: figuring out the if function was fun on this one.

"""
print("--------------------------------")
import time

def calc_name_val(name):
 
  name = name.lower()
  total_val = 0
  for char in name:
    if  'a' <= char <= 'z':
      total_val += ord(char) - ord('a') + 1
  return total_val

name = input("Enter a name: ")

name_val = calc_name_val(name)
print(f"The value of '{name}' is: {name_val}")

print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - ch8ex04")
print(time.ctime())
    


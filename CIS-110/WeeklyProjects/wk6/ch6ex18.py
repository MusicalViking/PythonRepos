"""
Program Name : ch6ex18
Program description: gives a Invalid Input message if an error occurs
Author: Arthur Belanger
Date created: 3-6-25
Notes: 
"""
print("--------------------------------")
import time
import math

def triArea(a, b, c):
    try:
        s = (a + b + c) / 2   
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return round(area, 2)

    except ValueError:
        return "Invalid Input"

def main():
    try:
        a = float(input("Enter the length of the first side: "))
        b = float(input("Enter the length of the second side: "))
        c = float(input("Enter the length of the third side: "))
        
        area = triArea(a, b, c)
        if area == "Invalid Input":
            print("Invalid Input")
        else:
            print(f"Area of the triangle: {area}")

    except ValueError:
        print("Invalid Input")

if __name__ == '__main__':
    main()

print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - ch6ex18 ")
print(time.ctime())
    


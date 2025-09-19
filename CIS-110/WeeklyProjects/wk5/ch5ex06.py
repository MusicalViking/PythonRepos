"""
Program Name: ch5ex06
Program description : Finds the area of a triangle
Author: Arthur Belanger
Date created: 2-27-25

Notes:

"""
print("--------------------------------")
import time
import math

def triArea():
    a = float(input("What's the length of the first side: "))
    b = float(input("What's the length of the second side: "))
    c = float(input("What's the length of the third side: "))
    
    s = (a + b + c) / 2   
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    print(f"Area of the triangle : {round(area,2)}")
triArea()

print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - ch5ex06 ")
print(time.ctime())
    


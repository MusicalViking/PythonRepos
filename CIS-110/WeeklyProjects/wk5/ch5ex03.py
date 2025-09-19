"""
Program Name: ch5ex03
Program description: Find the area and volume of a circle
Author: Arthur Belanger
Date created: 2-27-25

Notes:

"""
print("--------------------------------")
import time
import math

def sphereArea(radius):
    return 4 * math.pi * radius ** 2

def sphereVolume(radius):
    return (4 / 3) * math.pi * radius ** 3

radius = float(input("What is the radius? "))
print(f"With a radius of {radius} the surface area is: {round(sphereArea(radius), 2)}")
print(f"With a radius of {radius} the volume of a sphere is: {round(sphereVolume(radius), 2)}")

print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - ch5ex03 ")
print(time.ctime())
    


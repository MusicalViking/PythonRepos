"""
Program Name : ch12ex13
Program description : program to calculate the surface area and volume of a sphere
Author: Arthur Belanger
Date created: 4-23-25
Notes: I kept it simple and just followed with you in the videos, I was running behind and this week did all 
the projects along with the lesson in class.
"""
import time
import math

divider = ("_ _ _ ")
print(divider * 3)

class Sphere():
    def __init__(self, radius):
        self._radius = radius

    def getRadius(self):
        return self._radius

    def surfaceArea(self):
        return 4 * math.pi * self._radius ** 2

    def volume(self):
        return (4.0 / 3.0) * math.pi * self._radius ** 3

def main():
    print("This finds the volume and surface area of a sphere from input radius. \n")
    r = float(input("Please enter the radius of sphere: "))
    mySphere = Sphere(r)
    print(f'The surface area is: {mySphere.surfaceArea() :0.2f} square units')
    print(f'The volume is: {mySphere.volume() :0.2f} cubic units')

if __name__ == '__main__':
    main()



print(divider * 3)
print("Arthur Belanger")
print("CIS-110 - Program #ch12ex13 ")
print(time.ctime())
"""
ch4ex02
Bullseye Graphics
Author: Arthur Belanger
Date created: 2-15-25
Notes: I tried to get the font on the label to change but couldn't
get it to work which makes me think the font size will not change
on the "Zakk Wylde's Guitar Paintjob.
"""
print("--------------------------------")
import time
from graphics import *

def main(win, x, y, radius):
    colors = [ "white", "black", "blue", "red", "yellow"] 
    for i in range(5):
        circle = Circle(Point(x, y), radius - i * radius / 5)
        circle.setFill(colors[i])
        circle.draw(win)        
win = GraphWin("Zakk Wylde's Guitar Paintjob", 750, 750)
win.setCoords(0, 0, 500, 500)
main(win, 250, 250, 125)
win.getMouse()
win.close()

print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - ch4ex02 ")
print(time.ctime())
    


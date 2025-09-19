"""
Program Name: ch5ex09
Program description: Drwas 5 smiley faces and then closes on click
Author: Arthur Belanger
Date created: 2-27-25
Notes: Getting the coordinates set from the 20 radius was a pain but got it.

"""
print("--------------------------------")
import time
from graphics import *

def drawFace(center, win):
    face = Circle(center, 20)
    face.setFill("yellow")
    face.draw(win)
    
    l_Eye = Circle(Point(center.getX() - 6, center.getY() - 4), 4)
    l_Eye.setFill("black")
    l_Eye.draw(win)
    
    r_Eye = Circle(Point(center.getX() + 8, center.getY() - 4), 4)
    r_Eye.setFill("black")
    r_Eye.draw(win)
    
    mouth = Oval(Point(center.getX() - 8, center.getY() + 4), Point(center.getX() + 8, center.getY() + 8))
    mouth.setFill("black")
    mouth.draw(win)

def main():
    win = GraphWin("Smiley Faces", 500, 500)    
    for _ in range(5):
        clickPoint = win.getMouse()
        drawFace(clickPoint, win)    
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()

print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - ch5ex09 ")
print(time.ctime())
    


"""
ch4ex11
Builds a modular home (trailer) in 5 clicks
Author: Arthur Belanger
Date created: 3-2-25
Notes: Modified to draw a modular home instead of a traditional house.
Frame is bottom left to top right
door is bottom left
window is center
roof is the click- I had a hard time getting the roof to go to the whole this in one click using the triangle
and not a polygon, but I got it how I wanted it and the functions work like I wanted also so I am happy.
"""
import time
from graphics import *

def openGraphicWindow():
    win = GraphWin("Modular Home(Trailer Park Paradise)", 700, 500)
    return win

def drawFrame(win):
    p1 = win.getMouse()
    p2 = win.getMouse()
    frame = Rectangle(p1, p2)
    frame.setFill("#9cc1e3")
    frame.draw(win)
    return frame, p1, p2

def drawDoor(win, p1, p2):
    doorWidth = (p2.x - p1.x) / 10
    doorHeight = (p2.y - p1.y) / 2
    p3 = win.getMouse()
    door = Rectangle(p3, Point(p3.x + doorWidth, p3.y + doorHeight))
    door.setFill("#521417")
    door.draw(win)
    return door

def drawWindow(win):
    p4 = win.getMouse()
    windowSize = 40
    halfSize = windowSize / 2
    window = Rectangle(Point(p4.x - halfSize, p4.y - halfSize), Point(p4.x + halfSize, p4.y + halfSize))
    window.setFill("#eaf8f8")
    window.draw(win)
    return window

def drawRoof(win, p1, p2):
    p5 = win.getMouse()
    roof = Rectangle(Point(p1.x, p5.y), Point(p2.x, p2.y))
    roof.setFill("#636363")
    roof.draw(win)
    return roof

def promptToQuit(win):
    win.getMouse()
    win.close()

def main():
    win = openGraphicWindow()
    frame, p1, p2 = drawFrame(win)
    drawDoor(win, p1, p2)
    drawWindow(win)
    drawRoof(win, p1, p2)
    promptToQuit(win)
  

if __name__ == "__main__":
    main()

print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - ch4ex11 ")
print(time.ctime())

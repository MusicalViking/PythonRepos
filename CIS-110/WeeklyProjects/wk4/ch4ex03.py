"""
ch4ex03
Make a face with Python
Author: Arthur Belanger
Date created: 2-15-25

Notes: This was cool, I feel like if I added too much I wouldn't meet your
goals in this.

"""
print("--------------------------------")
import time
from graphics import *

def main():
    win = GraphWin("Face", 400, 400)    
    # Head
    head = Oval(Point(100, 100), Point(300, 300))
    head.setFill("yellow")
    head.draw(win)   
    # l_r eyes
    l_eye = Circle(Point(150, 180), 20)
    l_eye.setFill("black")  
    l_eye.draw(win)
    r_eye = Circle(Point(250, 180), 20)
    r_eye.setFill("black")
    r_eye.draw(win)    
    # nose
    nose = Polygon(Point(200, 220), Point(180, 240), Point(220, 240))
    nose.setFill("red")
    nose.draw(win)    
    # mouth
    mouth = Polygon(Point(150, 270), Point(200, 290), Point(250, 270))
    mouth.setFill("red")
    mouth.draw(win)
    win.getMouse()
    win.close()

main()



print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - ch4ex03 ")
print(time.ctime())
    


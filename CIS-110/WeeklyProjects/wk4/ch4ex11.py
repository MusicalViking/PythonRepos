"""
ch4ex11
Builds a house in 5 clicks
Author: Arthur Belanger
Date created: 2-15-25

Notes: I can say that this was the hardest one I have done yet,
looking forward to the next one.

"""
print("--------------------------------")
import time
from graphics import *

def main(win):
    p1 = win.getMouse()  # b-left
    p2 = win.getMouse()  # t-right
    house_width = p2.x - p1.x
    house_height = p2.y - p1.y
    rect = Rectangle(p1, p2)
    rect.setFill("green")
    rect.draw(win)

    p3 = win.getMouse()  # t-left door
    door_width = house_width / 5
    door_rect = Rectangle(Point(p3.x, p1.y), Point(p3.x + door_width, p3.y))
    door_rect.setFill("brown")
    door_rect.draw(win)


    p4 = win.getMouse()  # window
    window_radius = door_width / 2
    window_circle = Circle(p4, window_radius)
    window_circle.setFill("white")
    window_circle.draw(win)

    p5 = win.getMouse()  # Roof
    roof_p1 = Point(p1.x, p2.y)
    roof_p2 = Point(p2.x, p2.y)
    roof_p3 = p5
    roof = Polygon(roof_p1, roof_p2, roof_p3)
    roof.setFill("black")
    roof.draw(win)

win = GraphWin("The Poor House", 750, 750)
main(win)
win.getMouse()




print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - ch4ex11 ")
print(time.ctime())
    


import time
import math
#Program 3
#Arthur Belanger
#Calculate how far a connonball will travel, input speed and angle
#2-7-25
#Notes of interest
#--------------------------------

def main(speed, angle):
    angle_radians = math.radians(angle)
    distance = (speed**2 * math.sin(2 * angle_radians)) / 9.81
    
    return distance

speed = float(input("What is the speed? "))
angle = float(input("What is the angle? "))

print("The distance is: {:.1f}".format(main(speed, angle)))





#---End of code------------------
#Arthur Belanger
#Programming Fundamentals CIS-110
print(time.ctime())

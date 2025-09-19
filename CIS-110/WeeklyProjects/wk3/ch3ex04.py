import time
import math
#ch3ex04
#Arthur Belanger
#Determines the distance to lighting strike
#2-05-25
#In class exercises
#--------------------------------

def main():
    for i in range(3):
        
        secs_to_thunder = float(input("How many seconds since the flash of lightning? "))
                
        feet = secs_to_thunder * 1100
        distance = feet / 5280
        simplified = round(distance,1)
        
        print(f"The lightning is {simplified} miles away.")
    
main()
#---End of code------------------
#Arthur Belanger
#Programming Fundamentals CIS-110
print(time.ctime())

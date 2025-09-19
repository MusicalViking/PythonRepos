import time
#Program2
#Arthur Belanger
#tells how long a photo takes to reach nasa from mars
#1-27-2025
#the range function threw me for a loop...:)
#--------------------------------



def main():
    
    speed_of_light = 186000

    for _ in range(3):
            
        distance = int(input("What is the distance in miles you would like to calculate? "))
        duration = distance / speed_of_light
        
        print(f"Time taken to travel {distance} miles: {duration} seconds")

if __name__ == '__main__':
    main()


#---End of code------------------
#Arthur Belanger
#Programming Fundamentals CIS-110
print(time.ctime())
